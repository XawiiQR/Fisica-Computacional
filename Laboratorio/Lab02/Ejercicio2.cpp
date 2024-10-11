#include <iostream>
#include <cmath>
#include <vector>

namespace plt = matplotlibcpp;


double calcularAceleracion(double vi, double vf, double t) {
    return (vf - vi) / t;
}

double calcularFuerza(double masa, double aceleracion) {
    return masa * aceleracion;
}




int main() {
    
    double masa, distancia, tiempo, vi, vf;
    
    std::cout << "Ingrese la masa del móvil (kg): ";
    std::cin >> masa;
    std::cout << "Ingrese la distancia recorrida (m): ";
    std::cin >> distancia;
    std::cout << "Ingrese el tiempo total (s): ";
    std::cin >> tiempo;
    std::cout << "Ingrese la velocidad inicial (m/s): ";
    std::cin >> vi;
    std::cout << "Ingrese la velocidad final (m/s): ";
    std::cin >> vf;

    // Calcular aceleración
    double aceleracion = calcularAceleracion(vi, vf, tiempo);

    // Calcular fuerza
    double fuerza = calcularFuerza(masa, aceleracion);

    // Mostrar resultados
    std::cout << "La aceleración del móvil es: " << aceleracion << " m/s^2" << std::endl;
    std::cout << "La fuerza aplicada sobre el móvil es: " << fuerza << " N" << std::endl;

    

    return 0;
}
