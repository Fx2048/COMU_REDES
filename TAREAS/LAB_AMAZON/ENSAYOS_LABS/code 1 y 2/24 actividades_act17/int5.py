def crear_topologia_estrella(centro,nodos):
    red ={}
    red[centro]=nodos.copy()
    for nodo in nodos:
        red[nodo]=[centro]
    return red
def crear_topologia_malla(nodos):
    red={}
    for nodo in nodos:
        red[nodo]=[n for n in nodos if n!=nodo]
    return red
def demostrar_topologias():
    nodos_estrella=["Nodo1","Nodo2","Nodo3", "Nodo4"]
    red_estrella=crear_topologia_estrella("Centro",nodos_estrella)
    print("Topologia en estrella",red_estrella)
    nodos_malla=["NodoA","NodoB","NodoC","NodoD"]
    red_malla=crear_topologia_malla(nodos_malla)
if __name__=="__main__":
    demostrar_topologias()
    
