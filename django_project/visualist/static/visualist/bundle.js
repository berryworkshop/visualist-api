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
/******/ ({

/***/ 0:
/***/ function(module, exports, __webpack_require__) {

	module.exports = __webpack_require__(9);


/***/ },

/***/ 9:
/***/ function(module, exports) {

	"use strict";
	
	// Shorthand for $( document ).ready()
	$(function () {
	    var state = {
	        browse_modal: false
	    };
	
	    // controls
	    $('.browse_modal_toggle').on("click", toggle_browse_modal);
	
	    // esc key
	    // hat tip http://stackoverflow.com/a/3369743/652626
	    document.onkeydown = function (evt) {
	        evt = evt || window.event;
	        var isEscape = false;
	        if ("key" in evt) {
	            isEscape = evt.key == "Escape" || evt.key == "Esc";
	        } else {
	            isEscape = evt.keyCode == 27;
	        }
	        if (isEscape) {
	            state.browse_modal = false;
	        }
	        update_state();
	    };
	
	    function toggle_browse_modal() {
	        var x = state.browse_modal;
	        state.browse_modal = x == true ? false : true;
	        update_state();
	    }
	
	    function update_state() {
	        // browse modal
	        if (state.browse_modal == true) {
	            $('#browse_modal').removeClass('visually_hidden');
	        } else {
	            $('#browse_modal').addClass('visually_hidden');
	        }
	    }
	});

/***/ }

/******/ });
//# sourceMappingURL=bundle.js.map