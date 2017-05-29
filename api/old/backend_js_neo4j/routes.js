const express = require('express');
// const schemas = require('./schemas');
const router = express.Router();
const neo4j = require('neo4j-driver').v1;

router.get('/', (req, res) => {
  res.json({
    yep: 'nope',
  });
});

router.route('/people')
.post((req, res) => {
//   const bear = new Bear();
//   bear.name = req.body.name;
//   bear.save((err) => {
//     if (err) {
//       res.send(err);
//     } else {
//       res.json({ message: 'Bear created!' });
//     }
//   });
  const driver = neo4j.driver('bolt://localhost:7687');
    // neo4j.auth.basic('neo4j', 'neo4j')
  // );
  const session = driver.session();
  session.run('CREATE (a:Person {name: {name}, title: {title}})', {
    name: 'Arthur',
    title: 'King',
  })
  .then(() => session.run('MATCH (a:Person) WHERE a.name = {name} RETURN a.name AS name, a.title AS title', {
    name: 'Arthur',
  }))
  .then(() => { // result
    // console.log(result.records[0].get('title') + ' ' + result.records[0].get('name'));
    console.log('flurm');
    session.close();
    driver.close();
  });
  res.json({});
})
.get((req, res) => {
  // Bear.find((err, bears) => {
  //   if (err) {
  //     res.send(err);
  //   }
  //   res.json(bears);
  //   return bears;
  // });
  const people = [
    {
      name: {
        first: 'Allan',
        last: 'Berry',
      },
      _id: 'asdf1234',
      _updated: '2016-03-03T11:35:00-06:00',
      _created: '2016-03-03T11:35:00-06:00',
      _etag: 'ec5e8200b8fa0596afe9ca71a87f23e71ca30e2d',
      _links: {
        self: {
          href: 'people/asdf1234',
          title: 'person',
        },
      },
    },
    {
      name: {
        first: 'Meg',
        last: 'Duguid',
      },
      _id: 'jklm1234',
      _updated: '2016-03-03T11:35:00-06:00',
      _created: '2016-03-03T11:35:00-06:00',
      _etag: 'ec5e8200b8fa0596afe9ca71a87f23e71ca30e2d',
      _links: {
        self: {
          href: 'people/jklm1234',
          title: 'person',
        },
      },
    },
  ];
  res.json({
    _items: people,
    _meta: {
      max_results: 25,
      total: 1,
      page: 1,
    },
    _links: {
      self: {
        href: 'people',
        title: 'people',
      },
      parent: {
        href: '/',
        title: 'home',
      },
    },
  });
});
// router.route('/bears/:bear_id')
// .get((req, res) => {
//   Bear.findById(req.params.bear_id, (err, bear) => {
//     if (err) {
//       res.send(err);
//     }
//     res.json(bear);
//     return bear;
//   });
// })
// .put((req, res) => {
//   Bear.findById(req.params.bear_id, (err, bear) => {
//     if (err) {
//       res.send(err);
//     }
//     const newBear = Object.create(bear);
//     newBear.name = req.body.name;
//     newBear.save((err2) => {
//       if (err2) {
//         res.send(err);
//       }
//       res.json({
//         message: 'Bear updated!',
//       });
//     });
//   });
// })
// .delete((req, res) => {
//   Bear.remove({
//     _id: req.params.bear_id,
//   }, (err, bear) => {
//     if (err) {
//       res.send(err);
//     }
//     res.json({ message: `Bear ${bear} Successfully deleted` });
//   });
// });

module.exports = router;
