import React from 'react'
import ReactDOM from 'react-dom'
require('./card.scss')

export default class Card extends React.Component {
  render() {
    // var name = this.props.product.stocked ?
    //   this.props.product.name :
    //   <span style={{color: 'red'}}>
    //     {this.props.product.name}
    //   </span>;
    return (
      <div className="card">
        <div className="card_head">
            <h3>Card Name</h3>
        </div>
        <div className="card_body">
            <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod
            tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam,
            quis nostrud exercitation ullamco laboris... </p>
        </div>
      </div>
    )
  }
}