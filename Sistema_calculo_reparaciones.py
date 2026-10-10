#Sistema de control de ingesos para negocio de reparación de computadoras.
historial_de_cobros = []

def pedir_precio(mensaje):
    while True:
        try:
            dinero = float(input(mensaje))
            return dinero
        except ValueError:
            print("Ingrese un dígito válido.")
        

        
def sistema_calculo():
    while True:
        nuevo_cobro = pedir_precio("Por favor, ingrese el valor a registrar: ")
        historial_de_cobros.append(nuevo_cobro)
        respuesta = input("¿Desea agregar algún otro valor? (si/no): ").strip().lower()
        if respuesta != "si":
            break
        
def calculo_reparaciones():
    total = 0
    for cobro in historial_de_cobros:
        total += cobro
    return total
print("="*61)
print("BIENVENIDO AL SISTEMA DE HISTORIAL DE COBROS DE REPARACIONES.",)
print("="*61)

sistema_calculo()
cobros_del_dia = calculo_reparaciones()
print(f"Los valores de cobros son los siguientes: {historial_de_cobros}")
print(f"El valor total recaudado en reparaciones es: ${cobros_del_dia}")
    
        
        
        