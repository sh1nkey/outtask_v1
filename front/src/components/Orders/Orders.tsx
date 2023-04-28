import React from 'react'
import "../Orders/Order/Order"
import Order from '../Orders/Order/Order'

function Orders() {
    return (
        <div className='ordersTable'>
            <div className='tableOrders'>
                <h2>Предмет</h2>
                <p>Цена</p>
                <p>Крайний срок</p>
            </div>
            <div><Order subject={'Математика'} price={'1000'} deadline={'12.04.2024'} />
                <Order subject={'Математика'} price={'1000'} deadline={'12.04.2024'} />
                <Order subject={'Математика'} price={'1000'} deadline={'12.04.2024'} />
                <Order subject={'Математика'} price={'1000'} deadline={'12.04.2024'} />
                <Order subject={'Математика'} price={'1000'} deadline={'12.04.2024'} />
            </div>
        </div>
    )
}

export default Orders