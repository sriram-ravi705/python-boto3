import boto3

ec2=boto3.client("ec2")
ec2.stop_instances(InstanceIds=["i-02c09b89f799d587c"])
ec2.start_instances(InstanceIds=["i-02c09b89f799d587c"])
ec2.terminate_instances(InstanceIds=["i-02c09b89f799d587c"])