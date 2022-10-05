#include "./glove/glovehttpserver.hpp"
#include "json/json.h"
#include <iostream>
#include<fstream>
#include <chrono>
#include <thread>
#include <string>
#include <vector>
#include <vector>  
#include <sstream> 
#include "./glove/json.hpp"
#include "codigo/ListaSimple.cpp"
#include "List.h"
#include "nodo.h"
#include "ArbolB.h"
//HOOLAAA SI FUNCIONA ESTA MAMADAAAAAAAAAAA
List <Json::Value>usuarios_glob;
    List <Json::Value>articulos_glob;
    List <Json::Value>movimientos_glob;
    List <Json::Value>categoria;
    List<Json::Value>tut_global;
    ArbolB<Json::Value> usuariosB_glob;
   Node<Json::Value> *cuenta;
int atoi(std::string s)
{
    try
    {
        return std::stod(s);
    }
    catch (std::exception &e)
    {
        return 0;
    }
}

static std::string jsonkv(std::string k, std::string v)
{
    /* "k": "v" */
    return "\"" + k + "\": \"" + v + "\"";
}

Node<Json::Value> *login(List<Json::Value> usuarioh, string nombre, string contrasena)
{
     cout << "Estas dentro de la funcion de LOGIN :"<< endl;
    Node<Json::Value> *ahora;


            for(ahora = usuarioh.head; ahora != NULL; ahora=ahora->next)
            {
                cout << ahora->data << " \n";
                if (ahora->data["nick"].asString() == nombre && ahora->data["password"].asString()== contrasena)
                 {cout << "enconttro a betebetoven"<< endl;
                 return ahora;
                 break;
                 }
 
                
            }
            return new Node<Json::Value>;
            
} 


void eliminar_cuenta(Node<Json::Value> *cuenta_eliminar)
{
    Json::Value prueba;
    if (cuenta_eliminar->Prev != NULL)
    cuenta_eliminar->Prev->next = cuenta_eliminar->next;
    else
    usuarios_glob.head = cuenta_eliminar->next;
    if (cuenta_eliminar->next != NULL)
    cuenta_eliminar->next->Prev = cuenta_eliminar->Prev;
    cuenta_eliminar = NULL;
    cuenta = new Node<Json::Value>;

    

}

void anadir_usuario()
{   
    string nick;
    string password;
    string edad;
    cout <<"Ingrese UserName: \n"<< endl;
    cin >> nick;
cout <<"Ingrese contrasena: \n"<< endl;
cin >> password;
cout <<"Ingrese Edad: \n"<< endl;
cin >> edad;
    string jeson = "{\"nick\":\""+nick+"\",\"password\":\""+password+"\",\"monedas\":\"0\",\"edad\":\""+edad+"\"}";
    Json::Value actualJson;
    Json::Reader reader;
    reader.parse(jeson,actualJson);
    usuarios_glob.insert(actualJson);
    cout <<"Usuario Registrado: \n" <<actualJson<< endl;

}

void va(Node <Json::Value> *root, Json::Value entrada)
{
    if(root==NULL)
    {
    string jeson = "{\"categoria\": \""+entrada["categoria"].asString()+"\"}";
    Json::Value actualJson;
    Json::Reader reader;
    reader.parse(jeson,actualJson);
    categoria.insert(actualJson);
    }
    else 
    if (root->data["categoria"].asString()!=entrada["categoria"].asString() && root-> next != NULL)
    va(root->next, entrada);
    else 
    if (root->data["categoria"].asString()!=entrada["categoria"].asString() && root-> next == NULL)
    {
        string jeson = "{\"categoria\": \""+entrada["categoria"].asString()+"\"}";
        Json::Value actualJson;
        Json::Reader reader;
        reader.parse(jeson,actualJson);
        categoria.insert(actualJson);
        return;
        /* code */
    }
    else 
    return;
    
    
    
}

void llenaderecha(Node<Json::Value> *n,Json::Value x)
{
    if (n->derecha == NULL)
    {
        Node<Json::Value> *nuevo = new Node<Json::Value>;
        nuevo -> data = x;
        nuevo -> derecha = NULL;
        n->derecha = nuevo;

    }
    else
    {
        llenaderecha(n->derecha,x);
    }
}

void imprimederecha(Node<Json::Value> *n)
{
    cout << n->data;
    if (n->derecha != NULL)
        imprimederecha(n->derecha);

}


void categoria_constructor(Json::Value object)//aca entra el actualjson de carga masiva
{
    
    for (Json::Value objeto : object["articulos"])
        va(categoria.head,objeto);

    //ingresan todos los tipos de categorias sin repetirse


    Node<Json::Value> *cabecita = categoria.head;
    while (cabecita->next != NULL)
    {
        cabecita->derecha = NULL;
        cabecita = cabecita->next;
    }
    cabecita->derecha = NULL;
    //hacemos ingreso a la matriz rara esta de c++
    cabecita = categoria.head;
    while (cabecita != NULL)
    {
        for (Json::Value n : object["articulos"])
        {
            if (cabecita->data["categoria"].asString()==n["categoria"].asString())
            {
                Node<Json::Value> *primero = cabecita;
                llenaderecha(cabecita,n);
                cabecita = primero;
            }
        }
        cabecita = cabecita->next;
    }

    //MOSTRADO EN CONSOLA LA TIENDA DE CATEGORIAS
    cabecita = categoria.head;
    cout << "Tienda: "<<endl;
    while (cabecita != NULL)
    {   cout << "----------------------------"<<endl;
        imprimederecha(cabecita);
        cout << "----------------------------"<<endl;
        
        cabecita = cabecita->next;
    }

    
        

}


void carga_usuario(){
      ifstream file("example.json");//volve a cambair a f1_masiva
    //cout << "total json data: \n"<<file.<< endl;
    Json::Value actualJson;
    Json::Reader reader;
    Node<string> perez;
    perez.data = "hola mundio";


    reader.parse(file,actualJson);
    
    cout << perez.data<< endl;

    List <Json::Value>movimientos;

    for (Json::Value objeto : actualJson["usuarios"]) {
        usuarios_glob.insert(objeto);
        usuariosB_glob.insertar(objeto);
    }
    usuariosB_glob.Grafo();

    for (Json::Value objeto : actualJson["articulos"])
       articulos_glob.insert(objeto);
    categoria_constructor(actualJson);
    
    tut_global.insert(actualJson["tutorial"]);
    for (Json::Value objeto : actualJson["tutorial"]["movimientos"])
        tut_global.insert(objeto);
    
    

    cout << "USUARIOS---------------------------------"<< endl;
    usuarios_glob.display();
    cout << "TUTORIAL---------------------------------"<< endl;
    tut_global.display();
    

    





    
}

Json::Value dequeue_tutorial()
{
    Node<Json::Value> *n = tut_global.head;
    tut_global.head = tut_global.head->next;
    tut_global.tamano = tut_global.tamano-1;
    return n->data;
    
    


}

void mostrar_tutorial()
{
    //lo raro de esta funcion es que solo se puede realizar una sola vez
    cout << "DEQUEUE DE TUTORIAL: "<<endl;
    while (tut_global.tamano>=1)
    {
        cout << dequeue_tutorial()<<endl;
    }
    tut_global.display();
    
}

void split_str( std::string const &str, const char delim,  
        std::vector <std::string> &out )  
        {  
            // create a stream from the string  
            std::stringstream s(str);  
              
            std::string s2;  
            while (std:: getline (s, s2, delim) )  
            {  
                out.push_back(s2); // store the string in s2  
            }  
        }  




class Servidor
{
public:
    void get(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        response.contentType("text/json");
        if (request.special["Id"].empty())
            response << cuenta;
        else
        {
            response << "{ "
                     << jsonkv("status", "ok") << ",\n";
                     
        }
    }
    void post(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        std::string pedro = request.special["Id"];
        ofstream outdata;
        outdata.open("example.json");
        outdata << pedro;
         outdata.close();
        carga_usuario();
          response << "{ "
                 << jsonkv("status", "ok") << ",\n"
                 << jsonkv("Id_nuevo", request.special["Id"]) << " }";

    }
};
void hello(GloveHttpRequest &request, GloveHttpResponse& response)
{
  std::string pedro = request.special["Id"];
        ofstream outdata;
        outdata.open("example.json");
        outdata << pedro;
         outdata.close();
        carga_usuario();
        std::string salida = usuariosB_glob.Grafo();
          /*response << "{ "
                 << jsonkv("status", "ok") << ",\n"
                 << jsonkv("GRAPHVIZB", salida) << ",\n"
                 << jsonkv("Id_nuevo", request.special["Id"]) << " }";*/
                 response << salida;
}
void login_server(GloveHttpRequest &request, GloveHttpResponse& response)
{
  std::string pedro = request.special["Id"];
  const char delim = ','; 
  std::vector <std::string> out;
  split_str (pedro, delim, out); 
  std::string nombre = out[0];
  std::cout << nombre << std::endl;
  std::string password = out[1];
  std::cout << password << std::endl;
        cuenta = login(usuarios_glob,nombre,password);
        
          response << "{ "
                 << jsonkv("status", "ok") << ",\n"
                 << jsonkv("CUENTA", cuenta->data["nick"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["monedas"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["edad"].asString()) << " }";
}


void cambiar_nombre(GloveHttpRequest &request, GloveHttpResponse& response)
{
  std::string pedro = request.special["Id"];
        cuenta->data["nick"]=pedro;
          response << "{ "
                 << jsonkv("datos actualizados", "ok") << ",\n"
                 << jsonkv("CUENTA", cuenta->data["nick"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["password"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["monedas"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["edad"].asString()) << " }";
}
void cambiar_contrasena(GloveHttpRequest &request, GloveHttpResponse& response)
{
  std::string pedro = request.special["Id"];
        cuenta->data["password"]=pedro;
          response << "{ "
                 << jsonkv("datos actualizados", "ok") << ",\n"
                 << jsonkv("CUENTA", cuenta->data["nick"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["password"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["monedas"].asString()) << ",\n"
                 << jsonkv("CUENTA", cuenta->data["edad"].asString()) << " }";
}
void kill_switch(GloveHttpRequest &request, GloveHttpResponse& response)
{
  eliminar_cuenta(cuenta);
          response << "This is the response\n";
  response << "CUENTA ELIMINADA VUELVA A INGRESAR" << std::endl;
}






class Servidor2
{
public:
    void get(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        response.contentType("text/json");
        if (request.special["Id"].empty())
            response << cuenta->data.asString();
        else
        {
            response << "{ "
                     << jsonkv("status", "ok") << ",\n";
                     
        }
    }
    void post(GloveHttpRequest &request, GloveHttpResponse &response)
    {
        std::string pedro = request.special["Id"];
        cuenta = login(usuarios_glob,pedro,"jaja");
        
          response << "{ "
                 << jsonkv("status", "ok") << ",\n"
                 << jsonkv("CUENTA", cuenta->data.asString()) << " }";

    }
};

int main(int argc, char *argv[])
{
     
    Servidor cine;

    GloveHttpServer serv(8080, "", 2048);
    serv.compression("gzip, deflate");
    namespace ph = std::placeholders;
    serv.addRoute("/Lista/$Id", hello);
    serv.addRoute("/Login/$Id", login_server);
    serv.addRoute("/editN/$Id", cambiar_nombre);
    serv.addRoute("/editP/$Id", cambiar_contrasena);
    serv.addRoute("/KS/$Id", kill_switch);
    /*serv.addRest("/Lista/$Id", 1,
                 GloveHttpServer::jsonApiErrorCall,
                 std::bind(&Servidor::get, &cine, ph::_1, ph::_2),
                 std::bind(&Servidor::post, &cine, ph::_1, ph::_2));
    serv.addRest("/Login/$Id", 1,
                 GloveHttpServer::jsonApiErrorCall,
                 std::bind(&Servidor2::get, &cine, ph::_1, ph::_2),
                 std::bind(&Servidor2::post, &cine, ph::_1, ph::_2));*/




    std::cout << "Servidor en Ejecucion" << std::endl;
    while (1)
    {
        std::this_thread::sleep_for(std::chrono::seconds(1));
    }

    std::cout << "TEST" << std::endl;
}
