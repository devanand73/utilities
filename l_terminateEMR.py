#lambda script to terminate all active EMR clusters 
import boto3
emr_client = boto3.client('emr')
def lambda_handler(event, context):
    clusters = emr_client.list_clusters(ClusterStates=['STARTING', 'BOOTSTRAPPING', 'RUNNING', 'WAITING'])
    cluster_ids = [c["Id"] for c in clusters["Clusters"]]
    response = emr_client.set_termination_protection(
        JobFlowIds=cluster_ids,
        TerminationProtected=False
    )
    response = emr_client.terminate_job_flows(
        JobFlowIds=cluster_ids
        )
    print("Terminated all active clusters...")