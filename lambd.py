import boto3
import uuid

def lambda_handler(event, context):
    text = event.get("text", "Hello from Amazon Polly")
    polly = boto3.client('polly')
    s3 = boto3.client('s3')

    response = polly.synthesize_speech(
        Text=text,
        OutputFormat='mp3',
        VoiceId='Ivy'
    )

    audio_stream = response['AudioStream'].read()
    file_name = f"{uuid.uuid4()}.mp3"
    bucket_name = 'text-nar-saad' 

    s3.put_object(
        Bucket=bucket_name,
        Key=file_name,
        Body=audio_stream,
        ContentType='audio/mpeg'
    )

    return {
        'statusCode': 200,
        'body': f"Audio file saved as {file_name} in {text-nar-saad}}"
    }
