import React from 'react'
import ReactDOM from 'react-dom'
import Card from './card/card.jsx'

class EventList extends React.Component {
  render() {
    var events = []
    EVENTS.forEach(function(event) {
        events.push(<Card
            name={event.name}
            description={event.description}
            id={event.pk}
            key={event.pk}
        />)
    })
    return (
      <div>
        {events}
      </div>
    )
  }
}

var EVENTS = [
    {
        name: "An unforgettable night out.",
        pk: "123",
        description: "Lorem ipsum dolor sit amet, consectetur adipisicing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
    },
    {
        name: "Flurble Blork Fladdurk.",
        pk: "345",
        description: "Sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.."
    },
    {
        name: "Glimburbula.",
        pk: "567",
        description: "Labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident.."
    },
]

ReactDOM.render(
  <EventList />,
  document.getElementById('event_list-react_root')
)