import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import "./Dashboard.css"; 
import AddNewEntry from './writingpage';

const Dashboard = () => {
 
  const [blogs, setBlogs] = useState([]);

  useEffect(() => {
 
    const sampleBlogs = [
      {
        id: 1,
        topic: "Technology",
        title: "Introduction to React",
        content: "React is a JavaScript library...",
        date: "2023-09-20",
      },
      
    ];
    setBlogs(sampleBlogs);
  }, []);

  return (
    <div className="dashboard">
      <h1>Welcome </h1>
      <div className="dashboard-actions">
        <Link to="/writingpage">Create New Blog</Link>
      </div>
      <h2>Your Blogs</h2>
      <ul className="blog-list">
        {blogs.map((blog) => (
          <li key={blog.id}>
            <Link to={`/blog/${blog.id}`}>
              <h3>{blog.title}</h3>
              <p>{blog.topic}</p>
              <p>Date: {blog.date}</p>
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default Dashboard;
