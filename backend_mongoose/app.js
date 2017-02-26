const express = require('express');
const bodyParser = require('body-parser');
const mongoose = require('mongoose');
const router = require('./routes');

const app = express();
const port = process.env.PORT || 9090;

// base
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


// start
app.listen(port);
console.log(`Magic happens on port ${port}`);


// db
mongoose.connect('mongodb://localhost:27017/visualist');


// routes
app.use('/v1', router);


// middleware (auth, validation, etc.)
router.use((req, res, next) => {
  console.log('Middleware triggered.');
  next();
});
