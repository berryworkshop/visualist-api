import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Calendar from '@/components/Calendar';
import Directory from '@/components/Directory';
import Map from '@/components/Map';
import Search from '@/components/Search';
import User from '@/components/User';


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: {
        breadcrumb: 'Home',
      },
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: Calendar,
      meta: {
        breadcrumb: 'Calendar',
      },
    },
    {
      path: '/directory',
      name: 'directory',
      component: Directory,
      meta: {
        breadcrumb: 'Directory',
      },
    },
    {
      path: '/map',
      name: 'map',
      component: Map,
      meta: {
        breadcrumb: 'Map',
      },
    },
    {
      path: '/search',
      name: 'search',
      component: Search,
      meta: {
        breadcrumb: 'Search',
      },
    },
    {
      path: '/user',
      name: 'user',
      component: User,
      meta: {
        breadcrumb: 'User',
      },
    },
  ],
});
