import requests
import time
import logging
from typing import Dict, Any
import sys

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

POLLING_INTERVAL_SECONDS = 5  # Time to wait between status checks
EC2_INSTANCE_PUBLIC_URL = None

for url in ["http://localhost:3002", "http://ec2-35-90-90-3.us-west-2.compute.amazonaws.com:3002"]: 
    try:
        response = requests.get(url, timeout=2)
        if response.status_code == 200:
            EC2_INSTANCE_PUBLIC_URL = url
            break
    except requests.RequestException:
        continue

if EC2_INSTANCE_PUBLIC_URL is None:
    logger.error("Could not connect to any Firecrawl instance. Please ensure the service is running.")
    sys.exit(1)
else:
    logger.info(f"Using Firecrawl from URL: {EC2_INSTANCE_PUBLIC_URL}")
    


# Schema for the API request
API_SCHEMA = {
    "type": "object",
    "properties": {
        "marketing_statement": {
            "type": "string"
        },
        "pictures": {
            "type": "array",
            "items": {
                "type": "string"
            }
        }
    },
    "required": [
        "marketing_statement"
    ]
} 



def process_url(url: str, word_count: int, image_count: int) -> tuple[str, list[str]]:
    # Call the API
    result = APIClient.extract_content(url, word_count, image_count)
    
    # Check for errors
    if not result["success"]:
        return result["error"], []
    
    # Get the response
    api_response = result["response"]
    
    # Extract marketing statement and pictures
    marketing_statement = api_response.get("data", {}).get("marketing_statement", "No marketing statement available")
    pictures = api_response.get("data", {}).get("pictures", [])
    
    logger.info("Extracted marketing statement and pictures from response")
    
    return marketing_statement, pictures

class APIClient:
    @staticmethod
    def create_prompt(word_count: int, image_count: int) -> str:
        prompt = (
            f"Create a summary of approximately {word_count} words about the services "
            f"provided by the company. On the basis of this summary craft a marketing "
            f"statement in the first person. Extract {image_count} relevant pictures "
            f"from the profile to showcase and complement it. Ensure these images are valid image urls."
            f"relevance to the marketing statement."
        )
        logger.info(f"Created prompt with word_count={word_count}, image_count={image_count}")
        return prompt

    @staticmethod
    def get_status(request_id: str, max_retries: int = 30) -> Dict[str, Any]:
        """Poll the status endpoint until success or max retries reached"""
        status_url = f"{EC2_INSTANCE_PUBLIC_URL}/v1/extract/{request_id}"
        retries = 0
        logger.info(f"Starting status polling for request_id: {request_id}")

        while retries < max_retries:
            try:
                logger.debug(f"Polling attempt {retries + 1}/{max_retries}")
                response = requests.get(status_url)
                response.raise_for_status()
                result = response.json()

                # Check if the request is still processing
                if result.get("status") == "processing":
                    logger.info(f"Request still processing, waiting {POLLING_INTERVAL_SECONDS} seconds (attempt {retries + 1})")
                    time.sleep(POLLING_INTERVAL_SECONDS)
                    retries += 1
                    continue

                # If not processing, return the result
                logger.info("Received final response from status endpoint")
                return {"success": True, "response": result}

            except requests.RequestException as e:
                error_msg = f"Status check failed: {str(e)}"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}

        error_msg = "Maximum retries reached while waiting for processing to complete"
        logger.error(error_msg)
        return {"success": False, "error": error_msg}

    @staticmethod
    def extract_content(url: str, word_count: int, image_count: int) -> Dict[str, Any]:
        try:
            logger.info(f"Starting content extraction for URL: {url}")
            
            # Initial POST request
            payload = {
                "urls": [url],
                "prompt": APIClient.create_prompt(word_count, image_count),
                "schema": API_SCHEMA
            }
            
            headers = {
                "Content-Type": "application/json"
            }
            
            logger.info("Sending initial POST request")
            response = requests.post(f"{EC2_INSTANCE_PUBLIC_URL}/v1/extract", json=payload, headers=headers)
            response.raise_for_status()
            initial_response = response.json()

            if not initial_response.get("success"):
                error_msg = "Initial request failed"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}

            # Get the request ID
            request_id = initial_response.get("id")
            if not request_id:
                error_msg = "No request ID received"
                logger.error(error_msg)
                return {"success": False, "error": error_msg}

            logger.info(f"Received request ID: {request_id}")
            
            # Poll for results
            return APIClient.get_status(request_id)
            
        except requests.RequestException as e:
            error_msg = f"API request failed: {str(e)}"
            logger.error(error_msg)
            return {"success": False, "error": error_msg} 