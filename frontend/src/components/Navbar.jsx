import React from 'react';
import { Link, useLocation } from 'react-router-dom';
import { Newspaper, Sparkles, Cpu, Bot, GitBranch, LayoutGrid, Menu, X } from 'lucide-react';
import { motion, AnimatePresence } from 'framer-motion';
import { useState } from 'react';
import './Navbar.css';

const navLinks = [
  { name: 'Generative AI', path: '/generative_ai', icon: <Sparkles size={18} /> },
  { name: 'LLMs', path: '/llms', icon: <Cpu size={18} /> },
  { name: 'Agentic AI', path: '/agentic_ai', icon: <Bot size={18} /> },
  { name: 'MLOps', path: '/mlops', icon: <GitBranch size={18} /> },
  { name: 'Explore All', path: '/explore', icon: <LayoutGrid size={18} /> },
];

export default function Navbar() {
  const [isOpen, setIsOpen] = useState(false);
  const location = useLocation();

  return (
    <nav className="navbar">
      <div className="navbar-container">
        <Link to="/" className="navbar-logo">
          <motion.div
            initial={{ rotate: -180, opacity: 0 }}
            animate={{ rotate: 0, opacity: 1 }}
            transition={{ duration: 0.5 }}
          >
            <Newspaper className="logo-icon" size={28} />
          </motion.div>
          <span className="logo-text">
            NEWSMULTIAGENT
          </span>
        </Link>

        <div className="desktop-menu">
          {navLinks.map((link) => (
            <Link
              key={link.name}
              to={link.path}
              className={`nav-link ${location.pathname === link.path ? 'active' : ''}`}
            >
              {link.icon}
              <span>{link.name}</span>
            </Link>
          ))}
        </div>

        <button className="mobile-menu-btn" onClick={() => setIsOpen(!isOpen)}>
          {isOpen ? <X size={24} /> : <Menu size={24} />}
        </button>
      </div>

      <AnimatePresence>
        {isOpen && (
          <motion.div
            className="mobile-menu"
            initial={{ height: 0, opacity: 0 }}
            animate={{ height: 'auto', opacity: 1 }}
            exit={{ height: 0, opacity: 0 }}
            transition={{ duration: 0.3 }}
          >
            {navLinks.map((link) => (
              <Link
                key={link.name}
                to={link.path}
                className="mobile-nav-link"
                onClick={() => setIsOpen(false)}
              >
                {link.icon}
                <span>{link.name}</span>
              </Link>
            ))}
          </motion.div>
        )}
      </AnimatePresence>
    </nav>
  );
}
