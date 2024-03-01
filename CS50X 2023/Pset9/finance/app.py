# Maimoona Aziz
import os

from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, lookup, usd, valid_password

# Configure application
app = Flask(__name__)

# Custom filter
app.jinja_env.filters["usd"] = usd

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///finance.db")


@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/")
@login_required
def index():
    """Show portfolio of stocks"""
    # Get user ID
    user_id = session["user_id"]
    names = db.execute("SELECT username FROM users WHERE id = ?", user_id)
    if len(names) == 1:
        name = names[0]["username"]
    else:
        return apology("Error fetching username")

    # Get users total inventory information
    stock = db.execute(
        "SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol HAVING total_shares != 0",
        user_id,
    )

    grand_total = 0
    for s in stock:
        quote = lookup(s["symbol"])
        if quote is None:
            return apology("Invalid Symbol")

        s["name"] = quote["name"]
        s["price"] = quote["price"]
        s["shares"] = s["total_shares"]
        s["total"] = quote["price"] * s["shares"]

        grand_total += s["total"]

    # Retrieve users cash balance
    cash_list = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
    if len(cash_list) == 1:
        cash = cash_list[0]["cash"]
    else:
        return apology("Error fetching user's cash")

    grand_total += cash


    return render_template("portfolio.html", cash=cash, grand_total=grand_total, stocks=stock, name=name)


@app.route("/buy", methods=["GET", "POST"])
@login_required
def buy():
    """Buy shares of stock"""
    if request.method == "POST":
        user_id = session["user_id"]  # User id

        # Retrieve inputs
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if blank
        if not symbol:
            return apology("Symbol must not be blank")
        if not shares:
            return apology("Shares must not be blank")
        if not shares.isdigit():
            return apology("Shares must be a positive integer")

        # Convert shares to integer
        try:
            shares = int(shares)
        except ValueError:
            return apology("Shares must be a valid positive integer")

        quote = lookup(symbol)  # Look up information of symbol
        if quote is None:
            return apology("Invalid Symbol")

        # Check current users cash balance
        cash_list = db.execute("SELECT cash FROM users WHERE id = ?", user_id)
        # Extract the cash value from the list
        if len(cash_list) == 1:
            cash = cash_list[0]["cash"]
        else:
            return apology("Error fetching user's cash balance")

        total_price = quote["price"] * shares  # Calculate the total price for shares

        # Make sure users funds are sufficient
        if total_price > cash:
            return apology("Insufficient funds for this purchase")

        quantity = 1 * shares

        # PROCEED WITH BUYING ---------------

        try:
            # Update transaction in the table to keep track of history
            db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES(?, ?, ?, ?, datetime('now'))", user_id, symbol, quantity, quote["price"])

            # Deduct purchase amount from user's account
            db.execute("UPDATE users SET cash = cash - ? WHERE id = ?", total_price, user_id)

        except Exception as e:
            print("Error:", str(e))
            return apology("Transaction Failed")

        return redirect("/")

    else:
        return render_template("buy.html")


@app.route("/history")
@login_required
def history():
    """Show history of transactions"""
    user_id = session["user_id"]  # User id
    history = db.execute("SELECT symbol, shares, price, timestamp FROM transactions WHERE user_id = ? ORDER BY timestamp ASC", user_id)

    for h in history:
        quote = lookup(h["symbol"])
        if quote is None:
            return apology("Invalid Symbol")

        # Inserting name, price, and total into "stock dictionary"
        h["name"] = quote["name"]
        h["price"] = quote["price"]

    return render_template("history.html", history=history)

@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Ensure username was submitted
        if not request.form.get("username"):
            return apology("must provide username", 403)

        # Ensure password was submitted
        elif not request.form.get("password"):
            return apology("must provide password", 403)

        # Query database for username
        rows = db.execute("SELECT * FROM users WHERE username = ?", request.form.get("username"))

        # Ensure username exists and password is correct
        if len(rows) != 1 or not check_password_hash(rows[0]["hash"], request.form.get("password")):
            return apology("invalid username and/or password", 403)

        # Remember which user has logged in
        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")


@app.route("/logout")
def logout():
    """Log user out"""

    # Forget any user_id
    session.clear()

    # Redirect user to login form
    return redirect("/")


@app.route("/quote", methods=["GET", "POST"])
@login_required
def quote():
    """Get stock quote."""
    if request.method == "POST":
        # Retrieve inputs
        symbol = request.form.get("symbol")

        # Check if blank
        if not symbol:
            return apology("Symbol must not be blank")

        # Look up quote
        quote = lookup(symbol)
        if quote is None:
            return apology("Invalid symbol")

        # Switch to  page that shows quote
        return render_template("quoted.html", quote=quote)

    else:
        return render_template("quote.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    """Register user"""
    if request.method == "POST":
        # Forget any user_id
        session.clear()

        # Retrieve inputs
        name = request.form.get("username")
        password = request.form.get("password")
        confirm = request.form.get("confirmation")

        # Check if blank
        if not name:
            return apology("Username must not be blank")
        if not password:
            return apology("Password must not be blank")
        if confirm != password:
            return apology("Confirmation password must be the same as password")

        # Check is user already exists
        rows = db.execute("SELECT * FROM users WHERE username = ?", name)
        if len(rows) > 0:
            return apology("Username already exists")

        # Check if password has met security requirements
        password_error = valid_password(password)
        if password_error is not None:
            return apology(password_error)

        # INSERT DATA INTO DATABASE ----------------------

        # Hash password
        hashword = generate_password_hash(password, method="pbkdf2", salt_length=16)

        # Insert user and hashed password into database
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", name, hashword)

        # AUTOMATICALLY LOG IN ---------------------------

        # Query database for username
        user = db.execute("SELECT * FROM users WHERE username = ?", name)

        # Set user as current session
        session["user_id"] = user[0]["id"]

        # Redirect user to home page
        return redirect("/")
    else:
        return render_template("register.html")


@app.route("/sell", methods=["GET", "POST"])
@login_required
def sell():
    """Sell shares of stock"""
    user_id = session["user_id"]  # User id
    # Retrieve users inventory
    inventory = db.execute("SELECT symbol, SUM(shares) AS total_shares FROM transactions WHERE user_id = ? GROUP BY symbol", user_id)
    if request.method == "POST":
        # Retrieve inputs
        symbol = request.form.get("symbol")
        shares = request.form.get("shares")

        # Check if blank
        if not symbol:
            return apology("Symbol must not be blank")
        if not shares:
            return apology("Shares must not be blank")
        if not shares.isdigit():
            return apology("Shares must be a positive integer")

        # Convert shares to integer
        try:
            shares = int(shares)
        except ValueError:
            return apology("Shares must be a valid positive integer")

        quote = lookup(symbol)  # Look up information of symbol
        if quote is None:
            return apology("Invalid Symbol")

        quantity = -shares

        for stock in inventory:
            if stock["symbol"] == symbol:
                if "symbol" not in stock:
                    return apology("You don't have any shares of this stock")
                if shares > stock["total_shares"]:
                    return apology("You don't have sufficient shares of this stock")
                else:
                    total = quote["price"] * shares
                    try:
                        # Insert action into transactions
                        db.execute("INSERT INTO transactions (user_id, symbol, shares, price, timestamp) VALUES(?, ?, ?, ?, datetime('now'))", user_id, symbol, quantity, quote["price"])

                        # Receive cash
                        db.execute("UPDATE users SET cash = cash + ? WHERE id = ?", total, user_id)

                    except Exception as e:
                        print(f"Transaction failed: {str(e)}")
                        return apology("Transaction failed. Please try again later.")

                    break

        return redirect("/")

    else:
        return render_template("sell.html", user_symbol=inventory)
