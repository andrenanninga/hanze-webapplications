from app import db
from sqlalchemy.ext.associationproxy import association_proxy

# device_household = db.Table('apparaat_huishouden',
#     db.Column('id', db.Integer, primary_key=True),
#     db.Column('huishouden_fk', db.Integer, db.ForeignKey('huishouden.id')),
#     db.Column('apparaat_fk', db.Integer, db.ForeignKey('apparaat.id'))
# )

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
    users = db.relationship('User', secondary=household_user, backref='households')

    devices = association_proxy('householdDevices', 'device')

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
    category = db.Column('categorie', db.String(64))
    max = db.Column('max', db.Integer)

    households = association_proxy('householdDevices', 'household')

    def __init__(self, name=None, category=None, max=None, households=None):
        self.name = name
        self.category = category
        self.max = max
        self.households = households

    def __repr__(self):
        return '<Device %r>' % (self.name)

class HouseholdDevice(db.Model):
    __tablename__ = 'apparaat_huishouden'

    id = db.Column('id', db.Integer, primary_key=True)
    household_id = db.Column('huishouden_fk', db.Integer, db.ForeignKey('huishouden.id'))
    device_id = db.Column('apparaat_fk', db.Integer, db.ForeignKey('apparaat.id'))

    household = db.relationship(Household, backref='householdDevices')
    device = db.relationship(Device, backref='householdDevices')

    def __init__(self, household=None, device=None):
        self.household_id = household.id
        self.device_id = device.id

    def __repr__(self):
        return '<HouseholdDevice %r %r %r>' % (self.id, self.household, self.device)

