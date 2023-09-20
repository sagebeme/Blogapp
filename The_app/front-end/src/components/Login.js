import React from "react";
import './Login.css';
const LoginForm = () => {
  return (
    <div className="login-form">
      <h1>Login</h1>
      <form>
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <button type="submit">Login</button>
      </form>
      <a href="/register">Don't have an account? Register</a>
    </div>
  );
};

export default LoginForm;