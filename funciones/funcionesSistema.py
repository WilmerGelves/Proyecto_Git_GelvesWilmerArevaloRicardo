import funciones.globals as globals
import interface.interfaceSecundaria as secundaria
import modules.corefiles as cf

def newSucursal():
    title = """
    ******************
    * NUEVA SUCURSAL *
    ******************
    """
    globals.borrar_pantalla()
    print(title)
    try:
        codSucursal = int(input('Código de la sucursal: '))
        codSucursal = str(codSucursal)
        nombreSucursal = input('Nombre de la sucursal: ').lower()
        sucursal = {
            'codSucursal': codSucursal,
            'nombreSucursal': nombreSucursal
        }
        cf.AddData('data',codSucursal, sucursal) 
        globals.sucursal.get('data').update({codSucursal: sucursal})
        opciones = 'Desea registrar otra sucursal: \n1.Si\n2.No'
        print(opciones)
        try:
            op = int(input('=>'))
            while(op != 1 and op != 2):
                globals.borrar_pantalla()
                print('Opcion inválida...Intente Nuevamente')
                print(opciones)
                op = int(input('=>'))
            if(op == 1):
                newSucursal()
            else:
                secundaria.gestionSucursal(0)
        except ValueError:
            print('Opción inválida.Intente nuevamente')
            newSucursal()
    except ValueError:
        print('Estas ingresando caracteres no permitidos')
        globals.pausar_pantalla()
        newSucursal()

def buscarSucursal():
    globals.borrar_pantalla()
    tipo = input('Ingrese el código de la sucursal: ')
    try:
        info = globals.sucursal.get('data').get(tipo)
    except ValueError:
        return None
    else:
        return info
    

def modificarSucursal():
    try:
        dataSucursal = buscarSucursal()
        codSucursal,nombreSucursal = dataSucursal.values()
        for key in dataSucursal.keys():
            if(key != 'codSucursal'):
                if(bool(input(f'Desea modificar {key} S(si) Enter(no)'))):
                    dataSucursal[key] = input(f'Ingrese el nuevo valor de {key}: ')
        globals.sucursal.get('data').update({codSucursal: dataSucursal})
        cf.UpdateFile(globals.sucursal)
        print(globals.sucursal)
        secundaria.gestionSucursal(0)
    except AttributeError:
        print('Servicio no encontrado')
        globals.pausar_pantalla()
        secundaria.gestionSucursal(0)


def deleteSucursal():
    dataDel = buscarSucursal()
    try:
        if 'codSucursal' in dataDel:
            codSucursal = dataDel['codSucursal']
            opciones = 'Desea Eliminar\n1.Si\n2.No'
            print(opciones)
            op = int (input('=>'))
            while (op != 1 and op != 2):
                globals.borrar_pantalla()
                print(opciones)
                op = int (input('=>'))
            if (op == 1):
                globals.sucursal.get('data').pop(codSucursal)
                cf.UpdateFile(globals.sucursal)
                secundaria.gestionSucursal(0)
            else:
                secundaria.gestionSucursal(0)
        else:
            print('Sucursal no encontrada...')
            secundaria.gestionSucursal(0)
    except TypeError:
        print('Sucursal no encontrada...')
        globals.pausar_pantalla()
        secundaria.gestionSucursal(0)
            