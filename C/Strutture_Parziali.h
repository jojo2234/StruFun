#ifndef SHELL_H_INCLUDED
#define SHELL_H_INCLUDED

typedef struct node{
    char * dato;
    struct node *next;
}nodo;

typedef struct{
    nodo first;
    nodo n;
    int size;
}pila;

typedef struct{
    nodo first;
    nodo temp;
    nodo prec;
    int size;
}lista;

nodo insertNodo(nodo nd,char *ob){
    nd.dato = ob;
    nd.next = NULL;
    return nd;
}
nodo nextNodo(nodo nd, char *ob, nodo n){
    nd.dato = ob;
    nd.next = &n;
    return nd;
}

pila createPila(char *obj, pila stack){
    stack.first.next = NULL;
    stack.n = insertNodo(stack.n,obj);
    stack.size += 1;
    return stack;
}

pila push(char *obj, pila stack){
    stack.first = stack.n;
    stack.n = insertNodo(stack.n,obj);
    //stack.n.next = &stack.first;
    stack.size += 1;
    return stack;
}

#endif