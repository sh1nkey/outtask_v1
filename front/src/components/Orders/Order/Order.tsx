import React from 'react'
import "../../../CSS/mediaUpIn.css"

function Order(props: { subject: string, price: string, deadline: string }) {
    return (
        <div className='tableOrders'>
            <h2>{props.subject}</h2>
            <p>Цена: {props.price} руб.</p>
            <p>Крайний срок: {props.deadline}</p>
        </div>
    )
}

export default Order