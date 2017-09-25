<template>
  <div class="record">
    <h4>{{ data.label }}: {{ data.slug }}</h4>
    <slot>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam veniam libero in! Laborum in corrupti alias reprehenderit cumque enim, fugiat velit dolorum, nobis maxime ea veniam. Nam ducimus accusantium aliquam.</p>
    </slot>
  </div>
</template>


<script>
export default {
  name: 'record',
  props: [
    'data',
  ],
};
</script>


<style lang='scss' scoped>

.record {
  border: 1px solid hsl(0, 0%, 85%);
  background-color: white;
  padding-left: 1rem;
  padding-right: 1rem;
}

</style>
