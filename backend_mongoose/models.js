const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const BearSchema = new Schema({
  name: String
});

module.exports = {
    Bear: mongoose.model('Bear', BearSchema)
};
