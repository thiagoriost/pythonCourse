import os

def verArchivosEnUnaRuta(pathToSaveNewFile_):
    # Listar los archivos .txt en el directorio donde se creó el archivo
    # txt_files = [f for f in os.listdir('.') if f.endswith('.txt')]
    txt_files = [f for f in os.listdir(pathToSaveNewFile_) if f.endswith('.txt')]
    print("txt_files => ", txt_files)
    
# Ruta del archivo
cwd = os.getcwd() # get current working directory
print("cwd => ", cwd)
pathToSaveNewFile = os.path.join(cwd, 'platzy', 'librerias')  # Crea la ruta para guardar el archivo
print("pathToSaveNewFile => ", pathToSaveNewFile)
verArchivosEnUnaRuta(pathToSaveNewFile)

# Asegura de que el directorio existe
os.makedirs(pathToSaveNewFile, exist_ok=True)

nameFile = "nuevo_archivo.txt"
file_path = os.path.join(pathToSaveNewFile, nameFile)  # Crea la ruta completa
print("file_path => ", file_path)

# Crear el archivo .txt
with open(file_path, mode='w') as file:
    file.write("Este es un archivo de ejemplo creado con Python.\n")
    file.write("Usando la biblioteca os para manejar rutas.\n")

print(f"Archivo creado con éxito en: {file_path}")

nameFileToRenameFilePrevius = 'hola3.txt'
new_file_path = os.path.join(pathToSaveNewFile, nameFileToRenameFilePrevius)
print("new_file_path => ", new_file_path)

os.rename(file_path, new_file_path)

verArchivosEnUnaRuta(pathToSaveNewFile)

    