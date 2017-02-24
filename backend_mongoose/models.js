var mongoose = require('mongoose');
var Schema = mongoose.Schema;
var BearSchema = new Schema({
  name: String
});

module.exports = {
    Bear: mongoose.model('Bear', BearSchema)
};
