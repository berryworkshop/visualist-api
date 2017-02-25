const mongoose = require('mongoose');
const Schema = mongoose.Schema;

const BearSchema = new Schema({
  name: String
}, { strict: true });

module.exports = {
    Bear: mongoose.model('Bear', BearSchema)
};
