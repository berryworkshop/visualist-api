import Axios from 'axios';

export default class EventQuery {
  constructor(label) {
    this.label = label;
    this.outputList = [];
  }

  eventList() {
    const ajax = Axios.create({
      baseURL: process.env.API_BASE_URL,
    });
    return new Promise((resolve, reject) => {
      ajax.post('/cypher', {
        query: `
          MATCH (event:Event)
          OPTIONAL MATCH (event)-[rel:AT]->(location)
          RETURN event, rel, location`,
      })
      .then((response) => {
        response.data.data.forEach((triad) => {
          this.outputList.push({
            name: triad[0].data.name,
            location: (triad[2] ? triad[2].data.name : undefined),
            city: 'Chicago',
            address: '123 N Ave, Chicago IL 60000',
            opening: 'Tuesday, February 7th, 2-3p',
          });
        });
        resolve(this.outputList);
      })
      .catch((error) => {
        reject(error);
      });
    });
  }
}
