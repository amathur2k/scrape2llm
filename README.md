Setup
1) Setup AWS Bedrock to get acess to model of choice
2) Configure Bedrock APi Acesss :- https://github.com/aws-samples/bedrock-access-gateway
3) Create an AWS EC2 Instance
 - Ubuntu
 - t2.small
 - 20GB Storage

4) On this Instance perform Installation
   
   git clone https://github.com/amathur2k/scrape2llm.git
   cd scrape2llm
   source install.sh

5) edit the .env file to enter bedrock api access key
   
Below command will take 5-10 minutes 

6)  docker compose up --build

7)  Open another terminal
8)  cd scrape2llm
9)  conda activate scrape2llm
10) pip install -r requirements.txt  
12)  python example.py
