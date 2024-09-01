class Persona:
    def __init__(self, nombre="nombre", apellido="apellido", direccion="direccion", telefono="telefono", edad="edad", email="email"):
        self.nombre = nombre
        self.apellido = apellido
        self.direccion = direccion
        self.telefono = telefono
        self.edad = edad
        self.email = email

class Empleado(Persona):
    def __init__(self, nombre, apellido, direccion, telefono, edad, email, salario, jefe_inmediato, anos_experiencia, nombreCargo):
        super().__init__(nombre, apellido, direccion, telefono, edad, email)
        self.nombreCargo = nombreCargo
        self.salario = salario
        self.jefe_inmediato = jefe_inmediato
        self.anos_experiencia = anos_experiencia
        
    def asignar_cargo(self):
        if self.salario > 5000000 and self.anos_experiencia >= 5 and 25 <= self.edad <= 45:
            return "Senior"
        elif 900000 <= self.salario <= 1200000 and self.anos_experiencia <= 2 and 18 <= self.edad <= 22:
            return "Junior"
     

def pedir_datos_persona():
    nombre = input("Ingrese nombre: ")
    apellido = input("Ingrese apellido: ")
    direccion = input("Ingrese dirección: ")
    telefono = input("Ingrese número de teléfono: ")
    edad = int(input("Ingrese edad: "))
    email = input("Ingrese correo electrónico: ")
    return Persona(nombre, apellido, direccion, telefono, edad, email)

def pedir_datos_empleado():
    persona = pedir_datos_persona()
    salario = int(input("Ingrese el salario: ")) 
    jefe_inmediato = input("Ingrese el nombre del jefe inmediato: ") 
    experiencia = int(input("Ingrese la experiencia (en años): ")) 
    return Empleado(persona.nombre, persona.apellido, persona.direccion,
                    persona.telefono, persona.edad, persona.email,
                    salario, jefe_inmediato, experiencia,
                    persona.nombre)


empleado = pedir_datos_empleado()
print(f"Cargo asignado: {empleado.asignar_cargo()}")






