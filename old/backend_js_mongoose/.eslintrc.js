module.exports = {
  root: true,
  // parser: 'babel-eslint',
  parserOptions: {
    sourceType: 'module'
  },
  extends: 'airbnb-base',
  plugins: [
    'import'
  ],
  // add your custom rules here
  'rules': {
    // allow debugger during development
    'no-debugger': process.env.NODE_ENV === 'production' ? 2 : 0,
    // it's too damn useful to have the console available
    'no-console': 0,
    // wtf dangling underscores are everywhere
    'no-underscore-dangle': 0,
  }
}
