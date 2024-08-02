class Regla:
    def __init__(self, condicion, conclusion):
        self.condicion = condicion
        self.conclusion = conclusion

    def aplica(self, base_de_hechos):
        if all(hecho in base_de_hechos for hecho in self.condicion):
            return self.conclusion
        return None

base_de_hechos = {"el cliente ha pagado su mensualidad"}

reglas = [
    Regla(["el cliente no ha pagado su mensualidad"], "el cliente no puede ingresar al establecimiento del gimnasio"),
    Regla(["el cliente ha pagado su mensualidad"], "el cliente puede ingresar al establecimiento del gimnasio"),
    Regla(["el cliente puede ingresar al establecimiento del gimnasio"], "el cliente está registrado en la base de datos")
]

while True:
    nuevos_hechos = set()
    for regla in reglas:
        resultado = regla.aplica(base_de_hechos)
        if resultado and resultado not in base_de_hechos:
            nuevos_hechos.add(resultado)
    if not nuevos_hechos:
        break
    base_de_hechos.update(nuevos_hechos)

print(base_de_hechos)
