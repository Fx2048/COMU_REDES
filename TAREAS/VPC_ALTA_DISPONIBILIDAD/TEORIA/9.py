import boto3

# Configurar el cliente de Auto Scaling
autoscaling = boto3.client('autoscaling', region_name='us-east-1')

# Definir la configuración de lanzamiento (Launch Configuration)
launch_config = {
    'LaunchConfigurationName': 'my-launch-config',
    'ImageId': 'ami-12345678',
    'InstanceType': 't2.micro',
    'KeyName': 'my-key-pair',
    'SecurityGroups': ['sg-12345678'],
    'UserData': 'base64-encoded-user-data'
}

# Crear la configuración de lanzamiento
response = autoscaling.create_launch_configuration(**launch_config)

# Definir el grupo de Auto Scaling (Auto Scaling Group)
auto_scaling_group = {
    'AutoScalingGroupName': 'my-auto-scaling-group',
    'LaunchConfigurationName': 'my-launch-config',
    'MinSize': 2,
    'MaxSize': 5,
    'DesiredCapacity': 2,
    'AvailabilityZones': ['us-east-1a', 'us-east-1b'],
    'HealthCheckType': 'EC2',
    'HealthCheckGracePeriod': 300,
    'Tags': [
        {'Key': 'Name', 'Value': 'my-asg-instance'}
    ]
}

# Crear el grupo de Auto Scaling
response = autoscaling.create_auto_scaling_group(**auto_scaling_group)

# Imprimir la respuesta
print("Grupo de Auto Scaling creado:", response)
