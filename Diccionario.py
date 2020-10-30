
{"nombre"='Jose', "apellido"=Diez, "edad"=31, "telefono"=636041446}

#keys = dict.keys()



    # dict ()
    # Recibe como parámetro una representación de un diccionario y si es factible, devuelve un diccionario de datos.
    # dic =  dict(nombre='nestor', apellido='Plasencia', edad=22)
    # dic → {‘nombre’ : 'nestor', ‘apellido’ : 'Plasencia', ‘edad’ : 22}

    # items()
    # Devuelve una lista de tuplas, cada tupla se compone de dos elementos: el primero será la clave y el segundo, su valor.
    # items = dic.items()

    # keys()
    #Retorna una lista de elementos, los cuales serán las claves de nuestro diccionario.
    # keys= dic.keys()

    # values()
    # Retorna una lista de elementos, que serán los valores de nuestro diccionario.
    # values= dic.values()

    # clear()
    # Elimina todos los ítems del diccionario dejándolo vacío.
    # dic1.clean()

    # copy()
    # Retorna una copia del diccionario original.
    # dic1 = dic.copy()

    # fromkeys()
    # Recibe como parámetros un iterable y un valor, devolviendo un diccionario que contiene como claves los elementos del iterable con el mismo valor ingresado. Si el valor no es ingresado, devolverá none para todas las claves.
    # dic = dict.fromkeys(['a','b','c','d'],1)

    # get()
    # Recibe como parámetro una clave, devuelve el valor de la clave. Si no lo encuentra, devuelve un objeto none.
    # valor = dic.get(‘b’) 

    # pop()
    # Recibe como parámetro una clave, elimina esta y devuelve su valor. Si no lo encuentra, devuelve error.
    # valor = dic.pop(‘b’) 

    # setdefault()
    # Funciona de dos formas. En la primera como get
    # valor = dic.setdefault(‘a’)

    # Y en la segunda forma, nos sirve para agregar un nuevo elemento a nuestro diccionario.

    # dic = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
    # valor = dic.setdefault(‘e’,5)
    # dic → {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4 , ‘e’ : 5}

    # update()
    # Recibe como parámetro otro diccionario. Si se tienen claves iguales, actualiza el valor de la clave repetida; si no hay claves iguales, este par clave-valor es agregado al diccionario.

    # dic 1 = {‘a’ : 1, ’b’ : 2, ‘c’ : 3 , ‘d’ : 4}
    # dic 2 = {‘c’ : 6, ’b’ : 5, ‘e’ : 9 , ‘f’ : 10}
    # dic1.update(dic 2)

    # dic 1 → {‘a’ : 1, ’b’ : 5, ‘c’ : 6 , ‘d’ : 4 , ‘e’ : 9 , ‘f’ : 10}
