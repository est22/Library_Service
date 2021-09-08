from flask import Flask, redirect, request, render_template, jsonify, Blueprint, session, g
from models import User, Book
from db_connect import db
from flask_bcrypt import Bcrypt

user = Blueprint('user',__name__)
bcrypt = Bcrypt()


@user.before_app_request
def load_logged_in_user():
    user_id = session.get("login")
    if login is None:
        g.user = None
    else:
        g.user = db.session.query(User).filter(User.id == user_id).first()



@user.route("/join",methods=["GET","POST"])
def join():
    if request.method == 'GET':
        return render_template('join.html')
    else:
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        pw_hash = bcrypt.generate_password_hash(user_pw)
        
        user = User(user_id, pw_hash)
        db.session.add(user)
        db.session.commit()
        return jsonify({"result":"success"})



@user.route("/login",methods=["GET","POST"])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        user_id = request.form['user_id']
        user_pw = request.form['user_pw']
        user = User.query.filter(User.user_id == user_id).first()
        
        if user is not None:
            if bcrypt.check_password_hash(user.user_pw, user_pw):
                session['login'] = user.id
                return jsonify({"result":"success"})
            else:
                return jsonify({"result":"fail"})
        else:
            return jsonify({"result":"fail"})
        





@user.route("/logout")
def logout():
    session['login'] = None
    return redirect("/")




