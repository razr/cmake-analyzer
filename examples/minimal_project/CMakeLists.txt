cmake_minimum_required(VERSION 3.10)
project(MinimalExample LANGUAGES C CXX)

# Fix: request Python dev libraries
find_package(Python3 REQUIRED COMPONENTS Interpreter Development)
find_library(M_LIB m)

add_executable(main main.cpp)
target_link_libraries(main PRIVATE Python3::Python ${M_LIB})

