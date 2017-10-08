<template>
  <div class="record">
    <img src="https://unsplash.it/g/600/600?blur" alt="">
    <h4><router-link :to="{name: 'record', params: { recordId: 123 }}">{{ data.name }}</router-link></h4>
    <ul>
      <li>label: {{data.label}}</li>
      <li>slug: {{data.slug}}</li>
      <li v-if="data.sublabels">sublabels:
        <ul>
          <li :key="sublabel" v-for="sublabel of data.sublabels">{{ sublabel }}</li>
        </ul>
      </li>
    </ul>

    <p :key="desc.pk" v-for="desc of data.descriptions">{{ desc.value | truncate(250)}}</p>

    <!-- <slot>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Quisquam veniam libero in! Laborum in corrupti alias reprehenderit cumque enim, fugiat velit dolorum, nobis maxime ea veniam. Nam ducimus accusantium aliquam.</p>
    </slot> -->
  </div>
</template>


<script>
export default {
  name: 'record',
  props: [
    'data',
  ],
  filters: {
    truncate(value, length) {
      if (!value) return '';
      const val = value.substring(0, length);
      if (val.length <= value) return val;
      return `${val}...`;
    },
  },
};
</script>


<style lang='scss' scoped>

.record {
  border: 1px solid hsl(0, 0%, 85%);
  background-color: white;
  padding: 10rem 1rem 1rem 1rem;
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
