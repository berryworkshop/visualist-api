const express = require('express');
const router = express.Router();
const Bear = require('./models').Bear;

router.get('/', (req, res) => {
  res.json({ message: 'hooray! welcome to our api!' });
});

router.route('/bears')
.post( (req, res) => {
  const bear = new Bear();
  bear.name = req.body.name;
  bear.save((err) => {
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

router.route('/bears/:bear_id')
.get((req, res) => {
  Bear.findById(req.params.bear_id, (err, bear) => {
    if (err) {
      res.send(err);
    }
    res.json(bear);
  });
})
.put((req, res) => {
  Bear.findById(req.params.bear_id, (err, bear) => {
    if (err) { res.send(err); }
    bear.name = req.body.name; // update the bears info
    bear.save((err) => {
      if (err) {
        res.send(err);
      }
      res.json({
        message: 'Bear updated!'
      });
    });
  });
})
.delete((req, res) => {
  Bear.remove({
    _id: req.params.bear_id
  }, (err, bear) => {
    if (err) {
      res.send(err);
    }
    res.json({ message: 'Successfully deleted' });
  });
});

module.exports = router;
