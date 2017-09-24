import { assert } from 'chai';
import Vue from 'vue';
import Console from '@/components/common/Console';


describe('Console.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(Console);
    const vm = new Constructor().$mount();

    assert.equal(
      vm.$el.querySelector('h1').textContent,
      'The Visualist',
    );

    assert.equal(
      vm.$el.querySelector('p').textContent,
      'Chicago\'s Visual Arts Calendar',
    );
  });
});
