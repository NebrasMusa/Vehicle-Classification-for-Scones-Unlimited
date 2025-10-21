import json
import boto3
import base64
from botocore.exceptions import ClientError

sagemaker_runtime = boto3.client('sagemaker-runtime')
ENDPOINT = "image-classification-2025-10-04-04-32-33-573"

def lambda_handler(event, context):
    try:
        print("Received event:", json.dumps(event, indent=2))
        
        # Get data from Step Function
        body = event.get('body', {})
        if isinstance(body, str):
            body = json.loads(body)
            
        image_data = body.get('image_data')
        
        if not image_data:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    "error": "Missing image_data in event body"
                })
            }
        
        # Decode the image data
        image = base64.b64decode(image_data)

        # Make prediction using SageMaker Runtime
        response = sagemaker_runtime.invoke_endpoint(
            EndpointName=ENDPOINT,
            ContentType='image/png',
            Body=image
        )
        
        # Parse the response
        inferences = response['Body'].read().decode('utf-8')
        print(f"Raw inference response: {inferences}")

        # Update the event body with inferences
        body["inferences"] = json.loads(inferences)
        
        return {
            'statusCode': 200,
            'body': body
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        error_msg = f"SageMaker error ({error_code}): {e.response['Error']['Message']}"
        print(error_msg)
        
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": error_msg,
                "endpoint": ENDPOINT
            })
        }
    
    except Exception as e:
        error_msg = f"Unexpected error: {str(e)}"
        print(error_msg)
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": error_msg
            })
        }