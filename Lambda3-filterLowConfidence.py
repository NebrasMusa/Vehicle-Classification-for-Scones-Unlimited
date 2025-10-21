import json

THRESHOLD = 0.93

def lambda_handler(event, context):
    # Get inferences from event body
    body = event.get('body', {})
    inferences = body.get("inferences", [])
    
    # Check if any values in our inferences are above THRESHOLD
    meets_threshold = any(i >= THRESHOLD for i in inferences)
    
    # If our threshold is met, pass our data back out of the
    # Step Function, else, end the Step Function with an error
    if meets_threshold:
        max_confidence = max(inferences)
        print(f"Threshold met! Max confidence: {max_confidence:.2%}")
        return {
            'statusCode': 200,
            'body': body
        }
    else:
        max_confidence = max(inferences)
        print(f"Threshold not met! Max confidence: {max_confidence:.2%} < {THRESHOLD:.2%}")
        raise Exception(f"THRESHOLD_CONFIDENCE_NOT_MET")