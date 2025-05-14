import boto3

def lambda_handler(event, context):
    # Define EMR parameters
    emr_client = boto3.client('emr')
    cluster_name = "YourClusterName"
    release_label = "emr-6.3.0"
    instance_type = "m5.xlarge"
    instance_count = 2
    key_name = "YourKeyName"
    log_uri = "s3://YourBucket/logs/"
    applications = ["Hadoop", "Hive", "Hue", "Spark"]

    # Create EMR cluster
    response = emr_client.run_job_flow(
        Name=cluster_name,
        ReleaseLabel=release_label,
        Instances={
            'InstanceGroups': [
                {
                    'Name': 'Master',
                    'InstanceRole': 'MASTER',
                    'InstanceType': instance_type,
                    'InstanceCount': 1
                },
                {
                    'Name': 'Core',
                    'InstanceRole': 'CORE',
                    'InstanceType': instance_type,
                    'InstanceCount': instance_count - 1
                }
            ],
            'KeepJobFlowAliveWhenNoSteps': False,
            'TerminationProtected': False,
            'Ec2KeyName': key_name,
            'Ec2SubnetId': 'YourSubnetId',
        },
        Applications=[{'Name': app} for app in applications],
        LogUri=log_uri,
        ServiceRole='YourEMRServiceRole',
        VisibleToAllUsers=True
    )

    # Return cluster ID
    return response['JobFlowId']
