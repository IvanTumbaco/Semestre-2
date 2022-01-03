class deber:
    def ejercicio1(self):
        #Dados dos (2) números calcule la suma, resta, multiplicación, división y módulo
        num1 = int(input("Ingrese el numero 1: "))
        num2 = int(input("Ingrese el numero 2: "))
        suma = num1 + num2
        resta = num1 - num2 
        multiplicacion = num1 * num2
        division = num1 / num2
        modulo = num1 % num2
        print("La suma es: ",suma) 
        print("La resta es: ",resta) 
        print("La multiplicacion es: ",multiplicacion) 
        print("La division es: ",division) 
        print("El modulo es: ",modulo) 

    def ejercicio2(self):
        import math
        #Dados tres (3) números, Hacer una aplicación que calcule la resolvente.
        a = int(input("Ingrese el numero 1: "))
        b = int(input("Ingrese el numero 2: "))
        c = int(input("Ingrese el numero 3: "))
        x= ((b**2)-4*a*c)
        if x<0:
            print("Sin solución")
        else:
            x1=((-b-math.sqrt(x))/(2*a))
            x2=((-b+math.sqrt(x))/(2*a))  
            print(x1,x2)
            


    def ejercicio3(self):
        #Dados dos (2) lados de un triángulo en cm, calcular la hipotenusa del mismo.
        c1 = int(input("Ingrese cateto a: "))
        c2 = int(input("Ingresa cateto b: "))
        h = (c1**2)+(c2**2)
        print("La hipotenusa del triangulo es: ", h)    
    

    def ejercicio4(self):
        #Dado un (1) número, imprimir 0 si es par y 1 si es impar.
        num = int(input("ingrese un numero: "))
        if num % 2 == 0:
            print("0, es par")
        else:
            print("1, es impar")    

    def ejercicio5(self):
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su bit da paridad. El bit
        #de paridad es 1 si el número de bits 1 es impar y 0 en caso contrario.
        pass

    def ejercicio6(self):
        #Dado un (1) número binario de cuatro (4) dígitos imprimir su valor   
        pass

    def ejercicio7(self):
        #Dado un (1) número de cuatro (4) dígitos imprimirlo por separado en unidades,
        #decenas, centenas y unidades de mil 
        pass     

    def ejercicio8(self):
        # Todos los años que se dividen exactamente entre 400, o que son divisibles
        # exactamente entre 4 y no son divisibles exactamente entre 100 son años bisiestos.
        # Usando estas premisas crea un algoritmo que lea una fecha como un número
        # entero con el formato ddmmaaaa, y luego extraiga el año de la fecha indicando si
        # el mismo es un año bisiesto o no.   
        pass 

    def ejercicio9(self):
        # Dado un número entero cuya cantidad de dígitos es igual a 5, determine si es
        # capicúa.
        pass
           

    def ejercicio10(self): 
        #Cree un algoritmo que tome por entrada las horas y minutos de un día y dé como
        #resultado su equivalente en segundos.
        h = int(input("Ingrese las horas: "))
        m = int(input("Ingrese los minutos: "))
        hs = h*3600
        ms = m*60
        s = hs+ms
        print("El equivalente en segundos es: ",s)

    def ejercicio11(self): 
        # Para un valor entero positivo que representa una cantidad en segundos, indicar
        # su equivalente en minutos, horas y días.  
        num = int(input("Ingrese el numero entero: "))
        m = num / 60
        h = num / 3600
        d = num / 86400
        print("El equivalente en minutos es: ",m)
        print("El equivalente en horas es: ",h)
        print("El equivalente en dias es: ",d)
        

    def ejercicio12(self): 
        # Dados tres números enteros positivos A, B y C, determine ¿cuál de ellos es el
        # mayor? y ¿cuál es el segundo mayor?
        num1 = int(input("Ingrese el numero entero: "))
        num2 = int(input("Ingrese el numero entero: "))
        num3 = int(input("Ingrese el numero entero: "))
        if num1>num2 and num1>num3:
            print("el numero mayor es", num1)
        elif num2>num1 and num2>num3:
             print("el numero mayor es", num2)
        else:
            print("el numero mayor es", num3)



            
        


    def ejercicio13(self):
        # En un estacionamiento el monto a pagar se calcula multiplicando el número de
        # horas que permaneció el automóvil dentro del estacionamiento por Bs. 4 y se
        # incrementa esta cantidad en Bs. 2,50 por cada media hora adicional.
        # Ahora se desea que usted elabore un algoritmo que a partir de la hora de entrada
        # y la hora de salida de un vehículo (las mismas corresponden a un mismo día)
        # calcule el monto a pagar por el dueño del vehículo.
        # La entrada vendrá dada por dos enteros positivos el primero representa las horas
        # y el segundo los minutos, además por último se debe leer un carácter (A o P) que
        # indica si la hora es AM o PM.
        pass


    def ejercicio14(self):
        # El IMC resulta de la división de la masa del individuo (en kilogramos) entre el
        # cuadrado de la estatura (en metros). El índice de masa corporal es un indicador
        # del peso de una persona en relación con su altura.
        # Clasificación del IMC de acuerdo con la OMS de la ONU:
        # a. Menor a 16: Criterio de ingreso.
        # b. 16 a 16.9: infra peso.
        # c. 17 a 18.4: bajo peso.
        # d. 18.5 a 24.9: peso normal.
        # e. 25 a 29.9: sobrepeso.
        # f. 30 a 34.9: obesidad pre-mórbida.
        # g. 40 a 45: obesidad mórbida.
        # h. Mayor a 45: obesidad híper-mórbida.
        # Dado el peso de una persona en libras (1 libra = 0,453592 Kg) y su estatura en
        # centímetros, calcule su IMC e indique como salida el peso en kilogramos, el valor
        # de IMC de la persona y la categoría en la cual fue clasificado.
        li = float(input("ingrese su peso en libras: "))
        es = float(input("ingrese su estatura en centimetros: "))
        kg = li * 0.453592
        al = es / 100
        imc = kg / (al**2)
        if imc < 16:
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es CRITERIO DE INGRESO")
        elif imc>=16 and imc<=16.9:
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es INFRA PESO")
        elif imc>=17 and imc<=18.4:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es BAJO PESO")
        elif imc>=18.5 and imc<=24.9:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es PESO NORMAL")   
        elif imc>=25 and imc<=29.9:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es SOBREPESO") 
        elif imc>=30 and imc<=34.9:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es OBESIDAD PRE-MORDIBA") 
        elif imc>=40 and imc<=45:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es OBESIDAD MORBIDA") 
        else:   
            print("El peso en kilogramos es "+str(kg)+", el IMC es de "+str(imc)+" y su categoria es OBESIDAD HIPER-MORBIDA")                   


    def ejercicio15(self):
        # Escriba un algoritmo que reciba una fecha (día y mes) correspondiente al año
        # 2014 e imprima por pantalla el número de días que han pasado desde el 1 de
        # Enero de 2014 hasta la fecha dada.
        pass


    def ejercicio16(self):   
        # Solicitar un número entre el 1 y el 12 e imprimir el mes correspondiente a dicho número.
        num = int(input("Ingrese un numero del 1 al 12: "))
        if num==1:
            print(num,"es igual a Enero")
        elif num==2:
            print(num,"es igual a Febrero")
        elif num==3:
            print(num,"es igual a Marzo")
        elif num==4:
            print(num,"es igual a Abril")
        elif num==5:
            print(num,"es igual a Mayo")
        elif num==6:
            print(num,"es igual a Junio")
        elif num==7:
            print(num,"es igual a Julio") 
        elif num==8:
            print(num,"es igual a Agosto")
        elif num==9:
            print(num,"es igual a Septiembre")
        elif num==10:
            print(num,"es igual a Octubre")
        elif num==11:
            print(num,"es igual a Noviembre")
        elif num==12:
            print(num,"es igual a Diciembre")                                       
        else:
            print("No ingreso un numero correcto")

    def ejercicio17(self):   
        # En un almacén se hace un 20% de descuento a los clientes cuya compra supere
        # los Bs 1000, se desea que realice un algoritmo el cual tome por entrada el monto a
        # pagar por el cliente y arroje como salida el monto aplicando el descuento de ser
        # necesario.
        mtp = float(input("Ingrese el monto total de la compra: "))
        if mtp>1000:
            desc = mtp*0.20
            tp = mtp-desc
            print("Su descuento es de $ "+str(desc)+" y su total a pagar es de $ "+str(tp))
        else:
            print("Su total a pagar es de $",mtp)
    

    def ejercicio18(self):   
        # Dado un número entero N, calcular e informar al usuario cuántos dígitos tiene
        # dicho número.
        num=int(input("Ingrese un numero: "))
        c=len(str(num))
        print("El numero ingresado tiene "+ str(c)+ " digitos")

    # def invertir_numero(n):
    #     numero = 0
    #     while n != 0:
    #         numero = 10*numero+n % 10
    #         n //= 10
    #     return numero


    # def capicua(numero):
    #   return numero == invertir_numero(numero)
    # # Probar
    # numeros = [11, 20, 123, 9889, 2811, 1801, 777, 12321, ]
    # for numero in numeros:
    #          es_capicua = capicua(numero)
    #          print(f"El número {numero} es capicúa? {es_capicua}")


    def ejercicio20(self):   
        # Dado un número N determinar si es un número primo.
        num = float(input("Ingrese el numero: "))
        if num >= 0:
                 primo=True
                 divisor=2
                 while divisor < num and primo ==True:
                     res=num%divisor
                     if res == 0:
                         primo+=1
                     divisor+=1
                 if primo==True:
                     print("El numero",num,"es primo")
                 else:
                     print("El numero",num,"no es primo")


    def ejercicio21(self):   
        # Construya un programa que dado un valor entero N, haga el cálculo de la función
        # factorial utilizando estructuras iterativas.
        num = float(input("Ingrese el numero: "))
        if num >=0:
                 acu=1
                 for num in range (num,1,-1):
                     acu=acu*num
                 print("Factorial del numero {} es {}".format(num,acu))

        pass 

    def ejercicio22(self):  
        # Dado un número entero N que representa una contraseña y asumiendo que una
        # contraseña debe tener al menos 10 dígitos para ser segura, determine si la
        # contraseña ingresada por el usuario es correcta, de no serlo debe pedirla
        # nuevamente hasta que tenga los 10 (diez) dígitos solicitados y al ser correcta
        # mostrar un mensaje de éxito al usuario, por salida estándar. 
        
        pass 

    def ejercicio23(self):   
        # Dada una secuencia de números terminada en cero (0), elaborar un algoritmo que
        # informe al usuario qué valor tiene el número mayor y qué valor tiene el número
        # menor, sin contar el cero (0).
        
        pass 

    def ejercicio24(self):  
        # Se tiene una secuencia de enteros terminada en cero, que corresponde a la edad,
        # peso y estatura de una muestra de hombres y mujeres mayores de 18 años. Con
        # base en dicha secuencia se desea realizar un estudio a fin de conocer:
        # Edad promedio de todas las personas en la muestra.
        # Peso promedio de todas las personas en la muestra.
        # Estatura promedio de todas las personas en la muestra.
        # Cuántas personas hay con edad entre los 18 y 25 años.
        # Cuántas personas son mayores a 36 años.
        # Cuál es el promedio de peso de las personas con edades entre 18 y 35 años.
        
        pass 

    def ejercicio25(self):   
        # Construye un algoritmo que calcule e imprima la tabla de multiplicar, desde la tabla
        # del 1 hasta la del 10.

        
        pass 

    def ejercicio26(self):   
        # Escribir un algoritmo que muestre todas las fichas de dominó, sin repetir
        
        pass 

    def ejercicio27(self):   
        # Dados N número positivos (N>1) calcular el promedio de esta serie. Considere que la serie termina al leer un 0.
        
        pass 

    def ejercicio28(self):  
        # Construya una función que solicite edades al usuario y determine el promedio de
        # las edades mayores a 18 años. El usuario indicará cuando desea dejar de
        # suministrar datos de entrada. En la Acción Principal se informará el promedio calculado. 
        
        pass 

    def eleva(self):
        # Construya una función “Eleva” Que reciba como parámetros una base y un
        # exponente y retorne al algoritmo principal el resultado de elevar un numero al otro.
        base = int(input("Ingrese la base: "))
        expo = int(input("ingrese el exponente: "))
        r = base**expo
        print (r)





    def ejercicio30(self):
        # Escriba una función que calcule el perímetro del pentágono (siendo el perímetro la
        # suma de los lados del polígono).
        num= int(input("Ingrese el valor: "))
        p = num*5
        print("El perimetro del pentagono es: ",p)


        

    def ejercicio31(self):
        # En una empresa pagan según las horas trabajadas y una tarifa fija por hora. Si la
        # cantidad de horas trabajadas en una semana es mayor a 40, la tarifa se
        # incrementa en un 35% para las horas extras. Escribe una acción principal que
        # solicite la identificación de 5 empleados, el monto cancelado por hora, y la
        # cantidad de horas trabajadas por cada uno, llame a acciones/funciones que
        # calculen el salario semanal por horas trabajadas (<=40) y los ingresos por
        # concepto de horas extras, y finalmente informe los resultados en la acción principal.
        nom = input("Ingrese sus nombres y apellidos: ")
        ht = int(input("Ingrese las horas trabajadas: "))
        tf = float(input("Ingrese la tarifa por hora: "))
        if ht>40:
            he = ht - 40
            phe = he * ((tf*0.35)+tf)
            tpsi = 40*tf
            tp = tpsi + phe
            print(nom,"recibe un salario semanal de $"+str(tpsi)+ " mas ingresos de horas extras de $",str(phe),
            "por lo que el total a pagar es de $"+str(tp))
        else:
            tp = ht*tf
            print("El salario semanal de "+nom+"es de $ "+str(tp))



    def ejercicio32(self):
        # Escriba una acción (MillasAKilometros) que convierta una distancia en millas a
        # kilómetros (1milla = 1.60935km). Esta acción recibirá como parámetros: el nombre
        # de la ciudad origen, el nombre de la ciudad destino y la distancia en millas entre
        # ellas y debe retornar la distancia entre las ciudades en kilómetros.
        # Desarrolle además una acción principal en donde utilice a la acción
        # MillasAKilometros para convertir e informar la distancia en kilómetros entre 4 pares
        # de ciudades suministradas por el usuario.

        pass










tarea = deber()
tarea.ejercicio20()


