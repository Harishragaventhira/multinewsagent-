import React from 'react';
import { motion } from 'framer-motion';
import { Sparkles } from 'lucide-react';
import './NewsCard.css';

export default function NewsCard({ category, content, delay = 0 }) {
  // Format markdown lists and bold text into structured HTML elements
  const formatContent = (text) => {
    if (typeof text !== 'string') return text;
    const lines = text.split('\n').filter(line => line.trim() !== '');
    
    return lines.map((line, index) => {
      const trimmed = line.trim();
      const isSubBullet = line.startsWith('  ') || line.startsWith('\t') || line.startsWith(' *') || line.startsWith(' -');
      const isBullet = trimmed.startsWith('*') || trimmed.startsWith('-');
      
      let cleanText = trimmed;
      if (isBullet) {
        cleanText = trimmed.replace(/^[\*\-]\s*/, '');
      }

      // Parse bold markdown **text**
      const parts = cleanText.split(/(\*\*.*?\*\*)/g);
      const parsedElements = parts.map((part, i) => {
        if (part.startsWith('**') && part.endsWith('**')) {
          const boldText = part.slice(2, -2);
          return (
            <strong key={i} className="news-item-heading">
              {boldText}
            </strong>
          );
        }
        return part;
      });

      const className = `news-line ${isBullet ? 'bullet-item' : ''} ${isSubBullet ? 'sub-bullet' : ''}`;
      
      return (
        <div key={index} className={className}>
          {isBullet && !isSubBullet && <span className="bullet-dot">•</span>}
          {isSubBullet && <span className="sub-bullet-dot">○</span>}
          <span className="line-text">{parsedElements}</span>
        </div>
      );
    });
  };

  return (
    <motion.div 
      className="news-card"
      initial={{ opacity: 0, scale: 0.95 }}
      animate={{ opacity: 1, scale: 1 }}
      transition={{ duration: 0.5, delay }}
    >
      <div className="news-card-header">
        <div className="ai-badge">
          <Sparkles size={14} className="sparkle-icon" />
          <span>AI Summary</span>
        </div>
        <span className="news-category-label">{category.toUpperCase()}</span>
      </div>
      <div className="news-card-content">
        {typeof content === 'string' ? formatContent(content) : content}
      </div>
      <div className="news-card-footer">
        <div className="data-points">
          <span className="data-dot"></span>
          <span>Verified by AI Agents</span>
        </div>
        <span className="timestamp">Live</span>
      </div>
    </motion.div>
  );
}
