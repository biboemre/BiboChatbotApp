from chatbot import db

# Makaleler tablosu
class Articles(db.Model):
    __tablename__ = "Articles"
    id = db.Column(db.Integer, primary_key=True, auto_increment=True)
    title = db.Column(db.String(80))
    content = db.Column(db.Text(3000), nullable=False)