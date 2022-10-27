class alumno():
    def __innit__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        def __str__(self):
            return "El alumno {} se ha creado con éxito".format(self.nombre)
        def calificacion(nota):
            if int(nota) >= 5:
                return "alumno aprobado"
            else:
                return "alumno suspenso"
alumno2 = alumno("Jaime Cortezon",7)
print(alumno2)

    


