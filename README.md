# Polly Text-to-Speech Lambda Function

This project contains an AWS Lambda function that uses Amazon Polly to convert text into speech and stores the resulting audio file in an Amazon S3 bucket.

## Overview

The Lambda function takes text as input (either the default "Hello from Amazon Polly" or text provided in the event payload), uses the Amazon Polly service to synthesize speech using the 'Ivy' voice, and then saves the generated MP3 audio file to a specified S3 bucket. Each audio file is saved with a unique UUID as its filename.

## Prerequisites

Before deploying this Lambda function, you need to have the following:

 **AWS Account:** You need an active AWS account.
 **AWS CLI Configured:** Ensure you have the AWS Command Line Interface (CLI) installed and configured with your AWS credentials.
 **S3 Bucket:** An existing Amazon S3 bucket where the generated audio files will be stored. **Make sure to replace `'text-nar-saad'` in the code with the actual name of your bucket.**
 **IAM Role:** An IAM role with the necessary permissions for the Lambda function to:
    * Invoke the Amazon Polly service.
    * Put objects into the specified S3 bucket.

## Deployment

You can deploy this Lambda function using the AWS CLI or other infrastructure-as-code tools like AWS CloudFormation or Serverless Framework. Here's a basic outline using the AWS CLI:

1.  **Package the code:** Create a ZIP file containing your Python script (`lambda_function.py`).
    ```bash
    zip lambda_function.zip lambda_function.py
    ```

2.  **Create the Lambda function:** Use the `aws lambda create-function` command. **Replace the placeholders with your actual values.**

    ```bash
    aws lambda create-function \
        --function-name polly-text-to-speech \
        --zip-file fileb://lambda_function.zip \
        --handler lambda_function.lambda_handler \
        --runtime python3.x \
        --role arn:aws:iam::YOUR_ACCOUNT_ID:role/YOUR_LAMBDA_EXECUTION_ROLE \
        --region YOUR_AWS_REGION
    ```

     `--function-name`: The name you want to give your Lambda function.
     `--zip-file`: The path to the ZIP file you created.
     `--handler`: The entry point of your Lambda function code (`filename.function_name`).
     `--runtime`: The Python runtime environment you are using.
     `--role`: The ARN of the IAM role with the necessary permissions.
     `--region`: The AWS region where you want to deploy the function.

3.  **Update the S3 bucket name (if you haven't already) in the `lambda_function.py` file before zipping and deploying.**

## Usage

You can invoke this Lambda function in various ways, such as:

 **Directly from the AWS Management Console:** You can provide a JSON payload as input. For example:
    ```json
    {
      "text": "This is some custom text I want Polly to read."
    }
    ```
    If no "text" key is provided in the event, it will default to "Hello from Amazon Polly".

 **From other AWS services:** You can configure other AWS services (like API Gateway, S3 event triggers, etc.) to trigger this Lambda function.

## Output

Upon successful execution, the Lambda function will return a JSON response indicating the status code and a message containing the name of the saved audio file and the S3 bucket it was stored in. For example:

```json
{
  "statusCode": 200,
  "body": "Audio file saved as a1b2c3d4-e5f6-7890-1234-567890abcdef.mp3 in text-nar-saad}"
}
