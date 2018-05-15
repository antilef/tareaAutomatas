from DataStruct.Stack import Stack
from DataStruct.Queue import Queue

transiciones = []
pilaMemoria = Stack()
estadoInicial = ""
palabraEntrada = ""
colaEntrada = Queue()
estadoFinal =        ""
def transicion_esta_correcta(tran):
    ##hay que modificar esto
    return tran[0]!='(' or tran[2]!=',' or tran[4]!=',' or tran[6]!=')' or tran[7]!='=' or tran[8]!='(' or tran[10]!=',' or tran[len(tran)-1]!=')'
        
def pide_transiciones(transiciones):
    tran=input("Ingrese las transiciones (presiones ENTER para terminar):")
    tran=tran.replace(' ','')
    while tran!="":
        while(transicion_esta_correcta(tran)):
            tran=input("malloc...Ingrese las transiciones otra vez:")
            tran=tran.replace(' ','')
        transiciones.append(tran)
        tran=input("Ingrese las transiciones (presiones ENTER para terminar):")
        tran=tran.replace(' ','')
        
def por_stack_vacio():
    resp=str(input("El automata acepta por stack vacio(1) o estado final(2)"))
    resp=resp.replace(' ','')
    while resp not in ("1","2"):
        resp=str(input("Error...El automata acepta por stack vacio(1) o estado final(2)"))
        resp=resp.replace(' ','')
    return resp=="1"

def validaEntrada(mensaje):
    estado=str(input(mensaje))
    estado=estado.replace(' ','')
    while estado=="":
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
    print("Transición detectada: ")
    print(tran)
    if(tran[11]!="E"):
        pilaMemoria.apilar(tran[5])
    while pos<len(tran)-2:
        print("se Agrega símbolo ",tran[pos]," en posición:",pos)
        pilaMemoria.apilar(tran[pos])
        print("Pila de memoria:")
        if(not pilaMemoria.es_vacia()):
            for x in pilaMemoria.items:
                print (x)
        pos = pos + 1
    #Agrego la condición de que si el stack está vacío: entonces "E" (epsilon) es situado en la tapa para representar que está vacío
    #Esto es necesario para cierto tipo de transiciones, en donde se pregunta si el stack está vacío
    if(pilaMemoria.es_vacia()):
        pilaMemoria.apilar("E")
        print("PILA VACÍA")
    print()

def calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria,acept):
    iteracion = 1
    estadoActual= estadoInicial 
    while(not colaEntrada.es_vacia()):
        print("****************")
        print("Cola entrada:")
        for x in colaEntrada.items:
            print(x,end=" ")  
        sim = colaEntrada.desencolar()
        #Si la pila esta vacía, quiere decir que no se puede continuar
        print("pila: ")
        for x in pilaMemoria.items :
            print(x)
        variableStack=pilaMemoria.desapilar()
        print(" estadoActual: ",estadoActual," sim: ",sim," variableStack: ",variableStack)
        tran=buscar_transicion(transiciones,estadoActual,sim,variableStack)
        print(tran)
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
        print("termino la iteracion: ",iteracion)
        print("*****************")
        iteracion=iteracion+1
    print("Estado Final: ",estadoActual)
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
    if(final==estado_final and final!=-1):
        return True
    else:
        return False
def crearPalabra(palabraEntrada,colaEntrada):
    pos=0
    while pos<len(palabraEntrada):
        colaEntrada.encolar(palabraEntrada[pos])
        pos = pos + 1
def main():
    print("Bienvenido a nuesta super tarea salvaje(la epsilon=E ) #MuerteAlHeinz")
    pilaMemoria.apilar("R")
    print("Pila de memoria:")
    for x in pilaMemoria.items:
        print(x)
    pide_transiciones(transiciones)
    if transiciones==[]:
        print("Error 404, no hay transiciones")
    else:
        estadoInicial = validaEntrada("Ingrese el estado Inicial : ")
        palabraEntrada = validaEntrada("Ingrese la palabra de entrada : ")
        crearPalabra(palabraEntrada,colaEntrada)
        colaEntrada.encolar("E")
        if(por_stack_vacio() ):
            if(apd_stack_vacio(transiciones,estadoInicial,colaEntrada,pilaMemoria)):
                print("La palabra es aceptado por el APD por stack vacio")
            else:
                print("La palabra NO es aceptado por el APD por stack vacio ") 
        
        else:
            for x in pilaMemoria.items:
                print(x)
            estadoFinal=validaEntrada("Ingrese el estado Final : ")
            if(apd_estado_final(transiciones,estadoInicial,colaEntrada,estadoFinal,pilaMemoria)):
                print("La palabra es aceptado por el APD por estado final")
            else:
                print("La palabra NO es aceptada por el APD por estado final ")
            
main()
