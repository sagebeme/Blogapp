import React from "react";
import { Link } from "react-router-dom";
import PostForm from './writingpage';
import RegistrationForm from "./Register";
import LoginForm from './Login';
import './Header.css';
import Dashboard from './Dashboard';

const Header = () => {
  return (
    <header>
      <h1>Blog Hub</h1>

      <nav>
        <Link to="/Register">Register</Link>
        <Link to="/Login">Login</Link>
        <Link to="/Dashboard">Dashboard</Link>
        
      </nav>
    </header>
  );
};

export default Header;