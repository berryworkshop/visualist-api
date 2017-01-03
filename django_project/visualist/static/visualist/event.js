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

	module.exports = __webpack_require__(15);


/***/ },

/***/ 15:
/***/ function(module, exports, __webpack_require__) {

	'use strict';
	
	var _createClass = function () { function defineProperties(target, props) { for (var i = 0; i < props.length; i++) { var descriptor = props[i]; descriptor.enumerable = descriptor.enumerable || false; descriptor.configurable = true; if ("value" in descriptor) descriptor.writable = true; Object.defineProperty(target, descriptor.key, descriptor); } } return function (Constructor, protoProps, staticProps) { if (protoProps) defineProperties(Constructor.prototype, protoProps); if (staticProps) defineProperties(Constructor, staticProps); return Constructor; }; }();
	
	var _react = __webpack_require__(16);
	
	var _react2 = _interopRequireDefault(_react);
	
	var _reactDom = __webpack_require__(17);
	
	var _reactDom2 = _interopRequireDefault(_reactDom);
	
	function _interopRequireDefault(obj) { return obj && obj.__esModule ? obj : { default: obj }; }
	
	function _classCallCheck(instance, Constructor) { if (!(instance instanceof Constructor)) { throw new TypeError("Cannot call a class as a function"); } }
	
	function _possibleConstructorReturn(self, call) { if (!self) { throw new ReferenceError("this hasn't been initialised - super() hasn't been called"); } return call && (typeof call === "object" || typeof call === "function") ? call : self; }
	
	function _inherits(subClass, superClass) { if (typeof superClass !== "function" && superClass !== null) { throw new TypeError("Super expression must either be null or a function, not " + typeof superClass); } subClass.prototype = Object.create(superClass && superClass.prototype, { constructor: { value: subClass, enumerable: false, writable: true, configurable: true } }); if (superClass) Object.setPrototypeOf ? Object.setPrototypeOf(subClass, superClass) : subClass.__proto__ = superClass; }
	
	var Event = function (_React$Component) {
	    _inherits(Event, _React$Component);
	
	    function Event() {
	        _classCallCheck(this, Event);
	
	        return _possibleConstructorReturn(this, (Event.__proto__ || Object.getPrototypeOf(Event)).apply(this, arguments));
	    }
	
	    _createClass(Event, [{
	        key: 'render',
	        value: function render() {
	            var style = {
	                "backgroundColor": 'white'
	            };
	            return _react2.default.createElement(
	                'div',
	                { style: style },
	                _react2.default.createElement(
	                    'h1',
	                    null,
	                    'This is an awesome event.'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Other titles'
	                ),
	                _react2.default.createElement(
	                    'h2',
	                    null,
	                    'Friday, January 6, 2017'
	                ),
	                _react2.default.createElement(
	                    'h2',
	                    null,
	                    'Chicago Artist Coalition'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    '1234 Anywhere St.'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Chicago, IL 60600'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Distance to this event from your current location: 123 miles'
	                ),
	                _react2.default.createElement('img', { className: 'primary_visual' }),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'This is a caption for the above visual.'
	                ),
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    'Description'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'
	                ),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Other Descriptions'
	                ),
	                _react2.default.createElement(SecondaryVisuals, { title: 'Other Images' }),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'Record created by admin on January 1, 2017'
	                ),
	                _react2.default.createElement(Sources, null),
	                _react2.default.createElement(CrossReferences, null),
	                _react2.default.createElement(RelatedItems, { title: 'Related Items' }),
	                _react2.default.createElement(RelatedItems, { title: 'Similar Items' }),
	                _react2.default.createElement(Controls, null)
	            );
	        }
	    }]);
	
	    return Event;
	}(_react2.default.Component);
	
	var SecondaryVisuals = function (_React$Component2) {
	    _inherits(SecondaryVisuals, _React$Component2);
	
	    function SecondaryVisuals() {
	        _classCallCheck(this, SecondaryVisuals);
	
	        return _possibleConstructorReturn(this, (SecondaryVisuals.__proto__ || Object.getPrototypeOf(SecondaryVisuals)).apply(this, arguments));
	    }
	
	    _createClass(SecondaryVisuals, [{
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'ul',
	                null,
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    this.props.title
	                ),
	                _react2.default.createElement('img', { className: 'secondary_visual' }),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'This is a caption.'
	                ),
	                _react2.default.createElement('img', { className: 'secondary_visual' }),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'This is a caption.'
	                ),
	                _react2.default.createElement('img', { className: 'secondary_visual' }),
	                _react2.default.createElement(
	                    'p',
	                    null,
	                    'This is a caption.'
	                )
	            );
	        }
	    }]);
	
	    return SecondaryVisuals;
	}(_react2.default.Component);
	
	var Sources = function (_React$Component3) {
	    _inherits(Sources, _React$Component3);
	
	    function Sources() {
	        _classCallCheck(this, Sources);
	
	        return _possibleConstructorReturn(this, (Sources.__proto__ || Object.getPrototypeOf(Sources)).apply(this, arguments));
	    }
	
	    _createClass(Sources, [{
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    'Sources'
	                ),
	                _react2.default.createElement(
	                    'dl',
	                    null,
	                    _react2.default.createElement(
	                        'dd',
	                        null,
	                        'Source'
	                    ),
	                    _react2.default.createElement(
	                        'dt',
	                        null,
	                        'The Art Institute of Chicago'
	                    ),
	                    _react2.default.createElement(
	                        'dd',
	                        null,
	                        'Format'
	                    ),
	                    _react2.default.createElement(
	                        'dt',
	                        null,
	                        'Website'
	                    ),
	                    _react2.default.createElement(
	                        'dd',
	                        null,
	                        'Accessed'
	                    ),
	                    _react2.default.createElement(
	                        'dt',
	                        null,
	                        'January 1, 2017'
	                    ),
	                    _react2.default.createElement(
	                        'dd',
	                        null,
	                        'Rights'
	                    ),
	                    _react2.default.createElement(
	                        'dt',
	                        null,
	                        'Public Domain'
	                    )
	                )
	            );
	        }
	    }]);
	
	    return Sources;
	}(_react2.default.Component);
	
	var CrossReferences = function (_React$Component4) {
	    _inherits(CrossReferences, _React$Component4);
	
	    function CrossReferences() {
	        _classCallCheck(this, CrossReferences);
	
	        return _possibleConstructorReturn(this, (CrossReferences.__proto__ || Object.getPrototypeOf(CrossReferences)).apply(this, arguments));
	    }
	
	    _createClass(CrossReferences, [{
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    'Cross References'
	                ),
	                _react2.default.createElement(
	                    'ul',
	                    null,
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Getty'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Art Institute of Chicago'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Library of Congress'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Artnet'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Chicago Gallery News'
	                    )
	                )
	            );
	        }
	    }]);
	
	    return CrossReferences;
	}(_react2.default.Component);
	
	var RelatedItems = function (_React$Component5) {
	    _inherits(RelatedItems, _React$Component5);
	
	    function RelatedItems() {
	        _classCallCheck(this, RelatedItems);
	
	        return _possibleConstructorReturn(this, (RelatedItems.__proto__ || Object.getPrototypeOf(RelatedItems)).apply(this, arguments));
	    }
	
	    _createClass(RelatedItems, [{
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    this.props.title
	                ),
	                _react2.default.createElement(
	                    'ul',
	                    null,
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Related Item'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Related Item'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Related Item'
	                    )
	                )
	            );
	        }
	    }]);
	
	    return RelatedItems;
	}(_react2.default.Component);
	
	var Controls = function (_React$Component6) {
	    _inherits(Controls, _React$Component6);
	
	    function Controls() {
	        _classCallCheck(this, Controls);
	
	        return _possibleConstructorReturn(this, (Controls.__proto__ || Object.getPrototypeOf(Controls)).apply(this, arguments));
	    }
	
	    _createClass(Controls, [{
	        key: 'render',
	        value: function render() {
	            return _react2.default.createElement(
	                'div',
	                null,
	                _react2.default.createElement(
	                    'h3',
	                    null,
	                    'Controls'
	                ),
	                _react2.default.createElement(
	                    'ul',
	                    null,
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'New'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Edit'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Delete'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Map it'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Featured'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Bookmark'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        'Add to Bucket List'
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        _react2.default.createElement(
	                            'h4',
	                            null,
	                            'Cite'
	                        ),
	                        _react2.default.createElement(
	                            'ul',
	                            null,
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'APA'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Chicago'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'MLA'
	                            )
	                        )
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        _react2.default.createElement(
	                            'h4',
	                            null,
	                            'Permissions'
	                        ),
	                        _react2.default.createElement(
	                            'ul',
	                            null,
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Public'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Private'
	                            )
	                        )
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        _react2.default.createElement(
	                            'h4',
	                            null,
	                            'Share'
	                        ),
	                        _react2.default.createElement(
	                            'ul',
	                            null,
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Email'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Facebook'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Pinterest'
	                            )
	                        )
	                    ),
	                    _react2.default.createElement(
	                        'li',
	                        null,
	                        _react2.default.createElement(
	                            'h4',
	                            null,
	                            'Add to List'
	                        ),
	                        _react2.default.createElement(
	                            'ul',
	                            null,
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Checklist'
	                            ),
	                            _react2.default.createElement(
	                                'li',
	                                null,
	                                'Bookmarks'
	                            )
	                        )
	                    )
	                )
	            );
	        }
	    }]);
	
	    return Controls;
	}(_react2.default.Component);
	
	_reactDom2.default.render(_react2.default.createElement(Event, null), document.getElementById('app_root'));

/***/ },

/***/ 16:
/***/ function(module, exports) {

	module.exports = React;

/***/ },

/***/ 17:
/***/ function(module, exports) {

	module.exports = ReactDOM;

/***/ }

/******/ });
//# sourceMappingURL=event.js.map