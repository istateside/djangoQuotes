'use strict'

var React = require('react')
var ReactDOM = require('react-dom')
var Quote = require('./Quote.jsx')

require("./style.sass")

ReactDOM.render(
  <Quote />, 
  document.getElementById('react-container')
);