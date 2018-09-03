#################################################################################################
#	Author:  Nirmala G
#	Purpose: This script is to be used for AWS cloud to stop all running EC2 instances 
#		 automatically; as an additional bonus, am filtering the EC2s to be stopped based 
#		 based on the tag values been set in EC2s, rather than stopping all at once
#		 In Test & Production environments we need to eliminate those env. which are to 
# 		 to be up & running always and hence the tag/value usage
#	Version: 1.0
#
#################################################################################################

import boto3
client=boto3.client('ec2')
def lambda_handler(event, context):
    response=client.describe_instances(Filters=[{'Name': 'tag:Stop', 'Values': ['yes']}])
    for reservation in response["Reservations"]:
	    for instance in reservation["Instances"]:
		    print(instance["InstanceId"] + "stopping")
		    id=[instance["InstanceId"]]
    client.stop_instances(InstanceIds=id)
    return("Completed")