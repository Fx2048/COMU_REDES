import boto3

class Servidor:
    """
    Recibe el nombre del servidor y maneja sus solicitudes.
    """
    def __init__(self, nombre, instancia_id):
        self.nombre = nombre
        self.instancia_id = instancia_id

    def manejar_solicitud(self, solicitud):
        print(f"Servidor {self.nombre} está manejando la solicitud {solicitud}")

class BalanceadorCarga:
    """
    Define un diccionario de servidores y el tipo de Load Balancer (ALB o NLB).
    """
    def __init__(self, tipo, nombre_lb, region_name='us-west-2'):
        self.servidores = []
        self.tipo = tipo
        self.nombre_lb = nombre_lb
        self.elbv2_client = boto3.client('elbv2', region_name=region_name)
        self.ec2_client = boto3.client('ec2', region_name=region_name)
        self.target_group_arn = None
        self.load_balancer_arn = None

    def anadir_servidor(self, servidor):
        self.servidores.append(servidor)

    def crear_target_group(self, vpc_id, protocol='TCP', port=80):
        try:
            response = self.elbv2_client.create_target_group(
                Name=self.nombre_lb,
                Protocol=protocol,
                Port=port,
                VpcId=vpc_id,
                HealthCheckProtocol=protocol,
                HealthCheckPort=str(port),
                HealthCheckEnabled=True,
                HealthCheckPath='/',
                TargetType='instance'
            )
            self.target_group_arn = response['TargetGroups'][0]['TargetGroupArn']
            print(f"Target Group creado con ARN: {self.target_group_arn}")
        except Exception as e:
            print(f"Error creando el Target Group: {e}")

    def registrar_instancias(self):
        targets = [{'Id': servidor.instancia_id} for servidor in self.servidores]
        try:
            response = self.elbv2_client.register_targets(
                TargetGroupArn=self.target_group_arn,
                Targets=targets
            )
            print(f"Instancias registradas en el Target Group: {response}")
        except Exception as e:
            print(f"Error registrando instancias en el Target Group: {e}")

    def crear_load_balancer(self, subnets, security_groups, ip_address_type='ipv4'):
        try:
            response = self.elbv2_client.create_load_balancer(
                Name=self.nombre_lb,
                Subnets=subnets,
                SecurityGroups=security_groups,
                Scheme='internet-facing',
                Tags=[
                    {
                        'Key': 'Name',
                        'Value': self.nombre_lb
                    },
                ],
                Type='network' if self.tipo == 'NLB' else 'application',
                IpAddressType=ip_address_type
            )
            self.load_balancer_arn = response['LoadBalancers'][0]['LoadBalancerArn']
            print(f"Load Balancer creado con ARN: {self.load_balancer_arn}")
        except Exception as e:
            print(f"Error creando el Load Balancer: {e}")

    def crear_listener(self, port=80, protocol='TCP'):
        try:
            response = self.elbv2_client.create_listener(
                LoadBalancerArn=self.load_balancer_arn,
                Protocol=protocol,
                Port=port,
                DefaultActions=[
                    {
                        'Type': 'forward',
                        'TargetGroupArn': self.target_group_arn
                    }
                ]
            )
            listener_arn = response['Listeners'][0]['ListenerArn']
            print(f"Listener creado con ARN: {listener_arn}")
        except Exception as e:
            print(f"Error creando el Listener: {e}")

    # Métodos para el Clúster del NLB
    def add_nlb_cluster_node(self, instance_id):
        try:
            response = self.elbv2_client.register_targets(
                TargetGroupArn=self.target_group_arn,
                Targets=[{'Id': instance_id}]
            )
            print(f"Nodo {instance_id} agregado al clúster NLB")
        except Exception as e:
            print(f"Error agregando nodo al clúster NLB: {e}")

    def get_nlb_cluster_port_rule(self):
        try:
            response = self.elbv2_client.describe_listeners(
                LoadBalancerArn=self.load_balancer_arn
            )
            for listener in response['Listeners']:
                print(f"Listener ARN: {listener['ListenerArn']}, Puerto: {listener['Port']}, Protocolo: {listener['Protocol']}")
        except Exception as e:
            print(f"Error obteniendo reglas de puerto del clúster NLB: {e}")

    def get_nlb_cluster(self):
        print("Obteniendo información del clúster NLB...")
        try:
            response = self.elbv2_client.describe_load_balancers(
                LoadBalancerArns=[self.load_balancer_arn]
            )
            lb_info = response['LoadBalancers'][0]
            print(f"Load Balancer ARN: {lb_info['LoadBalancerArn']}")
            print(f"Estado: {lb_info['State']['Code']}")
            print(f"Tipo: {lb_info['Type']}")
            print(f"IP Address Type: {lb_info['IpAddressType']}")
        except Exception as e:
            print(f"Error obteniendo información del clúster NLB: {e}")

    def stop_nlb_cluster(self):
        print("Deteniendo clúster NLB...")
        try:
            instances = [{'Id': servidor.instancia_id} for servidor in self.servidores]
            self.ec2_client.stop_instances(InstanceIds=[i['Id'] for i in instances])
            print(f"Instancias detenidas: {[i['Id'] for i in instances]}")
        except Exception as e:
            print(f"Error deteniendo el clúster NLB: {e}")

    def suspend_nlb_cluster(self):
        print("Suspendiendo clúster NLB...")
        try:
            response = self.elbv2_client.modify_listener(
                ListenerArn=self.listener_arn,
                DefaultActions=[
                    {
                        'Type': 'fixed-response',
                        'FixedResponseConfig': {
                            'StatusCode': '503',
                            'ContentType': 'text/plain',
                            'MessageBody': 'Service Unavailable'
                        }
                    }
                ]
            )
            print("Distribución de tráfico suspendida.")
        except Exception as e:
            print(f"Error suspendiendo el clúster NLB: {e}")

    def start_nlb_cluster(self):
        print("Iniciando clúster NLB...")
        try:
            instances = [{'Id': servidor.instancia_id} for servidor in self.servidores]
            self.ec2_client.start_instances(InstanceIds=[i['Id'] for i in instances])
            print(f"Instancias iniciadas: {[i['Id'] for i in instances]}")
        except Exception as e:
            print(f"Error iniciando el clúster NLB: {e}")

    def remove_nlb_cluster(self):
        print("Removiendo clúster NLB...")
        try:
            self.elbv2_client.delete_load_balancer(LoadBalancerArn=self.load_balancer_arn)
            print(f"Load Balancer {self.load_balancer_arn} eliminado.")
            self.elbv2_client.delete_target_group(TargetGroupArn=self.target_group_arn)
            print(f"Target Group {self.target_group_arn} eliminado.")
        except Exception as e:
            print(f"Error removiendo el clúster NLB: {e}")

    def distribuir_solicitudes_tcp(self, solicitudes):
        if self.tipo == "NLB":
            print("Distribuyendo solicitudes TCP usando NLB")
        else:
            print("Distribuyendo solicitudes TCP usando estrategia estándar")

        for i, solicitud in enumerate(solicitudes):
            servidor = self.servidores[i % len(self.servidores)]
            servidor.manejar_solicitud(solicitud)

    def distribuir_solicitudes_http(self, solicitudes):
        if self.tipo == "ALB":
            print("Distribuyendo solicitudes HTTP usando ALB")
        else:
            print("Distribuyendo solicitudes HTTP usando estrategia estándar")

        for i, solicitud in enumerate(solicitudes):
            servidor = self.servidores[i % len(self.servidores)]
            servidor.manejar_solicitud(solicitud)

# Ejemplo de uso
servidor1 = Servidor("Servidor 1", "i-0123456789abcdef0")
servidor2 = Servidor("Servidor 2", "i-0123456789abcdef1")

# Simular Application Load Balancer (ALB)
alb = BalanceadorCarga("ALB", "mi-alb")
alb.anadir_servidor(servidor1)
alb.anadir_servidor(servidor2)

# Simular Network Load Balancer (NLB)
nlb = BalanceadorCarga("NLB", "mi-nlb")
nlb.anadir_servidor(servidor1)
nlb.anadir_servidor(servidor2)

# Simulación de solicitudes
solicitudes_tcp = ["Solicitud TCP 1", "Solicitud TCP 2", "Solicitud TCP 3"]
solicitudes_http = ["Solicitud HTTP 1", "Solicitud HTTP 2", "Solicitud HTTP 3"]

# Distribuir solicitudes
alb.distribuir_solicitudes_http(solicitudes_http)
nlb.distribuir_solicitudes_tcp(solicitudes_tcp)


