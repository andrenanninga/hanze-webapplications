from app import db

class User(db.Model):
    __tablename__ = 'gebruiker'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('naam', db.String(45), unique=True)
    email = db.Column('email', db.String(64), unique=True)
    password = db.Column('wachtwoord', db.String(64))
    phonenumber = db.Column('telefoonnummer', db.String(20))

    def __init__(self, name=None, email=None, password=None, phonenumber=None):
        self.name = name
        self.email = email
        self.password = password
        self.phonenumber = phonenumber

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    def __repr__(self):
        return '<User %r>' % (self.name)