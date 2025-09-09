#include <pybind11/pybind11.h>
#include <pybind11/stl.h>
#include <vector>
#include <random>
#include <ctime>

namespace py = pybind11;
using namespace std;

// Función para calcular la matriz de Wishart con vectores anidados
vector<vector<double>> calcular_wishart_flexible(int filas, int columnas) {
    default_random_engine engine(static_cast<unsigned int>(time(0)));
    normal_distribution<double> dist(0, 1);
    
    // Crear matriz X con valores aleatorios
    vector<vector<double>> X(filas, vector<double>(columnas));
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < columnas; ++j) {
            X[i][j] = dist(engine);
        }
    }
    
    // Calcular X * X^T (matriz de Wishart)
    vector<vector<double>> W(filas, vector<double>(filas, 0.0));
    
    for (int i = 0; i < filas; ++i) {
        for (int j = 0; j < filas; ++j) {
            for (int k = 0; k < columnas; ++k) {
                W[i][j] += X[i][k] * X[j][k]; // X[j][k] es el elemento de X^T
            }
        }
    }
    
    return W;
}

PYBIND11_MODULE(wishart_module, m) {
    m.doc() = "Módulo flexible para cálculo de matrices de Wishart";
    
    m.def("calcular_wishart", &calcular_wishart_flexible,
          "Calcula la matriz de Wishart para dimensiones especificadas",
          py::arg("filas"), py::arg("columnas"));
}