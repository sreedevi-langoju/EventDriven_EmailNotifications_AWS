import boto3
import os

# Create S3 and SNS clients
s3 = boto3.client('s3')
sns = boto3.client('sns')

# SNS topic ARN
sns_topic_arn = os.environ['sns_topic_arn']

def lambda_handler(event, context):
    # Get the bucket and file name from the S3 event
    bucket_name = event['Records'][0]['s3']['bucket']['name']
    file_key = event['Records'][0]['s3']['object']['key']
    
    # Read the content of the file
    response = s3.get_object(Bucket=bucket_name, Key=file_key)
    content = response['Body'].read().decode('utf-8')
    
    # Calculate word count
    word_count = len(content.split())
    
    # Send SNS message (email)
    email_message = f"The word count in the {file_key} file is {word_count}."
    sns.publish(
        TopicArn=sns_topic_arn,
        Message=email_message,
        Subject="Word Count Result"
    )
      
    return {
        'statusCode': 200,
        'body': 'Word count calculated and message sent successfully.'
    }
