import json
import boto3
import base64
from botocore.exceptions import ClientError

s3 = boto3.client('s3')

def lambda_handler(event, context):
    try:
        # Get parameters
        key = event.get("s3_key")
        bucket = event.get("s3_bucket")
        
        # Validate inputs
        if not key or not bucket:
            return {
                'statusCode': 400,
                'body': json.dumps({
                    "error": "Missing s3_bucket or s3_key in event"
                })
            }
        
        # Download and process the image
        s3.download_file(bucket, key, "/tmp/image.png")
        
        with open("/tmp/image.png", "rb") as f:
            image_data = base64.b64encode(f.read()).decode('utf-8')

        return {
            'statusCode': 200,
            'body': {
                "image_data": image_data,
                "s3_bucket": bucket,
                "s3_key": key,
                "inferences": []
            }
        }
        
    except ClientError as e:
        error_code = e.response['Error']['Code']
        if error_code == '403':
            return {
                'statusCode': 403,
                'body': json.dumps({
                    "error": "Access denied to S3 bucket",
                    "detail": "Check Lambda execution role permissions"
                })
            }
        elif error_code == 'NoSuchKey':
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"Object not found: {key}"
                })
            }
        elif error_code == 'NoSuchBucket':
            return {
                'statusCode': 404,
                'body': json.dumps({
                    "error": f"Bucket not found: {bucket}"
                })
            }
        else:
            return {
                'statusCode': 500,
                'body': json.dumps({
                    "error": f"S3 error: {str(e)}"
                })
            }
    
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps({
                "error": f"Unexpected error: {str(e)}"
            })
        }