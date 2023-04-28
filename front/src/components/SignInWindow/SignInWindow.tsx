import React, { useState } from 'react';
import './SignInWindow.css';
import '../../CSS/mediaUpIn.css'

const SignInWindow = () => {
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');

    const handleInputChange = (event: { target: any; }) => {
        const target = event.target;
        const value = target.value;
        const name = target.name;

        switch (name) {
            case 'email':
                setEmail(value);
                break;
            case 'password':
                setPassword(value);
                break;
            default:
                break;
        }
    }

    const handleSubmit = (event: { preventDefault: () => void; }) => {
        event.preventDefault();
        console.log('Email: ' + email);
        console.log('Password: ' + password);
    }

    return (
        <form onSubmit={handleSubmit}>
            <div className='block-header'>
                Sign In Form
            </div>
            <label>
                <input
                    type="email"
                    name="email"
                    value={email}
                    onChange={handleInputChange}
                    className="input-field"
                    placeholder="Enter email"
                />
            </label>

            <label>
                <input
                    type="password"
                    name="password"
                    value={password}
                    onChange={handleInputChange}
                    className="input-field"
                    placeholder="Enter password"
                />
            </label>
            <br />
            <input type="submit" value="Submit" className="submit-button" />
        </form>
    );
}

export default SignInWindow;
