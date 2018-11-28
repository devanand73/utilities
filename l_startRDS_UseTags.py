# script to check for each RDS instance tag values and start instance by the scheduled time
import boto3
client=boto3.client('rds')
def lambda_handler(event, context):
  response = client.describe_db_instances()
  for resp in response['DBInstances']:
    db_instance_arn = resp['DBInstanceArn']
    response = client.list_tags_for_resource(ResourceName=db_instance_arn)
    for tags in response['TagList']:
        if tags['Key'] == 'start' and tags['Value'] == 'yes':
            status = resp['DBInstanceStatus']
            InstanceID = resp['DBInstanceIdentifier']
            print(InstanceID)
            if status == 'available':
                print("shutting down %s " % InstanceID)
                client.start_db_instance(DBInstanceIdentifier= InstanceID)
            else:
                print("The database is " + status + " status!")