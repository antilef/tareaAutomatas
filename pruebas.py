from DataStruct.Stack import Stack
from DataStruct.Queue import Queue

transiciones = Queue()
pilaMemoria = Stack()
estadoInicial = ""
palabraEntrada=""

def pide_transiciones(transiciones):
    tran=str(input("Ingrese las transiciones (presiones ENTER para terminar):"))
    while tran!="":
        transiciones.encolar(tran)
        tran=str(input("Ingrese las transiciones (presiones ENTER para terminar):"))
def por_stack_vacio():
    resp=str(input("El automata acepta por stack vacio(1) o estado final(2)"))
    resp=resp.replace(' ','')
    while resp not in ("1","2"):
        resp=str(input("Error...El automata acepta por stack vacio(1) o estado final(2)"))
        resp=resp.replace(' ','')
    return resp=="1"
def main():
    print("Bienvenido a nuesta super tarea salvaje ")
    pide_transiciones(transiciones)
    if(transiciones.es_vacia()):
        print("Error")
    else:
        estadoInicial = str(input("Ingrese estado inicial "))
        palabraEntrada = str(input("Ingrese la palabra de entrada ")) 
        if(por_stack_vacio()):
            print("stack vacio")
        else:
            print("estado final")
main()