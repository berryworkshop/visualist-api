import { assert } from 'chai';
import Vue from 'vue';
import VisFooter from '@/components/common/VisFooter';


describe('VisFooter.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(VisFooter);
    const vm = new Constructor().$mount();

    assert.equal(
      vm.$el.querySelector('p').textContent,
      'Footer',
    );
  });
});
