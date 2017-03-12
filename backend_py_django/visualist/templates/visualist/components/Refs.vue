<template>
    <ul>
        <h3>{{ title }}</h3>
        <li>Getty</li>
        <li>Art Institute of Chicago</li>
        <li>Library of Congress</li>
        <li>Artnet</li>
        <li>Chicago Gallery News</li>
    </ul>
</template>

<script>
    export default {
      name: 'refs',
      data() {
        return {
          title: 'Cross References'
        }
      }
    }
</script>