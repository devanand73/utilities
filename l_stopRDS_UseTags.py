#################################################################################################
#	Author:  Nirmala G
#	Purpose: This script is to be used for AWS cloud to stop all running RDS instances 
#		 automatically; as an additional bonus, am filtering the RDS to be stopped based 
#		 based on the tag values been set in RDS, rather than stopping all at once
#		 In Test & Production environments we need to eliminate those env. which are to 
# 		 to be up & running always and hence the tag/value usage
#	Setup:	 One setup activity to be done is that, you need to set the tag as 'Stop:yes' 
#		 and/or 'Stop:no' for all RDS instances in you wanted to configure in aws account
#	Version: 1.0
#
#################################################################################################

# script to check for each RDS instance tag values and stop instance by the scheduled time
import boto3
client=boto3.client('rds')
def lambda_handler(event, context):
  response = client.describe_db_instances()
  for resp in response['DBInstances']:
    db_instance_arn = resp['DBInstanceArn']
    response = client.list_tags_for_resource(ResourceName=db_instance_arn)
    for tags in response['TagList']:
        if tags['Key'] == 'Stop' and tags['Value'] == 'yes':
            status = resp['DBInstanceStatus']
            InstanceID = resp['DBInstanceIdentifier']
            print(InstanceID)
            if status == 'available':
                print("shutting down %s " % InstanceID)
                client.stop_db_instance(DBInstanceIdentifier= InstanceID)
            else:
                print("The database is " + status + " status!")