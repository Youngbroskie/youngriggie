rom sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database connection string
engine = create_engine('postgresql://user:password@host:port/database')
Session = sessionmaker(bind=engine)
session = Session()

# Example query
result = session.query(User).filter_by(id=1).first()

from Flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"] =
"sqlite:///database.db"
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(64), unique=True,nullable=False)
    email = db.Column(db.String(120),unique =True, nullable = False)
    password = db.Column(db.String(128), nullable = False)
    wallet_balance = db.Column(db.Float, default=0.0)


@app.route("/deposit, methods=["GET", "POST"])
def deposit():
    if request.method =="POST":
        user_id = request.form["user_id"]
        amount = float(request.form["amount"])
        user = User.query.get(user_id)
        if user:
            user.wallet_balance += amount
            db.session.commit()
            return jsonify({"message":"Deposit Successful!"})
        else:
            return jsonify({"message":"User not found!"}),404
            