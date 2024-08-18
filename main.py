import interface.interfacePrincipal as principal
import modules.corefiles as cf
import funciones.globals as globals
if __name__ == '__main__':
    cf.DATA_SUCURSALES = 'data/sucursales.json'
    cf.checkFile(globals.sucursal)
    principal.menuPrincipal(0)
