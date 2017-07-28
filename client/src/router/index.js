import Vue from 'vue';
import Router from 'vue-router';
import Calendar from '../components/Calendar.vue';
import Directory from '../components/Directory.vue';
import Home from '../components/Home.vue';
import Login from '../components/Login.vue';
import Map_ from '../components/Map.vue';
import Profile from '../components/Profile.vue';
// import Record from '../components/Record.vue';
import ResultList from '../components/ResultList.vue';
import SiteMap from '../components/Sitemap.vue';


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
