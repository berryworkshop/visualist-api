<template>
  <div class="record">
    <img src="https://unsplash.it/g/600/600?blur" alt="">
    <h4>{{ data.name }}</h4>
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
  padding: 10rem 1rem 0 1rem;
  position: relative;

  img {
    max-height: 10rem;
    object-fit: cover;
    position: absolute;
    left: 0;
    right: 0;
    top: 0;
    width: 100%;
  }
}

</style>
