import boto3
import os

s3 = boto3.client('s3')

bucket_name = 'neureal'
prefix = 'images/' # The prefix for the images, e.g. 'images/'

response = s3.list_objects_v2(Bucket=bucket_name, Prefix=prefix)

def get_bucket_images():

    for object in response['Contents']:
        object_key = object['Key']
        if object_key.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif')):
            response = s3.get_object(Bucket=bucket_name, Key=object_key)
            file_name = os.path.join('static/images_2', object_key)
            os.makedirs(os.path.dirname(file_name), exist_ok=True)
            with open(file_name, 'wb') as f:
                f.write(response['Body'].read())
