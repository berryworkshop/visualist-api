/******/ (function(modules) { // webpackBootstrap
/******/ 	// The module cache
/******/ 	var installedModules = {};
/******/
/******/ 	// The require function
/******/ 	function __webpack_require__(moduleId) {
/******/
/******/ 		// Check if module is in cache
/******/ 		if(installedModules[moduleId])
/******/ 			return installedModules[moduleId].exports;
/******/
/******/ 		// Create a new module (and put it into the cache)
/******/ 		var module = installedModules[moduleId] = {
/******/ 			exports: {},
/******/ 			id: moduleId,
/******/ 			loaded: false
/******/ 		};
/******/
/******/ 		// Execute the module function
/******/ 		modules[moduleId].call(module.exports, module, module.exports, __webpack_require__);
/******/
/******/ 		// Flag the module as loaded
/******/ 		module.loaded = true;
/******/
/******/ 		// Return the exports of the module
/******/ 		return module.exports;
/******/ 	}
/******/
/******/
/******/ 	// expose the modules object (__webpack_modules__)
/******/ 	__webpack_require__.m = modules;
/******/
/******/ 	// expose the module cache
/******/ 	__webpack_require__.c = installedModules;
/******/
/******/ 	// __webpack_public_path__
/******/ 	__webpack_require__.p = "";
/******/
/******/ 	// Load entry module and return exports
/******/ 	return __webpack_require__(0);
/******/ })
/************************************************************************/
/******/ ([
/* 0 */
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var Refs = __webpack_require__(10);
	Vue.component('refs', Refs);
	
	var SecondaryVisuals = Vue.component('secondary_visuals', {
	    template: '\n        <ul>\n            <h3>Secondary Visuals</h3>\n            <mini_tile></mini_tile>\n            <mini_tile></mini_tile>\n            <mini_tile></mini_tile>\n        </ul>'
	});
	
	var MiniTile = Vue.component('mini_tile', {
	    template: '\n        <div>\n            <img class="secondary_visual" />\n            <p>This is a caption.</p>\n        </div>'
	});
	
	var RelatedItems = Vue.component('related_items', {
	    template: '\n        <ul>\n            <h3>Related Items</h3>\n            <ul>\n                <li>Related Item</li>\n                <li>Related Item</li>\n                <li>Related Item</li>\n            </ul>\n        </ul>\n    '
	});
	
	var Controls = Vue.component('controls', {
	    template: '\n        <div>\n            <h3>Controls</h3>\n            <ul>\n                <li>New</li>\n                <li>Edit</li>\n                <li>Delete</li>\n                <li>Map it</li>\n                <li>Featured</li>\n                <li>Bookmark</li>\n                <li>Add to Bucket List</li>\n                <li>\n                    <h4>Cite</h4>\n                    <ul>\n                        <li>APA</li>\n                        <li>Chicago</li>\n                        <li>MLA</li>\n                    </ul>\n                </li>\n                <li>\n                    <h4>Permissions</h4>\n                    <ul>\n                        <li>Public</li>\n                        <li>Private</li>\n                    </ul>\n                </li>\n                <li>\n                    <h4>Share</h4>\n                    <ul>\n                        <li>Email</li>\n                        <li>Facebook</li>\n                        <li>Pinterest</li>\n                    </ul>\n                </li>\n                <li>\n                    <h4>Add to List</h4>\n                    <ul>\n                        <li>Checklist</li>\n                        <li>Bookmarks</li>\n                    </ul>\n                </li>\n            </ul>\n        </div>'
	});
	
	var event = new Vue({
	    delimiters: ['[{', '}]'],
	    el: 'main',
	    data: {
	        obj: {
	            title: '',
	            date_start: 'January 1, 2014',
	            date_end: false,
	            description: 'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod\n            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,\n            quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo\n            consequat. Duis aute irure dolor in reprehenderit.'
	        },
	        components: [SecondaryVisuals, MiniTile, Refs, RelatedItems, Controls]
	    },
	    mounted: function mounted() {
	        $.ajax({
	            context: this,
	            url: "/timeline/events/1.json"
	        }).done(function (data) {
	            this.obj.title = data.name;
	        });
	    }
	});

/***/ },
/* 1 */,
/* 2 */,
/* 3 */,
/* 4 */,
/* 5 */,
/* 6 */,
/* 7 */,
/* 8 */,
/* 9 */,
/* 10 */
/***/ function(module, exports, __webpack_require__) {

	var __vue_exports__, __vue_options__
	var __vue_styles__ = {}
	
	/* script */
	__vue_exports__ = __webpack_require__(11)
	
	/* template */
	var __vue_template__ = __webpack_require__(12)
	__vue_options__ = __vue_exports__ = __vue_exports__ || {}
	if (
	  typeof __vue_exports__.default === "object" ||
	  typeof __vue_exports__.default === "function"
	) {
	if (Object.keys(__vue_exports__).some(function (key) { return key !== "default" && key !== "__esModule" })) {console.error("named exports are not supported in *.vue files.")}
	__vue_options__ = __vue_exports__ = __vue_exports__.default
	}
	if (typeof __vue_options__ === "function") {
	  __vue_options__ = __vue_options__.options
	}
	__vue_options__.__file = "/Users/aljabear/Projects/visualist/django_project/visualist/templates/visualist/components/Refs.vue"
	__vue_options__.render = __vue_template__.render
	__vue_options__.staticRenderFns = __vue_template__.staticRenderFns
	
	/* hot reload */
	if (false) {(function () {
	  var hotAPI = require("vue-hot-reload-api")
	  hotAPI.install(require("vue"), false)
	  if (!hotAPI.compatible) return
	  module.hot.accept()
	  if (!module.hot.data) {
	    hotAPI.createRecord("data-v-4376b818", __vue_options__)
	  } else {
	    hotAPI.reload("data-v-4376b818", __vue_options__)
	  }
	})()}
	if (__vue_options__.functional) {console.error("[vue-loader] Refs.vue: functional components are not supported and should be defined in plain js files using render functions.")}
	
	module.exports = __vue_exports__


/***/ },
/* 11 */
/***/ function(module, exports) {

	'use strict';
	
	Object.defineProperty(exports, "__esModule", {
	  value: true
	});
	//
	//
	//
	//
	//
	//
	//
	//
	//
	//
	//
	
	exports.default = {
	  name: 'refs',
	  data: function data() {
	    return {
	      title: 'Cross References'
	    };
	  }
	};

/***/ },
/* 12 */
/***/ function(module, exports, __webpack_require__) {

	module.exports={render:function (){var _vm=this;var _h=_vm.$createElement;var _c=_vm._self._c||_h;
	  return _c('ul', [_c('h3', [_vm._v(_vm._s(_vm.title))]), _vm._v(" "), _c('li', [_vm._v("Getty")]), _vm._v(" "), _c('li', [_vm._v("Art Institute of Chicago")]), _vm._v(" "), _c('li', [_vm._v("Library of Congress")]), _vm._v(" "), _c('li', [_vm._v("Artnet")]), _vm._v(" "), _c('li', [_vm._v("Chicago Gallery News")])])
	},staticRenderFns: []}
	module.exports.render._withStripped = true
	if (false) {
	  module.hot.accept()
	  if (module.hot.data) {
	     require("vue-hot-reload-api").rerender("data-v-4376b818", module.exports)
	  }
	}

/***/ }
/******/ ]);
//# sourceMappingURL=event.js.map