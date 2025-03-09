import React from "react";
import "../styles/home.scss";
import projectIMG from "../assets/cartoon5.png";
import technicalDocsIMG from "../assets/writing.png";
import profileIMG from "../assets/profile_imageNB.jpg";
import Contact from "../components/contact";

const Home: React.FC = () => {
  return (
    <div className="home-container">
      {/* Profile Section */}
      <section className="profile-section">
        <div className="profile">
            <div className="profile-image">
                <img src= {profileIMG} alt="Profile" className="profile-img" />
            </div>
          <h1>Seth Glover</h1>
          <p className="subtitle">Software Engineer | Problem Solver | Tech Enthusiast</p>
        </div>
      </section>
      <section className="about-section">
        <h2>About Me</h2>
        <p>
          Hello! I'm Seth Glover, a software engineer based in the United States. I have a passion for coding and technology, and I love to solve problems and build things. I have experience with a variety of programming languages and technologies, and I'm always looking to learn more. I'm excited to share my work with you and I hope you enjoy it!   
        </p>

      </section>

      {/* Cards Section */}
      <section className="cards-section">
        <div className="card">
          <div className="card-image"> 
          <img src= {projectIMG} alt="Projects" />
          </div>
          <h2>Projects</h2>
          <p>Browse my coding projects and technical work.</p>
          <a href="/projects" className="card-link">View More</a>
        </div>

        <div className="card">
          <img src={technicalDocsIMG} alt="Technical Documentation" />
          <h2>Technical Documentation</h2>
          <p>Read about my technical documentation and guides.</p>
          <a href="/technical-docs" className="card-link">View More</a>
        </div>
      </section>

      <section> 
        <Contact />
      </section>
    </div>
  );
};

export default Home;
