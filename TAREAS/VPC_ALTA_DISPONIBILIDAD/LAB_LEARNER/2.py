import boto3

# Configura las credenciales de AWS (asegúrate de configurar tus propias credenciales)
aws_access_key_id = 'TU_ACCESS_KEY'
aws_secret_access_key = 'TU_SECRET_KEY'
region_name = 'us-east-1'  # Cambia esto según tu región

# Crea un cliente para Auto Scaling
autoscaling_client = boto3.client('autoscaling', aws_access_key_id=aws_access_key_id,
                                  aws_secret_access_key=aws_secret_access_key, region_name=region_name)

# Define los parámetros del grupo de escalado
group_name = 'MiASG'  # Nombre de tu grupo de escalado
min_size = 2  # Número mínimo de instancias
max_size = 5  # Número máximo de instancias
desired_capacity = 3  # Número deseado de instancias
launch_template_id = 'ID_DE_TU_PLANTILLA_DE_LANZAMIENTO'  # Cambia esto por la ID de tu plantilla de lanzamiento

# Crea el grupo de escalado
response = autoscaling_client.create_auto_scaling_group(
    AutoScalingGroupName=group_name,
    MinSize=min_size,
    MaxSize=max_size,
    DesiredCapacity=desired_capacity,
    LaunchTemplate={
        'LaunchTemplateId': launch_template_id,
        'Version': '$Latest'  # Utiliza la última versión de la plantilla
    }
)

# Define una política de escalado basada en el uso de CPU
cpu_policy = {
    'AutoScalingGroupName': group_name,
    'PolicyName': 'CPUScalingPolicy',
    'AdjustmentType': 'ChangeInCapacity',
    'ScalingAdjustment': 1,  # Aumenta o disminuye en 1 instancia
    'Cooldown': 300,  # Tiempo de espera entre ajustes (en segundos)
    'MetricAggregationType': 'Average',
    'StepAdjustments': [
        {
            'MetricIntervalLowerBound': 0,
            'MetricIntervalUpperBound': 50,
            'ScalingAdjustment': 1
        },
        {
            'MetricIntervalLowerBound': 50,
            'ScalingAdjustment': -1
        }
    ]
}

# Crea la política de escalado
autoscaling_client.put_scaling_policy(PolicyName=cpu_policy['PolicyName'],
                                      AutoScalingGroupName=group_name,
                                      AdjustmentType=cpu_policy['AdjustmentType'],
                                      ScalingAdjustment=cpu_policy['ScalingAdjustment'],
                                      Cooldown=cpu_policy['Cooldown'],
                                      MetricAggregationType=cpu_policy['MetricAggregationType'],
                                      StepAdjustments=cpu_policy['StepAdjustments'])

print(f"Grupo de escalado {group_name} creado con éxito.")
print(f"Política de escalado basada en CPU creada: {cpu_policy['PolicyName']}")

# ¡Agrega más funciones y lógica según tus necesidades!
