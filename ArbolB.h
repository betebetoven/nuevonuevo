//
// Created by Alberto on 22/09/2022.
//

#ifndef F1_ARBOLB_H
#define F1_ARBOLB_H
#include <algorithm>

#include "NodoB.h"

template<typename T>
class ArbolB {
public:
    int orden_arbol = 5;
    NodoB<T> *raiz;

    ArbolB() {
        raiz = NULL;
    }
    void insertar(T id);
    pair<NodoB<T>*, pair<bool, bool>> insertarCrearRama(NodoB<T>* nodo, NodoB<T>* rama);
    NodoB<T>* dividir(NodoB<T>* rama);
    pair<NodoB<T>*, bool>  insertarEnRama(NodoB<T>* primero, NodoB<T>* nuevo);
    bool esHoja(NodoB<T>* primero);
    int contador(NodoB<T>* primero);
    string Grafo();
    string GrafoArbolAbb(NodoB<T>*rama);
    string GrafoRamas(NodoB<T>*rama);
    string GrafoConexionRamas(NodoB<T>*rama);
private:

};

#endif //F1_ARBOLB_H

