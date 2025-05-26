import uuid
import hashlib

def get_mac_address():
  mac_int = uuid.getnode()  # Obtém o endereço MAC como um número inteiro
  mac_hex = hex(mac_int)[2:].upper()  # Converte para hexadecimal e remove o prefixo "0x"
  return ":".join(mac_hex[i:i+2] for i in range(0, 12, 2))  # Formata com pontos

def criar_codigo_unico(mac_address):
    # Converter o MAC address para bytes
    mac_address_bytes = mac_address.encode('utf-8')

    # Gerar o hash SHA256
    hash_object = hashlib.sha256(mac_address_bytes)
    hash_hex = hash_object.hexdigest()

    return hash_hex

def generateCode():
    mac_address = get_mac_address()
    print(f"MAC Address: {mac_address}")
    return criar_codigo_unico(mac_address)

codigo_unico = generateCode()
print(f"Código Único: {codigo_unico}")