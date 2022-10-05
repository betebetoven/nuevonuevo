//
// Created by Alberto on 22/09/2022.
//

#ifndef F1_NODOB_H
#define F1_NODOB_H
#include <stddef.h>
#include<fstream>

#include <iostream>
#include <sstream>

using namespace std;
template<typename T>
class NodoB {
public:
    int id;
    T value;
    //Apuntadores dentro de la rama
    NodoB* siguiente;
    NodoB* anterior;

    //apuntadores al inicio de otra rama
    NodoB* derecha;
    NodoB* izquierda;
    int shor_dir(NodoB<T> *cpp)
    {
        ostringstream get_the_address;
        get_the_address << cpp;
        string address =  get_the_address.str();
        string nuevo = "";
        for (int i = 6; i<address.length();i++) {
            nuevo+= address[i];
        }
        //cout << address << "\n";// 6
        //cout << nuevo << "\n";// 6
        int i;
        sscanf(nuevo.c_str(), "%x", &i);

        return  i;
    }

    NodoB(T valor) {

        id = shor_dir(this);
        value = valor;
        siguiente = NULL;
        anterior = NULL;
        derecha = NULL;
        izquierda = NULL;
    }
private:

};
#endif //F1_NODOB_H

