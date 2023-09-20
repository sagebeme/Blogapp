import React, { useState } from "react";
import './Register.css';


const RegisterForm = () => {
  return (
    <div className="register-form">
      <h1>Register</h1>
      <form>
        <input type="text" placeholder="Name" />
        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />
        <input type="password" placeholder="Confirm Password" />
        <button type="submit">Register</button>
      </form>
    </div>
  );
};

export default RegisterForm;