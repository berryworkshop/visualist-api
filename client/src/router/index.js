import Vue from 'vue';
import Router from 'vue-router';
import Calendar from '@/components/Calendar';
import Directory from '@/components/Directory';
import Home from '@/components/Home';
import Login from '@/components/Login';
import Map_ from '@/components/Map';
import Profile from '@/components/Profile';
// import Record from '@/components/Record';
import ResultList from '@/components/ResultList';
import SiteMap from '@/components/Sitemap';


Vue.use(Router);

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
    },
    {
      path: '/calendar',
      name: 'calendar',
      component: Calendar,
    },
    {
      path: '/directory',
      name: 'directory',
      component: Directory,
    },
    {
      path: '/login',
      name: 'login',
      component: Login,
    },
    {
      path: '/map',
      name: 'map',
      component: Map_,
    },
    {
      path: '/profile',
      name: 'profile',
      component: Profile,
    },
    {
      path: '/search',
      name: 'search',
      component: ResultList,
    },
    {
      path: '/sitemap',
      name: 'sitemap',
      component: SiteMap,
    },
  ],
});
