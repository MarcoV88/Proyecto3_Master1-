from functools import reduce

# 1
def contar_frecuencias(texto):
    frecuencias = {}
    for letra in texto:
        if letra != " ":
            if letra in frecuencias:
                frecuencias[letra] += 1
            else:
                frecuencias[letra] = 1
    return frecuencias

# 2
def doblar_valores(lista):
    return list(map(lambda x: x * 2, lista))

# 3
def buscar_palabras(lista, palabra_objetivo):
    resultado = []
    for p in lista:
        if palabra_objetivo in p:
            resultado.append(p)
    return resultado

# 4
def restar_listas(l1, l2):
    return list(map(lambda x, y: x - y, l1, l2))

# 5
def comprobar_aprobado(notas, nota_aprobado=5):
    media = sum(notas) / len(notas)
    if media >= nota_aprobado:
        estado = "aprobado"
    else:
        estado = "suspenso"
    return (media, estado)

# 6
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# 7
def tuplas_a_texto(lista_tuplas):
    return list(map(lambda t: str(t), lista_tuplas))

# 8
def dividir_numeros():
    try:
        a = float(input("Primer número: "))
        b = float(input("Segundo número: "))
        res = a / b
        print("Resultado:", res)
        print("La división fue exitosa.")
    except ValueError:
        print("No has introducido un número válido.")
        print("La división no fue exitosa.")
    except ZeroDivisionError:
        print("No se puede dividir entre cero.")
        print("La división no fue exitosa.")

# 9
def filtrar_mascotas(lista):
    prohibidas = ["Mapache", "Tigre", "Serpiente Pitón", "Cocodrilo", "Oso"]
    return list(filter(lambda m: m not in prohibidas, lista))

# 10
class ListaVaciaError(Exception):
    pass

def media_con_excepcion(numeros):
    try:
        if len(numeros) == 0:
            raise ListaVaciaError("La lista no puede estar vacía")
        return sum(numeros) / len(numeros)
    except ListaVaciaError as e:
        print("Error:", e)

# 11
def pedir_edad():
    try:
        edad = int(input("Introduce tu edad: "))
        if edad < 0 or edad > 120:
            raise Exception("Edad fuera de rango permitido")
        print("Edad correcta:", edad)
    except ValueError:
        print("Debes ingresar un número entero.")
    except Exception as e:
        print("Error:", e)

# 12
def longitud_palabras(frase):
    palabras = frase.split()
    return list(map(lambda p: len(p), palabras))

# 13
def pares_mayus_minus(caracteres):
    unicos = list(set(caracteres))
    return list(map(lambda c: (c.upper(), c.lower()), unicos))

# 14
def palabras_por_letra(lista, letra):
    return list(filter(lambda p: p.startswith(letra), lista))

# 15
sumar_tres = lambda lista: list(map(lambda x: x + 3, lista))

# 16
def palabras_largas(texto, n):
    palabras = texto.split()
    return list(filter(lambda p: len(p) > n, palabras))

# 17
def juntar_digitos(digitos):
    return reduce(lambda acumulado, d: acumulado * 10 + d, digitos)

# 18
def filtrar_estudiantes():
    estudiantes = [
        {"nombre": "Ana", "edad": 20, "calificacion": 95},
        {"nombre": "Luis", "edad": 22, "calificacion": 70},
        {"nombre": "Marta", "edad": 19, "calificacion": 90}
    ]
    return list(filter(lambda e: e["calificacion"] >= 90, estudiantes))

# 19
filtrar_impares = lambda lista: list(filter(lambda x: x % 2 != 0, lista))

# 20
def solo_enteros(lista):
    return list(filter(lambda x: type(x) == int, lista))

# 21
cubo = lambda x: x ** 3

# 22
def multiplicar_lista(numeros):
    return reduce(lambda a, b: a * b, numeros)

# 23
def unir_palabras(palabras):
    return reduce(lambda a, b: a + b, palabras)

# 24
def restar_elementos(numeros):
    return reduce(lambda a, b: a - b, numeros)

# 25
def contar_caracteres(texto):
    return len(texto)

# 26
resto_division = lambda a, b: a % b

# 27
def calcular_media(numeros):
    return sum(numeros) / len(numeros)

# 28
def primer_duplicado(lista):
    vistos = []
    for elemento in lista:
        if elemento in vistos:
            return elemento
        vistos.append(elemento)
    return None

# 29
def enmascarar(variable):
    texto = str(variable)
    if len(texto) <= 4:
        return texto
    almohadillas = "#" * (len(texto) - 4)
    return almohadillas + texto[-4:]

# 30
def son_anagramas(p1, p2):
    return sorted(p1.lower()) == sorted(p2.lower())

# 31
def buscar_nombre():
    nombres_input = input("Introduce nombres separados por comas: ")
    lista_nombres = [n.strip() for n in nombres_input.split(",")]
    buscar = input("Nombre a buscar: ").strip()
    
    if buscar in lista_nombres:
        print("El nombre fue encontrado.")
    else:
        raise Exception("El nombre no está en la lista.")

# 32
def buscar_empleado(nombre, empleados):
    for emp in empleados:
        if emp["nombre"] == nombre:
            return emp["puesto"]
    return "La persona no trabaja aquí."

# 33
sumar_dos_listas = lambda l1, l2: list(map(lambda a, b: a + b, l1, l2))

# 34
class Arbol:
    def __init__(self):
        self.tronco = 1
        self.ramas = []

    def crecer_tronco(self):
        self.tronco += 1

    def nueva_rama(self):
        self.ramas.append(1)

    def crecer_ramas(self):
        for i in range(len(self.ramas)):
            self.ramas[i] += 1

    def quitar_rama(self, pos):
        self.ramas.pop(pos)

    def info_arbol(self):
        return {
            "tronco": self.tronco,
            "total_ramas": len(self.ramas),
            "ramas": self.ramas
        }

# Caso de uso 34
mi_arbol = Arbol()
mi_arbol.crecer_tronco()
mi_arbol.nueva_rama()
mi_arbol.crecer_ramas()
mi_arbol.nueva_rama()
mi_arbol.nueva_rama()
mi_arbol.quitar_rama(2)
info = mi_arbol.info_arbol()

# 35
class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        self.saldo += cantidad

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise Exception("No hay suficiente saldo.")
        self.saldo -= cantidad

    def transferir_dinero(self, otro_usuario, cantidad):
        if not self.cuenta_corriente or not otro_usuario.cuenta_corriente:
            raise Exception("Ambos deben tener cuenta corriente.")
        self.retirar_dinero(cantidad)
        otro_usuario.agregar_dinero(cantidad)

# Caso de uso 35
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

bob.agregar_dinero(20)
try:
    bob.transferir_dinero(alicia, 80)
except Exception as e:
    pass
alicia.retirar_dinero(50)

# 36
def contar_palabras(texto):
    palabras = texto.split()
    conteo = {}
    for p in palabras:
        if p in conteo:
            conteo[p] += 1
        else:
            conteo[p] = 1
    return conteo

def reemplazar_palabras(texto, original, nueva):
    return texto.replace(original, nueva)

def eliminar_palabra(texto, palabra):
    palabras = texto.split()
    resultado = []
    for p in palabras:
        if p != palabra:
            resultado.append(p)
    return " ".join(resultado)

def procesar_texto(texto, opcion, *args):
    if opcion == "contar":
        return contar_palabras(texto)
    elif opcion == "reemplazar":
        return reemplazar_palabras(texto, args[0], args[1])
    elif opcion == "eliminar":
        return eliminar_palabra(texto, args[0])

# 37
def periodo_dia():
    hora = int(input("Introduce la hora (0-23): "))
    if 6 <= hora <= 13:
        print("Es de día")
    elif 14 <= hora <= 20:
        print("Es de tarde")
    else:
        print("Es de noche")

# 38
def obtener_nota(nota):
    if 0 <= nota <= 69:
        return "insuficiente"
    elif 70 <= nota <= 79:
        return "bien"
    elif 80 <= nota <= 89:
        return "muy bien"
    elif 90 <= nota <= 100:
        return "excelente"

# 39
def calcular_area(figura, datos):
    if figura == "rectangulo":
        return datos[0] * datos[1]
    elif figura == "circulo":
        return 3.1416 * (datos[0] ** 2)
    elif figura == "triangulo":
        return (datos[0] * datos[1]) / 2

# 40
def calcular_compra():
    precio = float(input("Precio original: "))
    tiene_cupon = input("¿Tienes cupón de descuento? (sí/no): ").lower()

    if tiene_cupon == "sí" or tiene_cupon == "si":
        cupon = float(input("Valor del cupón: "))
        if cupon > 0:
            precio_final = precio - cupon
            if precio_final < 0:
                precio_final = 0
            print("Precio final con descuento:", precio_final)
        else:
            print("El cupón no es válido.")
            print("Precio final:", precio)
    elif tiene_cupon == "no":
        print("Precio final:", precio)
    else:
        print("Opción no reconocida. Precio final:", precio)

# Pruebas de las katas
if __name__ == "__main__":
    print("--- Ejecutando pruebas de katas ---\n")

    # 1
    print("Kata 1:", contar_frecuencias("tres tristes tigres"))

    # 2
    print("Kata 2:", doblar_valores([4, 8, 15, 16, 23, 42]))

    # 3
    print("Kata 3:", buscar_palabras(["ordenador", "torre", "teclado", "raton"], "or"))

    # 4
    print("Kata 4:", restar_listas([50, 40, 30], [5, 10, 15]))

    # 5
    print("Kata 5:", comprobar_aprobado([7, 8, 6, 9]))

    # 6
    print("Kata 6:", factorial(7))

    # 7
    print("Kata 7:", tuplas_a_texto([(10, 20), ("x", "y"), ("python", 3)]))

    # 9
    animales = ["Gato", "Cocodrilo", "Perro", "Serpiente Pitón", "Canario"]
    print("Kata 9:", filtrar_mascotas(animales))

    # 10
    print("Kata 10:", media_con_excepcion([15, 25, 35]))

    # 12
    print("Kata 12:", longitud_palabras("Resolviendo ejercicios basicos de programacion"))

    # 13
    print("Kata 13:", pares_mayus_minus("murcielago"))

    # 14
    ciudades = ["Madrid", "Barcelona", "Malaga", "Sevilla", "Murcia"]
    print("Kata 14:", palabras_por_letra(ciudades, "M"))

    # 15
    print("Kata 15:", sumar_tres([5, 10, 15, 20]))

    # 16
    print("Kata 16:", palabras_largas("el sol brilla sobre la ciudad", 4))

    # 17
    print("Kata 17:", juntar_digitos([4, 1, 8, 3]))

    # 18
    print("Kata 18:", filtrar_estudiantes())

    # 19
    print("Kata 19:", filtrar_impares([12, 17, 22, 29, 34, 41]))

    # 20
    valores_variados = [10, "dato", 25, "50", True, 99, "fin"]
    print("Kata 20:", solo_enteros(valores_variados))

    # 21
    print("Kata 21:", cubo(4))

    # 22
    print("Kata 22:", multiplicar_lista([3, 5, 2]))

    # 23
    print("Kata 23:", unir_palabras(["Python", "Es", "Genial"]))

    # 24
    print("Kata 24:", restar_elementos([80, 15, 5]))

    # 25
    print("Kata 25:", contar_caracteres("Estructuras de datos"))

    # 26
    print("Kata 26:", resto_division(25, 4))

    # 27
    print("Kata 27:", calcular_media([12, 14, 16, 18]))

    # 28
    print("Kata 28:", primer_duplicado(["a", "b", "c", "d", "b", "e"]))

    # 29
    print("Kata 29:", enmascarar("4567891234"))

    # 30
    print("Kata 30:", son_anagramas("frase", "fresa"))

    # 32
    plantilla = [
        {"nombre": "Carlos Perez", "puesto": "Backend Dev"},
        {"nombre": "Sara Ruiz", "puesto": "Product Manager"}
    ]
    print("Kata 32:", buscar_empleado("Carlos Perez", plantilla))

    # 33
    print("Kata 33:", sumar_dos_listas([5, 10, 15], [2, 4, 6]))

    # 34
    print("\n--- Test Kata 34 (Arbol) ---")
    arbol_test = Arbol()
    arbol_test.crecer_tronco()
    arbol_test.nueva_rama()
    arbol_test.crecer_ramas()
    arbol_test.nueva_rama()
    arbol_test.nueva_rama()
    arbol_test.quitar_rama(2)
    print("Estado del arbol:", arbol_test.info_arbol())

    # 35
    print("\n--- Test Kata 35 (UsuarioBanco) ---")
    user1 = UsuarioBanco("Alicia", 100, True)
    user2 = UsuarioBanco("Bob", 50, True)
    user2.agregar_dinero(20)
    try:
        user2.transferir_dinero(user1, 80)
    except Exception as err:
        print("Error en transferencia esperado:", err)
    user1.retirar_dinero(50)
    print(f"Saldos finales -> Alicia: {user1.saldo} | Bob: {user2.saldo}")

    # 36
    print("\n--- Test Kata 36 (Procesar texto) ---")
    frase_demo = "sol playa mar playa sol sol"
    print("Contar:", procesar_texto(frase_demo, "contar"))
    print("Reemplazar:", procesar_texto(frase_demo, "reemplazar", "playa", "arena"))
    print("Eliminar:", procesar_texto(frase_demo, "eliminar", "mar"))

    # 38
    print("\n--- Test Kata 38 (Notas) ---")
    print("Nota con 74:", obtener_nota(74))
    print("Nota con 92:", obtener_nota(92))

    # 39
    print("\n--- Test Kata 39 (Areas) ---")
    print("Area rectangulo:", calcular_area("rectangulo", (8, 4)))
    print("Area circulo:", round(calcular_area("circulo", (5,)), 2))

    print("\nPruebas automaticas listas. Descomenta las de abajo para probar las interactivas con input():")

    # Katas interactivas

    # print("\n--- Probando Kata 8 ---")
    # dividir_numeros()

    # print("\n--- Probando Kata 11 ---")
    # pedir_edad()

    # print("\n--- Probando Kata 31 ---")
    # buscar_nombre()

    # print("\n--- Probando Kata 37 ---")
    # periodo_dia()

    # print("\n--- Probando Kata 40 ---")
    # calcular_compra()