import React from 'react';
import { motion } from 'framer-motion';
import { Link } from 'react-router-dom';
import { ArrowUpRight } from 'lucide-react';
import './CategoryCard.css';

export default function CategoryCard({ title, path, icon: Icon, description, delay }) {
  return (
    <Link to={path} className="category-card-link">
      <motion.div
        className="category-card"
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.6, delay }}
        whileHover={{ scale: 1.05, translateY: -10 }}
        whileTap={{ scale: 0.98 }}
      >
        <div className="card-glow"></div>
        <div className="category-icon-wrapper">
          <Icon size={32} className="category-icon" />
        </div>
        <h3 className="category-title">{title}</h3>
        <p className="category-desc">{description}</p>
        <div className="category-action">
          <span>Read Latest</span>
          <ArrowUpRight size={18} />
        </div>
      </motion.div>
    </Link>
  );
}
