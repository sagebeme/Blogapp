import React, { useState } from "react";
import './writingpage.css';

const AddNewEntry = () => {
  const [date, setDate] = useState(new Date());
  const [topic, setTopic] = useState('');
  const [title, setTitle] = useState('');
  const [content, setContent] = useState('');

  const handleSubmit = (event) => {
    event.preventDefault();

    // TODO: Submit the form data to the backend
  };

  return (
    <form onSubmit={handleSubmit}>
      
      <input
        type="text"
        placeholder="Topic"
        value={topic}
        onChange={(event) => setTopic(event.target.value)}
      />
      <input
        type="text"
        placeholder="Title"
        value={title}
        onChange={(event) => setTitle(event.target.value)}
      />
      <textarea
        placeholder="Content"
        value={content}
        onChange={(event) => setContent(event.target.value)}
      />
      <input
        type="date"
        value={date}
        onChange={(event) => setDate(event.target.value)}
      />
      <button type="submit">Submit</button>
    </form>
  );
};

export default AddNewEntry;
