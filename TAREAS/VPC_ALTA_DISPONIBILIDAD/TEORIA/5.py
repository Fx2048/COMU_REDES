import boto3

class MyLoadBalancer:
    def __init__(self, lb_name, instance_ids):
        """
        Clase para configurar un balanceador de carga en una VPC.

        Args:
            lb_name (str): Nombre del balanceador de carga.
            instance_ids (list): Lista de IDs de instancias de servidor.
        """
        self.lb_name = lb_name
        self.instance_ids = instance_ids
        self.elb_client = boto3.client('elbv2', region_name='us-east-1')  # Cambia la región según tus necesidades

    def create_load_balancer(self):
        """
        Crea un balanceador de carga en la VPC.

        Returns:
            str: ARN del balanceador de carga creado.
        """
        response = self.elb_client.create_load_balancer(
            Name=self.lb_name,
            Subnets=['subnet-12345678', 'subnet-87654321'],  # Cambia las subredes
            SecurityGroups=['sg-abcdef12'],  # Cambia los grupos de seguridad
            Scheme='internet-facing',
            LoadBalancerAttributes={
                'deletion_protection.enabled': False
            }
        )
        print(f"Load balancer {self.lb_name} creado con éxito.")
        return response['LoadBalancers'][0]['LoadBalancerArn']

    def register_targets(self, lb_arn):
        """
        Registra las instancias de servidor en el grupo de objetivos.

        Args:
            lb_arn (str): ARN del balanceador de carga.

        Returns:
            dict: Respuesta de registro de instancias.
        """
        response = self.elb_client.register_targets(
            TargetGroupArn='arn:aws:elasticloadbalancing:us-east-1:123456789012:targetgroup/my-targets/1234567890123456',
            Targets=[{'Id': instance_id} for instance_id in self.instance_ids]
        )
        print(f"Instancias registradas en el grupo de objetivos.")
        return response

    def create_listener(self, lb_arn):
        """
        Crea un listener para el balanceador de carga.

        Args:
            lb_arn (str): ARN del balanceador de carga.

        Returns:
            dict: Respuesta de creación del listener.
        """
        response = self.elb_client.create_listener(
            LoadBalancerArn=lb_arn,
            Protocol='HTTP',
            Port=80,
            DefaultActions=[
                {
                    'Type': 'fixed-response',
                    'FixedResponseConfig': {
                        'StatusCode': '200',
                        'MessageBody': 'Hello from the load balancer!'
                    }
                }
            ]
        )
        print(f"Listener creado para el load balancer.")
        return response

if __name__ == '__main__':
    instance_ids = ['i-1234567890abcdef0', 'i-0987654321fedcba0']  # Cambia las instancias
    lb_name = 'MyLoadBalancer'
    lb = MyLoadBalancer(lb_name, instance_ids)
    lb_arn = lb.create_load_balancer()
    lb.register_targets(lb_arn)
    lb.create_listener(lb_arn)
