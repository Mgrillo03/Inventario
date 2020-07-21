import pandas as pd
import numpy as np
import os 
##Funciones Del Proyecto
def cargar_cambios():
    ##Hace un pull de github y carga los posibles cambios del inventario en elDataFrame
    ## Leer inventario en dataFrame
    os.system('git pull origin master')
    df = pd.read_csv('stock_general.csv')

def commit_cambios(mensage = 'Commit sin mensaje'):
    """ 
    Hace un git commit con los cambios del programa
    mensaje string con el mensaje del commit
    regresa print con el estado
    """
    clear()
    desicion = input('Seguro que desea guardar los cambios?[y/n]  ')
    clear()
    if desicion.upper() == 'Y':
        os.system('git pull origin master')
        ##Aqui habria que escribir el csv para subirlo actualizado
        os.system(f'git commit -am "{mensage}"')
        os.system('git push origin master')
        os.system('git status')
        input('Pulsa enter para continuar')
    else: 
        input('Otro dia sera...')    
def clear():
    os.system('cls')
def convertir_int(df,rango):
    """
    Funcion  para convertir en integer columnas de un data frame
    df dataFrame  rango range
    retorna dataFrame con numeros en integer
    """
    for i in rango:
        df.iloc[:,i] = df.iloc[:,i].apply(int)

    return df
def salir(df):
    """
    MENU de preguntas y respuestas para salir del programa
    df el DataFrame con la data - Lee las entradas del usuario
    Termina el programa si se cumplen las condiondes o regresa al menu
    """
    clear()
    print('Esta a punto de salir, Seguro que desea hacerlo')
    a = input('[y/n] ')
    a = a.capitalize()
    if a == 'Y':
        clear()
        print('SEGUROOOOOO?? ASEGURATE BIEN')
        a = input('[y/n] ')
        a = a.capitalize()
        if a == 'Y':
            clear()
            print('Bueno, esta bien.')
            print('Chaitooo')
            input()
            clear()
        else:
            menu(df)
    else:
        menu(df)
def imprimir_lista(lista):
    """
    Imprime una lista elemento por elemento
    lista es una lista
    regresa impresion en la pantalla
    """
    for element in lista:
        print(f'{lista.index(element)+1}-  {element}')
def opciones(a):
    """ 
    Imprime en pantalla todas las opciones que puede realizar el menu
    Se pueden mostrar diferentes opciones dependiendo del argumento
    a integer entre 0 y 1 dependiendo de las opciones
    retorna integer con la respuesta del usuario (falta filtrar opciones incorrectas)
    """
    clear()
    if a == 0:
        print('Escoge una opcion')
        print('1- Ver Stock')
        print('2- Cambiar Stock')
        print('3- Guardar Cambios')
        print('4- Salir')
        return int(input('Opcion(1,2,3,4): '))
    if a == 1:
        print('1- Ver otro articulo')
        print('2- Volver al menu')
        return int(input('Opcion(1,2): '))   
def lista_articulos(df,pos):
    """ 
    Recibe un data frame y devuelve una lista con los articulos sin duplicados
    df dataFarem,  pos integer con la columna a modificar
    reresa lista - lista de strings
    """
    lista = df.iloc[:,pos]
    lista = lista.drop_duplicates()
    return list(lista)
def ver_inventario(df):
    """
    Realiza el procedimiento de la opcion ver inventario
    df dataFrame
    regresa vista en pantalla del inventario
    """
    clear()
    lista = lista_articulos(df,0)
    print ('Seleccione el articulo que desea ver ')
    imprimir_lista(lista)
    opcion = int(input('Opcion: '))
    opcion -= 1
    clear()
    print(df[df.iloc[:,0] == lista[opcion]])
    print('Oprima enter para continuar')
    input()
    opcion = opciones(1)
    if opcion == 1:
        ver_inventario(df)
    if opcion == 2:
        menu(df)
def modificar_inventario(df):
    """
    Funcion para modificar un data frame con los datos que ingrese el usuario
    recibe df dataFrame con los datos
    regresa df_m dataFrame modificado
    """
    clear()
    lista_art = lista_articulos(df,0)
    ##SELECCION ARTICULO
    print("Seleccione el articulo que desea modificar :")
    imprimir_lista(lista_art)
    opcion_art = int(input("Opcion: "))
    opcion_art -= 1
    clear()
    df_2 = df[df.iloc[:,0] == lista_art[opcion_art]]
    df_2 = df_2.reset_index()
    print(df.iloc[0,0])
    print(df_2.iloc[:,1:])
    print("Seleccione el Color: ")
    opcion_color = int(input('Color : '))

    cond = True
    while cond : 
        clear()
        df_2 = df[df.iloc[:,0] == lista_art[opcion_art]]
        df_2 = df_2.reset_index()
        print('Seleccione el talle a cambiar')
        print(df_2.iloc[opcion_color])
        talle = input('Talle: ')
        if talle in df_2.columns:
            fila = df[(df.iloc[:,0] == lista_art[opcion_art]) & (df.iloc[:,1] == df_2.iloc[opcion_color,2])].index
            df.loc[fila[0],talle] = int(input('Indique nuevo valor : '))
            clear()
            print('GENIAALL!!! TU STOCK FUE ACTUALIZADO CON EXITO...') 
            print() 
            print()
            print(df.loc[fila[0],:])
            print() 
            resp = input('Desea Modificar Otro talle?[y/n]   ')
            resp = resp.capitalize()
            if resp == 'N':
                cond = False
        else: 
            clear()
            print('Escribe bien el talle menor')
            input()

    
    return df
def menu(df):
    """
    Funcion para crear un menu para navegar facilmente dentro  del stock
    data frame 
    retorna impresiones en pantalla
    """
    clear()
    opcion = opciones(0)
    if opcion == 1:
        ver_inventario(df)
    elif opcion == 2:
        df = modificar_inventario(df)
        menu(df)
    elif opcion == 3:
        clear()
        mensaje = input('ingrese el mensaje del commit:  ')
        commit_cambios(mensage = mensaje)
        menu(df)
    else: 
        salir(df)

if __name__ == "__main__":
        
    ## Cuperpo del programa
    ##Leer data
    stock_zapatos = pd.read_csv('stock_zapatos.csv')
    stock_general = pd.read_csv('stock_general.csv')
    ## Eliminar todos los NaN
    stock_general = stock_general.fillna(0)
    stock_zapatos = stock_zapatos.fillna(0)

    stock_general = convertir_int(stock_general,range(2,8))


    #print(stock_general)
    menu(stock_general)