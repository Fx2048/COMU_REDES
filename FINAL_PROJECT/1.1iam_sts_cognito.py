
#Interacción de AWS(iam, sts, y cognito ):
#importación de bibliotecas boto3 y json:
import boto3
import json
#Crear definición de clientes AWS para IAM, STS, y cognito:
iam_client=boto3.client('iam', region_name='us-east-1')
sts_client=boto3.client('sts',region_name='us-east-1')
cognito_client=boto3.client('cognito-idp', region_name='us-east-1')


#Creando nuevo rol en IAM:
def create_iam_role(role_name,assume_role_policy):
    """
    Objetivo: Realizar una auditoría de seguridad completa de la configuración actual en AWS. 
Descripción: 
• Utiliza herramientas como AWS Inspector o servicios de terceros para realizar una auditoría 
de seguridad de las configuraciones de VPC, IAM, y Amazon Cognito. 
• Identifica vulnerabilidades potenciales y elaborar un plan de mitigación. 

• Implementa las correcciones recomendadas y volver a realizar la auditoría para asegurar que 
las vulnerabilidades se han abordado adecuadamente. 

    
    """
    try:
        response=iam_client.create_role(
            RoleName = role_name,
            AssumeRolePolicyDocument = assume_role_policy
        )
        print(f"Role {role_name}creado exitosamente.")
        return response['Role']['Arn']
    except Exception as e:
        print(f" Error creating role:{e}")
#Anexar una política a un rol previamente creado en IAM:
def attach_policy_to_role(role_name,policy_arn):
    try:
        iam_client.attach_role_policy(
            RoleName=role_name,
            PolicyArn=policy_arn
        )
        print(f"POlicy{policy_arn}attached to role {role_name} successfully.")
    except Exception as e:
        print(f"Error attaching policy:{e}")
        
# Crear un nuevo POOL de usuarios en Cognito:
def create_user_pool_name(pool_name):
    try:
        response=cognito_client.create_user_pool(PoolName = pool_name)
        print(f" User Pool {pool_name} creado exitosamente")
        return response['UserPool']['Id']
    except Exception as e:
        print (f"Error creating user pool:{e}")
#crear CLIENTE de pool de usuarios en cognito:
def create_user_pool_client(user_pool_id,client_name):
    try:
        response = cognito_client.create_user_pool_client(
            UserPoolId=id,
            ClientName=client_name
        )
        print(f"User Pool Client {client_name} creado exitosamente")
        return response['UserPoolClient']['ClientId']
    except Exception as e:
        print(f"Error creating user pool client:{e}")
# Definimos main(), variables y creación de roles y políticas para asumirlas
def main():
    role_name='MySecurityRole'
    assume_role_policy=json.dumps({
        "Version":"2012-10-17",
        "Statement":[
            {
                "Effect":"Allow",
                "Principal":{
                    "Service":"ec2.amazonaws.com"
                },
                "Action": "sts:AssumeRole"
            }
        ]
    })
    policy_arn='arn:aws:iam::aws:policy/AmazonEC2ReadOnlyAccess'
    #crearemos roles e incluiremos políticas:
    role_arn = create_iam_role(role_name, assume_role_policy)
    #Anexamos una política al rol
    if role_arn:
        attach_policy_to_role(role_name,policy_arn)
    user_pool_id = create_user_pool('MyUserPool')
    if user_pool_id:
        create_user_pool_client(user_pool_id,'MyUserPoolClient')
        
#Ejecutar función principal
if __name__=='__main__':
    main()

        


