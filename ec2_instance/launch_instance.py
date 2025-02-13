import boto3

ec2=boto3.client("ec2")
response=ec2.run_instances(ImageId="ami-085ad6ae776d8f09c",InstanceType="t2.micro",
                           MaxCount=1,MinCount=1)

for instance in response["Instances"]:
    print(instance["InstanceId"])