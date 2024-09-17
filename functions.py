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


def deposit(username,amount,fund):
    try:
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        sql_insert = text("INSERT INTO deposits (user_id,amount,fund,sent_date) VALUES (:user_id,:amount,:fund,NOW())")
        db.session.execute(sql_insert, {"user_id":user_id, "amount":amount, "fund":fund})
        db.session.commit()
    except:
        return False
    return True


def logout():
    del session["username"]
