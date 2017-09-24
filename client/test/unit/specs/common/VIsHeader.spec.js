import { assert } from 'chai';
import Vue from 'vue';
import VisHeader from '@/components/common/VisHeader';


describe('VisHeader.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(VisHeader);
    const vm = new Constructor().$mount();

    assert.equal(
      vm.$el.querySelector('p').textContent,
      'Header',
    );
  });
});
