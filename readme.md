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
- **Model**: SARIMAX, N-BEATS, Informer, and Hmm with Exogenous features (e.g., compressed news sentiment, macroeconomic indicators)
- **Purpose**: Predict short-term price trends and market dynamics, and detect market regimes
- **Output**: Forecasted price changes or returns, and detected market regimes

### 4. **Algorithmic Trading**
- **Technique**: Reinforcement learning (e.g., Q-Learning).  
- **Use Case**: Design automated trading strategies based on forecasting outputs and real-time portfolio states.(State Representation: Includes discretized return bins and simplified forecast signals (e.g., price up, down, or flat).Action Space: Limited to basic actions: buy, sell, hold—avoiding percentage-based complexities if less compute needed.Reward Function: The reward is calculated based on portfolio performance, taking into account price movements, trading volume, and transaction costs.
Alpaca Integration: Once a trading signal is generated, it is transmitted to the Alpaca API for order execution, which can be tested in Paper Trading or executed in a real account.)
- **Output**: Dynamic buy/sell/hold signals based on learned trading policies.

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
   git clone https://github.com/kaispace30098/QuantitativeInvestmentResearchSuite.git