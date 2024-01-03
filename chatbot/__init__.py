from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Flask uygulaması oluşturuluyor
app = Flask(__name__, template_folder='templates')
app.config["SECRET_KEY"] = "74fe13370e062efda7e52bc7aa7336t2" 
# Veritabanı bağlantısı
conn = 'mysql+mysqlconnector://root:123456@localhost/chatbot'
app.config['SQLALCHEMY_DATABASE_URI'] = conn
db = SQLAlchemy(app)

from chatbot import utils
from chatbot import views
