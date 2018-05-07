print("pruebas idiotas ")
transiciones = ["(1,1,1)=(1,1)","(2,2,2)=(2,2)"]
def buscar_transicion(transiciones,estadoActual,sim,variableStack):
    pos=0
    while pos<len(transiciones):
        if transiciones[pos][1]==estadoActual and transiciones[pos][3]==sim and transiciones[pos][5]==variableStack :
            return transiciones[pos]
        pos = pos + 1
    return ""
print(buscar_transicion(transiciones,"1","","1"))