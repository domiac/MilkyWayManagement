from db_conn import db
from sqlalchemy import text
from flask import session

def user_specified_funds():
    if "username" in session:
        username = session["username"]
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]

        sql_funds = text("SELECT f.fund_name, SUM(t.amount) as total_amount FROM transaction t JOIN fund f ON t.fund_id = f.id WHERE t.user_id = :user_id GROUP BY f.fund_name")
        result = db.session.execute(sql_funds, {"user_id": user_id})
        funds = result.fetchall()

        # this had to be done so i can call SUM in the template
        funds = [{"fund_name": row[0], "SUM": row[1]} for row in funds]

        return funds
    else:
        return []
