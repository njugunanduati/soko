import datetime as dt

from soko.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Farmer(SurrogatePK, Model):
    __tablename__ = 'farmers'
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='farmers')
    id_number = Column(db.Integer, nullable=True)
    photo = Column(db.String(80), nullable=True)
    product_id = reference_col('products', nullable=True)
    product = relationship('Product', backref='farmers')
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, user, id_number, photo, product):
        self.user = user
        self.id_number = id_number
        self.photo = photo
        self.product = product

    def __repr__(self):
        return '<Farmer %r>' % self.user + self.id_number + self.photo + self.product + self.branch


class Branch(SurrogatePK, Model):
    __tablename__ = 'branches'
    name = Column(db.String(80), nullable=False)
    farmer_id = reference_col('farmers', nullable=True)
    farmer = relationship('Farmer', backref='branches')
    location = Column(db.String(300), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, name, location, farmer):
        self.name = name
        self.location = location
        self.farmer = farmer

    def __repr__(self):
        return '<Branch %r>' % self.name + self.location + self.farmer


class FarmerAddress(SurrogatePK, Model):
    __tablename__ = 'farmer_address'
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='farmer_address')
    primary_address = Column(db.String(300), nullable=False)
    location = Column(db.String(80), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, user_id, primary_address, location):
        self.user_id = user_id
        self.primary_address = primary_address
        self.location = location

    def serialize(self):
        return {
            "id": self.id,
            "user": self.user_id,
            "primary_address": self.primary_address,
            "location": self.location,
            "Date": self.created_at,
        }