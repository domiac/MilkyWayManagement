from db_conn import db
from sqlalchemy import text
from flask import session
 



def watchlist_specific_funds():
    if "username" in session:
        username = session["username"]
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        sql_non_listed = text("SELECT fund_name FROM fund WHERE id NOT IN (SELECT fund_id FROM watchlist WHERE user_id = :user_id)")
        result = db.session.execute(sql_non_listed, {"user_id": user_id})
        funds_non_listed = result.fetchall()
        
    
        return funds_non_listed
    
    else:
        return []


def chosen_watchlist_funds():
    if "username" in session:
        username = session["username"]
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        sql_listed = text("SELECT fund_name FROM fund WHERE id IN (SELECT fund_id FROM watchlist WHERE user_id = :user_id)")
        result = db.session.execute(sql_listed, {"user_id": user_id})
        funds_listed = result.fetchall()
        return funds_listed
    else:
        return []



def watchlist_sums():
    if "username" in session:
        username = session["username"]
        sql_id = text("SELECT id FROM users WHERE username = :username")
        result = db.session.execute(sql_id, {"username": username})
        user_id = result.fetchone()[0]
        # got help from claude.ai with this query
        sql_watchlist = text("""SELECT f.fund_name, COALESCE(SUM(t.amount), 0) as total_amount FROM fund f LEFT JOIN transaction t ON f.id = t.fund_id WHERE f.id IN (SELECT fund_id FROM watchlist WHERE user_id = :user_id) GROUP BY f.fund_name""")
        
        result = db.session.execute(sql_watchlist, {"user_id": user_id})
        funds = result.fetchall()
        return funds
    else:
        return []