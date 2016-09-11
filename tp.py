from config import *
import googlemaps
import shelve
gmaps=googlemaps.Client(key = "AIzaSyDEt-2dtjvfTd9Y88QvzydDeQk7swAHmJ4")




trayectos = []
def agregarTrayecto(desde,hasta): # crea trayecto a partir de dos ciudades, si no hay trayecto tira error
                                  # si origen y destino son iguales tira error
    if desde != hasta:
        print("agregados exitosamente")
        ruta1 = gmaps.distance_matrix(desde, hasta) # esto es la ruta entre los dos puntos
        if ruta1 != '':
            print (ruta1)
            trayectos.append(ruta1)
            
            
        else:
            raise Error('no existe ruta entre los dos puntos') #si ruta 1 es null tira excepcion
    else:
        raise Error('Origen y destinos iguales')

#def agregarCiudadFinalTrayecto(desde, ciudad):

#def agregarCiudadIntermediaTrayecto(trayecto, ciudad):

#def concatenarDosTrayectos(trayecto1, trayecto2):
   # if trayecto1 != trayecto2:

#def compararTrayectos(trayecto1, trayecto2):
   # if trayecto1 == trayecto2:
   #     print ('Trayectos iguales')
   # else:

def mostrarTrayecto(desde, hasta):
    trayecto = agregarTrayecto(desde, hasta)
    d1 = trayecto['rows'][0]['elements'][0]['distance']['value']
    t1 = trayecto['rows'][0]['elements'][0]['duration']['value']
    dias1=int(t1/24/60/60)
    t1=t1-dias1*24*60*60
    horas1=int(t1/60/60)
    t1=t1-horas1*60*60
    min1=int(t1/60)
     
    print("Nombre:", desde, hasta)
    print("Distancia ruta 1: {0:8.4f} km".format(d1/1000000))
    print("Tiempo estimado: {0:2d} dias, {1:2d} horas, {2:2d} min".format(dias1, horas1, min1))

#def mostrarRutas(trayecto):
          #forma en la que debe mostrar las rutas
          #<origen 1> - <destino 1>
          #<distancia en km> km
          #<dias> días, <horas> hs
          #<línea en blanco>
          #<destino 1> - <destino 2>
          #<distancia en km> km
          #<dias> días, <horas> hs

#def listarTrayectos(archivo):

def almacenarDisco(trayecto):
    if trayecto == null:
        for x in trayectos:
            s = shelve.open('drows.db')
            try:
                s = x
            finally:
                s.close()
    else:
        s = shelve.open('drows.db')
        try:
            s = trayecto
        finally:
            s.close()
            
    

#def recuperarDeDisco(archivo):

#Recupera el archivo guardado en disco

#def salirDelSistema():
          #cierra archivos y guarda trayectos en memoria

          


    
        
