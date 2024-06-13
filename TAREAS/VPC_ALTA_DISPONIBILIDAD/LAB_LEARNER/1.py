import boto3

def create_vpc():
    """
    Crea una VPC con dos subnets públicas en diferentes zonas de disponibilidad.
    """
    ec2 = boto3.client('ec2')
    
    # Crear VPC
    vpc_response = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc_response['Vpc']['VpcId']
    
    # Crear subnets en diferentes zonas de disponibilidad
    subnet1_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24', AvailabilityZone='us-east-1a')
    subnet2_response = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.2.0/24', AvailabilityZone='us-east-1b')
    
    return vpc_id, subnet1_response['Subnet']['SubnetId'], subnet2_response['Subnet']['SubnetId']

def create_ec2_instances(subnet1_id, subnet2_id):
    """
    Lanza dos instancias EC2 en diferentes subnets.
    """
    ec2 = boto3.resource('ec2')
    
    # Crear instancias EC2
    instance1 = ec2.create_instances(ImageId='ami-12345678', InstanceType='t2.micro', SubnetId=subnet1_id)
    instance2 = ec2.create_instances(ImageId='ami-12345678', InstanceType='t2.micro', SubnetId=subnet2_id)
    
    return instance1[0].id, instance2[0].id

def create_alb(target_group_arns):
    """
    Crea un Application Load Balancer y agrega las instancias EC2 como objetivos.
    """
    elbv2 = boto3.client('elbv2')
    
    # Crear ALB
    alb_response = elbv2.create_load_balancer(Name='MyALB', Subnets=['subnet-1', 'subnet-2'], Scheme='internet-facing')
    alb_arn = alb_response['LoadBalancers'][0]['LoadBalancerArn']
    
    # Crear grupo de objetivos
    target_group_response = elbv2.create_target_group(Name='MyTargetGroup', Protocol='HTTP', Port=80, VpcId='vpc-12345678')
    target_group_arn = target_group_response['TargetGroups'][0]['TargetGroupArn']
    
    # Registrar instancias EC2 en el grupo de objetivos
    elbv2.register_targets(TargetGroupArn=target_group_arn, Targets=[{'Id': 'i-12345678'}, {'Id': 'i-98765432'}])
    
    # Agregar regla de listener para enrutar tráfico HTTP al grupo de objetivos
    elbv2.create_listener(LoadBalancerArn=alb_arn, Protocol='HTTP', Port=80, DefaultActions=[{'Type': 'forward', 'TargetGroupArn': target_group_arn}])
    
    return alb_arn

if __name__ == '__main__':
    vpc_id, subnet1_id, subnet2_id = create_vpc()
    instance1_id, instance2_id = create_ec2_instances(subnet1_id, subnet2_id)
    target_group_arns = [f'arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/MyTargetGroup/{target_group_id}' for target_group_id in [instance1_id, instance2_id]]
    alb_arn = create_alb(target_group_arns)
    print(f"ALB creado con ARN: {alb_arn}")
