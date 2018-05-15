class Stack:
    def __init__(self):
        self.items=[]
    def apilar(self,x):
        self.items.append(x)
    def es_vacia(self):
        return self.items==[]
    def desapilar(self):
        try:
            return self.items.pop()
        except IndexError:
            raise ValueError("The Stack is empty ")
