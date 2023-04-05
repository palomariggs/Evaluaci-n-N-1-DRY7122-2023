# Solicitar el número de ACL IPv4 al usuario
numero_acl = input("Ingrese el número de ACL IPv4: ")

# Identificar el tipo de ACL IPv4
if int(numero_acl) in range(1,100):
    print("El número de ACL IPv4 " + numero_acl + " es una ACL Estándar.")
elif int(numero_acl) in range(100,199):
    print("El número de ACL IPv4 " + numero_acl + " es una ACL Extendida.")
else:
    print("El número " + numero_acl + " no corresponde a una lista de acceso.")
