![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e60a325e-11c3-4386-be7b-51615bf5b8d9)

# Instructions  from Configuración de IAM en AWS :


1. Acceso a la Consola de Administración de AWS

Inicia sesión en tu cuenta de AWS.

Ve a la Consola de Administración de AWS.

2. Navegación a la Sección de IAM

En el menú de servicios, busca “Almacenamiento” y selecciona “EC2”.

En el panel de navegación izquierdo, selecciona “Volúmenes”.

3. Creación de un Usuario IAM

Ve a la sección “Usuarios” en IAM.

Haz clic en “Agregar usuario”.

Asigna un nombre de usuario y selecciona el tipo de acceso (programático o de 
consola).

Configura los permisos y grupos para el usuario.

4. Creación de un Grupo IAM

Ve a la sección “Grupos” en IAM.

Haz clic en “Crear grupo”.

Asigna un nombre al grupo y selecciona las políticas que deseas asociar.

Agrega usuarios al grupo.

5. Creación de una Política IAM Personalizada

Ve a la sección “Políticas” en IAM.

Haz clic en “Crear política”.

Define los permisos necesarios para tu caso de uso.

Asocia la política con un grupo o usuario.

6. Pruebas de Acceso

Inicia sesión con las credenciales del usuario IAM.

Verifica que puedas acceder a los recursos y realizar las acciones permitidas.

7. Eliminación de Recursos (Opcional)

Si ya no necesitas los usuarios, grupos o políticas, elimínalos para mantener 
una gestión ordenada
_________________________________________________________________________________________________________________
_________________________________________________________________________________________________________________

# policy assigned speciffied to S3 amazon
````
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "ec2:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "elasticloadbalancing:Describe*",
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:ListMetrics",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:Describe*"
            ],
            "Resource": "*"
        },
        {
            "Effect": "Allow",
            "Action": "autoscaling:Describe*",
            "Resource": "*"
        }
    ]
}

````
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/adea7570-4c2d-422f-a1a3-2f83d0222a25){
![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/96f71678-9461-4c6d-887d-512a0253750c)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/d5039191-8b42-4bc7-89f3-8f8b1abf0dcc)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e83cad0f-e13e-40e0-8970-81f4efb11ab8)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5c860670-37ae-4ac3-8760-73070b5ac6bd)


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e39a0dfd-3d27-4f81-b4a8-265e26d7e914)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/915d74b4-cc3e-447f-89b3-882ca2cf8e04)

#INSTANCIAS EN EC2 PARA USER 2 , al iniciar sesión; a comparación de User 1, que tenía acceso a sopport Amazon S3 , en cambio, el user 2, no puede acceder a estos, dado que no tiene permiso, solo para visualizar, y tampoco puede editar desde las instancias de C2

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/7b0dc41b-1934-4402-a80b-3cb41082e2a1)

Aquí el user 3 puede acceder a Amazon C2 para detener una instancia,porque a diferencia de los anteriores, está asociado como administrador de este servicio, y tiene los permisos respectivos :)

![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/1cc8bf70-05a8-4f9c-ac18-fe4918f679d6)

# Anexos:



1. **Versión**:
   - La versión de la política. En este caso, es "2012-10-17".

2. **Declaraciones (Statements)**:
   - Cada declaración describe una acción permitida o denegada.
   - Las acciones permitidas son:
     - `ec2:Describe*`: Permite describir recursos EC2 (instancias, volúmenes, etc.).
     - `elasticloadbalancing:Describe*`: Permite describir recursos de Elastic Load Balancing (balanceadores de carga).
     - `cloudwatch:ListMetrics`, `cloudwatch:GetMetricStatistics`, `cloudwatch:Describe*`: Permite acceder a métricas y estadísticas de CloudWatch.
     - `autoscaling:Describe*`: Permite describir recursos de Auto Scaling (escalado automático).


```python
import boto3

def create_custom_policy():
    # Crea una política personalizada con las declaraciones especificadas
    custom_policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Action": "ec2:Describe*",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": "elasticloadbalancing:Describe*",
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": [
                    "cloudwatch:ListMetrics",
                    "cloudwatch:GetMetricStatistics",
                    "cloudwatch:Describe*"
                ],
                "Resource": "*"
            },
            {
                "Effect": "Allow",
                "Action": "autoscaling:Describe*",
                "Resource": "*"
            }
        ]
    }
    return custom_policy

# Ejemplo de uso
if __name__ == "__main__":
    iam_client = boto3.client("iam")
    policy_name = "MyCustomPolicy"
    policy_document = create_custom_policy()

    try:
        response = iam_client.create_policy(
            PolicyName=policy_name,
            PolicyDocument=json.dumps(policy_document)
        )
        print(f"Política {policy_name} creada con éxito.")
    except Exception as e:
        print(f"Error al crear la política: {str(e)}")
```


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/5faeb5a6-2983-4bce-8f1a-5f25ff4cccdb)
