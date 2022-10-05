// Linked List CPP 
#pragma once
#include "List.h"
#include<iostream>

using namespace std;
//HOla mundo desde vscode
template <typename T>
class Node
{
public:
    
    T data;
    Node<T> *next;
    Node<T> *Prev;
    Node<T> *derecha;
    Node<T> *inventario;
    Node<T> *movimientos;
    
};
