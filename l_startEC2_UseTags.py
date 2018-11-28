# code to start EC2 instaces based on the Tag Key start and value yes
# pl. amend the tag values against your EC2 accordingly
# rule will stop instances by 9AM GMT
import boto3
client=boto3.client('ec2')
def lambda_handler(event, context):
    response=client.describe_instances(Filters=[{'Name': 'tag:start', 'Values': ['yes', 'Yes']}, 
                                                {'Name': 'instance-state-name','Values': ['stopped']}])
    for reservation in response["Reservations"]:
	    for instance in reservation["Instances"]:
		    id=[instance["InstanceId"]]
            client.stop_instances(InstanceIds=id)
            print(instance["InstanceId"] + "started")
    return("Completed")