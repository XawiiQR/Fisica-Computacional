import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

def monte_carlo_integration(func, a, b, n_samples=10000):
    """
    Método de Monte Carlo para calcular una integral definida.

    Parameters:
        func (callable): Función a integrar.
        a (float): Límite inferior de la integración.
        b (float): Límite superior de la integración.
        n_samples (int): Número de muestras aleatorias.

    Returns:
        float: Aproximación del valor de la integral.
    """
    samples = np.random.uniform(a, b, n_samples)
    values = func(samples)
    return (b - a) * np.mean(values)

# Definición de las funciones
functions = [
    lambda x: np.exp(x**2),
    lambda x: np.exp(x) * 4,
    lambda x: np.sqrt(np.maximum(0, 1 - np.exp(x**2))),  # Corrección aquí
    lambda x: x * (1 + x**2)**-2,
    lambda x: np.exp(x + x**2),
    lambda x: np.exp(-x),
    lambda x: (1 - x**2)**(3/2)
]

function_labels = [
    "exp(x^2)",
    "4 * exp(x)",
    "sqrt(1 - exp(x^2))",
    "x / (1 + x^2)^2",
    "exp(x + x^2)",
    "exp(-x)",
    "(1 - x^2)^(3/2)"
]

limits = [
    (0, 1),
    (-1, 1),
    (0, 1),
    (0, np.inf),
    (0, 1),
    (0, np.inf),
    (0, 1)  # Consideramos que el dominio de (1 - x^2)^(3/2) está restringido a [0, 1]
]

n_samples = 100000
colors = cm.get_cmap('tab10', len(functions))  # Generar colores únicos para cada función

# Resultados
for i, (func, label, (a, b)) in enumerate(zip(functions, function_labels, limits)):
    # Evaluar la integral
    if np.isinf(b):
        # Para límites superiores infinitos, reescalamos con una transformación.
        transformed_func = lambda x: func(x / (1 - x)) / (1 - x)**2
        integral = monte_carlo_integration(transformed_func, 0, 1, n_samples)
    else:
        integral = monte_carlo_integration(func, a, b, n_samples)

    # Imprimir resultado
    print(f"Integral {i + 1}: {integral}")

    # Graficar la función
    x = np.linspace(a, b, 500) if not np.isinf(b) else np.linspace(a, 5, 500)
    y = func(x)
    plt.figure()
    plt.plot(x, y, label=f"f(x) = {label}", color=colors(i))
    plt.title(f"f(x) = {label}")
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.legend()
    plt.grid()
    plt.show()
