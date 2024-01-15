import requests
import sqlite3
from Database import consultas





def enviar_pago_al_webhook():
    url = 'http://192.168.43.141:5000/pagos'  # Reemplaza XXX por la dirección IP real de la computadora A
    try:
        pago  = consultas.llamarUltimoPago()
        print(pago)
        respuesta = requests.post(url, json=pago)
        print(respuesta.text)
    except requests.RequestException as e:
        print('Error al enviar datos al webhook:', e)

def confirmarExistencia(codigo):
    url = 'http://192.168.43.141:5000/confirmarExistencia'  # Reemplaza XXX por la dirección IP real de la computadora A
    try:
        respuesta = requests.post(url, json=codigo)
        return(respuesta.text)
    except requests.RequestException as e:
        print('Error al enviar datos al webhook:', e)

'''
def agregar_datos_a_la_lista():
    clave =input("relacion :")
    valor =input ("relacion 2:")
    datos[clave] = valor
'''
def menu():
    while True:
        print("que quieres hacer")
        print("1. enviar los datos al servidor")
        print("2. ver el historial de caja")
        print("3. agregar pago")
        option =input("opción:" )
        if option=="1":
            enviar_pago_al_webhook()
        elif option=="2":
            historial =consultas.llamarHistorialPagos()
            for row in historial:
                print(row)
        
        elif option=="3":
            x="2"
            while True :
                if x=="0":
                    print("alumno inexistente, ingrese un codigo valido")
                codigo = str(input("codigo:" ))
                x =confirmarExistencia(codigo)
                print(x)
                if x== "1":
                    break
            monto = int(input("monto:" ))
            concepto = input("concepto:" )
            consultas.agregarPago(codigo, monto, concepto)
        else:
            break

menu()