from . import db, login_manager
from flask_login import UserMixin

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True)
    article = db.Column(db.UnicodeText)


class Admin(UserMixin, db.Model):
    __tablename__ = "Admin"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64))
    password = db.Column(db.String(128))

    def verify_password(self,passwrod):
        return self.password == passwrod

@login_manager.user_loader
def load_user(user_id):
    return Admin.query.get(int(user_id))