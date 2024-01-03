import nltk
from nltk.stem import WordNetLemmatizer
import json
import random
import pickle
import numpy as np
from keras.models import load_model


lemmatizer = WordNetLemmatizer()

# Gerekli kütüphanelerin ve modüllerin import edilmesi
model = load_model('chatbot/builds/chatbot_model.h5')
intents = json.loads(open('chatbot/static/js/job_intents.json', encoding='utf-8').read())

# Önceden oluşturulan veri yapılarının yüklenmesi
words = pickle.load(open('chatbot/builds/words.pkl','rb'))
classes = pickle.load(open('chatbot/builds/classes.pkl','rb'))


# Cümleyi temizleyen bir işlev
def clean_up_sentence(sentence):
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word.lower()) for word in sentence_words]
    return sentence_words


# Cümleyi torba kelime temsiline dönüştüren bir işlev
def bow(sentence, words, show_details=True):
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for s in sentence_words:
        for i,w in enumerate(words):
            if w == s:
                bag[i] = 1
                if show_details:
                    print ("found in bag: %s" % w)
    return(np.array(bag))


# Cümlenin hangi sınıfa ait olduğunu tahmin eden bir işlev
def predict_class(sentence, model):
    p = bow(sentence, words, show_details=False)
    res = model.predict(np.array([p]))[0]
    ERROR_THRESHOLD = 0.25
    results = [[i,r] for i,r in enumerate(res) if r > ERROR_THRESHOLD]
    results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in results:
        return_list.append({"intent": classes[r[0]], "probability": str(r[1])})
    return return_list


# Tahmin edilen sınıfa göre uygun yanıtı döndüren bir işlev
def getResponse(ints, intents_json):
    try:
        tag = ints[0]['intent']
        list_of_intents = intents_json['intents']
        for i in list_of_intents:
            if i['tag'] == tag:
                result = random.choice(i['responses'])
                break
    except Exception:
        result = "Anlamadım, lütfen başka bir soru sorun."     
    return result

# Kullanıcının mesajına yanıt veren ana işlev
def chatbot_response(msg):
    ints = predict_class(msg, model)
    res = getResponse(ints, intents)
    return res

def check_and_delete_files():
    import os
    folder_path = "chatbot/builds"
    files = os.listdir(folder_path)

    for file in files:
        file_path = os.path.join(folder_path,file)
        if os.path.isfile(file_path):
            os.remove(file_path)

    
