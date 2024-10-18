
def calcular_fuerza(masa, aceleracion):
    fuerza = masa * aceleracion
    return fuerza


masa = float(input("Ingrese la masa en kilogramos (kg): "))
aceleracion = float(input("Ingrese la aceleración en metros por segundo al cuadrado (m/s^2): "))


fuerza = calcular_fuerza(masa, aceleracion)


print(f"La fuerza resultante es {fuerza} Newtons (N).")
