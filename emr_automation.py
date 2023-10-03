import boto3

emr_client = boto3.client('emr', region_name='your-region')
ecs_client = boto3.client('ecs', region_name='your-region')

emr_cluster_config = {
    'Name': 'YourClusterName',
    'ReleaseLabel': 'emr-5.32.0',
    'Applications': [
        {'Name': 'Spark'},
        {'Name': 'Hive'},
        {'Name': 'Livy'},
        {'Name': 'Presto'}
    ],
    'Instances': {
        'InstanceGroups': [
            {
                'Name': 'Master',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'MASTER',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 1
            },
            {
                'Name': 'Core',
                'Market': 'ON_DEMAND',
                'InstanceRole': 'CORE',
                'InstanceType': 'm5.xlarge',
                'InstanceCount': 2
            }
        ],
        'Ec2KeyName': 'YourKeyPairName',
        'KeepJobFlowAliveWhenNoSteps': True,
        'TerminationProtected': False
    },
    'VisibleToAllUsers': True,
    'LogUri': 's3://your-log-bucket/logs',
    'JobFlowRole': 'EMR_EC2_DefaultRole',
    'ServiceRole': 'EMR_DefaultRole'
}

response = emr_client.run_job_flow(**emr_cluster_config)
cluster_id = response['JobFlowId']

ecs_task_definition = {
    'family': 'YourTaskDefinitionFamily',
    'containerDefinitions': [
        {
            'name': 'YourContainerName',
            'image': 'your-docker-image',
            'memory': 512,
            'cpu': 256,
            'essential': True
        }
    ]
}

ecs_response = ecs_client.register_task_definition(**ecs_task_definition)
task_definition_arn = ecs_response['taskDefinition']['taskDefinitionArn']

emr_client.add_job_flow_steps(JobFlowId=cluster_id, Steps=[
    {
        'Name': 'ConnectToECS',
        'ActionOnFailure': 'CONTINUE',
        'HadoopJarStep': {
            'Jar': 'command-runner.jar',
            'Args': [
                'ecs', 'synchronize', '--cluster', 'YourECSClusterName', '--task-definition', task_definition_arn
            ]
        }
    }
])

print(f'EMR Cluster ID: {cluster_id} created and connected to ECS Task Definition: {task_definition_arn}')
