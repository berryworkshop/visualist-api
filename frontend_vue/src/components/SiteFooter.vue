<template>
  <footer id="site-footer">
    <div class="container">
      <p>Copyright © {{ year }}, <a>Culture/Math</a>. All rights reserved.</p>
      <p>Website by <a href="http://berryworkshop.com">Berry Catalog Workshop</a>.</p>
      <ul>
        <li>Rights</li>
        <li>About</li>
        <li>Colophon</li>
      </ul>
    </div>
  </footer>
</template>

<script>
export default {
  name: 'site-footer',
  data() {
    return {
      year: 2016,
    };
  },
};
</script>

<style lang="scss" scoped>
  footer#site-footer {
    background-color: #222;
    color: #777;
    padding-bottom: 8rem;
    
    a {
      color: #a60;
      text-decoration: none;
    }
  }
</style>
