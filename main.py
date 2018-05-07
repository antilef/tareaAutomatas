from DataStruct.Stack import Stack
from DataStruct.Queue import Queue

transiciones = Queue()
pilaMemoria = Stack()
estadoInicial = ""
palabraEntrada = ""
estadoFinal = ""
def transicion_Mala(tran):
    return tran[0]!='(' or tran[2]!=',' or tran[4]!=',' or tran[6]!=')' or tran[7]!='=' or tran[8]!='(' or tran[10]!=',' or tran[12]!=')'
        
def pide_transiciones(transiciones):
    tran=str(input("Ingrese las transiciones (presiones ENTER para terminar):"))
    tran=tran.replace(' ','')
    while tran!="":
        while(transicion_Mala(tran)):
            tran=str(input("Error..Ingrese las transiciones otra vez:"))
            tran=tran.replace(' ','')
        transiciones.encolar(tran)
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
"""
def apd_stack_vacio(transiciones,estadoInicial,palabraEntrada,pilaMemoria):
    estadoActual= estadoInicial 
    simbolo=0
    while(len(palabraEntrada)>0):
        if()
    return True
"""
def main():
    print("Bienvenido a nuesta super tarea salvaje #MuerteAlHeinz")
    pilaMemoria.apilar("R")
    pide_transiciones(transiciones)
    if(transiciones.es_vacia()):
        print("Error")
    else:
        estadoInicial = validaEntrada("Ingrese el estado Inicial : ")
        palabraEntrada = validaEntrada("Ingrese la palabra de entrada : ") 
        if(por_stack_vacio() ):
            """
            if(apd_stack_vacio(transiciones,estadoInicial,palabraEntrada,pilaMemoria)):
                print("La palabra es aceptado por el APD por stack vacio")
            else:
                print("no se llama ") 
            """        
        else:
            estadoFinal=validaEntrada("Ingrese el estado Final : ")
            """
            if(apd_estado_final(transiciones,estadoInicial,palabraEntrada,estado_final,pilaMemoria)):
                print("La palabra es aceptado por el APD por estado_final")
            else:
                print("no se llama ")
            """
main()