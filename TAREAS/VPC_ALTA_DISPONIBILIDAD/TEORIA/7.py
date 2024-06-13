import boto3

# Configurar cliente de AWS para CLB
elb_client = boto3.client('elb', region_name='us-east-1')

# Crear un Classic Load Balancer
response = elb_client.create_load_balancer(
    LoadBalancerName='my-clb',
    Listeners=[
        {
            'Protocol': 'HTTP',
            'LoadBalancerPort': 80,
            'InstanceProtocol': 'HTTP',
            'InstancePort': 80,
        },
    ],
    AvailabilityZones=[
        'us-east-1a',  # Agregar aquí las zonas de disponibilidad deseadas
        'us-east-1b',
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyCLB'
        },
    ]
)

# Imprimir la respuesta de creación
print("Classic Load Balancer creado:", response)
