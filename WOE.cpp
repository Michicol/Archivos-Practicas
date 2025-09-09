//#include <pybind11/pybind11.h>
//#include <pybind11/stl.h>
#include <iostream>
#include <array>
#include <random>
#include <ctime>
//#include <Eigen/Dense>

using namespace std;
//using Eigen::MatrixXd;

default_random_engine engine(static_cast<unsigned int>(time(0)));
normal_distribution<double> dist(0,1);

int main() {
    const size_t filas{4};
    const size_t Columnas{16};
    array<array<double,Columnas>,filas> X = {};
    array<array<double,filas>,Columnas> XTrans = {};
    array<array<double,filas>,filas> W = {};

    //Se crea la matriz X con entradas aleatorias
    for (int i=0; i < filas;++i){
        for (int j = 0; j < Columnas;++j){
            X[i][j] = dist(engine); //distribución normal
        }
    }

    //Ciclo para transponer la matriz
    for (int j=0; j < Columnas; ++j){
        for (int i=0; i < filas; ++i){
            XTrans[j][i] = X[i][j];
        }
    }

    //Construcción de la matriz de wishart
    for (int i=0; i < filas; ++i){
        for (int j=0; j < filas; ++j){
            for (int k=0; k < Columnas;++k){
                W[i][j] += X[i][k] * XTrans[k][i];
            }
        }
    }
}