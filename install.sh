#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Update package lists
sudo apt-get update -y

# Install Docker
sudo apt-get install -y docker.io

# Install required packages for apt to use a repository over HTTPS
sudo apt-get install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's official GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker's official APT repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package lists again to include Docker's repository
sudo apt-get update -y

# Install Docker Compose plugin
sudo apt-get install -y docker-compose-plugin

# Verify Docker Compose installation
docker compose version

# Add the current user to the 'docker' group to run Docker without 'sudo'
sudo usermod -aG docker $USER

# Apply the new group membership
newgrp docker

# Print success message
echo "Docker and Docker Compose have been installed successfully."

mkdir -p ~/miniconda3
wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh -O ~/miniconda3/miniconda.sh
bash ~/miniconda3/miniconda.sh -b -u -p ~/miniconda3
rm ~/miniconda3/miniconda.sh

source ~/miniconda3/bin/activate
conda init --all
conda create -n scrape2llm python=3.12

git clone https://github.com/mendableai/firecrawl.git
cd firecrawl
cp ../.env.firecrawl .env
