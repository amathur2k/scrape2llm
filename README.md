Setup

Setup AWS Bedrock to get acess to model of choice
Configure Bedrock APi Acesss :- https://github.com/aws-samples/bedrock-access-gateway
Create an AWS EC2 Instance
Ubuntu
t2.small
20GB Storage
On this Instance perform Installation git clone https://github.com/amathur2k/scrape2llm.git cd scrape2llm source install.sh

edit the .env file to enter bedrock api access key

Below command will take 5-10 minutes 6) docker compose up --build

Open another terminal
cd scrape2llm
conda activate scrape2llm
pip install -r requirements.txt
python example.py
