# 🌱 Local Farm Agent

A local AI-powered farm monitoring agent built with **Python, LangGraph, SQLite, and pandas**. It analyzes farm plots and recent sensor readings to help farmers decide when to check a sensor, irrigate, or wait.

The goal is to combine structured agricultural data with LLM-based reasoning to produce practical, context-aware recommendations.

## 🎯 Features

- **Farm monitoring:** Retrieve plot information and recent sensor readings from a local SQLite database.
- **Data processing:** Use pandas to combine plot metadata with sensor measurements.
- **Anomaly detection:** Identify potentially abnormal sensor readings before making decisions.
- **Decision-making:** Recommend an appropriate next action based on soil moisture, crop requirements, and sensor data.
- **Structured recommendations:** Use Pydantic models to keep the LLM's output consistent and easy to process.
- **Graph-based workflow:** Organize the agent's logic into nodes and conditional transitions with LangGraph.
- **Local data storage:** Store farm plots and sensor readings in SQLite.

## 🏗️ Architecture

The agent follows a structured workflow:

```text
        ┌──────────────────────┐
        │   SQLite Database    │
        │                      │
        │  Farm Plots          │
        │  Sensor Readings     │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │   Data Retrieval     │
        │                      │
        │   SQLite → pandas    │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Recommendation Node │
        │                      │
        │   LLM + Pydantic     │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Anomaly Assessment  │
        │                      │
        │  Conditional Logic   │
        └──────────┬───────────┘
                   │
                   ▼
        ┌──────────────────────┐
        │  Farm Recommendation │
        │                      │
        │  Check sensor        │
        │  Irrigate            │
        │  Wait                │
        └──────────────────────┘
