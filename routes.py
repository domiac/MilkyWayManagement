from app import app
from flask import Flask
from flask import redirect, render_template, request, session, flash
import funds
import functions
from all_possible_funds import all_possible_funds
from user_specified_funds import user_specified_funds



@app.route("/")
def index():
    list = funds.funds()
    return render_template("index.html", funds=list)


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if functions.log_in(username, password):
            return redirect("/")
        else:
            return render_template("error.html", message="Wrong username or password")
    
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    if request.method == "POST":
        admin = False
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if request.form["admin_creds"]=="admin1234":
            admin = True
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if functions.register(username, password1, admin):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")
         


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if "username" not in session:
        return redirect("/login")
    available_funds = all_possible_funds()
    if request.method == "POST":
        amount = request.form["amount"]
        fund = request.form["fund"]
        success = functions.deposit(session["username"], amount, fund)
        if success:
            flash("Deposit successful", "success")
            return redirect("/")
        else:
            flash("Deposit failed", "error")
    return render_template("deposit.html", funds=available_funds)



@app.route("/withdraw", methods=["GET", "POST"])
def withdraw():
    if "username" not in session:
        return redirect("/login")
    available_funds_for_account = user_specified_funds() or []
    if request.method == "POST":
        amount = request.form["amount"]
        fund = request.form["fund"]
        success = functions.withdraw(session["username"], amount, fund)
        if success:
            flash("Withdrawal successful", "success")
            return redirect("/")
        else:
            flash("Withdrawal failed", "error")
    return render_template("withdraw.html", funds=available_funds_for_account)



@app.route("/logout")
def logout():
    functions.logout()
    return redirect("/")


@app.route("/error")
def error():
     return render_template("error.html")
