import interface.interfaceSecundaria as secundaria
import funciones.globals as globals

def menuPrincipal(op):
    globals.borrar_pantalla()
    encabezdo = """
    *****************
    * Menu Pricipal *
    *****************
    """
    options = '\t1.Gestión de sucursales.\n\t2.Salir.'
    if (op != 3):
        print(encabezdo)
        print(options)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida...')
            globals.pausar_pantalla()
            menuPrincipal(0)
        else:
            match (op):
                case 1: 
                    secundaria.gestionSucursal(0)
                case 2: 
                    globals.borrar_pantalla()
                    print('Fue un gusto servirle...Vuelva pronto.')
                    globals.pausar_pantalla()
                
                case _:
                    globals.borrar_pantalla()
                    print('Está ingresando una opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuPrincipal(0)

