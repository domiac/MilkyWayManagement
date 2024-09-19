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


def balance_check(username, amount, fund):
    sql_balance = text("SELECT SUM(amount) FROM transaction WHERE user_id = (SELECT id FROM users WHERE username = :username) AND fund = :fund")
    result = db.session.execute(sql_balance, {"username": username, "fund": fund})
    current_balance = result.scalar() or 0
    if current_balance >= float(amount):
        return True
    else:  
        return False



def withdraw(username, amount, fund):
    if not balance_check(username, amount, fund):
        return False
    sql_id = text("SELECT id FROM users WHERE username = :username")
    result = db.session.execute(sql_id, {"username": username})
    user_id = result.fetchone()[0]
    sql_insert = text("INSERT INTO transaction (user_id, amount, fund, sent_date) VALUES (:user_id, :amount, :fund,NOW())")
    db.session.execute(sql_insert, {"user_id": user_id, "amount": -float(amount), "fund": fund})
    db.session.commit()
    return True



def fund_creator(admin, fund_name):
    sql = text("SELECT id FROM users WHERE username = :admin")
    result = db.session.execute(sql, {"admin": admin})
    admin_id = result.fetchone()[0]
    try:
        sql_insert = text("INSERT INTO funds (admin_id, fund_name) VALUES (:admin_id, :fund_name)")
        db.session.execute(sql_insert, {"admin_id": admin_id, "fund_name": fund_name})
        db.session.commit()
    except:
        return False
    return True





def logout():
    del session["username"]




