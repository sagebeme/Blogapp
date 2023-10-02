import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Header from "../src/components/Header";
import LoginForm from "../src/components/Login";
import RegistrationForm from "../src/components/Register";
import AddNewEntry from "../src/components/writingpage"; 
import Dashboard from "../src/components/Dashboard";
import LandingPage from "../src/components/landingpage";

const App = () => {
  return (
    <Router>
      <div className="App">
        <Header />
        <main>
          <Routes>
            <Route path="/" element={<LandingPage />} />
            <Route path="/login" element={<LoginForm />} /> {/* Updated path */}
            <Route path="/register" element={<RegistrationForm />} /> {/* Updated path */}
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/writingpage" element={<AddNewEntry />} /> {/* Added route for AddNewEntry */}
          </Routes>
        </main>
      </div>
    </Router>
  );
};

export default App;
