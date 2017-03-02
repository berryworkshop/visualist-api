<template>
  <div class="modal">
    <div class="body">
      <p>This is a modal.</p>
      <p>Incididunt proident dolore duis ut ipsum sint magna ex officia do. Labore excepteur enim eiusmod incididunt aliqua dolore consequat laborum pariatur. Qui ullamco fugiat Lorem nulla ipsum sint amet consectetur. Pariatur occaecat cillum mollit magna eu officia elit aliqua sunt non eu cupidatat.</p>

      <p>Incididunt proident dolore duis ut ipsum sint magna ex officia do. Labore excepteur enim eiusmod incididunt aliqua dolore consequat laborum pariatur. Qui ullamco fugiat Lorem nulla ipsum sint amet consectetur. Pariatur occaecat cillum mollit magna eu officia elit aliqua sunt non eu cupidatat.</p>

      <p>Incididunt proident dolore duis ut ipsum sint magna ex officia do. Labore excepteur enim eiusmod incididunt aliqua dolore consequat laborum pariatur. Qui ullamco fugiat Lorem nulla ipsum sint amet consectetur. Pariatur occaecat cillum mollit magna eu officia elit aliqua sunt non eu cupidatat.</p>

      <p>Incididunt proident dolore duis ut ipsum sint magna ex officia do. Labore excepteur enim eiusmod incididunt aliqua dolore consequat laborum pariatur. Qui ullamco fugiat Lorem nulla ipsum sint amet consectetur. Pariatur occaecat cillum mollit magna eu officia elit aliqua sunt non eu cupidatat.</p>

      <p>Incididunt proident dolore duis ut ipsum sint magna ex officia do. Labore excepteur enim eiusmod incididunt aliqua dolore consequat laborum pariatur. Qui ullamco fugiat Lorem nulla ipsum sint amet consectetur. Pariatur occaecat cillum mollit magna eu officia elit aliqua sunt non eu cupidatat.</p>
    </div>
  </div>
</template>

<script>
export default {
  name: 'modal',
  data() {
    return {};
  },
};
</script>

<style lang="scss" scoped>
  @import "../styles/brand.scss";
  @import "../styles/grid.scss";

  .modal {
    position: fixed;
    width: 100vw;
    height: 100vh;
    background-color: hsla(0, 0, 0, .75);
    z-index: 10;
    .body {
      background-color: $primary_bg;
      z-index: 11;

      @include sm_only {
        max-height: calc(100% - 7rem);
        max-width: calc(100% - 4rem);
        position: fixed;
        top: 5rem;
        left: 2rem;
      }

      @include md_up {
        max-height: calc(100% - 10rem);
        position: fixed;
        top: 50%;
        left: 25%;
        transform: translate(-16.66%, -50%);
      }
      overflow-y: scroll;
      padding: 1rem;
      border: 2px solid silver;
    }
  }
</style>
