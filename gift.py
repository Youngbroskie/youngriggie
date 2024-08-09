rom sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

# Replace with your database connection string
engine = create_engine('postgresql://user:password@host:port/database')
Session = sessionmaker(bind=engine)
session = Session()

# Example query
result = session.query(User).filter_by(id=1).first()

from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(_name_)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class User(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  username = db.Column(db.String(80), unique=True, nullable=False)
  balance = db.Column(db.Float, default=0.0)

class Transaction(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  type = db.Column(db.String(20))  # deposit, withdrawal
  amount = db.Column(db.Float)
  status = db.Column(db.String(20), default='pending')  # pending, completed

gift_codes = { 
  '3cd45ed5c7': {'amount': 30, 'used': False},
  '5ad79kc': {'amount': 50, 'used': False},
  '73bd546dk': {'amount': 70,'used': False},
  '5a68ecgd6': {'amount': 100, 'used': False},
  '34c6efj7': {'amount': 200, 'used': False},
  'xsg77276gx': {'amount': 300,'used': False},
  '74vc37ct36': {'amount': 41, 'used':False},
  '2w3gag52': {'amount': 27, 'used':False},
  
}

@app.before_first_request
def create_tables():
  db.create_all()

def redeem_gift_code(code, user_id):
  if code in gift_codes and not gift_codes[code]['used']:
    gift_codes[code]['used'] = True  # Mark code as used
    user_data['wallet_balance'] += gift_codes[code]['amount']
    return f"Gift code redeemed! You received {gift_codes[code]['amount']} KES."
  else:
    return "Invalid or used gift code."
