from . import main

# Definimos una ruta dentro del Blueprint
@main.route('/')
def index():
    return "hola mundo, esto es el INDEX visto desde un Blueprint"

# Otra ruta dentro del Blueprint
@main.route('/materiales')
def about():
    return "hola mundo, esto es la LISTA DE MATERIALES visto desde un Blueprint"

