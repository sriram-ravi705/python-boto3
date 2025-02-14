import boto3

ec2_client=boto3.client('ec2')
ec2_resource=boto3.resource('ec2')
sns_client=boto3.client('sns')

tag=[
    {
        'Key': 'Backup',
        'Value': 'Yes'
    }
]

ec2_client.run_instances(ImageId="ami-085ad6ae776d8f09c",MaxCount=1,MinCount=1,InstanceType="t2.micro",
                  TagSpecifications=[{'ResourceType':'instance','Tags':tag}])
backup_filter=[
    {
        'Name': 'tag:Backup',
        'Values': ['Yes']
    }
]

snapshot_ids=[]

for instance in ec2_resource.instances.filter(Filters=backup_filter):
    for volume in instance.volumes.all():
        snapshot=volume.create_snapshot(Description='created by boto3')
        snapshot_ids.append(snapshot.snapshot_id)

sns_client.publish(
    TopicArn="arn:aws:sns:us-east-1:266735803751:pythonboto2",
    Subject="Volume is succes fully backuped",
    Message=str(snapshot_ids)
)