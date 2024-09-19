from db_conn import db
from sqlalchemy import text
from flask import session
from werkzeug.security import check_password_hash, generate_password_hash




def funds():

    if "username" in session:
        username = session["username"]
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        sql_funds = text("SELECT fund_id, SUM(amount) FROM transaction WHERE user_id = :user_id GROUP BY fund_id")
        result = db.session.execute(sql_funds, {"user_id": user_id})
        funds = result.fetchall()
        return funds
    else:
        return None

    
