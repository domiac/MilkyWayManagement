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




def register(username, password, admin):
    hash_value = generate_password_hash(password)
    if not log_in(username, password):  
        try:
            sql_insert = text("INSERT INTO users (username,password, admin) VALUES (:username,:password,:admin)")
            db.session.execute(sql_insert, {"username":username, "password":hash_value, "admin":admin})
            db.session.commit()
        except:
            return False
        return log_in(username, password)
    
    else:
        return False


def fund_id_func(fund_name):
    sql = text("SELECT id FROM fund WHERE fund_name = :fund_name")
    result = db.session.execute(sql, {"fund_name": fund_name})
    fund_id = result.fetchone()[0]
    return fund_id





def deposit(username,amount,fund_name):
    if float(amount)<0:
        return False
    try:
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        fund_id = fund_id_func(fund_name)
        sql_insert = text("INSERT INTO transaction (amount, fund_id, user_id, sent_date) VALUES (:amount, :fund_id, :user_id, NOW())")
        db.session.execute(sql_insert, {"amount": float(amount), "fund_id": fund_id, "user_id": user_id})
        db.session.commit()
    except:
        return False
    return True


def balance_check(username, amount, fund_id):
    sql_balance = text("SELECT SUM(amount) FROM transaction WHERE user_id=(SELECT id FROM users WHERE username = :username) AND fund_id = :fund_id")
    result = db.session.execute(sql_balance, {"username": username, "fund_id": fund_id})
    current_balance = result.scalar() or 0
    if current_balance >= float(amount):
        return True
    else:  
        return False



def withdraw(username, amount, fund_name):
    fund_id = fund_id_func(fund_name)
    if not balance_check(username, amount, fund_id):
        return False
    sql_id = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql_id, {"username": username})
    user_id = result.fetchone()[0]
    sql_insert = text("INSERT INTO transaction (user_id, amount, fund_id, sent_date) VALUES (:user_id, :amount, :fund_id,NOW())")
    db.session.execute(sql_insert, {"user_id": user_id, "amount": -float(amount), "fund_id": fund_id})
    db.session.commit()
    return True


def admin_check(username):
    sql = text("SELECT admin FROM users WHERE username = :username")
    result = db.session.execute(sql, {"username": username})
    admin = result.fetchone()[0]
    return admin


def create_fund(fund_name, intrest, username):
    sql_id = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql_id, {"username": username})
    user_id = result.fetchone()[0]
    try:
        sql_insert = text("INSERT INTO fund (intrest, fund_name, user_id, create_date) VALUES (:intrest, :fund_name, :user_id, NOW())")
        db.session.execute(sql_insert, {"intrest": intrest, "fund_name": fund_name, "user_id": user_id})
        db.session.commit()
    except:
        return False
    return True


def add_to_watchlist(username, fund_name):
    fund_id = fund_id_func(fund_name)
    sql_id = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql_id, {"username": username})
    user_id = result.fetchone()[0]
    try:
        sql_insert = text("INSERT INTO watchlist (user_id, fund_id) VALUES (:user_id, :fund_id)")
        db.session.execute(sql_insert, {"user_id": user_id, "fund_id": fund_id})
        db.session.commit()
    except:
        return False
    return True


def logout():
    del session["username"]




