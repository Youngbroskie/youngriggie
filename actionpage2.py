from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database connection string
engine = create_engine('postgresql://user:password@host:port/database')
Session = sessionmaker(bind=engine)
session = Session()

# Example query
result = session.query(User).filter_by(id=1).first()

from flask import Flask,request.jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmalow import Marshmallow
import datetime

app = Flask(_name_)
app.config["SQLALCHEMY_DATABASE_URI"] =
"sqlite:///database.db"
db = SQLAlchemy(app)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True,nullable=False)
    email = db.Column(db.String(120), unique=True,nullable=False)
    password = db.Column(db.String(120),nullable=False)
    wallet_balance = db.Column(db.Float, default=0.0)
    referral_code = db.Column(db.String(10),unique=True, nullable=False)
   

class Products(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    rental_price = db.Column(db.Float,nullable=False)
    rental_period = db.Column(db.Integer,nullable=False)
    daily_income =  db.Column(db.Float,nullable=False)

class investments(db.Model):
     id = db.Column(db.Integer,primary_key=True)
     user_id = db,Column(db.Integer,db.ForeignKey("user.id"))
     user = db.relationship("User", backref ="rentals")
     product_id = db.Column(db.Integer, db.ForeignKey("product.id")) 
     product = db.relationship("Products", backref="rentals")
     start_date = db.Column(db.DateTime, default =datetime.datetime.utcnow)
     end_date = db.Column(db.DateTime)

class Referrals(db.Model): 
    id = db.Column(db.Integer,primary_key=True)
    referral_code = db.Column(db.String(50),unique=True,nullable=False)
    user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    is_active = db.Column(db.Boolean,default=True)
    user = db.relationship("User", backref="referrals")
    referred_user_id = db.Column(db.Integer,db.ForeignKey("user.id"))
    referred_user = db.relationship("User", backref="referred_by")
    reward_amount = db.Column(db.Float, default=200.0)
    timestamp = db.Column(db.DateTime, default=datetime.datetime.utcnow)

products = {
'product_id1': {
'product_name': 'Money Market',
'rental_price': 900,
'daily_income': 55,
'rental_period': 30,
  },
'product_id2': {
'product_name': 'USDJPY',
'rental_price': 1000,
'daily_income': 60,
'rental_period': 30,
  },
'product_id3': {
'product_name': 'EURUSD',
'rental_price': 2100,
'daily_income': 130,
'rental_period': 30,
  },
'product_id4': {
'product_name': 'XAUUSD',
'rental_price': 3500,
'daily_income': 197,
'rental_period': 35,
  },
'product_id5': {
'product_name': 'Solana',
'rental_price': 4500,
'daily_income': 225,
'rental_period': 35,
  },
'product_id6': {
'product_name': 'Etherium',
'rental_price': 7000,
'daily_income': 400,
'rental_period': 25,
  },
'product_id7': {
'product_name': 'Bitcoin',
'rental_price': 15000,
'daily_income': 875,
'rental_period': 30,
  },
'product_id8': {
'product_name': 'Real Estate',
'rental_price': 1200,
'daily_income': 60,
'rental_period': 30,
  },
'product_id9': {
'product_name': 'Google',
'rental_price': 1500,
'daily_income': 100,
'rental_period': 30,
  },
'product_id10': {
'product_name': 'Netflix',
'rental_price': 2100,
'daily_income': 120,
'rental_period': 30,
  },
'product_id11': {
'product_name': 'Amazon',
'rental_price': 2700,
'daily_income': 140,
'rental_period': 30,
  },
'product_id12': {
'product_name': 'Copper',
'rental_price': 7000,
'daily_income': 375,
'rental_period': 30,
  },
'product_id13': {
'product_name': 'Gold',
'rental_price': 17000,
'daily_income': 1030,
'rental_period': 25,
  },
'product_id14': {
'product_name': 'Oil',
'rental_price': 23000,
'daily_income': 1200,
'rental_period': 30,
  },

}

user_data = {
  'wallet_balance': 0,
  'todays_income': 0,
  # Add other user details if needed (e.g., rented_products)
}

today = datetime.date.today()  # Import datetime module

def purchase_rent(product_id, user_id):
  if product_id in Products:
    product = Products[product_id]
    # Deduct rent price from user balance
    user_data['wallet_balance'] -= product['rent_price']
    # Update user data (optional, based on your implementation)
    # ...

    # Check if it's a weekday (excluding Sat/Sun)
    if not (today.weekday() == 5 or today.weekday() == 6):
      user_data['wallet_balance'] += product['daily_income']
      user_data['todays_income'] = product['daily_income']
  else:
    print("Invalid product ID")

@app.route("/users", methods=["POST"])
def create_user():
    data = request.get_json()
    email = data.get("email")
    if not email:
        return jsonify({"error": "Email is required"}), 400
    user =User(email=email)
    db.session.add(user)
    db.session.commit()
    referral_code = generate_referral_code()
    referral = Referral(code=referral_code,user=user)
    db.session.add(referral)
    db.session.commit()
    return jsonify({"user_id": user.id,"referral_code": referral_code})


@app.route("/referrals/<referral_code>", methods=["GET"])
def get_referral(referral_code):
    referral =
Referral.query.filter_by(code=referral_code).first()
    if not referral or not referral.is_active:
        return jsonify({'error': 'Invalid referral code'}), 400
    return jsonify({"user_id": referral.user.id})
def generate_referral_code():



@app.route("/register", method=["POST"])
def register_user():
    data = request.get_json()
    user = User(username=data["username"],
    email= data["email"],password=data["password"])
    db.session.add(user)
    db.session.commit()
    return jsonify({"message": "Account created successfully!"})


@app.route("/login", methods=["POST"])
def login_user():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"], password=data["password"]).first()
    if user:
        return jsonify({"token":"some_token"})
    return jsonify({"error": "Invalid username or password"}),401

@app.route("/products", methods=["GET"])
def get_products():
    products = Product.query.all()
    return jsonify([{"id":p.id,"name": p.name,"description":p.description,"rental_price": p.rental_price}for p in products])


@app.route("/rent_product", methods=["POST"])
def rent_product():
    data = request.get_json()
    user = User.query.filter_by(id=data["product_id"]).first()
    product = Product.query.filter_by(id=data["product_id"]).first()
    if user and product:
        rental = Rental(user=user,product=product)
        db.session.add(rental)
        db.session.commit()
        user.wallet_balance -=product.rental_price
        db.session.commit()
        return jsonify({"message":"Product rented successfully"})
    return jsonify({"error": "Invalid user or product"}),400


@app.route("Investments", methods=["GET"])
def get_my_investments():
    user_id = request.args.get("user_id")
    investments = Rental.query.filter_by(user_id=user_id).all()
    return jsonify([{"id":r.id,"product_name":
r.product_name,"start_date": r.start_date,"end_date":
r.end_date} for r in rentals])

if _name_ == '_ _main_ _':
    db.create_all()
    app.run(debug=True)

