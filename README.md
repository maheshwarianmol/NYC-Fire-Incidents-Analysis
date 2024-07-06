# NYC-Fire-Incidents-Analysis
**Repository Description:**  Analyzing NYC fire incident data with Python scripts, Docker for containerization, and OpenSearch for visualizations. Explore response times and incident classifications.


**Project Background and Approach:**
The project involves the analysis of a vast dataset containing millions of records related to fire incidents in New York City. The dataset includes various variables such as dispatch response time, incident response time, and incident dates. The approach to this project can be summarized as follows:

1) EC2 Provisioning: Setting up Amazon Elastic Compute Cloud (EC2) instances.

2) Containerization: Utilizing container technology to manage and deploy the project.

3) Terminal Navigation: Navigating and working with the system through the command-line terminal.

4) Python Scripting: Developing and using Python scripts for data manipulation and analysis.

5) OpenSearch and Visualizations: Employing OpenSearch for data storage and visualization.

**Project Process:**

- The first step was to create an Elasticsearch (ES) domain. The project utilized a master username and password for accessing the ES domain's endpoint and the OpenSearch dashboard URL.

- An EC2 instance was established and accessed via a web browser. This instance played a crucial role in setting up the required folder structure and project files.

- Preliminary tests were conducted to ensure that data retrieval was functioning correctly. Initially, a small number of rows were retrieved using the page_size parameter for testing purposes.

In summary, this project aimed to analyze a substantial dataset of NYC fire incidents using various technologies and tools, including EC2, containerization, Python scripting, and OpenSearch for effective data storage and visualization.

**DOCKER RUN COMMAND:**

docker run -e INDEX_NAME="fire" -e DATASET_ID="8m42-w767" -e APP_TOKEN="HE1n5LIqNun5UJUdHk0cwXw6F" -e ES_HOST="https://search-nyc-fire-data-f4543eu5y6wx7xz7pfbegnu2dy.us-east-2.es.amazonaws.com" -e ES_USERNAME="anmolmaheshwari" -e ES_PASSWORD="Consistent10." bigdataproject1:1.0 --page_size=2000 --num_pages=3200


OpenSearch Dashboards URL:
https://search-nyc-fire-data-f4543eu5y6wx7xz7pfbegnu2dy.us-east-2.es.amazonaws.com/_dashboards 
Domain endpoint:
https://search-nyc-fire-data-f4543eu5y6wx7xz7pfbegnu2dy.us-east-2.es.amazonaws.com 
