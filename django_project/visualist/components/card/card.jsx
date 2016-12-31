import React from 'react'
import ReactDOM from 'react-dom'
require('./card.scss')

ReactDOM.render(
  <div className="card">
    <div className="card_head">
        <h3>Card Name</h3>
    </div>
    <div className="card_body">
        <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
        tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
        quis nostrud exercitation ullamco laboris... </p>
    </div>
  </div>,
  document.getElementById('card_root')
)
