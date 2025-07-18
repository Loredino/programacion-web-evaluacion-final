from pymongo import MongoClient
from sys import exit
import bcrypt

BD_NOMBRE = "loredana_romano"
C_USUARIOS = "usuarios"

def main():
    mc = MongoClient("mongodb://localhost:27017")

    # Verifica bd y colección
    if BD_NOMBRE in mc.list_database_names():
        print(f"¡Base de datos '{BD_NOMBRE}' ya inicializada!")
        exit(0)

    # Base de datos
    db = mc[BD_NOMBRE]

    # Colección usuarios
    c_usuarios = db[C_USUARIOS]

    # Usuarios a insertar
    for u in [
            {
                "nombre": "juan",
                "clave": bcrypt.hashpw(b"admin", bcrypt.gensalt()).decode()
            },
            {
                "nombre": "pepe",
                "clave": bcrypt.hashpw(b"user", bcrypt.gensalt()).decode()
            }
        ]:
        c_usuarios.insert_one(u)
    print("¡Usuarios creados!")

if __name__ == "__main__":
    main()