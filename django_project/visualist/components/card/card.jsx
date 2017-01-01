import React from 'react'
import ReactDOM from 'react-dom'
require('./card.scss')

export default class Card extends React.Component {
  constructor(props) {
    super(props)

    console.log(props)
    this.id = "card_" + this.props.id
  }
  render() {
    // var name = this.props.product.stocked ?
      //   this.props.product.name :
      //   <span style={{color: 'red'}}>
      //     {this.props.product.name}
      //   </span>;

    return (
      <div className="card" id={this.id}>
        <div className="card_head">
            <h3>{this.props.name}</h3>
        </div>
        <div className="card_body">
            <p>{this.props.description}</p>
        </div>
      </div>
    )
  }
}