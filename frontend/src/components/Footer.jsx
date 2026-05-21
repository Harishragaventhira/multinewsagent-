import React from 'react';
import { Link } from 'react-router-dom';
import { Newspaper } from 'lucide-react';
import './Footer.css';

export default function Footer() {
  return (
    <footer className="footer">
      <div className="footer-content">
        <div className="footer-brand">
          <Link to="/" className="footer-logo">
            <Newspaper size={24} />
            <span>NEWSMULTIAGENT</span>
          </Link>
          <p className="footer-description">
            Autonomous multi-agent intelligence platform delivering real-time, comprehensive 
            insights across 20 specialized AI and machine learning domains.
          </p>
        </div>
        
        <div className="footer-links-group">
          <h4 className="footer-heading">Topics</h4>
          <div className="footer-links">
            <Link to="/generative_ai">Generative AI</Link>
            <Link to="/llms">LLMs</Link>
            <Link to="/agentic_ai">Agentic AI</Link>
            <Link to="/mlops">MLOps</Link>
            <Link to="/rag">RAG & Vector DBs</Link>
          </div>
        </div>
      </div>
      <div className="footer-bottom">
        <p>Powered by Advanced Multi-Agent Intelligence &mdash; Real-time AI News Hub</p>
      </div>
    </footer>
  );
}
