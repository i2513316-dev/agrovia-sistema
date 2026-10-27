from werkzeug.security import generate_password_hash
from db import query, execute

correo = input("Correo del administrador: ").strip()
password = input("Contrasena: ").strip()
dni = input("DNI: ").strip()
nombres = input("Nombres: ").strip()
apellido = input("Apellido paterno: ").strip()
telefono = input("Telefono (9 digitos): ").strip()

exists = query(
    "SELECT id_usuario FROM usuarios WHERE correo=%s OR numero_documento=%s OR telefono=%s",
    (correo, dni, telefono),
    one=True,
)
if exists:
    print("Ya existe un usuario con ese correo, documento o telefono.")
    raise SystemExit

uid = execute("""
INSERT INTO usuarios
(codigo_usuario,tipo_documento,numero_documento,nombres,apellido_paterno,telefono,correo,password_hash,estado,origen_registro)
VALUES (%s,'DNI',%s,%s,%s,%s,%s,%s,'ACTIVO','WEB')
""", ("USR-" + dni, dni, nombres, apellido, telefono, correo, generate_password_hash(password)))

execute("INSERT INTO usuarios_roles(id_usuario,id_rol,estado) VALUES(%s,2,'ACTIVO')", (uid,))
print("Administrador creado. Ya puedes iniciar sesion.")
