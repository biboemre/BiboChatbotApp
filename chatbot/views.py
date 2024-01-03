from chatbot import app, db
from flask_admin.contrib.sqla import ModelView
from flask import render_template, request, jsonify
from flask_admin import Admin
from chatbot.utils import chatbot_response, check_and_delete_files
import nltk
from nltk.stem import WordNetLemmatizer
import json
import pickle
from chatbot.models import Articles

import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Activation, Dropout
from keras.optimizers import SGD
import random

# NLTK kütüphanesinin gerekli veri setlerinin indirilmesi
nltk.download('punkt')
nltk.download('wordnet')
# Kelimeleri köklerine ayırmak için kullanılacak olan WordNetLemmatizer sınıfının örnekleştirilmesi
lemmatizer = WordNetLemmatizer()


@app.route("/", methods = ['GET', 'POST'])
def index():
    check_and_delete_files()
    create_model()
    return render_template('index.html')

# Kullanıcıdan gelen soruya chatbot yanıtı veren route
@app.route('/chatbot', methods=["GET", "POST"])
def chatbotResponse():

    if request.method == 'POST':
        the_question = request.form['question']

        response = chatbot_response(the_question)

    return jsonify({"response": response })

# Makale detayının görüntülendiği route
@app.route('/articles', methods=["GET"])
def articles():
    articles = Articles.query.all()
    return render_template("articles.html", articles = articles)

# Makale detayının görüntülendiği route
@app.route('/article-detail/<int:id>', methods=["GET"])
def article_detail(id):
    article = Articles.query.filter_by(id=id).first()
    return render_template("article-detail.html", article=article)

def create_model():
    words=[]
    classes = []
    documents = []
    ignore_words = ['?', '!']
    data_file = open('chatbot/static/js/job_intents.json', encoding='utf-8').read()
    intents = json.loads(data_file)

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            w = nltk.word_tokenize(pattern)
            words.extend(w)
            documents.append((w, intent['tag']))
            if intent['tag'] not in classes:
                classes.append(intent['tag'])
    words = [lemmatizer.lemmatize(w.lower()) for w in words if w not in ignore_words]
    words = sorted(list(set(words)))
    classes = sorted(list(set(classes)))

    pickle.dump(words,open('chatbot/builds/words.pkl','wb'))
    pickle.dump(classes,open('chatbot/builds/classes.pkl','wb'))

    training = []
    output_empty = [0] * len(classes)
    for doc in documents:
        bag = []
        pattern_words = doc[0]
        pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]

        for w in words:
            bag.append(1) if w in pattern_words else bag.append(0)

        output_row = list(output_empty)
        output_row[classes.index(doc[1])] = 1
        training.append([bag, output_row])

    random.shuffle(training)
    training = np.array(training)
    train_x = list(training[:,0])
    train_y = list(training[:,1])

    model = Sequential()
    model.add(Dense(128, input_shape=(len(train_x[0]),), activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(64, activation='relu'))
    model.add(Dropout(0.5))
    model.add(Dense(len(train_y[0]), activation='softmax'))

    sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
    model.compile(loss='categorical_crossentropy', optimizer=sgd, metrics=['accuracy'])

    hist = model.fit(np.array(train_x), np.array(train_y), epochs=200, batch_size=5, verbose=1)
    model.save('chatbot/builds/chatbot_model.h5', hist)


# Flask Admin arayüzünün tanımlanması
admin = Admin(app)

admin.add_view(ModelView(Articles, db.session))
