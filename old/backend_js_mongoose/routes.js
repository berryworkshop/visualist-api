const express = require('express');
const Bear = require('./models').Bear;

const router = express.Router();

router.get('/', (req, res) => {
  res.json({
    _links: {
      child: [
        {
          href: 'bears',
          title: 'bears',
        },
      ],
    },
  });
});

router.route('/bears')
.post((req, res) => {
  const bear = new Bear();
  bear.name = req.body.name;
  bear.save((err) => {
    if (err) {
      res.send(err);
    } else {
      res.json({ message: 'Bear created!' });
    }
  });
})
.get((req, res) => {
  Bear.find((err, bears) => {
    if (err) {
      res.send(err);
    }
    res.json(bears);
    return bears;
  });
});

router.route('/bears/:bear_id')
.get((req, res) => {
  Bear.findById(req.params.bear_id, (err, bear) => {
    if (err) {
      res.send(err);
    }
    res.json(bear);
    return bear;
  });
})
.put((req, res) => {
  Bear.findById(req.params.bear_id, (err, bear) => {
    if (err) {
      res.send(err);
    }
    const newBear = Object.create(bear);
    newBear.name = req.body.name;
    newBear.save((err2) => {
      if (err2) {
        res.send(err);
      }
      res.json({
        message: 'Bear updated!',
      });
    });
  });
})
.delete((req, res) => {
  Bear.remove({
    _id: req.params.bear_id,
  }, (err, bear) => {
    if (err) {
      res.send(err);
    }
    res.json({ message: `Bear ${bear} Successfully deleted` });
  });
});

module.exports = router;
