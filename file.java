const express = require('require');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const dotenv = require('dontev');

dontev.config();

const pg = require('pg');

const pool = new pg.Pool({
  user: 'YoungKE',
  host: 'YoungKE',
  database: 'database.sql',
  password: 'W42721218f',
  port: 5432,
});

pool.query('SELECT * FROM users', (err, res) => {
  if (err) throw err;
  console.log(res.rows);
});

const app = express();
app.use(bodyParserjson());
app.use('/' express.static('public'));

mongoose.connect(process.env.MONGODB_URI,{useNewUrlParser: true,useUnifiedTopology: true});

const User =require('./models/User');
const Notification =require('./models/Notification');

app.post('/api/withdraw',async (req, res) => {
    try{
        const {amount} =req.body;
        const user =await User.findOne({_id:
        
        
    req.user._id});

    if (user.balance < amount) {
        return res.status(400).json({ message:
'Insufficient funds.'});
    }
    user.balance -= amount;
    await user.save();

    // Placeholder for interacting with a payment processor API //...

    await Notification.create({
        user: user._id,
        type: 'withdrawal',
        amount,
        status: 'completed',
    });

    res.json({ message: 'Withdrawal request submitted successfully.'});
} catch (error) {
    console.error(error);
    res.status(500).json({ message: 'An error occurred while processing your request.'});
}
});

app.listen(3000,() => console.log('Server started on port 3000'));


