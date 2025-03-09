import React, { useState } from "react";
import "../styles/contact.scss";
import { API_BASE_URL } from "../config";

const Contact: React.FC = () => {
  const [formData, setFormData] = useState({
    name: "",
    email: "",
    phone: "",
    title: "",
    message: "",
  });
  const [status, setStatus] = useState(""); // Status message for user feedback

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("Sending...");

    try {
      const response = await fetch(`${API_BASE_URL}/api/contact`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setStatus("✅ Message sent successfully!");
        setFormData({ name: "", email: "", phone: "", title: "", message: "" });
      } else {
        const errorData = await response.json();
        setStatus(`❌ Error: ${errorData.detail}`);
      }
    } catch (error) {
      setStatus("❌ Failed to send message.");
    }
  };

  return (
    <div className="contact-container">
      <h2>Contact Me</h2>
      <form onSubmit={handleSubmit} className="contact-form">
        <div>
          <label htmlFor="name">Name</label>
          <input 
            id="name"
            type="text" 
            name="name" 
            value={formData.name} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="email">Email</label>
          <input 
            id="email"
            type="email" 
            name="email" 
            value={formData.email} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="phone">Phone</label>
          <input 
            id="phone"
            type="tel" 
            name="phone" 
            value={formData.phone} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="title">Title</label>
          <input 
            id="title"
            type="text" 
            name="title" 
            value={formData.title} 
            onChange={handleChange} 
            required 
          />
        </div>

        <div>
          <label htmlFor="message">Message</label>
          <textarea 
            id="message"
            name="message" 
            rows={5} 
            value={formData.message} 
            onChange={handleChange} 
            required
          ></textarea>
        </div>

        <button type="submit">Send Message</button>
      </form>
      {status && <div className="status-message">{status}</div>}
    </div>
  );
};

export default Contact;