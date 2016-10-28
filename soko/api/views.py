from flask import Blueprint, flash, redirect, render_template, request, url_for, jsonify, make_response, json
from flask_login import login_required, login_user, logout_user
from flask_restful import reqparse
from sqlalchemy import orm

from soko.user.models import User
from soko.database import db
from soko.utils import flash_errors
from soko.extensions import csrf_protect, bcrypt

import uuid

blueprint = Blueprint('api', __name__, url_prefix='/api/v1')


@blueprint.route('/get_users', methods=['GET'])
def get_users():
    # Query the database and return all users
    # users = User.query.all()
    # try:
    #     results = jsonify({'status': 'success', 'data': users})
    # except:
    #     results = jsonify({'status': 'failure', 'message': 'No users found in the database'})
    # return make_response(results)
    # users = User.query.all()
    users = db.session.query(User).all()
    return jsonify(users)


@csrf_protect.exempt
@blueprint.route('/register', methods=['POST'])
def reg_user():
    data = request.json
    user = User(
        username=data['username'],
        surname=data['surname'],
        first_name=data['first_name'],
        last_name=data['last_name'],
        email=data['email'],
        password=data['password'],
        phone_number=data['phone_number'],
        is_admin=data['is_admin'],
        active=data['active'],
        token=data['token'],
        category=data['category']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'the user is already registered'
    db.session.close()
    return jsonify({'result': status})


@csrf_protect.exempt
@blueprint.route('/login', methods=["POST"])
def login():
    data = request.json
    username = data['username']
    password = data['password']
    registered_user = User.query.filter_by(username=username).first()
    if registered_user is None:
        status = {'status': 'failure', 'message': 'Username does not exist. Register'}
    else:
        if registered_user.check_password(password):
            registered_user.token = uuid.uuid4()
            db.session.add(registered_user)
            db.session.commit()
            login_user(registered_user)
            status = {'status': 'success', 'message': 'success'}
        else:
            status = {'status': 'faillure', 'message': 'Password is invalid'}
    return jsonify(status)
