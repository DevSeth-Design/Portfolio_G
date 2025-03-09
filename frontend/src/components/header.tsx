import React, { useState } from "react";
import { Link } from "react-router-dom";
import "../styles/header.scss";

const Header: React.FC = () => {
  const [menuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!menuOpen);
  };

  return (
    <header className="header">
      <Link to="/" className="logo">Seth Glover</Link>

      <nav className={`nav-links ${menuOpen ? "show" : ""}`}>
        <Link to="/projects" className="nav-link">Projects</Link>
        <Link to="/technical-docs" className="nav-link">Technical Docs</Link>
      </nav>

      <button className="menu-button" onClick={toggleMenu}>☰</button>
    </header>
  );
};

export default Header;
