const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = process.env.PORT || 9090;

// base
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


// start
app.listen(port);
console.log('Magic happens on port ' + port);


// db
const mongoose = require('mongoose');
mongoose.connect('mongodb://localhost:27017/visualist');


// routes
const router = require('./routes');
app.use('/v1', router);


// middleware (auth, validation, etc.)
router.use((req, res, next) => {
  console.log('Middleware triggered.');
  next();
});
