import interface.interfacePrincipal as principal
import funciones.globals as globals
import funciones.funcionesSistema as sistema
def gestionSucursal(op : int ):
    title = """
    **********************
    * Gestión de Sucursal*
    **********************
    """
    menuS = '\t1.Agregar Sucursal.\n\t2.Editar Sucursal.\n\t3.Eliminar Sucursal.\n\t4.Buscar Sucursal\n\t5.Salir'
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
                    sistema.newSucursal()
                case 2:
                    sistema.modificarSucursal()
                case 3:
                    sistema.deleteSucursal()
                case 4:
                    resultado = sistema.buscarSucursal()
                    if resultado is None:
                        print('Sucursal no encontrada...')
                        globals.pausar_pantalla()
                        gestionSucursal(0)
                    else:
                        print(resultado)
                        globals.pausar_pantalla()
                        globals.borrar_pantalla()
                        gestionSucursal(0)
                case 5:
                    globals.borrar_pantalla()
                    print('Has salido de gestión de Sucursales')
                    globals.pausar_pantalla()
                    principal.menuPrincipal(0)
                case _:
                    print('Opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    gestionSucursal(0)
