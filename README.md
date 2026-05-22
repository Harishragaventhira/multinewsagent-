# AI Multi-Agent News Hub

A real-time, multi-agent AI News Hub powered by **LangGraph**, **FastAPI**, and **React (Vite)**. The platform orchestrates 20 specialized AI category agents to scrape, process, and summarize the latest news headlines.

---

## 🚀 About the Project

This system organizes autonomous AI agents that fetch and analyze news across 20 distinct technical domains (such as Machine Learning, Large Language Models, MLOps, AI Ethics, Computer Vision, and RAG). 

- **Orchestration**: Built using **LangGraph** to coordinate agents sequentially, passing a shared state containing summaries of all topics.
- **Backend API**: A **FastAPI** web service featuring a background **APSScheduler** that automatically refreshes the agent workflow at designated intervals.
- **Frontend Dashboard**: A responsive **React** application stylized with modern gradients, micro-animations, and glassmorphic card designs to display real-time news streams.

### 🧠 AI & API Integrations
1. **Llama 3.3 70B Model via Groq**: The backend uses LangChain's ChatOpenAI wrapper to run prompt templates against the high-throughput `llama-3.3-70b-versatile` model hosted on the [Groq Cloud Console](https://console.groq.com/).
2. **News API**: Category news headlines and articles are fetched dynamically using the [News API Service](https://newsapi.org/).

---

## 📋 System Requirements

Ensure you have the following installed on your machine:
- **Python**: Version `3.8` or higher (with `pip`)
- **Node.js**: Version `18.x` or higher (with `npm`)
- **Operating System**: Windows, macOS, or Linux

---

## 🛠️ Installation & Setup

Follow these step-by-step commands to get the application running locally on your system.

### 🔑 Step 1: Environment Configuration
Create or configure the `.env` file in the `backend/` folder:
- **File Location**: `backend/.env`
- **Required Variables**:
  ```env
  GROQ_API_KEY=your_groq_api_key_here
  NEWS_API_KEY=your_news_api_key_here
  ```
> [!NOTE]
> - Get a Groq API key by signing up at [Groq Developer Console](https://console.groq.com/).
> - Get a News API key by registering at [News API](https://newsapi.org/).

---

### 💻 Step 2: Run the Backend Server

Open a new terminal window and navigate to the project directory:

1. **Navigate to the Project Root & Activate the Virtual Environment:**
   - **On Windows (PowerShell)**:
     ```powershell
     c:
     cd "c:\Users\admin\Desktop\NEWS multiagent"
     .\.venv\Scripts\Activate.ps1
     ```
   - **On Windows (Command Prompt - CMD)**:
     ```cmd
     c:
     cd "c:\Users\admin\Desktop\NEWS multiagent"
     .\.venv\Scripts\activate.bat
     ```
   - **On macOS / Linux**:
     ```bash
     cd "/path/to/NEWS multiagent"
     source .venv/bin/activate
     ```

2. **Install Backend Dependencies:**
   ```bash
   pip install -r backend/requirements.txt
   ```

3. **Navigate to Backend Directory & Start the API Server:**
   ```bash
   cd backend
   uvicorn api:app --reload
   ```
   *The backend server will launch at `http://127.0.0.1:8000`. You can inspect the API documentation at `http://127.0.0.1:8000/docs`.*

---

### 💻 Step 3: Run the Frontend Dashboard

Open a **second** terminal window and navigate to the project directory:

1. **Navigate into the Frontend Directory:**
   - **On Windows (PowerShell or CMD)**:
     ```powershell
     c:
     cd "c:\Users\admin\Desktop\NEWS multiagent\frontend"
     ```
   - **On macOS / Linux**:
     ```bash
     cd "/path/to/NEWS multiagent/frontend"
     ```

2. **Install Frontend Dependencies:**
   ```bash
   npm install
   ```

3. **Start the Vite Development Server:**
   ```bash
   npm run dev
   ```
   *The frontend dashboard will compile and open at `http://localhost:5173` (or the local URL printed in the terminal).*

---

## 🏷️ Category Agents Managed

The multi-agent workflow compiles summaries for:
- Machine Learning
- Deep Learning
- Generative AI
- Natural Language Processing (NLP)
- Computer Vision
- Large Language Models (LLMs)
- Agentic AI
- Reinforcement Learning
- Retrieval-Augmented Generation (RAG)
- AI Automation
- MLOps
- Data Science
- Neural Networks
- Transformers
- Prompt Engineering
- AI Ethics & Responsible AI
- Speech AI
- Recommendation Systems
- Time Series Forecasting
- Anomaly Detection
