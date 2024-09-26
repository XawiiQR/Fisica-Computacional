#include <iostream>
using namespace std;

double calcularVelocidad(double posInicial, double posFinal, double tiempoInicial, double tiempoFinal) {
    double delta_x = posFinal - posInicial;
    double delta_t = tiempoFinal - tiempoInicial;
    if (delta_t == 0) {
        cout << "Error: El intervalo de tiempo Δt no puede ser cero." << endl;
        return 0;
    }
    return delta_x / delta_t;
}

double calcularAceleracion(double velInicial, double velFinal, double tiempoInicial, double tiempoFinal) {
    double delta_v = velFinal - velInicial;
    double delta_t = tiempoFinal - tiempoInicial;
    if (delta_t == 0) {
        cout << "Error: El intervalo de tiempo Δt no puede ser cero." << endl;
        return 0;
    }
    return delta_v / delta_t;
}

double calcularAceleracionConMovimiento(double delta_x, double velInicial, double delta_t) {
    if (delta_t == 0) {
        cout << "Error: El intervalo de tiempo Δt no puede ser cero." << endl;
        return 0;
    }
    return (2 * (delta_x - velInicial * delta_t)) / (delta_t * delta_t);
}

int main() {
    double posInicial, posFinal, tiempoInicial, tiempoFinal;
    double velInicial, velFinal;

    cout << "Introduce la posición inicial: ";
    cin >> posInicial;
    cout << "Introduce la posición final: ";
    cin >> posFinal;
    cout << "Introduce el tiempo inicial: ";
    cin >> tiempoInicial;
    cout << "Introduce el tiempo final: ";
    cin >> tiempoFinal;
    
    double velocidad = calcularVelocidad(posInicial, posFinal, tiempoInicial, tiempoFinal);
    cout << "La velocidad calculada es: " << velocidad << " unidades/tiempo" << endl;

    
    cout << "Introduce la velocidad inicial: ";
    cin >> velInicial;
    cout << "Introduce la velocidad final: ";
    cin >> velFinal;
    
    double aceleracionVel = calcularAceleracion(velInicial, velFinal, tiempoInicial, tiempoFinal);
    cout << "La aceleración calculada a partir de velocidades es: " << aceleracionVel << " unidades/tiempo^2" << endl;

    double delta_x = posFinal - posInicial;
    double delta_t = tiempoFinal - tiempoInicial;
    
    double aceleracionMovimiento = calcularAceleracionConMovimiento(delta_x, velInicial, delta_t);
    cout << "La aceleración calculada usando la ecuación de movimiento es: " << aceleracionMovimiento << " unidades/tiempo^2" << endl;

    return 0;
}
