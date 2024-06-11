import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError
#incializar clase buckets3 y prepara lista de buckets crados
class BucketS3:
    """
    Clase para gestionar diversas operaciones en Amazon S3 como etiquetas de objetos,
    configuración, copia de objetos, almacenamiento, etc.
    """
    
    def __init__(self, id_user, arn):
        self.buckets = []  # Lista para almacenar los nombres de los buckets
        self.id_user = id_user
        self.arn = arn
        self.s3_client = boto3.client('s3')
        #creamos bucket  en una region especifica
    def create_bucket(self, bucket_name, region=None):
        try:
            if region: 
                self.s3_client.create_bucket(
                    Bucket=bucket_name,
                    CreateBucketConfiguration={'LocationConstraint': region}
                )
            else:
                self.s3_client.create_bucket(Bucket=bucket_name)
            self.buckets.append(bucket_name)
            print(f'Bucket {bucket_name} creado.')
        except self.s3_client.exceptions.BucketAlreadyExists as e:
            print(f'Error: {e}')
#definir configurar lambda:
    def configure_lambda(self, function_name, role_arn, handler, zip_file):
    """
    Configura una función Lambda para interactuar con objetos en S3.
    """
        lambda_client = boto3.client('lambda')
    
        try:
            with open(zip_file, 'rb') as f:
                zip_data = f.read()
        
            response = lambda_client.create_function(
                FunctionName=function_name,
                Runtime='python3.8',
                Role=role_arn,
                Handler=handler,
                Code={'ZipFile': zip_data},
                Description='Función Lambda para interactuar con S3',
                Timeout=15,
                MemorySize=128,
                Publish=True
            )
            print(f'Función Lambda {function_name} creada.')
            return response
        except lambda_client.exceptions.ResourceConflictException as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')

        
       
 #definir glacier flexible retrieval
    def glacier_flexible_retrieval(self, bucket_name, object_key):
    """
    Inicia una solicitud de recuperación flexible para un objeto almacenado en Glacier.
    """
        try:
            response = self.s3_client.restore_object(
                Bucket=bucket_name,
                Key=object_key,
                RestoreRequest={
                    'Days': 7,
                    'GlacierJobParameters': {'Tier': 'Standard'}
                }
            )
            print(f'Solicitud de recuperación flexible iniciada para el objeto {object_key}.')
            return response
        except self.s3_client.exceptions.ClientError as e:
            print(f'Error: {e}')

        
        
#definir glacier deep archive

    def glacier_deep_archive(self, bucket_name, object_key):
    """
    Mueve un objeto al archivo profundo de Glacier.
    """
        try:
            self.s3_client.copy_object(
                Bucket=bucket_name,
                CopySource={'Bucket': bucket_name, 'Key': object_key},
                Key=object_key,
                StorageClass='DEEP_ARCHIVE'
            )
            print(f'Objeto {object_key} movido a Glacier Deep Archive.')
        except self.s3_client.exceptions.ClientError as e:
            print(f'Error: {e}')

        
#definir replicación s3 rtc

    def replicacion_s3_rtc(self, source_bucket, destination_bucket, role_arn):
    """
    Configura la replicación RTC (Replicación en Tiempo Real) entre dos buckets.
    """
        replication_configuration = {
            'Role': role_arn,
            'Rules': [{
                'ID': 'ReplicacionRTC',
                'Status': 'Enabled',
                'Priority': 1,
                'Filter': {'Prefix': ''},
                'Destination': {
                    'Bucket': f'arn:aws:s3:::{destination_bucket}',
                    'StorageClass': 'STANDARD'
                },
                'DeleteMarkerReplication': {'Status': 'Disabled'}
            }]
        }

        try:
            response = self.s3_client.put_bucket_replication(
                Bucket=source_bucket,
                ReplicationConfiguration=replication_configuration
            )
            print(f'Replicación RTC configurada entre {source_bucket} y {destination_bucket}.')
            return response
        except self.s3_client.exceptions.ClientError as e:
            print(f'Error: {e}')

        
        
#definir control versiones  para modifcar eliminar ,adicionar o modificar versiones de objetos en bucket
   def control_version(self, bucket_name, action, object_key=None, version_id=None):
    """
    Controla las versiones de los objetos en un bucket.

    :param bucket_name: Nombre del bucket.
    :param action: Acción a realizar ('modificar', 'eliminar', 'adicionar').
    :param object_key: Clave del objeto a modificar/eliminar/adicionar.
    :param version_id: ID de la versión del objeto a modificar/eliminar.
    """
        if action == 'modificar':
            # Implementar la lógica para modificar versiones
            # Por ejemplo, cambiar el almacenamiento de una versión específica
            try:
                if not object_key or not version_id:
                    raise ValueError("Para modificar una versión se requiere tanto object_key como version_id.")
                response = self.s3_client.copy_object(
                    Bucket=bucket_name,
                    CopySource={'Bucket': bucket_name, 'Key': object_key, 'VersionId': version_id},
                    Key=object_key,
                    StorageClass='STANDARD_IA'  # Ejemplo: cambiar a Almacenamiento de Acceso Poco Frecuente
                )
                print(f'Versión {version_id} del objeto {object_key} modificada.')
                return response
            except self.s3_client.exceptions.ClientError as e:
                print(f'Error: {e}')

        elif action == 'eliminar':
            # Implementar la lógica para eliminar versiones
            try:
                if not object_key or not version_id:
                    raise ValueError("Para eliminar una versión se requiere tanto object_key como version_id.")
                response = self.s3_client.delete_object(
                    Bucket=bucket_name,
                    Key=object_key,
                    VersionId=version_id
                )
                print(f'Versión {version_id} del objeto {object_key} eliminada.')
                return response
            except self.s3_client.exceptions.ClientError as e:
                print(f'Error: {e}')

        elif action == 'adicionar':
            # Implementar la lógica para adicionar versiones
            # En S3, adicionar versiones puede implicar cargar un nuevo objeto con la misma clave
            try:
                if not object_key:
                    raise ValueError("Para adicionar una versión se requiere object_key.")
                response = self.s3_client.put_object(
                    Bucket=bucket_name,
                    Key=object_key,
                    Body=b'Tu contenido aquí'  # Contenido del nuevo objeto/versión
                )
                print(f'Nueva versión del objeto {object_key} adicionada.')
                return response
            except self.s3_client.exceptions.ClientError as e:
                print(f'Error: {e}')

            
#definir enablement _mfa
    def enablement_mfa(self, bucket_name):
    """
    Habilita MFA (autenticación multifactor) para operaciones de borrado en un bucket.
    """
        mfa_delete_policy = {
            'Version': '2012-10-17',
            'Statement': [{
                'Sid': 'AddMfaDelete',
                'Effect': 'Deny',
                'Principal': '*',
                'Action': 's3:DeleteObject',
                'Resource': f'arn:aws:s3:::{bucket_name}/*',
                'Condition': {
                    'Bool': {'aws:MultiFactorAuthPresent': 'false'}
                }
            }]
        }

        try:
            response = self.s3_client.put_bucket_versioning(
                Bucket=bucket_name,
                VersioningConfiguration={
                    'MFADelete': 'Enabled',
                    'Status': 'Enabled'
                },
                MFA=mfa_delete_policy
            )
            print(f'MFA habilitado para el bucket {bucket_name}.')
            return response
        except self.s3_client.exceptions.ClientError as e:
            print(f'Error: {e}')

        
#definir segundo factor_uf2
    def segundo_factor_u2f(self, bucket_name, user_arn, device_serial_number):
    """
    Habilita el segundo factor U2F (Universal 2nd Factor) para un usuario.
    """
        iam_client = boto3.client('iam')
        try:
            response = iam_client.create_virtual_mfa_device(
                VirtualMFADeviceName=device_serial_number,
                Path='/',
            )
            print(f'Dispositivo U2F {device_serial_number} creado para el usuario {user_arn}.')
            return response
        except iam_client.exceptions.EntityAlreadyExistsException as e:
            print(f'Error: {e}')
        except Exception as e:
            print(f'Error: {e}')

        
#definir object lock
    def object_lock(self, bucket_name, object_key, action):
        if action == 'eliminar':
            try:
                self.s3_client.delete_object(Bucket=bucket_name, Key=object_key)
                print(f'Objeto {object_key} eliminado del bucket {bucket_name}.')
            except self.s3_client.exceptions.ClientError as e:
                print(f'Error: {e}')
        # Agregar otras acciones relacionadas con object lock
#definir  multiregion acccesss point
    def multi_region_access_point(self, name, regions):
    """
    Crea un punto de acceso multirregión para un bucket.

    :param name: Nombre del punto de acceso multirregión.
    :param regions: Lista de diccionarios con los nombres de los buckets y las regiones respectivas.
                    Ejemplo: [{'Bucket': 'bucket-name-1', 'Region': 'us-east-1'}, {'Bucket': 'bucket-name-2', 'Region': 'eu-west-1'}]
    """
        s3control_client = boto3.client('s3control')

        try:
            response = s3control_client.create_multi_region_access_point(
                AccountId=self.id_user,
                Details={
                    'Name': name,
                    'Regions': [
                        {
                            'Bucket': region['Bucket'],
                            'Region': region['Region']
                        } for region in regions
                    ]
                }
            )
            print(f'Punto de acceso multirregión {name} creado.')
            return response
        except s3control_client.exceptions.ClientError as e:
            print(f'Error: {e}')

#definir meotodo bloockk public access 
    def block_public_access(self, bucket_name, block_options):
        try:
            #metodo bloockk public access 
            self.s3_client.put_public_access_block(
                Bucket=bucket_name,
                PublicAccessBlockConfiguration=block_options
            )
            print(f'Bloqueo de acceso público configurado para el bucket {bucket_name}.')
        except self.s3_client.exceptions.ClientError as e:
            print(f'Error: {e}')
            #define metodo poprgramatico access para obtener configuracion de bloqueo acceso publcio 
    def programmatic_access(self, bucket_name):
        try:
            response = self.s3_client.get_public_access_block(Bucket=bucket_name)
            print(response)
        except self.s3_client.exceptions.NoSuchPublicAccessBlockConfiguration as e:
            print(f'No hay configuración de bloqueo de acceso público para {bucket_name}: {e}')
        except NoCredentialsError:
            print('Error: No se encontraron credenciales.')
        except PartialCredentialsError:
            print('Error: Credenciales incompletas.')

# Ejemplo de uso
bucket_s3_instance = BucketS3(id_user="123456789012", arn="arn:aws:iam::123456789012:user/ExampleUser")

# Crear un bucket en la región us-west-1
bucket_s3_instance.create_bucket(bucket_name="mi-bucket-ejemplo", region="us-west-1")

# Bloquear acceso público al bucket
block_options = {
    'BlockPublicAcls': True,
    'IgnorePublicAcls': False,
    'BlockPublicPolicy': True,
    'RestrictPublicBuckets': True
}
bucket_s3_instance.block_public_access(bucket_name="mi-bucket-ejemplo", block_options=block_options)
