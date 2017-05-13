const express = require('express');
const bodyParser = require('body-parser');
// const neo4j = require('neo4j-driver');
const router = require('./routes');

const app = express();
const port = process.env.PORT || 9090;

// base
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


// start
app.listen(port);
console.log(`API listening on ${port}`);


// routes
app.use('/v1', router);


// middleware (auth, validation, etc.)
router.use((req, res, next) => {
  console.log('Middleware triggered.');
  next();
});
