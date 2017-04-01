// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import App from './App';

import Atlas from './pages/Atlas';
import Calendar from './pages/Calendar';
import Error403 from './pages/Error403';
import Error404 from './pages/Error404';
import Event from './pages/Event';
import Home from './pages/Home';
import List from './pages/List';
import Login from './pages/Login';
import Organization from './pages/Organization';
import Search from './pages/Search';

Vue.use(VueRouter);
Vue.use(Vuex);

const routes = [
  { name: 'atlas', path: '/atlas', component: Atlas },
  { name: 'calendar', path: '/calendar', component: Calendar },
  { name: '403', path: '/403', component: Error403 },
  { name: '404', path: '/404', component: Error404 },
  { name: 'home', path: '/', component: Home },
  { name: 'list', path: '/list', component: List },
  { name: 'login', path: '/login', component: Login },
  { name: 'search', path: '/search', component: Search },

  { name: 'event-list', path: '/events', component: List },
  { name: 'event', path: '/events/:event_id', component: Event },

  { name: 'organization-list', path: '/orgs', component: List },
  { name: 'organization', path: '/orgs/:organization_id', component: Organization },
];

const siteDefaults = {};
const pageDefaults = {};

const store = new Vuex.Store({
  state: {
    site: siteDefaults,
    page: pageDefaults,
  },
  mutations: {
  /* eslint-disable no-param-reassign */
    resetPageData(state) {
      state.page = pageDefaults;
    },
    setPageData(state, payload) {
      state.page = payload;
    },
  /* eslint-enable no-param-reassign */
  },
});

const router = new VueRouter({
  routes, // short for routes: routes
  mode: 'history',
});

module.exports = new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: { App },
  store,
});
