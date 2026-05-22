import React from 'react';
import CategoryCard from '../components/CategoryCard';
import { 
  Brain, Network, Sparkles, MessageSquare, Eye, Cpu, Bot, Award, Database, 
  Workflow, GitBranch, BarChart2, Layers, Zap, Terminal, ShieldCheck, Mic, ThumbsUp, TrendingUp, AlertTriangle,
  Cloud, Code2, Server
} from 'lucide-react';
import './Explore.css';

const categories = [
  { 
    name: 'Machine Learning', 
    path: '/machine_learning', 
    icon: Brain, 
    desc: 'Algorithms, models, and mathematical approaches enabling computers to learn.' 
  },
  { 
    name: 'Deep Learning', 
    path: '/deep_learning', 
    icon: Network, 
    desc: 'Multi-layered neural networks, backpropagation, and deep feature representation.' 
  },
  { 
    name: 'Generative AI', 
    path: '/generative_ai', 
    icon: Sparkles, 
    desc: 'Creation of text, images, video, and code using AI systems.' 
  },
  { 
    name: 'Natural Language Processing (NLP)', 
    path: '/nlp', 
    icon: MessageSquare, 
    desc: 'Computers understanding, interpreting, and generating human languages.' 
  },
  { 
    name: 'Computer Vision', 
    path: '/computer_vision', 
    icon: Eye, 
    desc: 'Image processing, object detection, segmentation, and visual understanding.' 
  },
  { 
    name: 'Large Language Models (LLMs)', 
    path: '/llms', 
    icon: Cpu, 
    desc: 'GPT models, open source LLMs, fine-tuning, and model evaluations.' 
  },
  { 
    name: 'Agentic AI', 
    path: '/agentic_ai', 
    icon: Bot, 
    desc: 'Autonomous AI agents, planning, tool usage, and multi-agent systems.' 
  },
  { 
    name: 'Reinforcement Learning', 
    path: '/reinforcement_learning', 
    icon: Award, 
    desc: 'Policy gradients, Q-learning, agent reward optimization, and robotics.' 
  },
  { 
    name: 'Retrieval-Augmented Generation (RAG)', 
    path: '/rag', 
    icon: Database, 
    desc: 'Vector databases, document ingestion, embeddings, and context retrieval.' 
  },
  { 
    name: 'AI Automation', 
    path: '/ai_automation', 
    icon: Workflow, 
    desc: 'Workflow automation, RPA, code generation, and developer productivity.' 
  },
  { 
    name: 'MLOps', 
    path: '/mlops', 
    icon: GitBranch, 
    desc: 'Deployment, CI/CD for models, drift monitoring, and ML pipelines.' 
  },
  { 
    name: 'Data Science', 
    path: '/data_science', 
    icon: BarChart2, 
    desc: 'Data wrangling, statistical analysis, visualization, and predictive insights.' 
  },
  { 
    name: 'Neural Networks', 
    path: '/neural_networks', 
    icon: Layers, 
    desc: 'CNNs, RNNs, Graph Neural Networks, and foundational network architectures.' 
  },
  { 
    name: 'Transformers', 
    path: '/transformers', 
    icon: Zap, 
    desc: 'Attention mechanism, vision transformers, and state space models.' 
  },
  { 
    name: 'Prompt Engineering', 
    path: '/prompt_engineering', 
    icon: Terminal, 
    desc: 'Few-shot prompting, prompt templates, chain-of-thought, and system instructions.' 
  },
  { 
    name: 'AI Ethics & Responsible AI', 
    path: '/ai_ethics', 
    icon: ShieldCheck, 
    desc: 'Fairness, bias mitigation, alignment, safety, and regulation policies.' 
  },
  { 
    name: 'Speech AI', 
    path: '/speech_ai', 
    icon: Mic, 
    desc: 'Speech-to-text, text-to-speech, whisper models, and voice cloning.' 
  },
  { 
    name: 'Recommendation Systems', 
    path: '/recommendation_systems', 
    icon: ThumbsUp, 
    desc: 'Collaborative filtering, matrix factorization, and user personalization.' 
  },
  { 
    name: 'Time Series Forecasting', 
    path: '/time_series', 
    icon: TrendingUp, 
    desc: 'Temporal models, ARIMA, LSTM, and predictive time-sequence forecasting.' 
  },
  { 
    name: 'Anomaly Detection', 
    path: '/anomaly_detection', 
    icon: AlertTriangle, 
    desc: 'Outlier detection, security intelligence, fraud modeling, and diagnostic health.' 
  },
  { 
    name: 'Cloud Agent', 
    path: '/cloud_agent', 
    icon: Cloud, 
    desc: 'Cloud infrastructure, serverless, AWS, Azure, GCP, and AI cloud services.' 
  },
  { 
    name: 'API Agent', 
    path: '/api_agent', 
    icon: Code2, 
    desc: 'AI API services, integration, RESTful endpoints, and developer tooling.' 
  },
  { 
    name: 'Computing Agent', 
    path: '/computing_agent', 
    icon: Server, 
    desc: 'High-performance computing, GPUs, TPUs, quantum hardware, and AI processors.' 
  }
];

export default function Explore() {
  return (
    <div className="explore-page">
      <section id="categories" className="categories-section">
        <div className="section-header">
          <h2 className="section-title">Explore AI Topics</h2>
          <p className="section-subtitle">Select a dedicated AI agent to get specialized updates.</p>
        </div>
        
        <div className="categories-grid">
          {categories.map((cat, index) => (
            <CategoryCard
              key={cat.name}
              title={cat.name}
              path={cat.path}
              icon={cat.icon}
              description={cat.desc}
              delay={index * 0.05}
            />
          ))}
        </div>
      </section>
    </div>
  );
}
