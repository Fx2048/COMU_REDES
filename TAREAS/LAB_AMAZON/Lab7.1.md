![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/e60a325e-11c3-4386-be7b-51615bf5b8d9)
# policy assigned speciffied to S3 amazon
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


![image](https://github.com/Fx2048/COMU_REDES/assets/131219987/adea7570-4c2d-422f-a1a3-2f83d0222a25){


Anexos:

¡Claro! El fragmento que proporcionaste es una **política de AWS Identity and Access Management (IAM)** escrita en formato JSON. Esta política define permisos para realizar ciertas acciones en recursos específicos dentro de AWS. Permíteme explicarte cada parte y luego proporcionaré un pseudocódigo y un ejemplo en Python.

1. **Versión**:
   - La versión de la política. En este caso, es "2012-10-17".

2. **Declaraciones (Statements)**:
   - Cada declaración describe una acción permitida o denegada.
   - Las acciones permitidas son:
     - `ec2:Describe*`: Permite describir recursos EC2 (instancias, volúmenes, etc.).
     - `elasticloadbalancing:Describe*`: Permite describir recursos de Elastic Load Balancing (balanceadores de carga).
     - `cloudwatch:ListMetrics`, `cloudwatch:GetMetricStatistics`, `cloudwatch:Describe*`: Permite acceder a métricas y estadísticas de CloudWatch.
     - `autoscaling:Describe*`: Permite describir recursos de Auto Scaling (escalado automático).

Ahora, aquí tienes un pseudocódigo y un ejemplo en Python para crear una política similar:

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
