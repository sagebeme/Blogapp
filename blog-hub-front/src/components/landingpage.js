import React from "react";
import { Link } from "react-router-dom";
import "./landingpage.css"; 

const LandingPage = () => {
  return (
    <div className="landing-page">
      <header>
        <h1>Welcome to Blog Hub</h1>
        <p>Your Destination for Writing and Sharing Articles</p>
      </header>
      <section className="cta-section">
        <h2>Start Writing Today!</h2>
        <p>Join our community of writers and share your knowledge and experiences with the world.</p>
        <Link to="/dashboard" className="cta-button">
          Get Started
        </Link>
      </section>
      <section className="features-section">
        <h2>Features</h2>
        <ul>
          <li>Easy-to-use article editor</li>
          <li>Connect with other writers</li>
          <li>Explore a wide range of topics</li>
          <li>Get feedback and improve your writing</li>
        </ul>
      </section>
      <section className="about-section">
        <h2>About Us</h2>
        <p>
          Blog Hub is a platform designed for writers of all levels to create, share, and discover articles. Whether you're a seasoned author or just starting your writing journey, Blog Hub provides the tools and community you need to succeed.
        </p>
      </section>
      <footer>
        <p>&copy; {new Date().getFullYear()} Blog Hub</p>
      </footer>
    </div>
  );
};

export default LandingPage;
