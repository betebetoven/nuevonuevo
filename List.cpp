// Linked List CPP 
#include "List.h"
//#include "nodo.h"
#include "json/json.h"
#include<iostream>
#include<string>

using namespace std;
//HOla mundo desde vscode
template<typename G>
 List<G>::List()
{
    tamano = 0;
    head = NULL;
    tail = NULL;
    j = "estoy vivo otra vez";
}
template<typename G>
bool List<G>::isEmpty()
    {
        return head == NULL;
    }


template<typename G>
void List<G>::insert(G x)
{
        temp = new Node<G>;
        temp->data = x;
        if(isEmpty())
        {
            temp->next = NULL;
            temp->Prev = NULL;
            head = temp;

        }
        else
        {
            Node<G> *ahora;
            ahora = head;
            while (ahora->next != NULL)
            {
                ahora = ahora->next;

            }
            ahora->next =temp;
            temp->Prev = ahora;
            temp-> next = NULL;
        }
        tamano= tamano+1;

          
    }


template<typename G>
    void List<G>::display()
    {
        if(!isEmpty())
        {
            for(temp = head; temp != NULL; temp=temp->next)
                cout << temp->data << " ";



            cout << endl;
        }
        else
        {
            cout << "LISTA VACIA" << endl;
        }
    }
    template class List<string>;
    template class Node<string>;
    template class List<Json::Value>;
    template class Node<Json::Value>;
    





