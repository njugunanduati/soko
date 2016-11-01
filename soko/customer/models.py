# -*- coding: utf-8 -*-
"""Transporter models."""
import datetime as dt


from soko.database import Column, Model, SurrogatePK, db, reference_col, relationship


class Customer(SurrogatePK, Model):
    __tablename__ = 'customers'
    user_id = reference_col('users', nullable=True)
    user = relationship('User', backref='customers')
    vehicle_id = reference_col('vehicles', nullable=False)
    vehicle = relationship('Vehicle', backref='customers')
    photo = Column(db.String(80), nullable=False)
    dob = Column(db.String(80), unique=True, nullable=False)
    home_address = Column(db.String(150), nullable=True)
    work_address = Column(db.String(150), nullable=True)
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, user, vehicle, photo, licence, location):
        self.user = user
        self.vehicle = vehicle
        self.photo = photo
        self.licence = licence
        self.location = location

    def __repr__(self):
        return '<Transporter %r>' % self.user + self.vehicle + self.licence + self.location

class ShoppingList(SurrogatePK, Model):
    __tablename__ = 'shopping_list'
    customer_id = reference_col('customers', nullable=True)
    customer = relationship('Customer', backref='shopping_list')
    product = Column(db.String(30), nullable=True)
    quantity = Column(db.Integer),
    created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)

    def __init__(self, user, product, quantity):
        self.user = user
        self.product = product
        self.quantity = quantity


    def __repr__(self):
        return '<Shopping List %r>' % self.user + self.product + self.quantity


# class CheckOut(SurrogatePK, Model):
#     __tablename__ = 'checkout'
#     customer_id = reference_col('customers', nullable=True)
#     customer = relationship('Customer', backref='checkout')
#     date = Column(db.DateTime)
#     store_id = reference_col('stores', nullable=True)
#     store = relationship('Store', backref='checkout')
#     subtotal = Column(db.Numeric(15,2), nullable=True)
#     paid = Column(db.String(30), default=False)
#     created_at = Column(db.DateTime, nullable=False, default=dt.datetime.utcnow)
#
#     def __init__(self, customer, date, store, paid):
#         self.customer = customer
#         self.date = date
#         self.store = store
#         self.paid = paid
#
#     def __repr__(self):
#         return '<Checkout %r>' % self.customer + self.date + self.store + self.paid