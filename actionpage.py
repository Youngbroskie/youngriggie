from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database connection string
engine = create_engine('postgresql://user:password@host:port/database')
Session = sessionmaker(bind=engine)
session = Session()

# Example query
result = session.query(User).filter_by(id=1).first()

from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user,login_required, logout_user, current_user
from flask_sqlalchemy import flask_sqlalchemy


app = Flask(_name_)
app.config["SECRET_KEY"] = "secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"

db =SQLAlchemy(app)
login_manager= LoginManager()
login_manager.int_app(app)
login_manager.login_view = "login"

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(80),unique= True, nullable = False)
    password = db.Column(db.String(120), nullable = False)
    wallet_balance = db.Column(db.Float, default= 0.0)
    todays_income = db.Column(db.Float, default= 0.0)
    total_withdrawals = db.Column(db.Float, default= 0.0)

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route("/register", methods = ["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User(username=username)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        flash("Account created successfully!")
        return redirect(url_for("login"))
        return render_template(register.html)


@app.route("/login", methods= ["GET", "POST"])
def login():
    if request.method== "POST":
        username = request.form["username"]
        password = request.form["password"]
        user = User.query.filter_by(username=username).first()

        if user and user.check_password(password):
            login_user(user)
            flash("Login Successful!")
            return redirect(url_for("dashboard"))
        else:
            flash("Invalid username or password")
    return render_template("login.html")


@app.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out!")
    return redirect(url_for("login"))

    @app.route("/dashbboard")
    @login_required
    def withdraw():
        amount= float(request.form["amount"])
        if amount > 0 and amount <= current_user.balance:
            current_user -= amount
            current_user.total_withdrawals += amount
            db.session.commit()
            flash("Withdrawal succesful!")
            
        else:
            flash("Invalid withdrawal amount")
        return redirect(url_for("dashboard"))

if _name_ == "_main_":
    app.run(debug= True)


@app.route("/dashboard")
@login_required
def dashbboard():
    user= current_user


    return render_template("dashboard.html", user=user)
       