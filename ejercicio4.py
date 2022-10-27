class alumno():
    def __innit__(self, nombre, nota):
        self.nombre= nombre
        self.nota= nota
        print("alumno ha sido creado con éxito")
    def __str__(self):
        return "El alumno {} tiene un {} de nota".format(self.nombre, self.nota)
    def calificacion(nota):
            if int(nota) >= 5:
                return "alumno aprobado"
            else:
                return "alumno suspenso"
alumno1 = alumno("Jaime Cortezon",7)
alumno2 = alumno("Karim Benzema",3)
alumno3 = alumno("Iker Casillas",8)

print(alumno1)
print(alumno2)
print(alumno3)

print(alumno.calificacion(alumno1.nota))
print(alumno.calificacion(alumno2.nota))
print(alumno.calificacion(alumno3.nota))