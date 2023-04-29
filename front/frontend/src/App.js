import logo from './logo.svg';
import './App.css';
import React from 'react';

import axios from 'axios';

class App extends React.Component {
  state = {
    details: [],
  };

  componentDidMount() {
	let data;
    axios.get('http://localhost:8000/rest/market/')
      .then(res => {
	  data = res.data;
        this.setState({
          details: data,
        });
      })
      .catch((err) => {
        console.log(err);
      });
  }

  render() {
    return (
      <div>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <h2>Django data</h2>
            <h2>{output.subj}</h2>
            <h2>{output.task}</h2>
            <h2>{output.price}</h2>
            <h2>{output.deadline}</h2>
          </div>
        ))}
      </div>
    );
  }
}


export default App;
