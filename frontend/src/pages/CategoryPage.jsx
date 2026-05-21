import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import { motion } from 'framer-motion';
import { Loader2, RefreshCw } from 'lucide-react';
import NewsCard from '../components/NewsCard';
import './CategoryPage.css';

export default function CategoryPage() {
  const { categoryId } = useParams();
  const [news, setNews] = useState(null);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);

  const fetchNews = async () => {
    setLoading(true);
    setError(null);
    try {
      const response = await fetch("http://127.0.0.1:8000/news");
      const data = await response.json();
      
      // If we are looking for a specific category, find it case-insensitively
      const targetCategoryKey = Object.keys(data).find(
        key => key.toLowerCase() === categoryId?.toLowerCase()
      );
      
      if (targetCategoryKey && data[targetCategoryKey]) {
        setNews({ [targetCategoryKey]: data[targetCategoryKey] });
      } else {
        // Fallback if category not found specifically, maybe show error or empty state
        setNews({});
      }
    } catch (err) {
      console.error(err);
      setError("Failed to fetch AI news stream. Please try again.");
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchNews();
    const interval = setInterval(fetchNews, 60000); // refresh every minute
    return () => clearInterval(interval);
  }, [categoryId]);

  return (
    <div className="category-page">
      <div className="category-header">
        <motion.h1 
          className="page-title"
          initial={{ opacity: 0, x: -20 }}
          animate={{ opacity: 1, x: 0 }}
        >
          {categoryId?.toUpperCase()} <span className="text-gradient">NEWS</span>
        </motion.h1>
        <button className="refresh-btn" onClick={fetchNews} disabled={loading}>
          <RefreshCw size={18} className={loading ? "spinning" : ""} />
          <span>Refresh</span>
        </button>
      </div>

      {loading && !news ? (
        <div className="loading-state">
          <Loader2 size={48} className="spinner" />
          <p>AI Agents are compiling the latest updates...</p>
        </div>
      ) : error ? (
        <div className="error-state">
          <p>{error}</p>
          <button onClick={fetchNews} className="btn-primary">Retry</button>
        </div>
      ) : news && Object.keys(news).length > 0 ? (
        <div className="news-feed">
          {Object.keys(news).map((key, index) => (
            <NewsCard 
              key={key} 
              category={key} 
              content={news[key]} 
              delay={index * 0.1}
            />
          ))}
        </div>
      ) : (
        <div className="empty-state">
          <p>No recent updates found for this category.</p>
        </div>
      )}
    </div>
  );
}
