from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
# Tu contraseña en texto plano
contrasena = "A"

# Generar el hash de la contraseña
hash_contrasena = generate_password_hash(contrasena)

# Imprimir el hash generado
print("Hash de la contraseña:", hash_contrasena)

print(check_password_hash(hash_contrasena,'A'))