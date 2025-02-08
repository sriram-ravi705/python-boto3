import boto3

s3_client = boto3.client('s3')

# creating a bucket
response = s3_client.create_bucket(Bucket="my-bucket-08022025")

# upload a file in a bucket
response = s3_client.upload_file('boto3.txt','my-bucket-08022025','boto3.txt')

# download a file from a bucket
response = s3_client.download_file('my-bucket-08022025','boto3.txt','download/boto3.txt')

# delete a object from a bucket
response = s3_client.delete_object(Bucket='my-bucket-08022025',Key='boto3.txt')

# delete a bucket
response = s3_client.delete_bucket(Bucket='my-bucket-08022025')

print(response)
