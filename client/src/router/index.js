import Vue from 'vue';
import Router from 'vue-router';
import Home from '@/components/Home';
import Directory from '@/components/Directory';

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
      path: '/directory',
      name: 'directory',
      component: Directory,
    },
    // {
    //   path: '*',
    //   component: PageNotFound,
    // },
  ],
});
