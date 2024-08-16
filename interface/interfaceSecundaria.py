import interface.interfacePrincipal as principal
import funciones.globals as globals
def gestionSucursal(op : int ):
    title = """
    **********************
    * Gestión de Sucursal*
    **********************
    """
    menuS = '\t1.Agregar Sucursal.\n\t2.Editar Sucrusal.\n\t3.Eliminar Sucursal.\n\t4.Salir'
    globals.borrar_pantalla()
    if (op != 4):
        print(title)
        print(menuS)
        try:
            op = int(input('\t=>'))
        except ValueError:
            print('Opción inválida')
            globals.pausar_pantalla()
            gestionSucursal(0)
        else:
            match(op):
                case 1:
                    pass
                case 2:
                    pass
                case 3:
                    pass
                case 4:
                    globals.borrar_pantalla()
                    print('Has salido de gestión de Sucursales')
                    globals.pausar_pantalla()
                    principal.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionSucursal(0)
