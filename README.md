# 🌐 Scrape2LLM

> Transform web content into AI-powered insights using AWS Bedrock

Scrape2LLM is a powerful web scraping and content generation tool that leverages AWS Bedrock's Language Models to analyze and transform web content into meaningful insights.

## ✨ Features

- 🔍 Intelligent web content scraping
- 🖼️ Automatic image extraction
- 📝 Content summarization
- 🎯 Marketing copy generation
- ☁️ Seamless AWS Bedrock integration

## 🚀 Quick Start

### Prerequisites

- AWS Account with Bedrock access
- Ubuntu EC2 instance (t2.small or larger)
- Docker and Docker Compose
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/amathur2k/scrape2llm.git
   cd scrape2llm
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   source install.sh
   ```

3. **Configure environment**
   ```bash
   cp .env.example .env
   # Edit .env with your AWS Bedrock credentials
   ```

### Usage

1. **Start the service**
   ```bash
   docker compose up --build
   ```

2. **Run the example**
   ```bash
   conda activate scrape2llm
   python example.py
   ```

## 🛠️ Configuration

### AWS Setup

1. Configure [AWS Bedrock](https://aws.amazon.com/bedrock/) access
2. Set up [Bedrock API Gateway](https://github.com/aws-samples/bedrock-access-gateway)

### EC2 Instance Requirements

- **Instance Type:** t2.small (minimum)
- **OS:** Ubuntu
- **Storage:** 20GB
- **Security Group:** Allow inbound traffic on port 3002

## 📚 Documentation

For detailed usage examples and API documentation, see our [Wiki](https://github.com/amathur2k/scrape2llm/wiki).

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📧 Contact

For support or queries, please [open an issue](https://github.com/amathur2k/scrape2llm/issues).

---

Made with ❤️ by [amathur2k](https://github.com/amathur2k)
