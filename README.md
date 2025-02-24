# Scrape2LLM Setup Guide

## Prerequisites
1. AWS Bedrock access configured for your chosen model
2. Bedrock API Gateway setup ([configuration guide](https://github.com/aws-samples/bedrock-access-gateway))

## Infrastructure Setup

### AWS EC2 Instance Requirements
- OS: Ubuntu
- Instance Type: t2.small
- Storage: 20GB

## Installation Steps

1. Clone the repository:
   ```bash
   git clone https://github.com/amathur2k/scrape2llm.git
   cd scrape2llm
   ```

2. Run the installation script:
   ```bash
   source install.sh
   ```

3. Configure the environment:
   - Edit the `.env` file
   - Add your Bedrock API access key
   - Add your Bedrock API access URL

4. Build and start the Docker container:
   ```bash
   docker compose up --build
   ```
   > Note: This process may take 5-10 minutes to complete.

5. In a new terminal window, set up the Python environment:
   ```bash
   cd ~/scrape2llm
   conda activate scrape2llm
   pip install -r requirements.txt
   ```

6. Run the example:
   ```bash
   python example.py
   ```
