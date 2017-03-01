// The Vue build version to load with the `import` command
// (runtime-only or standalone) has been set in webpack.base.conf with an alias.
import Vue from 'vue';
import VueRouter from 'vue-router';
import Vuex from 'vuex';
import App from './App';

import Home from './components/Home';
import Error403 from './components/Error403';
import Error404 from './components/Error404';
import Login from './components/Login';
import Search from './components/Search';
import NodeList from './components/NodeList';
// import Artists from './components/Artists';
// import Artworks from './components/Artworks';
// import Events from './components/Events';
// import Venues from './components/Venues';

Vue.use(VueRouter);
Vue.use(Vuex);

const routes = [
  { path: '/', component: Home },
  { path: '/403', component: Error403 },
  { path: '/404', component: Error404 },
  { path: '/login', component: Login },
  { path: '/search', component: Search },
  { path: '/nodes', component: NodeList },
  // { path: '/events', component: EventList }, // Events },
  // { path: '/artists', component: NodeList }, // Artists },
  // { path: '/artworks', component: NodeList }, // Artworks },
  // { path: '/venues', component: NodeList }, // Venues },
];

const store = new Vuex.Store({
  state: {
    site: {
      rightsStatement: 'All rights reserved, unless otherwise specified.',
      logo: '<image_id>',
      version: 0.1,
      primaryNav: {
        home: '/',
        events: '/',
        artists: '/',
        venues: '/',
        search: '/',
        help: '/',
      },
      secondaryNav: {
        rights: '/',
        privacy: '/',
        sitemap: '/',
        links: '/',
        archive: '/',
      },
    },
    page: {
      title: 'The Visualist',
      subtitle: 'This is the subtitle.',
      description: 'Aute eu deserunt sit aliquip veniam Lorem duis anim excepteur. Velit incididunt officia irure dolor voluptate quis elit et consectetur. Nostrud occaecat aliqua exercitation elit id duis mollit do ad ipsum irure esse velit consectetur.',
    },
  },
});

const router = new VueRouter({
  routes, // short for routes: routes
  mode: 'history',
});

/* eslint-disable no-new */
new Vue({
  router,
  el: '#app',
  template: '<App/>',
  components: { App },
  store,
});
