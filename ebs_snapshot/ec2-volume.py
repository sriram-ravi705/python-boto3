import boto3
import datetime

ec2_resource = boto3.resource('ec2')
ec2_sns = boto3.client('sns')

current_date = datetime.datetime.now(datetime.timezone.utc)

snapshots=ec2_resource.snapshots.filter(OwnerIds=['self'])

snapshot_ids=[]

for snapshot in snapshots:
    snapshot_id = snapshot.id
    snapshot_date = snapshot.start_time

    snapshot_age = current_date - snapshot_date.replace(tzinfo=datetime.timezone.utc)

    if snapshot_age.days > 30:
        snapshot_ids.append(snapshot_id)
        snapshot.delete()



ec2_sns.publish(
    TopicArn="arn:aws:sns:us-east-1:266735803751:pythonboto2",
    Subject="These snapshots has been deleted",
    Message=str(snapshot_ids),
)