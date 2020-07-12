import pandas as pd
import os 
##Funciones
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
        print('3- Salir')
        return int(input('Opcion(1,2,3): '))
    if a == 1:
        print('1- Ver otro articulo')
        print('2- Volver al menu')
        return int(input('Opcion(1,2): '))
    
def ver_inventario(df):
    """
    Realiza el procedimiento de la opcion ver inventario
    df dataFrame
    """
    clear()
    lista = df.iloc[:,0]
    lista = lista.drop_duplicates()
    lista = list(lista)
    print ('Seleccione el articulo que desea ver ')
    imprimir_lista(lista)
    opcion = int(input('Opcion: '))
    opcion -= 1
    clear()
    print(df[df.iloc[:,0] == lista[opcion]])
    print('Oprima enter tecla para continuar')
    input()
    opcion = opciones(1)
    if opcion == 1:
        ver_inventario(df)
    if opcion == 2:
        menu(df)

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
    elif opcion == 3:
        clear()
        print('Esta a punto de salir, Seguro que desea hacerlo')
        a = input('[y/n] ')
        if a == 'y':
            clear()
            print('SEGUROOOOOO??')
            a = input('[y/n] ')
            if a == 'y':
                clear()
                print('Bueno, esta bien.')
                print('Chaitooo')
            else:
                menu(df)
        else:
            menu(df)

##Leer data
stock_zapatos = pd.read_csv('stock_zapatos.csv')
stock_general = pd.read_csv('stock_general.csv')
## Eliminar todos los NaN
stock_general = stock_general.fillna(0)
stock_zapatos = stock_zapatos.fillna(0)

stock_general = convertir_int(stock_general,range(2,8))


#print(stock_general)
menu(stock_general)