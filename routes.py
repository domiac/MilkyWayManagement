from app import app
from flask import Flask
from flask import redirect, render_template, request, session
import funds
import functions




@app.route("/")
def index():
    list = funds.funds()
    return render_template("index.html",count=len(list), funds=list)


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
        username = request.form["username"]
        password1 = request.form["password1"]
        password2 = request.form["password2"]
        if password1 != password2:
            return render_template("error.html", message="Salasanat eroavat")
        if functions.register(username, password1):
            return redirect("/")
        else:
            return render_template("error.html", message="Registration failed")
         


@app.route("/deposit", methods=["GET", "POST"])
def deposit():
    if request.method == "GET":
        return render_template("deposit.html")
    if request.method == "POST":
        username = session["username"]
        amount = request.form["amount"]
        fund = request.form["fund"]
        if functions.deposit(username,amount,fund):
            return redirect("/")
        else:
            return render_template("error.html", message="Deposit failed")



@app.route("/logout")
def logout():
    functions.logout()
    return redirect("/")


@app.route("/error")
def error():
     return render_template("error.html")
