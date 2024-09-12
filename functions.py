from db_conn import db
from sqlalchemy import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash


def log_in(username, password):
    sql = text("SELECT id, password FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    user = result.fetchone()

    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["username"] = username
            return True
        else:
            return False




def register(username, password):
    hash_value = generate_password_hash(password)
    if not log_in(username, password):  
        try:
            sql_insert = text("INSERT INTO users (username,password) VALUES (:username,:password)")
            db.session.execute(sql_insert, {"username":username, "password":hash_value})
            db.session.commit()
        except:
            return False
        return log_in(username, password)
    
    else:
        return False


def logout():
    del session["username"]
