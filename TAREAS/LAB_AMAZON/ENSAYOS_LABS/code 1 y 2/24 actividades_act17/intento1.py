def cifrado_cesar(texto,desplazamiento):
    resultado=""
    for char in texto:
        if char.isalpha():
            offset=65 if char.isupper() else 97
            resultado+= chr((ord(char) -offset+desplazamiento)% 26 +offset)
        else:
            resultado += char
        return resultado
def descifrado_cesar(texto_cifrado,desplazamiento):
    return cifrado_cesar(texto_cifrado,-desplazamiento)

def demostracion():
    mensaje_original="hola mundo"
    desplazamiento= 4
    mensaje_cifrado= cifrado_cesar(mensaje_original,desplazamiento)
    print("mensaje cifrado" , mensaje_cifrado)
    mensaje_descifrado=descifrado_cesar(mensaje_cifrado,desplazamiento)
    print("Mensaje descifrado",mensaje_descifrado)
if __name__=="__main__":
    demostracion()
    
