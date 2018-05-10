from DataStruct.Stack import Stack
from DataStruct.Queue import Queue

transiciones = []
pilaMemoria = Stack()
estadoInicial = ""
palabraEntra   da = ""
colaEntrada = Queue()
estadoFinal =        ""
def transicion_esta_correcta(tran):
    ##hay que modificar esto
    return tran[0]!='(' or tran[2]!=',' or tran[4]!=',' or tran[6]!=')' or tran[7]!='=' or tran[8]!='(' or tran[10]!=',' or tran[len(tran)-1]!=')'
        
def pide_transiciones(transiciones):
    tran=str(input("Ingrese las transiciones (presiones ENTER para terminar):"))
    tran=tran.replace(' ','')
    while tran!="":
        while(transicion_esta_correcta(tran)):
            tran=str(input("Error..Ingrese las transiciones otra vez:"))
            tran=tran.replace(' ','')
        transiciones.append(tran)
        tran=str(input("Ingrese las transiciones (presiones ENTER para terminar):"))
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
    while tran[pos]!=")":
        if tran[pos]=="E":
            if pilaMemoria.es_vacia():
                return
            else :
                r=pilaMemoria.desapilar()
        else:
            pilaMemoria.apilar(tran[pos])
        pos = pos + 1

def calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria):
    estadoActual= estadoInicial 
    while(colaEntrada.es_vacia()):
        sim = colaEntrada.desencolar()
        if pilaMemoria.es_vacia():
            return estadoActual
        variableStack=pilaMemoria.desapilar()
        tran=buscar_transicion(transiciones,estadoActual,sim,variableStack)
        if(tran!=""):
            estadoActual=tran[9]
            apilado(pilaMemoria,tran)
        else:
            print("no existe la transicion ")
            return           

def apd_stack_vacio(transiciones,estadoInicial,colaEntrada,pilaMemoria):
    a=calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria)
    if(pilaMemoria.es_vacia()):
        return True
    else:
        return False

def apd_estado_final(transiciones,estadoInicial,colaEntrada,estado_final,pilaMemoria):
    final=calculaTransiciones(transiciones,estadoInicial,colaEntrada,pilaMemoria)
    if(final==estado_final):
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
    pide_transiciones(transiciones)
    if transiciones==[]:
        print("Error")
    else:
        estadoInicial = validaEntrada("Ingrese el estado Inicial : ")
        palabraEntrada = validaEntrada("Ingrese la palabra de entrada : ")
        crearPalabra(palabraEntrada,colaEntrada)
        if(por_stack_vacio() ):
            if(apd_stack_vacio(transiciones,estadoInicial,colaEntrada,pilaMemoria)):
                print("La palabra es aceptado por el APD por stack vacio")
            else:
                print("La palabra NO es aceptado por el APD por stack vacio ") 
        
        else:
            estadoFinal=validaEntrada("Ingrese el estado Final : ")
            if(apd_estado_final(transiciones,estadoInicial,colaEntrada,estadoFinal,pilaMemoria)):
                print("La palabra es aceptado por el APD por estado final")
            else:
                print("La palabra NO es aceptada por el APD por estado final ")
            
main()