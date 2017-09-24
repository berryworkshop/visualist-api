<template>
  <div class="hello">
	<!-- Header -->
			<vis-header></vis-header>

		<!-- Main -->
			<div id="main">

				<!-- One -->
        <section-one></section-one>

				<!-- Two -->
				<section-two></section-two>

				<!-- Three -->
				<section-three></section-three>

				<!-- Four -->
				<section-four></section-four>

			</div>

		<!-- Footer -->
      <vis-footer></vis-footer>

      <!-- Scripts -->

      <!-- <script src="../assets/js/jquery.min.js"></script>
			<script src="../assets/js/jquery.poptrox.min.js"></script>
			<script src="../assets/js/skel.min.js"></script>
			<script src="../assets/js/util.js"></script>
			<script src="../assets/js/main.js"></script> -->

  </div>
</template>

<script>
import VisHeader from './Header';
import VisFooter from './Footer';
import SectionOne from './SectionOne';
import SectionTwo from './SectionTwo';
import SectionThree from './SectionThree';
import SectionFour from './SectionFour';

export default {
  name: 'hello',
  components: {
    VisHeader,
    VisFooter,
    SectionOne,
    SectionTwo,
    SectionThree,
    SectionFour,
  },
  data() {
    return {
      msg: 'Welcome to Your Vue.js App',
    };
  },
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style lang='scss'>
@import '../assets/css/main.css';


h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
