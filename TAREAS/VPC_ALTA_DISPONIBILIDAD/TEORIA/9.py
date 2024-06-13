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


# Configurar la plantilla de lanzamiento (Launch Template)
launch_template = {
    'LaunchTemplateName': 'my-launch-template',
    'Version': '1',
    'LaunchTemplateData': {
        'ImageId': 'ami-87654321',
        'InstanceType': 't3.micro',
        'KeyName': 'my-key-pair',
        'SecurityGroupIds': ['sg-87654321'],
        'UserData': 'base64-encoded-user-data'
    }
}

# Crear la plantilla de lanzamiento
response = autoscaling.create_launch_template(**launch_template)

# Utilizar la plantilla de lanzamiento en un nuevo grupo de Auto Scaling
auto_scaling_group_with_template = {
    'AutoScalingGroupName': 'my-auto-scaling-group-with-template',
    'LaunchTemplate': {
        'LaunchTemplateName': 'my-launch-template',
        'Version': '1'
    },
    'MinSize': 2,
    'MaxSize': 5,
    'DesiredCapacity': 2,
    'AvailabilityZones': ['us-east-1a', 'us-east-1b'],
    'HealthCheckType': 'EC2',
    'HealthCheckGracePeriod': 300,
    'Tags': [
        {'Key': 'Name', 'Value': 'my-asg-instance-with-template'}
    ]
}

# Crear el grupo de Auto Scaling utilizando la plantilla de lanzamiento
response = autoscaling.create_auto_scaling_group(**auto_scaling_group_with_template)

# Imprimir la respuesta
print("Grupo de Auto Scaling con plantilla creado:", response)

