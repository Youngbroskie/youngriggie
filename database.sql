CREATE TABLE Users (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    password TEXT NOT NULL,
    wallet_balance REAL DEFAULT 0.0,
    todays_balance REAL DEFAULT 0.0,
    referral_code TEXT NOT NULL,
    referred_users REAL DEFAULT 0,
    investments TEXT NOT NULL DEFAULT Investments will appear here,
    records TEXT NOT NULL DEFAULT  Records will appear here,
    total_withdrawals REAL DEFAULT 0.0

);


CREATE TABLE Products (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    rental_price REAL NOT NULL,
    rental_period INTEGER NOT NULL -- in days,
    daily_income REAL NOT NULL

);


CREATE TABLE investments (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    start_date DATE NOT NULL DEFAULT
    CURRENT_DATE,
    end_date DATE NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (product_id) REFERENCES products (id)
);


CREATE TABLE Deposits (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    name REAL NOT NULL,
    amount REAL NOT NULL,
    timestamp DATE NOT NULL 
    DEFAULT CURRENT_DATE,
    transaction_id REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES users (id)
    
);


CREATE TABLE Withdrawals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    username REAL NOT NULL,
    amount REAL NOT NULL,
    timestamp DATE NOT NULL 
    DEFAULT CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users (id)
    
);

CREATE TABLE Referrals (
    id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    referred_user_id INTEGER NOT NULL,
    reward_amount REAL NOT NULL DEFAULT 200.0,
    referral_code REAL NOT NULL,
    timestamp DATE NOT NULL DEFAULT
    CURRENT_DATE,
    FOREIGN KEY (user_id) REFERENCES users (id),
    FOREIGN KEY (referred_user_id) REFERENCES
    users (id)
);