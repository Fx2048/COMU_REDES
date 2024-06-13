import os
import shutil

class LocalBucket:
    def __init__(self, base_directory):
        self.base_directory = base_directory
        if not os.path.exists(base_directory):
            os.makedirs(base_directory)
        print(f'Bucket local {base_directory} creado.')

    # La función create_directory crea un nuevo directorio dentro del bucket local
    def create_directory(self, directory_name):
        path = os.path.join(self.base_directory, directory_name)
        os.makedirs(path, exist_ok=True)
        print(f'Directorio {directory_name} creado en {self.base_directory}.')

    # La función upload_file copia un archivo desde una ubicación de origen a un directorio de destino dentro del bucket local
    def upload_file(self, source_file, target_directory):
        target_path = os.path.join(self.base_directory, target_directory)
        if not os.path.exists(target_path):
            os.makedirs(target_path)
        shutil.copy(source_file, target_path)
        print(f'Archivo {source_file} subido a {target_path}.')

    # La función set_file_permissions establece los permisos de un archivo dentro del bucket local
    def set_file_permissions(self, file_path, mode):
        os.chmod(file_path, mode)
        print(f'Permisos {oct(mode)} establecidos para el archivo {file_path}.')

    # La función delete_file elimina un archivo del bucket local
    def delete_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f'Archivo {file_path} eliminado.')
        else:
            print(f'El archivo {file_path} no existe.')

    # La función check_permissions verifica los permisos de un archivo dentro del bucket local
    def check_permissions(self, file_path):
        if not os.path.exists(file_path):
            print(f'El archivo {file_path} no existe.')
            return

        mode = oct(os.stat(file_path).st_mode)[-3:]  # Obtén los últimos tres dígitos octales
        if mode == '644':
            print(f'El archivo {file_path} es público.')
        elif mode == '600':
            print(f'El archivo {file_path} es privado.')
        else:
            print(f'El archivo {file_path} tiene permisos {mode}.')

# Ejemplo de uso
bucket_name = "bowlmy"
bucket = LocalBucket(base_directory=bucket_name)

# Crear directorio dentro del bucket local
carpeta = "carpeta1"
bucket.create_directory(carpeta)

# Crear archivos de ejemplo
index_path = os.path.join(carpeta, 'index.html')
with open('index.html', 'w') as f:
    f.write('Contenido del archivo index.html')

in_path = os.path.join(carpeta, 'in.html')
with open('in.html', 'w') as f:
    f.write('Contenido del archivo in.html')

# Subir archivos al bucket local y organizarlos en carpetas
bucket.upload_file(source_file="index.html", target_directory=carpeta)
bucket.upload_file(source_file="in.html", target_directory=carpeta)

# Configurar permisos para los archivos
# Público: 644
bucket.set_file_permissions(file_path=os.path.join(bucket_name, index_path), mode=0o644)
# Privado: 600
bucket.set_file_permissions(file_path=os.path.join(bucket_name, in_path), mode=0o600)

# Comprobar permisos
bucket.check_permissions(file_path=os.path.join(bucket_name, index_path))
bucket.check_permissions(file_path=os.path.join(bucket_name, in_path))

# Eliminar uno de los archivos del bucket (opcional)
# bucket.delete_file(file_path=os.path.join(bucket_name, in_path))
