from DataStruct.Stack import Stack
from DataStruct.Queue import Queue

transiciones = []
pilaMemoria = Stack()
estadoInicial = ""
palabraEntrada = ""
colaEntrada = Queue()
estadosFinales =[]

def transicion_esta_correcta(tran):
    ##hay que modificar esto
    return tran[0]!='(' or tran[2]!=',' or tran[4]!=',' or tran[6]!=')' or tran[7]!='=' or tran[8]!='(' or tran[10]!=',' or tran[len(tran)-1]!=')'
        
def pide_transiciones(transiciones):
    tran=input("Ingrese transicion (presiones ENTER para terminar,exit para terminar la ejecucion del programa):")
    tran=tran.replace(' ','')
    while tran!="":
        while(transicion_esta_correcta(tran)):
            if (tran=="exit"):
                while(tran!="S" and tran!="s" and tran!="N" and tran!="n"):
                    tran=input("Ha elegido salir de el programa, ¿Esta usted seguro de salir? s(si) - n(no)")
                if(tran=="S" or tran=="s"):
                    return True
            tran=input("Error...Ingrese transicion otra vez (o 'exit' para salir):")
            tran=tran.replace(' ','')
        transiciones.append(tran)
        tran=input("Ingrese transicion (presiones ENTER para terminar,exit para terminar la ejecucion del programa):")
        tran=tran.replace(' ','')
    return False
        
def por_stack_vacio():
    resp=str(input("El automata acepta por stack vacio(1) o estado final(2)?:"))
    resp=resp.replace(' ','')
    while resp not in ("1","2"):
        resp=str(input("Error...El automata acepta por stack vacio(1) o estado final(2)?:"))
        resp=resp.replace(' ','')
    return resp=="1"

def validaEntrada(mensaje,motivo):
    estado=str(input(mensaje))
    estado=estado.replace(' ','')
    while (estado=="" and motivo!="estadofinal"):
        estado=str(input("Error..."+mensaje))
        estado=estado.replace(' ','')
    return estado

def buscar_transicion(transiciones,estadoActual,sim,variableStack):
    pos=0
    while pos<len(transiciones):
        if transiciones[pos][1]==estadoActual and transiciones[pos][3]==sim and transiciones[pos][5]==variableStack :
            return transiciones[pos]
        pos = pos + 1
    return ""

def apilado(pilaMemoria,tran):
    pos=11
    if(tran[11]!="E"):
        pilaMemoria.apilar(tran[5])
    while pos<len(tran)-2:
        pilaMemoria.apilar(tran[pos])
        pos = pos + 1
    #Agrego la condición de que si el stack está vacío: entonces "E" (epsilon) es situado en la tapa para representar que está vacío
    #Esto es necesario para cierto tipo de transiciones, en donde se pregunta si el stack está vacío
    #Es posible que se acumule más de una 'E' en la tapa del stack en algunos autómatas, pero esto no afecta al resultado final
    if(pilaMemoria.es_vacia()):
        pilaMemoria.apilar("E")
        print("PILA VACÍA")
    print()

def calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria,acept):
    estadoActual= estadoInicial 
    while(not colaEntrada.es_vacia()):
        sim = colaEntrada.desencolar()
        variableStack=pilaMemoria.desapilar()
        tran=buscar_transicion(transiciones,estadoActual,sim,variableStack)
        #Agregada nueva condición: si el símbolo leido es E, quiere decir que llegamos al final de la palabra
        #Por lo tanto, es posible que no hayan más trnasiciones
        #Esto debido a que no todos los automatas tienen transiciones cuando leen un epsilon
        #Si no existe la transición y llegamos al final de la palabra, devolvemos
        #si es que habia el simbolo que quitamos anteriormente
        if (sim=="E" and tran==""):
            pilaMemoria.apilar(variableStack)
            return 1
        #Si existe la transición, pasará a este "elif", en donde se procede normalmente
        elif(tran!=""):
            estadoActual=tran[9]
            apilado(pilaMemoria,tran)
        #En el caso de no estar leyendo "E", y la transición no existe: queire decir que el APD no acepta la palabra:
        else:
            print("no existe la transicion ")
            return -1
    print("Estado al final de la ejecución: ",estadoActual)
    return estadoActual


def apd_stack_vacio(transiciones,estadoInicial,colaEntrada,pilaMemoria):
    existe=calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria,"pilaVacia")
    #Agregada nueva condición: si existe==-1 quiere decir que una transición no existe,
    #Y por lo tanto: la palabra no es aceptada por el APD
    if(pilaMemoria.desapilar()=="E" and existe!=-1):
        return True
    else:
        return False

def apd_estado_final(transiciones,estadoInicial,colaEntrada,estado_final,pilaMemoria):
    final=calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria,"estadoFinal")
    #Agregada nueva condición: si final =-1, significa que no existe una transición,
    #Y por lo tanto: que la palabra no es aceptada por el APD
    es_final=False
    x=0
    while(x<len(estadosFinales) and final!=estadosFinales[x]):
        x=x+1
    if(x!=len(estadosFinales)):
        es_final=True
    if(es_final and final!=-1):
        return True
    else:
        return False

def crearPalabra(palabraEntrada,colaEntrada):
    pos=0
    while pos<len(palabraEntrada):
        colaEntrada.encolar(palabraEntrada[pos])
        pos = pos + 1

def main():
    #PRESENTACIÓN:
    print("Bienvenido a nuesta super tarea salvaje(la epsilon=E )")
    print("Al momento de escribir las transiciones, se puede escribir el comando 'exit' (sin comillas) para salir del programa")
    print("Las transiciones deben ingresarse de la forma:")
    print("          (1,a,R)=(2,AR)")
    print("o tambien (q,b,R)=(w,AAR)   ")
    print()
    print("Donde cada elemento es:")
    print("   1(ó q) :Estado actual (los estados solo se pueden representar por un solo símbolo(letra, o número de un dígito por ejemplo: 'a', '1', 'q',etc))")
    print("   a(ó b) :El símbolo leido en la palabra (puede que ser cualquier símbolo)")
    print("   R :Símbolo en la tapa del stack al leer la símnolo de la palabra")
    print("   2(ó w) :estado final al completarse la transición")
    print("   RA(ó AAR) : 'A' Se apilará en la tapa del stack")
    print("No se puede usar la letra 'E' como simbolo de palabra ni del Stack, ya que está reservada por el programa(si se el programa no funcionará de manera correcta)")
    print("Por último, el símbolo inicial del stack de memoria siempre es :'R'")
    print()
    print()
    #Se inica el código
    salir=False
    salir=pide_transiciones(transiciones)
    while(transiciones==[] and salir==False):
        print("Error, no se han ingresado transiciones, por favor ingrese transiciones o ")
        salir=pide_transiciones(transiciones)
    while(salir==False):
        pilaMemoria.apilar("R")
        estadoInicial = validaEntrada("Ingrese el estado Inicial : ","inicial")
        palabraEntrada = validaEntrada("Ingrese la palabra de entrada : ","palabra")
        crearPalabra(palabraEntrada,colaEntrada)
        colaEntrada.encolar("E")
        if(por_stack_vacio() ):
            if(apd_stack_vacio(transiciones,estadoInicial,colaEntrada,pilaMemoria)):
                print("La palabra es aceptado por el APD por stack vacio")
            else:
                print("La palabra NO es aceptado por el APD por stack vacio ") 
        
        else:
            estadoFinal=validaEntrada("Ingrese estados Final (presione ENTER para continuar): ","estadofinal")
            while (estadoFinal!=""):
                estadoFinal=estadoFinal.replace(' ','')
                estadosFinales.append(estadoFinal)
                estadoFinal=validaEntrada("Ingrese otro estados Final (presione ENTER para continuar): ","estadofinal")
            if(apd_estado_final(transiciones,estadoInicial,colaEntrada,estadoFinal,pilaMemoria)):
                print("La palabra es aceptado por el APD por estado final")
            else:
                print("La palabra NO es aceptada por el APD por estado final ")
        
        pregunta=str(input("Quiere ingresar otra palabra para este autómata? S(si) - N(no:El programa finalizará)"))
        pregunta=pregunta.replace(' ','')
        while pregunta not in ("S","N","n"):
            pregunta=str(input("Error...Debe ingresar 'S' o 'N' : "))
            pregunta=pregunta.replace(' ','')
        if pregunta=="N" or pregunta=="n":
            salir=True
        while (not pilaMemoria.es_vacia()):
            pilaMemoria.desapilar()
        while(not colaEntrada.es_vacia()):
            colaEntrada.desencolar()
    print("Fin de la Ejecucion.....Que tenga buen día! :3")
    print()
    print()
    input("Presione ENTER para cerrar esta ventana")
            
main()
