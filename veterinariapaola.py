#Nombre: Paola Andrea Realpe Zambrano
# Programa: Ingeniería de Sistemas
# Semestre: VIII 

#Clase
from math import inf
from posixpath import split


class VeterinariaInstalacion:
    #Atributos
    nit = 0
    nombreEmpresa = ''
    direccion = ''
    tamaño = 0
    numPisos = 0
    numTrabajadores = 0
    
    #Constructor
    def __init__(self, nit, nombreEmpresa, direccion, tamaño, numPisos, numTrabajadores):
        self.nit = nit
        self.nombreEmpresa = nombreEmpresa
        self.direccion = direccion
        self.tamaño = tamaño
        self.numPisos = numPisos
        self.numTrabajadores = numTrabajadores

    #Mensaje separador
    print("")
    print("METODOS DE LA CLASE VETERINARIAINSTALACION")
    print("")
    
    #Metodos
    def empresaTrabajadores(numTrabajadores): #Determina el tamaño de la empresa segun la cantidad de trabajadores
        if numTrabajadores > 0 and numTrabajadores < 11 :
            print('Es una veterinaria (MICROEMPRESA)')  
        if numTrabajadores > 10 and numTrabajadores < 51 :
            print('Es una veterinaria (EMPRESA PEQUEÑA)') 
        if numTrabajadores > 50 and numTrabajadores < 201 :
            print('Es una veterinaria (EMPRESA MEDIANA)')
        if numTrabajadores > 200 :
            print('Es una veterinaria (EMPRESA GRANDE)')    

    empresaTrabajadores(65)


    def sedesPisos(numPisos):
        if numPisos == 0 :
            print('No existe empresa')  
        if numPisos == 1:
            print('La veterinaria no es muy grande') 
        if numPisos > 1 :
            print('La veterinaria cuenta con buenas instalaciones y servicios')
    sedesPisos(3)


    def cantTotalServicios(agua, luz, gas):
        servicios = 0
        servicios = (agua+luz+gas)
        print("La cantidad de servicios a pagar en la veterinaria incluyendo el recibo del agua luz y el gas es", servicios)
    cantTotalServicios(200000, 340400, 43000)


#Clase
class Cliente:
    #Atributos
    identificacion = 0
    nombre = ''
    edad = 0
    idMascota = 0
    celular = 0
    direccion = ''
    
    #Constructor
    def __init__(self, identificacion, nombre, edad, idMascota, celular, direccion):
        self.identificacion = identificacion
        self.nombre = nombre
        self.edad = edad
        self.idMascota = idMascota
        self.celular = celular
        self.direccion = direccion

    #Mensaje separador      
    print("")
    print("METODOS DE LA CLASE CLIENTE")
    print("")
    
    #Metodos
    def repeticionNombre(nombre, num):
        #num = input("Introduce el número de veces que se quiere repetir el nombre del cliente: ")
        print((nombre + "\n") * int(num))
    
    repeticionNombre('Paola Realpe', 2)


    def mayorEdad(edad):
        if edad < 18: 
            print ("El cliente es menor de edad")
        else:
            print("El cliente es mayor de edad")
    
    mayorEdad(17)


    def informacionCliente(nombre, edad, direccion):
        print("El cliente se llama ", nombre , " tiene ", edad, " y vive en la ", direccion)

    informacionCliente('Paola Realpe', 20, 'calle 18#31C20 Maridiaz')

#Clase
class Veterinario:
     #Atributos
    idVeterinario = 0
    nombre = ''
    edad = 0
    especialidad = ''
    salario = 0
    horario = ''
    
    #Constructor
    def __init__(self, idVeterinario , nombre, edad, especialidad, salario, horario):
        self.idVeterinario  = idVeterinario 
        self.nombre = nombre
        self.edad = edad
        self.especialidad = especialidad
        self.salario = salario
        self.horario = horario

    #Mensaje separador      
    print("")
    print("METODOS DE LA CLASE VETERINARIO")
    print("")
    
    #Metodos
    def cantAños(edad):
        if edad > 50:
            print('El veterinario es demasiado mayor')  
        if edad < 50 and edad > 17:
            print('El veterinario es demasiado joven')
        if edad < 17:
            print('El veterinario no puede ser menor de edad')
    cantAños(2)    


    def riqueza(salario):
        if salario == 1000000 :
            print('El trabajador(veterinario) gana el salario minimo')  
        if salario > 1000000 :
            print('El trabajador(veterinario) gana más que el salario minimo ')  

    riqueza(180000000) 


    def salarioMenosSubsidioTransporte(salario):
        #salario = input ("Digite su salario total: ")
        #salario = int(salario)
        #subsidio = 0
        subsidio = salario - 117172
        print("La cantidad de tu salario sin el subsidio de transporte es", subsidio)
        
    salarioMenosSubsidioTransporte(1500000)


#Clase
class Mascota:
    #Atributos
    idMascota = 0
    nombre = ''
    edad = 0
    peso = 0
    tipo = ''
    raza = ''
    
    #Constructor
    def __init__(self, idMascota, nombre, edad, peso, tipo, raza):
        self.idMascota = idMascota
        self.nombre = nombre
        self.edad = edad
        self.peso = peso
        self.tipo = tipo
        self.raza = raza
    
    #Mensaje separador      
    print("")
    print("METODOS DE LA CLASE MASCOTA")
    print("")

    #Metodos
    def cantAños(edad):
        if edad > 8:
            print('El animal es viejo')  
        else:
            print('El animal es joven')

    cantAños(2)    


    def obesidad(peso):
        if peso > 30 and peso < 45 :
            print('El animal es pesado')  
        if peso > 12 and peso < 30:
            print('El animal esta rellenito, pero no tanto')
        if peso > 1 and peso < 12:
            print('El animal es demasiado ligero o liviano')

    obesidad(18) 


    def tipoAnimal(tipo):
        if tipo == 'perro' :
            print('Depende mucho de su dueño')  
        if tipo == 'gato' :
            print('Independiente de su dueño')
        if tipo != 'perro' and tipo != 'gato':
            print('Es una mascota que no es dependiente o independiente de su dueño')

    tipoAnimal('gato') 


#Clase
class Diagnostico:

    #Atributos
    fecha = ''
    hora = 0
    sintomas = ''
    evaluacion = ''
    medicamento = ''

    
    #Constructor
    def __init__(self, idMascota, fecha, hora, sintomas, evaluacion, medicamento):
        super().__init__(idMascota)
        self.fecha = fecha
        self.hora = hora
        self.sintomas = sintomas
        self.evaluacion = evaluacion
        self.medicamento = medicamento

    #Mensaje separador      
    print("")
    print("METODOS DE LA CLASE DIAGNOSTICO")
    print("")

    #Metodos
    def cantSintomas(sintomas):
        res = len(sintomas.split()) 
        print("La cantidad de sintomas que presenta la mascota son : " + str(res)) 
        print(sintomas.split())

    cantSintomas("debilidad cansancio fiebre") 


    def horasMedicamento(medicamento):
        if medicamento == 'Adaptil':
            print("Se debe dar el medicamento ", medicamento, " cada 10 horas")
        if medicamento == 'Advantage':
            print("Se debe dar el medicamento ", medicamento, " cada 5 horas")
        if medicamento == 'Alapiel':
            print("Se debe dar el medicamento ", medicamento, " cada 24 horas")
        if medicamento == 'Apoquel':
            print("Se debe dar el medicamento ", medicamento, " cada 12 horas")
    
    horasMedicamento('Alapiel')


    def gravedadDiagnostico(evaluacion):
        if evaluacion == 'Parvovirus' or evaluacion == 'Moquillo' or evaluacion == 'Rabia':
            print("La enfermedad ", evaluacion, " es grave")
        if evaluacion == 'Brucelosis':
            print("La enfermedad ", evaluacion, " es medio grave")
        if evaluacion == 'Diarrea' or evaluacion == 'Alergia':
            print("La enfermedad ", evaluacion, " es muy comun")
    
    gravedadDiagnostico('Alergia')




