

def menuPrincipal(op):
    globals.borrar_pantalla()
    encabezdo = """
    *****************
    * Menu Pricipal *
    *****************
    """
    options = '\t1.Registrar Sucursal.\n\t2.Eliminar Sucursal.\n\t4.Sucursales.\n\t5.Salir.'
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
                    pass
                case 2: 
                    pass
                case 3: 
                    globals.borrar_pantalla()
                    print('Fue un gusto servirle...Vuelva pronto.')
                    globals.pausar_pantalla()
                case 4: 
                    pass
                case _:
                    globals.borrar_pantalla()
                    print('Está ingresando una opción inválida...Intente nuevamente.')
                    globals.pausar_pantalla()
                    menuPrincipal(0)

if __name__ == '__main__':
    menuPrincipal(0)