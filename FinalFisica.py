import numpy as np
import random
import matplotlib.pyplot as plt
from scipy.special import gamma  # Para la función gamma


def gsa(fun, x0, l, u, qv, qa, Imax):
    """
    Algoritmo de Recocido Simulado Generalizado (GSA) para minimizar una función objetivo.
    
    Parámetros:
        fun: Función objetivo a minimizar.
        x0: Vector inicial.
        l: Límite inferior de los parámetros.
        u: Límite superior de los parámetros.
        qv: Parámetro de visita.
        qa: Parámetro de aceptación.
        Imax: Máximo número de iteraciones.
    
    Retorna:
        xo: Vector solución óptima.
        fo: Valor mínimo de la función objetivo en xo.
    """
    # Inicialización
    xo = x0
    fx = fun(x0)
    fo = fx
    Dim = len(x0)
    
    # Constante de Boltzmann
    k = 1.38e-23

    # Bucle externo
    for t in range(1, Imax + 1):
        # Esquema de enfriamiento
        Tqvo = Imax
        if qv == 1:
            Tqv = Tqvo / np.log(1 + t)  # CSA
        elif qv == 2:
            Tqv = Tqvo / (1 + t)  # FSA
        else:
            Tqv = Tqvo * ((2 ** (qv - 1)) - 1) / (((1 + t) ** (qv - 1)) - 1)  # GSA
        
        Tqa = Tqv / t  # Temperatura de aceptación

        # Distribución de visita de Tsallis
        for _ in range(Imax // 5):  # Simular el equilibrio térmico
            dx = tsallis_rnd(qv, Tqv, Dim) * (u - l)
            x1 = xo + dx
            x1 = np.clip(x1, l, u)  # Confina la solución dentro de los límites

            # Evaluar la nueva solución
            fx1 = fun(x1)
            df = fx1 - fx

            # Probabilidad de aceptación
            if df < 0:
                Pa = 1
            else:
                Pa = 1 / ((1 + (qa - 1) * df / (k * Tqa)) ** (1 / (qa - 1)))

            # Criterio de aceptación
            if df < 0 or Pa > random.random():
                xo = x1
                fx = fx1

            # Actualizar la mejor solución encontrada
            if fx < fo:
                fo = fx

    return xo, fo


def tsallis_rnd(qv, Tqv, Dim):
    """
    Generador de números aleatorios basado en la distribución de Tsallis.
    
    Parámetros:
        qv: Parámetro de visita.
        Tqv: Temperatura de visita.
        Dim: Dimensión del vector solución.
    
    Retorna:
        Z: Vector de números aleatorios.
    """
    n = (3 - qv) / (qv - 1)
    s = np.sqrt(2 * (qv - 1)) / (Tqv ** (1 / (3 - qv)))
    cov = (n * (qv - 1) / (Tqv ** (2 / (3 - qv)))) ** -1
    mu = 0  # Media
    sigma = np.sqrt(cov)  # Desviación estándar

    # Generar números aleatorios iid
    X = mu + sigma * np.random.randn(Dim)
    U = np.random.gamma(n / 2, 1)
    Y = s * np.sqrt(U)

    return X / Y


def transmission_error(params, x_data, transmission_data):
    """
    Función objetivo para minimizar el error entre los datos de transmisión experimental
    y los datos ajustados por el modelo.

    Parámetros:
        params: Parámetros a optimizar (a, b, v, r).
        x_data: Datos de grosor del material (x).
        transmission_data: Datos experimentales de transmisión.

    Retorna:
        Error cuadrático medio entre los datos experimentales y los ajustados.
    """
    a, b, v, r = params
    model = r * np.exp(-a * x_data ** b) + (1 - r) * np.exp(-v * x_data)
    error = np.mean((transmission_data - model) ** 2)
    return error


def reconstruct_spectrum(x_data, transmission_data, bounds, qv=2.7, qa=-5, Imax=200):
    """
    Reconstrucción del espectro de energía utilizando la metodología del recocido simulado generalizado.

    Parámetros:
        x_data: Datos de grosor del material (x).
        transmission_data: Datos experimentales de transmisión.
        bounds: Límites de los parámetros (a, b, v, r).
        qv: Parámetro de visita.
        qa: Parámetro de aceptación.
        Imax: Máximo número de iteraciones.

    Retorna:
        params: Parámetros ajustados del modelo (a, b, v, r).
    """
    # Inicialización de los parámetros
    l, u = np.array(bounds)[:, 0], np.array(bounds)[:, 1]
    x0 = np.random.uniform(l, u)

    # Minimización usando GSA
    params, _ = gsa(
        lambda p: transmission_error(p, x_data, transmission_data),
        x0,
        l,
        u,
        qv,
        qa,
        Imax,
    )
    return params


# Datos experimentales
# Grosor de aluminio (cm)
x_data_80kVp = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5])
x_data_120kVp = np.array([0.0, 0.2, 0.4, 0.5, 0.6, 0.7])

# Transmisión normalizada (80 kVp y 120 kVp)
transmission_80kVp = np.array([1.0, 0.85, 0.72, 0.61, 0.52, 0.45])
transmission_120kVp = np.array([1.0, 0.74, 0.55, 0.45, 0.37, 0.3])

# Límite de los parámetros (a, b, v, r)
bounds = [(0, 10), (0, 1), (0, 1), (0, 1)]

# Reconstrucción del espectro para 80 kVp
params_80kVp = reconstruct_spectrum(x_data_80kVp, transmission_80kVp, bounds)
print("Parámetros ajustados para 80 kVp:", params_80kVp)

# Reconstrucción del espectro para 120 kVp
params_120kVp = reconstruct_spectrum(x_data_120kVp, transmission_120kVp, bounds)
print("Parámetros ajustados para 120 kVp:", params_120kVp)

# Graficar los datos experimentales y ajustados
x_fit = np.linspace(0, 0.7, 100)
fit_80kVp = params_80kVp[3] * np.exp(-params_80kVp[0] * x_fit ** params_80kVp[1]) + \
            (1 - params_80kVp[3]) * np.exp(-params_80kVp[2] * x_fit)
fit_120kVp = params_120kVp[3] * np.exp(-params_120kVp[0] * x_fit ** params_120kVp[1]) + \
             (1 - params_120kVp[3]) * np.exp(-params_120kVp[2] * x_fit)

plt.figure(figsize=(12, 6))
plt.subplot(1, 2, 1)
plt.plot(x_data_80kVp, transmission_80kVp, 'o', label='Datos 80 kVp')
plt.plot(x_fit, fit_80kVp, '-', label='Ajuste 80 kVp')
plt.xlabel('Grosor de aluminio (cm)')
plt.ylabel('Transmisión')
plt.legend()
plt.title('80 kVp')

plt.subplot(1, 2, 2)
plt.plot(x_data_120kVp, transmission_120kVp, 'o', label='Datos 120 kVp')
plt.plot(x_fit, fit_120kVp, '-', label='Ajuste 120 kVp')
plt.xlabel('Grosor de aluminio (cm)')
plt.ylabel('Transmisión')
plt.legend()
plt.title('120 kVp')

plt.tight_layout()
plt.show()