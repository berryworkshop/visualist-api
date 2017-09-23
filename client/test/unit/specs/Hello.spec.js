import { assert } from 'chai';
import Vue from 'vue';
import Hello from '@/components/Hello';


describe('Hello.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Hello);
    const vm = new Constructor().$mount();
    assert.equal(
      vm.$el.querySelector('.hello h1').textContent,
      'Welcome to Your Vue.js App',
    );
  });
});
