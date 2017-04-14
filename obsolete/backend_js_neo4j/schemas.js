function Schema(schema, base) {
  this.schema = Object.assign(schema, base);
}

const base = new Schema({
  name: {
    type: 'string',
  },
  synopsis: {
    type: 'string',
  },
});

const person = new Schema({
  name: {
    type: 'dict',
    schema: {
      first: {
        type: 'string',
      },
      last: {
        type: 'string',
        required: true,
      },
    },
  },
}, base);

module.exports = {
  person,
};
