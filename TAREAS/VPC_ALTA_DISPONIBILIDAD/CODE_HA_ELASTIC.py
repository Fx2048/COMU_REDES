# Configuración de alta disponibilidad y escalabilidad en AWS[^1^][1]

# Definir la infraestructura básica
vpc = create_vpc('mi_vpc')
subnet_publica = create_subnet(vpc, 'subnet_publica')
subnet_privada = create_subnet(vpc, 'subnet_privada')

# Crear instancias EC2 en múltiples zonas de disponibilidad[^2^][2]
instancia_ec2_1 = create_ec2_instance(subnet_publica, 't2.micro', 'ami-12345678')
instancia_ec2_2 = create_ec2_instance(subnet_privada, 't2.micro', 'ami-12345678')

# Configurar Auto Scaling
auto_scaling_group = create_auto_scaling_group([instancia_ec2_1, instancia_ec2_2], min_size=2, max_size=10)

# Configurar Elastic Load Balancer (ELB)
elb = create_elb([instancia_ec2_1, instancia_ec2_2], 'internet-facing')

# Configurar reglas de seguridad
security_group = create_security_group(vpc, 'mi_grupo_seguridad')
add_ingress_rule(security_group, '0.0.0.0/0', 80, 'tcp')  # Permitir tráfico HTTP
add_ingress_rule(security_group, '0.0.0.0/0', 443, 'tcp') # Permitir tráfico HTTPS

# Asociar el grupo de seguridad a las instancias EC2
associate_security_group(instancia_ec2_1, security_group)
associate_security_group(instancia_ec2_2, security_group)

# Configurar almacenamiento compartido con EFS
efs = create_efs(vpc, 'mi_efs')
mount_efs(instancia_ec2_1, efs, '/mnt/efs')
mount_efs(instancia_ec2_2, efs, '/mnt/efs')

# Configurar WAF para proteger la aplicación web[^3^][3]
waf = create_waf('mi_waf')
add_waf_rule(waf, 'SQL_Injection_Rule')
add_waf_rule(waf, 'XSS_Rule')

# Asociar WAF con el ELB
associate_waf_with_elb(waf, elb)

# Configurar monitoreo y alertas
cloudwatch = create_cloudwatch('mi_cloudwatch')
add_alarm(cloudwatch, 'CPU_Utilization', 'GreaterThanThreshold', 80, auto_scaling_group)

# Implementar la aplicación
deploy_application(instancia_ec2_1, 'mi_aplicacion')
deploy_application(instancia_ec2_2, 'mi_aplicacion')

# Verificar la configuración
check_configuration(vpc, elb, auto_scaling_group, security_group, efs, waf, cloudwatch)
