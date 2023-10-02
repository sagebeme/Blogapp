import React from "react";
import { Link } from "react-router-dom";
import './Header.css';
import LandingPage from "./landingpage";

const Header = () => {
  return (
    <header>
      <h1>Blog Hub</h1>
      <nav>
        <Link to="/">Home</Link> {LandingPage}
        <Link to="/register">Register</Link>
        <Link to="/login">Login</Link>
        <Link to="/dashboard">Dashboard</Link>
      </nav>
    </header>
  );
};

export default Header;
