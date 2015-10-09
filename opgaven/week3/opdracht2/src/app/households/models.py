from app import db

device_household = db.Table('apparaat_huishouden',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('huishouden_fk', db.Integer, db.ForeignKey('huishouden.id')),
    db.Column('apparaat_fk', db.Integer, db.ForeignKey('apparaat.id'))
)

household_user = db.Table('huishouden_gebruiker',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('huishouden_fk', db.Integer, db.ForeignKey('huishouden.id')),
    db.Column('gebruiker_fk', db.Integer, db.ForeignKey('gebruiker.id'))
)

class Household(db.Model):
    __tablename__ = 'huishouden'

    id = db.Column('id', db.Integer, primary_key=True)
    postcode = db.Column('postcode', db.String(6))
    housenumber = db.Column('huisnummer', db.String(10))
    size = db.Column('grootte', db.Integer)
    devices = db.relationship('Device', secondary=device_household, backref='households')
    users = db.relationship('User', secondary=household_user, backref='households')

    def __init__(self, postcode=None, housenumber=None, size=None):
        self.postcode = postcode
        self.housenumber = housenumber
        self.size = size

    def __repr__(self):
        return '<Household %r %r>' % (self.postcode, self.housenumber)

class Device(db.Model):
    __tablename__ = 'apparaat'

    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('naam', db.String(64))
    max = db.Column('max', db.Integer)

    def __init__(self, name=None, max=None):
        self.name = name
        self.max = max

    def __repr__(self):
        return '<Device %r>' % (self.name)
