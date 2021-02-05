class Persona:
    def __init__(self,edad,nombre):
        self.edad=edad
        self.nombre=nombre
        print("se ha creado a",self.nombre,"de",self.edad)
    def hablar(self,**palabras): #mira el diccionario y los asteriscos
        for frase in palabras:
            print(self.nombre,":", palabras[frase])
class Deportista(Persona):
    def __init__(self,edad,nombre,deporte):
        self.edad = edad
        self.nombre = nombre
        self.__deporte=deporte
        print("se ha creado a ",self.nombre, " de ", self.edad)

    def practicarDeporte(self):
        print(self.nombre,"; voy a practicar")

juan=Persona(18,"Juan")
juan.hablar(t1="Hola estoy hablando",t2="Este soy yo")
luis=Persona(20,"Luis")
luis.hablar(t1="Hola estoy hablando",t2="Este soy yo")
