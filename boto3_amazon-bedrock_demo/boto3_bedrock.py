import boto3
import json
from botocore.exceptions import ClientError

# Creates a Bedrock Runtime client in the us-east-1 AWS region
bedrock_client = boto3.client("bedrock-runtime", region_name="us-east-1")

# ModelId for the Anthropic Claude Haiku model
model_id = "anthropic.claude-3-haiku-20240307-v1:0"

# Ask for the user input prompt
print("Please enter your query:")
prompt = input()
print("")

# Format the request payload using the model's native structure.
native_request = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 1024,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}],
        }
    ],
}

# Convert the native request to JSON.
request = json.dumps(native_request)

# Invoke the model with the request.
try:
    response = bedrock_client.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

model_response = json.loads(response["body"].read())

# Extract and print the response text.
result = model_response["content"][0]["text"]
print(result)