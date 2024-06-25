def encode_base64(text):
    base64_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bytes_text=text.encode()
    result=""
    for i in range(0, len(bytes_text),3):
        chunk=bytes_text[i:i+3]
        if len(chunk)<3:
           chunk+=b'\x00'*(3-len(chunk))
        values=[byte for byte in chunk]
        index1=(values[0]&0xfc)>>2
        index2=((values[0]&0x03)<<4) | ((values[1]& 0xf0) >> 4)
        index3=((values[0]&0x0f)<<2) | ((values[2]& 0xc0) >> 6)
        index4=values[0]&0x03
        result += base64_chars[index1]+ base64_chars[index2]+base64_chars[index3]+base64_chars[index4]
                
    if len(bytes_text)%3==1:
           result=result[:-2]+"=="
    elif len(bytes_text)%3==2:
         result =result[:-1]+"="
    return result
def decode_base64(encoded_text):
    base64_chars="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    bytes_text=bytearray()
    for char in encoded_text:
        if char =='=':
            break
        bytes_text.append(base64_chars.index(char))
    result =bytearray()
    for i in range(0, len(bytes_text),4):
        chunk=bytes_text[i:i+4]
        values=[byte for byte in chunk]
        if len (values)>= 3:
           byte1=(values[0]<<2)|(values[1]>>4)
           byte2=((values[1]&0x0f) <<4) | ((values[2]& 0x3c) >> 2)
           byte3=((values[2]&0x03)<<6)| (values[3] if len(values)>3 else 0)
           result.extend([byte1,byte2,byte3])
    if encoded_text[-1]=='=':
        result.pop()
        if encoded_text[-2]=='=':
            result.pop()
    return bytes(result).decode()
text_to_encoded="Hello world"
encoded_text=encode_base64(text_to_encoded)
print("texto codificadod",encoded_text)
decoded_text=decode_base64(encoded_text)
print("Texto decodiificado",decoded_text)

    
