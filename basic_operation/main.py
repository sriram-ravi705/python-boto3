import boto3

s3 = boto3.client('s3')
resource = s3.list_buckets()
for bucket in resource['Buckets']:
    print(bucket['Name'])