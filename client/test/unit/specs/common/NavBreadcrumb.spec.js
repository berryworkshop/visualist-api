import { assert } from 'chai';
import Vue from 'vue';
import NavBreadcrumb from '@/components/common/NavBreadcrumb';


describe('NavBreadcrumb.vue', () => {
  it('should render correct contents', () => {
    const Constructor = Vue.extend(NavBreadcrumb);
    const vm = new Constructor().$mount();

    assert.equal(
      vm.$el.querySelector('p').textContent,
      'Breadcrumb',
    );
  });
});
