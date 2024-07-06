# NYC-Fire-Incidents-Analysis
**Repository Description:**  Analyzing NYC fire incident data with Python scripts, Docker for containerization, and OpenSearch for visualizations. Explore response times and incident classifications.

## Overview
This repository hosts tools and scripts for analyzing a large dataset of fire incidents in New York City. The project aims to uncover insights into response times, incident classifications, and temporal trends across NYC boroughs. It utilizes Python for data manipulation, Docker for containerization, and OpenSearch for efficient data storage and visualization.

## Key Features
- **Data Exploration**: Dive into detailed analysis of dispatch and incident response times.
- **Visualization**: Generate interactive charts and graphs using OpenSearch Dashboards.
- **Scripted Analysis**: Python scripts automate data preprocessing, analysis, and visualization tasks.
- **Containerized Deployment**: Easily replicate the environment with Docker for consistent results across platforms.

## Project Structure
- **data/**: Raw and processed datasets, including CSV files and data dictionaries.
- **scripts/**: Python scripts for data cleaning, analysis, and visualization.
- **docker/**: Dockerfile for setting up the development environment.
- **visualizations/**: Output directory for generated graphs and charts.

## Technologies Used
- **Python**: Pandas, Matplotlib, and Seaborn for data analysis and visualization.
- **Docker**: Simplifies environment setup and ensures reproducibility.
- **OpenSearch**: Stores and queries data, providing insights through visual dashboards.

## Setup Instructions
1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/NYC-Fire-Incidents-Analysis.git
   cd NYC-Fire-Incidents-Analysis
   ```
2. **Build and Run Docker Container**:
   ```bash
   docker build -t nyc-fire-analysis .
   docker run -p 8080:8080 nyc-fire-analysis
   ```
3. **Explore Data and Scripts**:
   - Use scripts in `scripts/` to preprocess data, generate visualizations, and analyze trends.
   - Customize scripts and parameters for specific analysis needs.

## Visualizations
- **Response Time Analysis**: Visualize average response times by borough and incident type.
- **Temporal Trends**: Analyze monthly and yearly trends in fire incidents.
- **Incident Classification**: Explore the distribution of incident types across NYC neighborhoods.

