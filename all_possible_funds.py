from db_conn import db
from sqlalchemy import text
from flask import session




def all_possible_funds():
        if "username" in session:
            username = session["username"]
            sql_id = text("SELECT fund_name, intrest FROM fund")
            result = db.session.execute(sql_id)
            funds = result.fetchall()
            return funds
        else:
            return None