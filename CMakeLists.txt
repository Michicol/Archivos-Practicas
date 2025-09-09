cmake_minimum_required(VERSION 3.12)
project(wishart_module)

# Configuración básica
set(CMAKE_CXX_STANDARD 14)
set(CMAKE_CXX_STANDARD_REQUIRED ON)

# Encontrar pybind11
find_package(pybind11 REQUIRED)

# Crear el módulo de Python
pybind11_add_module(wishart_module WOEpybind.cpp)