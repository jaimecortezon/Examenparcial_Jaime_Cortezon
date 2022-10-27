class alumno():
    def __innit__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        def __str__(self):
            return "nombre: {}, nota: {}".format(self.nombre, self.nota)
        print("el alumno se ha creado con éxito")
calificación=(int("¿Qué nota ha sacado el alumno?"))
if calificación >= 5:
    print("el alumno ha aprobado")
    else:
        print("el alumno ha suspendido")   
    


