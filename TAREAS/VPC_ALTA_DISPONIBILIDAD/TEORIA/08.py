import boto3

# Configurar el cliente de Auto Scaling
autoscaling = boto3.client('autoscaling', region_name='us-east-1')

# Definir el nombre del grupo de Auto Scaling
auto_scaling_group_name = 'my-auto-scaling-group'

# Definir la política de escalado basada en métricas (ejemplo: tráfico de red)
response = autoscaling.put_scaling_policy(
    AutoScalingGroupName=auto_scaling_group_name,
    PolicyName='NetworkTrafficScalingPolicy',
    PolicyType='TargetTrackingScaling',
    TargetTrackingConfiguration={
        'PredefinedMetricSpecification': {
            'PredefinedMetricType': 'ALBRequestCountPerTarget',
        },
        'TargetValue': 1000,  # Número objetivo de solicitudes por minuto
        'ScaleInCooldown': 60,  # Tiempo mínimo entre escalados hacia abajo
        'ScaleOutCooldown': 60,  # Tiempo mínimo entre escalados hacia arriba
    },
    EstimatedInstanceWarmup=300,  # Tiempo estimado para que las nuevas instancias se activen
    Enabled=True
)

# Imprimir la respuesta de la configuración de la política de escalado
print("Política de escalado creada:", response)

# Crear un grupo de Auto Scaling
aws autoscaling create-auto-scaling-group \
    --auto-scaling-group-name MyAutoScalingGroup \
    --launch-configuration-name MyLaunchConfig \
    --min-size 2 \
    --max-size 5 \
    --desired-capacity 3

# Crear una política de escalado
aws autoscaling put-scaling-policy \
    --auto-scaling-group-name MyAutoScalingGroup \
    --policy-name MyScalingPolicy \
    --adjustment-type ChangeInCapacity \
    --scaling-adjustment 1

