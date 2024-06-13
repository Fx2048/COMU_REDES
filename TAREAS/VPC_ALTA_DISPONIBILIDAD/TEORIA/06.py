#Paquete BOTO3
import boto3

# Configurar cliente de AWS para NLB y GWLB:
elbv2_client = boto3.client('elbv2', region_name='us-east-1')
network_firewall_client = boto3.client('network-firewall', region_name='us-east-1')

# Crear un Network Load Balancer (NLB)
response_nlb = elbv2_client.create_load_balancer(
    Name='MyNLB',
    Subnets=['subnet-12345678', 'subnet-87654321'],
    Scheme='internet-facing',
    Type='network',
    IpAddressType='ipv4',
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyNLB'
        },
    ]
)

# Crear un Gateway Load Balancer (GWLB)
response_gwlb = network_firewall_client.create_firewall(
    FirewallName='MyGWLB', #políticas de firewall
    FirewallPolicyArn='arn:aws:network-firewall:us-east-1:123456789012:stateful-rule-group/applications/MyFirewallPolicy',#políticas de firewall
    VpcId='vpc-12345678',
    SubnetMappings=[
        {
            'SubnetId': 'subnet-12345678',
        },
        {
            'SubnetId': 'subnet-87654321',
        },
    ],
    Tags=[
        {
            'Key': 'Name',
            'Value': 'MyGWLB'
        },
    ]
)

# Imprimir las respuestas de creación
print("NLB creado:", response_nlb)
print("GWLB creado:", response_gwlb)
