import { URL } from 'url';
// import root from '../pages/root';

// For authoring Nightwatch tests, see
// http://nightwatchjs.org/guide#usage


module.exports = {
  '/': function test(browser) {
    // automatically uses dev Server port from /config.index.js
    // default: http://localhost:8080
    // see nightwatch.conf.js
    const url = new URL('/', browser.globals.devServerURL);

    browser
      .url(url.href)
      .waitForElementVisible('#app', 5000)
      .assert.elementPresent('#console')
      .assert.containsText('h1', 'The Visualist')
      .assert.containsText('p', 'Chicago\'s Visual Arts Calendar')
      .assert.elementPresent('#header')
      .assert.elementPresent('#breadcrumb')
      .assert.elementPresent('#main')
      .assert.elementPresent('#footer')
      .end();
  },
};
