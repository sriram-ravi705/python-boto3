import boto3

ec2 = boto3.resource('ec2')

for res in ec2.instances.all():
    print(res)