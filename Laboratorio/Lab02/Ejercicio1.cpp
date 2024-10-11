#include <iostream>
#include <cmath>

const double G = 6.67430e-11;
const double PI = 3.141592653589793;

double calcularVelocidadOrbital(double masaEstrella, double distancia) {
    return std::sqrt(G * masaEstrella / distancia);
}

double calcularPeriodoOrbital(double masaEstrella, double distancia) {
    double periodo = 2 * PI * std::sqrt(std::pow(distancia, 3) / (G * masaEstrella));
    return periodo;
}

int main() {
    double masaEstrella;
    double distancia;
    double excentricidad;
    
    std::cout << "Ingrese la masa de la estrella (en kilogramos): ";
    std::cin >> masaEstrella;
    
    std::cout << "Ingrese la distancia promedio entre el planeta y la estrella (en metros): ";
    std::cin >> distancia;
    

    double velocidad = calcularVelocidadOrbital(masaEstrella, distancia);
    double periodo = calcularPeriodoOrbital(masaEstrella, distancia);
    double periodoAnios = periodo / (60 * 60 * 24 * 365.25);

    std::cout << "La velocidad orbital del planeta es: " << velocidad << " m/s" << std::endl;
    std::cout << "El periodo orbital del planeta es: " << periodo << " segundos (" << periodoAnios << " años terrestres)" << std::endl;

    

    return 0;
}
