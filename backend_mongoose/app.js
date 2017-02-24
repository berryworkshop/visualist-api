// server.js

//
// Base
//
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const port = process.env.PORT || 9090;
const router = express.Router();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


//
// Start server
//
app.listen(port);
console.log('Magic happens on port ' + port);


//
// Init database
//
const mongoose = require('mongoose');

mongoose.connect('mongodb://localhost:27017/visualist');


//
// Models
//
const Bear = require('./models').Bear



//
// Routes
//

// prefix
app.use('/v1', router);

// middleware (auth, validation, etc.)
router.use((req, res, next) => {
  console.log('Middleware triggered.');
  next();
});

router.get('/', (req, res) => {
  res.json({ message: 'hooray! welcome to our api!' });
});

router.route('/bears')
.post( (req, res) => {
  const bear = new Bear();
  bear.name = req.body.name;
  bear.save(function(err) {
    if (err) {
      res.send(err)
    };
    res.json({ message: 'Bear created!' });
  });
})
.get((req, res) => {
  Bear.find((err, bears) => {
    if (err) {
      res.send(err)
    };
    res.json(bears);
  });
});
