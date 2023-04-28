import "./App.css"
import { BrowserRouter as Router, Routes, Route, Link } from 'react-router-dom';
import SignInWindow from "./components/SignInWindow/SignInWindow";
import RegistrationWindow from "./components/RegistrationWindow/RegistrationWindow";
import MakeAnOrder from "./components/MakeAnOrder/MakeAnOrder";
import Orders from "./components/Orders/Orders";

function App() {
  return (
    <Router>
      <div>
        <nav>
          <ul>
            <li>
              <Link to="/">Outtask</Link>
            </li>
          </ul>
          <ul className="orders-ul">
            <li>
              <Link to="/orders">Orders</Link>
            </li>
          </ul>
          <ul className="last-ul">
            <li>
              <Link to="/sign-in">In</Link>
            </li>
            <li>
              <Link to="/sign-up">Up</Link>
            </li>
          </ul>
        </nav>
        <Routes>
          <Route path="/sign-up" element={<Reg />} />
          <Route path="/sign-in" element={<In />} />
          <Route path="/orders" element={<Orders />} />
          <Route path="/" element={<Home />} />
        </Routes>
      </div>
    </Router>
  );
}

function Home() {
  return <MakeAnOrder />;
}

function Reg() {
  return <RegistrationWindow />;
}

function In() {
  return <SignInWindow />;
}

function Order() {
  return <Orders />;
}

export default App;
