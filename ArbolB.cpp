#include "ArbolB.h"
#include "json/json.h"
//#include <windows.h>
#include <fstream>
#include <string>
#include <sstream>
#include <iostream>
template<typename T>
void ArbolB<T>::insertar(T id) {
    NodoB<T>* nodo = new NodoB<T>(id);
    if (raiz == NULL) {
        raiz = nodo;
    } else {
        pair < NodoB<T>*, pair<bool, bool>> ret = insertarCrearRama(nodo, raiz);
        NodoB<T>* obj = ret.first;
        if ((ret.second.first or ret.second.second) and obj != NULL) {//si se divide la rama o se inserta al inicio, la raiz cambia
            cout << "se cambia de rama principal ID:" << obj->id << "\n";
            raiz = obj;
        }
    }
}

/**
 * Metodo recorre el arbol e inserta los valores nuevos, verifica si es necesario dividir ramas
 *
 * @param NodoB* nodo es el nodo a insertar
 * @param NodoB* rama es la rama en la cual se inicia la busqueda de la posicion donde insertarlo
 *
 * @retun retorna un listado de elementos que nos permiten identificar lo siguiente:
 *
 * NodoB*: nodo inicial de la rama donde se inserto un elemento
 *
 * bool: true or false indicando si una rama se dividio en dos nuevas
 *
 * bool: true or false indicando si el inicio de la rama cambio debio a un insert al inicio.
 */
template<typename T>
pair<NodoB<T>*, pair<bool, bool>> ArbolB<T>::insertarCrearRama(NodoB<T>* nodo, NodoB<T>* rama) {
    pair < NodoB<T>*, pair<bool, bool>> ResultadoRama;
    ResultadoRama.first = NULL; //nodo Inicial de la rama
    ResultadoRama.second.first = false; //indica si se dividio la rama
    ResultadoRama.second.second = false; //indica si se modifica el inicio de la rama
    if (esHoja(rama)) {//si el nodo es hoja se inseta directamente dentro de ella
        pair < NodoB<T>*, bool> resultado = insertarEnRama(rama, nodo); //insertamos el nuevo elemento dentro de la rama actual
        ResultadoRama.first = resultado.first; //posee la rama con el valor ya insertado
        ResultadoRama.second.second = resultado.second; //posee el resultado de si se modifico el inicio en el insert anterior
        if (contador(resultado.first) == orden_arbol) {//si la rama posee mas elementos de los permitidos se divide
            cout << "La rama debe dividirse\n";
            ResultadoRama.first = dividir(resultado.first); //dividimos la rama y obtenemos una nueva rama con sus respectivos apuntadores
            ResultadoRama.second.first = true; //identificar que la rama se dividio
        }
    } else {//si el nodo es rama se debe buscar la posicion donde insertarlo
        NodoB<T>*temp = rama;
        do {
            if (nodo->value["nick"].asString() == temp->value["nick"].asString()) {//valor ya insertado, no se permiten repeditos
                cout << "insertarCrearRama(), El ID " << nodo->value["nick"].asString() << " ya existe\n";//donde dice value.nombre cabiar a las instancias del JSON:value
                return ResultadoRama;
            } else if (nodo->id < temp->id) {
                pair < NodoB<T>*, pair<bool, bool>> ResultadoInsert = insertarCrearRama(nodo, temp->izquierda);
                if (ResultadoInsert.second.second and ResultadoInsert.first != NULL) {//si se modifico el inicio de la rama
                    ResultadoRama.second.second = true;
                    temp->izquierda = ResultadoInsert.first;
                }
                if (ResultadoInsert.second.first) {//se dividio la subrama
                    pair < NodoB<T>*, bool> auxInsert = insertarEnRama(rama, ResultadoInsert.first);
                    rama = auxInsert.first;
                    if (auxInsert.second) {
                        ResultadoRama.first = rama;
                    }
                    if (contador(rama) == orden_arbol) {
                        ResultadoRama.first = dividir(rama);
                        ResultadoRama.second.first = true;
                    }
                }
                return ResultadoRama;
            } else if (temp->siguiente == NULL) {
                pair < NodoB<T>*, pair<bool, bool>> ResultadoInsert = insertarCrearRama(nodo, temp->derecha);
                if (ResultadoInsert.second.second and ResultadoInsert.first != NULL) {//si se modifico el inicio de la rama
                    ResultadoRama.second.second = true;
                    temp->derecha = ResultadoInsert.first;
                }
                if (ResultadoInsert.second.first) {//se dividio la subrama
                    pair < NodoB<T>*, bool> auxInsert = insertarEnRama(rama, ResultadoInsert.first);
                    rama = auxInsert.first;
                    if (auxInsert.second) {
                        ResultadoRama.first = rama;
                    }
                    if (contador(rama) == orden_arbol) {
                        ResultadoRama.first = dividir(rama);
                        ResultadoRama.second.first = true;
                    }
                }
                return ResultadoRama;
            }
            temp = temp->siguiente;
        } while (temp != NULL);
    }
    return ResultadoRama;
}

template<typename  T>
NodoB<T>* ArbolB<T>::dividir(NodoB<T>* rama) {
    //int val = -999;
    //T val = T("nulo");
    T val;
    //val.id = -999;
    NodoB<T>*temp = NULL;
    NodoB<T>*Nuevito = NULL;
    NodoB<T>*aux = rama;

    NodoB<T>*rderecha = NULL;
    NodoB<T>*rizquierda = NULL;

    int cont = 0;
    while (aux != NULL) {
        cont++;
        //implementacion para dividir unicamente ramas de 4 nodos
        if (cont < 3) {
            //val = aux->id;
            val = aux->value;
            temp = new NodoB<T>(val);
            temp->izquierda = aux->izquierda;
            if (cont == 2) {
                temp->derecha = aux->siguiente->izquierda;
            } else {
                temp->derecha = aux->derecha;
            }
            rizquierda = insertarEnRama(rizquierda, temp).first;
        } else if (cont == 3) {
            val = aux->value;
            Nuevito = new NodoB<T>(val);
        } else {
            val = aux->value;
            temp = new NodoB<T>(val);
            temp->izquierda = aux->izquierda;
            temp->derecha = aux->derecha;
            rderecha = insertarEnRama(rderecha, temp).first;
        }
        aux = aux->siguiente;
    }
    Nuevito->derecha = rderecha;
    Nuevito->izquierda = rizquierda;
    return Nuevito;
}
template <typename T>
pair<NodoB<T>*, bool> ArbolB<T>::insertarEnRama(NodoB<T>* primero, NodoB<T>* nuevo) {
    pair < NodoB<T>*, bool> ret;
    ret.second = false;
    if (primero == NULL) {
        //primero en la lista
        ret.second = true;
        primero = nuevo;
    } else {
        //recorrer e insertar
        NodoB<T>* aux = primero;
        while (aux != NULL) {
            if (aux->value["nick"].asString() == nuevo->value["nick"].asString()) {//------------->ya existe en el arbol//VALIDAR ESTA IGUALDAD DE LA CHINGADA
                cout << "insertarEnRama(), El ID " << nuevo->id << " ya existe\n";
                break;
            } else {
                if (aux->id > nuevo->id) {
                    if (aux == primero) {//------------->insertar al inicio
                        aux->anterior = nuevo;
                        nuevo->siguiente = aux;
                        //ramas del nodo
                        aux->izquierda = nuevo->derecha;
                        nuevo->derecha = NULL;
                        ret.second = true;
                        primero = nuevo;
                        break;
                    } else {//------------->insertar en medio;
                        nuevo->siguiente = aux;
                        //ramas del nodo
                        aux->izquierda = nuevo->derecha;
                        nuevo->derecha = NULL;

                        nuevo->anterior = aux->anterior;
                        aux->anterior->siguiente = nuevo;
                        aux->anterior = nuevo;
                        break;
                    }
                } else if (aux->siguiente == NULL) {//------------->insertar al final
                    aux->siguiente = nuevo;
                    nuevo->anterior = aux;
                    break;
                }
            }
            aux = aux->siguiente;
        }

    }
    ret.first = primero;

    return ret;
}

/*
 * Metodo para verificar si es hoja
 * Un nodo hoja no pose apuntadores a otros nodos hacia izquierda o derecha
 */
template<typename T>
bool ArbolB<T>::esHoja(NodoB<T>* primero) {
    NodoB<T>* aux = primero;
    while (aux != NULL) {
        cout << "[" << aux->id << "]->";
        if (aux->izquierda != NULL or aux->derecha != NULL) {
            return false;
        }
        aux = aux->siguiente;
    }
    cout << "Null\n";
    return true;
}

/*Metodo para contar los elementos de una rama*/
template <typename T>
int ArbolB<T>::contador(NodoB<T>* primero) {
    int contador = 0;
    NodoB<T>* aux = primero;
    while (aux != NULL) {
        contador++;
        aux = aux->siguiente;
    }
    return contador;
}

//================================Grafo solo del arbol b=====================
template <typename T>
string ArbolB<T>::Grafo() {
    string dotFull = "";
    //escribir dot

    dotFull += "digraph G {\n";
    dotFull += "node[shape=record]\n";
    dotFull += "\t\t//Agregar Nodos Rama\n";
    dotFull += GrafoArbolAbb(raiz);
    //agregar conexiones de ramas
    dotFull += "\t\t//Agregar conexiones\n";
    dotFull += GrafoConexionRamas(raiz);

    dotFull += "}";

    //------->escribir archivo
    cout << dotFull << "\n";
    /*ofstream file;
    file.open("Pruebas.dot");
    file << dotFull;
    file.close();

    //------->generar png
    system(("dot -Tpng Pruebas.dot -o  Pruebas.png"));

    //------>abrir archivo
    system(("Pruebas.png"));*/
    return dotFull;

}
template <typename T>
string ArbolB<T>::GrafoArbolAbb(NodoB<T>* rama) {
    string dot = "";
    if (rama != NULL) {
        //agrear rama actual
        dot += GrafoRamas(rama);
        //agregar las ramas siguientes recursivamente
        NodoB<T>*aux = rama;
        while (aux != NULL) {
            if (aux->izquierda != NULL) {
                dot += GrafoArbolAbb(aux->izquierda);
            }
            if (aux->siguiente == NULL) {
                if (aux->derecha != NULL) {
                    dot += GrafoArbolAbb(aux->derecha);
                }
            }
            aux = aux->siguiente;
        }
    }
    return dot;
}
template<typename T>
string ArbolB<T>::GrafoRamas(NodoB<T>*rama) {
    string dot = "";
    stringstream auxTXT;
    if (rama != NULL) {
        //============================================agregar rama=================================
        NodoB<T>*aux = rama;
        auxTXT.str("");
        auxTXT << rama;
        dot = dot + "R" + auxTXT.str() + "[label=\"";
        int r = 1;
        while (aux != NULL) {
            if (aux->izquierda != NULL) {
                dot = dot + "<C" + to_string(r) + ">|";
                r++;
            }
            if (aux->siguiente != NULL) {
                dot = dot + to_string(aux->id) +" \n "+ aux->value["nick"].asString() + "|";//ACA HUBO CAMBIO---------------------------------------------------------------------------
            } else {
                dot = dot + to_string(aux->id)+" \n "+ aux->value["nick"].asString();//ACA TAMBIEEEEEN HUBO CAMBIOOOOOOOO-------------------------------------------------------------------------------
                if (aux->derecha != NULL) {
                    dot = dot + "|<C" + to_string(r) + ">";
                }
            }
            aux = aux->siguiente;
        }
        dot = dot + "\"];\n";
    }
    return dot;
}
template<typename T>
string ArbolB<T>::GrafoConexionRamas(NodoB<T>*rama) {
    string dot = "";
    stringstream auxTXT;
    if (rama != NULL) {
        //============================================agregar rama=================================
        NodoB<T>*aux = rama;
        auxTXT << rama;
        string actual = "R" + auxTXT.str();
        int r = 1;
        while (aux != NULL) {
            if (aux->izquierda != NULL) {
                auxTXT.str("");
                auxTXT << aux->izquierda;
                dot += actual + ":C" + to_string(r) + "->" + "R" + auxTXT.str() + ";\n";
                r++;
                dot += GrafoConexionRamas(aux->izquierda);
            }
            if (aux->siguiente == NULL) {
                if (aux->derecha != NULL) {
                    auxTXT.str("");
                    auxTXT << aux->derecha;
                    dot += actual + ":C" + to_string(r) + "->" + "R" + auxTXT.str() + ";\n";
                    r++;
                    dot += GrafoConexionRamas(aux->derecha);
                }
            }
            aux = aux->siguiente;
        }
    }
    return dot;

}

template class NodoB<Json::Value>;
template class ArbolB<Json::Value>;//
// Created by Alberto on 22/09/2022.
//

