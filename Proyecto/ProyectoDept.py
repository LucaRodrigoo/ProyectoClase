import datetime

# Diccionario completo de departamentos y municipios de Honduras
localidades = {
    "01": {"nombre": "Atlántida", "municipios": {"01": "La Ceiba", "02": "El Porvenir", "03": "Tela", "04": "Arizona", "05": "Esparta", "06": "Jutiapa", "07": "La Masica", "08": "San Francisco"}},
    "02": {"nombre": "Choluteca", "municipios": {"01": "Choluteca", "02": "Apacilagua", "03": "Concepción de María", "04": "Duyure", "05": "El Corpus", "06": "El Triunfo", "07": "Marcovia", "08": "Morolica", "09": "Namasigüe", "10": "Orocuina", "11": "Pespire", "12": "San Antonio de Flores", "13": "San Isidro", "14": "San José", "15": "San Marcos de Colón", "16": "Santa Ana de Yusguare"}},
    "03": {"nombre": "Colón", "municipios": {"01": "Trujillo", "02": "Balfate", "03": "Iriona", "04": "Limón", "05": "Sabá", "06": "Santa Fe", "07": "Santa Rosa de Aguán", "08": "Sonaguera", "09": "Tocoa", "10": "Bonito Oriental"}},
    "04": {"nombre": "Comayagua", "municipios": {"01": "Comayagua", "02": "Ajuterique", "03": "El Rosario", "04": "Esquías", "05": "Humuya", "06": "La Libertad", "07": "Lamaní", "08": "La Trinidad", "09": "Lejamani", "10": "Meámbar", "11": "Minas de Oro", "12": "Ojos de Agua", "13": "San Jerónimo", "14": "San José de Comayagua", "15": "San José del Potrero", "16": "San Luis", "17": "San Sebastián", "18": "Siguatepeque", "19": "Villa de San Antonio", "20": "Las Lajas", "21": "Taulabé"}},
    "05": {"nombre": "Copán", "municipios": {"01": "Santa Rosa de Copán", "02": "Cabañas", "03": "Concepción", "04": "Copán Ruinas", "05": "Corquín", "06": "Cucuyagua", "07": "Dolores", "08": "Dulce Nombre", "09": "El Paraíso", "10": "Florida", "11": "La Jigua", "12": "La Unión", "13": "Nueva Arcadia", "14": "San Agustín", "15": "San Antonio", "16": "San Jerónimo", "17": "San José", "18": "San Juan de Opoa", "19": "San Nicolás", "20": "San Pedro", "21": "Santa Rita", "22": "Trinidad de Copán", "23": "Veracruz"}},
    "06": {"nombre": "Cortés", "municipios": {"01": "San Pedro Sula", "02": "Choloma", "03": "Omoa", "04": "Pimienta", "05": "Potrerillos", "06": "Puerto Cortés", "07": "San Antonio de Cortés", "08": "San Francisco de Yojoa", "09": "San Manuel", "10": "Santa Cruz de Yojoa", "11": "Villanueva", "12": "La Lima"}},
    "07": {"nombre": "El Paraíso", "municipios": {"01": "Yuscarán", "02": "Alauca", "03": "Danlí", "04": "El Paraíso", "05": "Güinope", "06": "Jacaleapa", "07": "Liure", "08": "Morocelí", "09": "Oropolí", "10": "Potrerillos", "11": "San Antonio de Flores", "12": "San Lucas", "13": "San Matías", "14": "Soledad", "15": "Teupasenti", "16": "Texiguat", "17": "Vado Ancho", "18": "Yauyupe", "19": "Trojes"}},
    "08": {"nombre": "Francisco Morazán", "municipios": {"01": "Tegucigalpa", "02": "Alubarén", "03": "Cedros", "04": "Curarén", "05": "El Porvenir", "06": "Guaimaca", "07": "La Libertad", "08": "La Venta", "09": "Lepaterique", "10": "Maraita", "11": "Marale", "12": "Nueva Armenia", "13": "Ojojona", "14": "Orica", "15": "Reitoca", "16": "Sabanagrande", "17": "San Antonio de Oriente", "18": "San Buenaventura", "19": "San Ignacio", "20": "San Juan de Flores", "21": "San Miguelito", "22": "Santa Ana", "23": "Santa Lucía", "24": "Talanga", "25": "Tatumbla", "26": "Valle de Ángeles", "27": "Villa de San Francisco", "28": "Vallecillo"}},
    "09": {"nombre": "Gracias a Dios", "municipios": {"01": "Puerto Lempira", "02": "Brus Laguna", "03": "Ahuas", "04": "Juan Francisco Bulnes", "05": "Ramón Villeda Morales", "06": "Wampusirpi"}},
    "10": {"nombre": "Intibucá", "municipios": {"01": "La Esperanza", "02": "Camasca", "03": "Colomoncagua", "04": "Concepción", "05": "Dolores", "06": "Intibucá", "07": "Jesús de Otoro", "08": "Magdalena", "09": "Masaguara", "10": "San Antonio", "11": "San Isidro", "12": "San Juan", "13": "San Marcos de la Sierra", "14": "San Miguel Guancapla", "15": "Santa Lucía", "16": "Yamaranguila"}},
    "11": {"nombre": "Islas de la Bahía", "municipios": {"01": "Roatán", "02": "Guanaja", "03": "José Santos Guardiola", "04": "Utila"}},
    "12": {"nombre": "La Paz", "municipios": {"01": "La Paz", "02": "Aguanqueterique", "03": "Cabañas", "04": "Cane", "05": "Chinacla", "06": "Guajiquiro", "07": "Lauterique", "08": "Marcala", "09": "Mercedes de Oriente", "10": "Opatoro", "11": "San Antonio del Norte", "12": "San José", "13": "San Juan", "14": "San Pedro de Tutule", "15": "Santa Ana", "16": "Santa Elena", "17": "Santa María", "18": "Santiago de Puringla", "19": "Yarula"}},
    "13": {"nombre": "Lempira", "municipios": {"01": "Gracias", "02": "Belén", "03": "Candelaria", "04": "Cololaca", "05": "Erandique", "06": "Gualcince", "07": "Guarita", "08": "La Campa", "09": "La Iguala", "10": "Las Flores", "11": "La Unión", "12": "La Virtud", "13": "Lepaera", "14": "Mapulaca", "15": "Piraera", "16": "San Andrés", "17": "San Francisco", "18": "San Juan Guarita", "19": "San Manuel Colohete", "20": "San Rafael", "21": "San Sebastián", "22": "Santa Cruz", "23": "Talgua", "24": "Tambla", "25": "Tomalá", "26": "Valladolid", "27": "Virginia", "28": "San Marcos de Caiquín"}},
    "14": {"nombre": "Ocotepeque", "municipios": {"01": "Ocotepeque", "02": "Belén Gualcho", "03": "Concepción", "04": "Dolores Merendón", "05": "Fraternidad", "06": "La Encarnación", "07": "La Labor", "08": "Lucerna", "09": "Mercedes", "10": "San Fernando", "11": "San Francisco del Valle", "12": "San Jorge", "13": "San Marcos", "14": "Santa Fé", "15": "Sensenti", "16": "Sinuapa"}},
    "15": {"nombre": "Olancho", "municipios": {"01": "Juticalpa", "02": "Campamento", "03": "Catacamas", "04": "Concordia", "05": "Dulce Nombre de Culmí", "06": "El Rosario", "07": "Esquipulas del Norte", "08": "Gualaco", "09": "Guarizama", "10": "Guata", "11": "Guayape", "12": "Jano", "13": "La Unión", "14": "Mangulile", "15": "Manto", "16": "Salamá", "17": "San Esteban", "18": "San Francisco de Becerra", "19": "San Francisco de La Paz", "20": "Santa María del Real", "21": "Silca", "22": "Yocón"}},
    "16": {"nombre": "Santa Bárbara", "municipios": {"01": "Santa Bárbara", "02": "Arada", "03": "Atima", "04": "Azacualpa", "05": "Ceguaca", "06": "Concepción del Norte", "07": "Concepción del Sur", "08": "Chinda", "09": "El Níspero", "10": "Gualala", "11": "Ilama", "12": "Las Vegas", "13": "Macuelizo", "14": "Naranjito", "15": "Nuevo Celilac", "16": "Petoa", "17": "Protección", "18": "Quimistán", "19": "San Francisco de Ojuera", "20": "San José de Colinas", "21": "San Luis", "22": "San Marcos", "23": "San Nicolás", "24": "San Pedro Zacapa", "25": "San Vicente Centenario", "26": "Santa Rita", "27": "Trinidad"}},
    "17": {"nombre": "Valle", "municipios": {"01": "Nacaome", "02": "Alianza", "03": "Amapala", "04": "Aramecina", "05": "Caridad", "06": "Goascorán", "07": "Langue", "08": "San Francisco de Coray", "09": "San Lorenzo"}},
    "18": {"nombre": "Yoro", "municipios": {"01": "Yoro", "02": "Arenal", "03": "El Negrito", "04": "El Progreso", "05": "Jocón", "06": "Morazán", "07": "Olanchito", "08": "Santa Rita", "09": "Sulaco", "10": "Victoria", "11": "Yorito"}}
}

# Diccionario de usuarios (usuario: contraseña)
usuarios = {
    "admin": "admin123",
    "Lucas": "12345",
    "Jose": "12345",
}
#usuario 
def autenticar_usuario(usuario, contraseña):
    return usuarios.get(usuario) == contraseña

# Función para autenticación
def calcular_edad(anio_nacimiento):
    anio_actual = datetime.datetime.now().year
    return anio_actual - anio_nacimiento

def descomponer_identidad(identidad):
    if len(identidad) != 13 or not identidad.isdigit():
        raise ValueError("El número de identidad debe tener 13 dígitos numéricos.")

    depto_codigo = identidad[:2]
    muni_codigo = identidad[2:4]
    anio_nacimiento = int(identidad[4:8])
    num_inscrito = int(identidad[8:])

    departamento = localidades.get(depto_codigo, {"nombre": "Desconocido"}).get("nombre", "Desconocido")
    municipio = localidades.get(depto_codigo, {"municipios": {}}).get("municipios", {}).get(muni_codigo, "Desconocido")
    edad = calcular_edad(anio_nacimiento)

    return departamento, municipio, anio_nacimiento, num_inscrito, edad

def buscar_municipios_por_departamento(depto_codigo):
    departamento = localidades.get(depto_codigo, {"nombre": "Desconocido"}).get("nombre", "Desconocido")
    municipios = localidades.get(depto_codigo, {"municipios": {}}).get("municipios", {})
    return departamento, municipios

def buscar_departamento_por_codigo(depto_codigo):
    return localidades.get(depto_codigo, {"nombre": "Desconocido"}).get("nombre", "Desconocido")

def buscar_departamento_municipio(depto_codigo, muni_codigo):
    departamento = localidades.get(depto_codigo, {"nombre": "Desconocido"}).get("nombre", "Desconocido")
    municipio = localidades.get(depto_codigo, {"municipios": {}}).get("municipios", {}).get(muni_codigo, "Desconocido")
    return departamento, municipio

# Menú principal
def menu_principal():
     while True:
        print("\nMenu:")
        print("1. Buscar por número de identidad")
        print("2. Buscar municipios por código de departamento")
        print("3. Buscar departamento por código")
        print("4. Buscar departamento y municipio por códigos")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            identidad = input("Ingrese su número de identidad (13 dígitos): ")
            try:
                departamento, municipio, anio_nacimiento, num_inscrito, edad = descomponer_identidad(identidad)
                print(f"\nDepartamento: {departamento}")
                print(f"Municipio: {municipio}")
                print(f"Año de Nacimiento: {anio_nacimiento}")
                print(f"Número de niño inscrito: {num_inscrito}")
                print(f"Edad: {edad}")
            except ValueError as e:
                print(e)
        
        elif opcion == "2":
            depto_codigo = input("Ingrese el código del departamento (2 dígitos): ")
            departamento, municipios = buscar_municipios_por_departamento(depto_codigo)
            print(f"\nDepartamento: {departamento}")
            print("Municipios:")
            for codigo, nombre in municipios.items():
                print(f"{codigo}: {nombre}")
        
        elif opcion == "3":
            depto_codigo = input("Ingrese el código del departamento (2 dígitos): ")
            departamento = buscar_departamento_por_codigo(depto_codigo)
            print(f"\nDepartamento: {departamento}")
        
        elif opcion == "4":
            depto_codigo = input("Ingrese el código del departamento (2 dígitos): ")
            muni_codigo = input("Ingrese el código del municipio (2 dígitos): ")
            departamento, municipio = buscar_departamento_municipio(depto_codigo, muni_codigo)
            print(f"\nDepartamento: {departamento}")
            print(f"Municipio: {municipio}")

        elif opcion == "5":
            print("Saliendo del programa...")
            break
        
        else:
            print("Opción no válida, por favor intente de nuevo.")


# Función principal
def main():
    usuario = input("Ingrese su usuario: ")
    contraseña = input("Ingrese su contraseña: ")

    if autenticar_usuario(usuario, contraseña):
        print("Autenticación exitosa.")
        menu_principal()
    else:
        print("Usuario o contraseña incorrectos.")

main()
