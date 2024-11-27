# Quantitative Investment Research Suite

This project is dedicated to building an interconnected system that bridges traditional investment principles with advanced AI techniques, delivering a comprehensive decision-support framework.  

The repository offers a fully integrated pipeline for data-driven investment strategies, spanning stock screening, portfolio optimization, forecasting, and algorithmic trading, with a user-friendly LLM-powered dashboard for interaction and insights. The workflow is designed to create a seamless flow of information between modules:

---

## Features

### 1. **Stock Screening**
- **Methodology**: Implements the CANSLIM framework to identify high-potential stocks.  
- **Key Inputs**: Fundamental and technical indicators.  
- **Output**: A ranked list of stocks ready for optimization.

### 2. **Portfolio Optimization**
- **Approach**: Uses a mean-variance optimization framework.  
- **Goal**: Balance risk and expected return to construct an efficient portfolio.  
- **Output**: Optimal asset allocation weights.

### 3. **Forecasting**
- **Model**: SARIMAX, N-BEATS, and Informer and with Exogenous features (e.g., compressed news sentiment, macroeconomic indicators).  
- **Purpose**: Predict short-term price trends and market dynamics.  
- **Output**: Forecasted price changes or returns.

### 4. **Algorithmic Trading**
- **Technique**: Reinforcement learning (e.g., Q-Learning).  
- **Use Case**: Design automated trading strategies based on forecasting outputs and real-time portfolio states.  
- **Output**: Dynamic buy/sell/hold signals.

### 5. **LLM RAG Dashboard**
- **Functionality**: A retrieval-augmented generation (RAG) dashboard powered by large language models.  
- **Purpose**:  
  - Interactive insights presentation.  
  - Real-time query answering.  
  - Re-run analyses with adjusted assumptions.  
- **Output**: User-friendly decision-support system.

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/QuantitativeInvestmentResearchSuite.git