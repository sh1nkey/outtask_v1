import React from 'react';
import axios from 'axios';
import Order from '../Orders/Order/Order';

function Orders() {
  class Ord extends React.Component {
    state = {
      details: [],
    };

    componentDidMount() {
      axios
        .get('http://localhost:8000/rest/market/')
        .then((res) => {
          this.setState({
            details: res.data,
          });
        })
        .catch((err) => {
          console.log(err);
        });
    }

    render() {
      return (
        <div>
          <div className='ordersTable'>
            <div className='tableOrders'>
              <h2>Предмет</h2>
              <h2>Задание</h2>
              <h2>Цена</h2>
              <h2>Крайний срок</h2>
            </div>
            {this.state.details.map((output, id) => (
              <div key={id}>
                <Order
                  subject={output.subj}
                  task={output.task}
                  price={output.price}
                  deadline={output.deadline}
                />
              </div>
            ))}
          </div>
        </div>
      );
    }
  }

  return <Ord />;
}

export default Orders;
