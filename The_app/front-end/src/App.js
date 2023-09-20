import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "./components/Header";
import LoginForm from "./components/Login";
import RegistrationForm from "./components/Register";
import PostForm from "./components/writingpage";
import Dashboard from "./components/Dashboard";

const App = () => {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/Login" element={<LoginForm />} />
            <Route path="/Register" element={<RegistrationForm />} />
            <Route path="/Dashboard" element={<Dashboard/>} />
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;