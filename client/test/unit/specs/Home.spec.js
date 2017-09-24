import { assert } from 'chai';
import Vue from 'vue';
import Home from '@/components/Home';


describe('Home.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Home);
    const vm = new Constructor().$mount();

    assert.equal(
      vm.$el.querySelector('h2').textContent,
      'Welcome to the Visualist.',
    );
  });
});
