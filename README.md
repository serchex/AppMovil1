📱 RestaurantApp
Aplicación móvil sencilla desarrollada con Python y Kivy para gestionar pedidos de comida, permitiendo seleccionar platillos, agregarlos a una lista, eliminarlos y mostrar un resumen con el total a pagar.

📸 Capturas de Pantalla
(Agrega aquí imágenes de la app en funcionamiento si deseas)

📦 Requisitos
Python 3.x

Kivy >= 2.0.0

Para instalar Kivy:

bash
Copiar
Editar
pip install kivy
🚀 ¿Cómo usar?
Clona o descarga este repositorio.

Asegúrate de tener la carpeta images/ con las imágenes:

main.png (fondo de la app)

arrow_down.png (ícono de spinner)

Ejecuta el archivo principal:

bash
Copiar
Editar
python appmovil.py
🎨 Funcionalidades
Selector de comida: Desplegable con diferentes platillos disponibles y sus precios.

Agregar comida: Añade el platillo seleccionado a la lista de pedidos.

Eliminar comida: Elimina el último platillo agregado.

Mostrar resumen: Muestra una ventana emergente con el total a pagar por los platillos seleccionados.

Diseño personalizado: Fondo de pantalla y personalización de elementos gráficos.

🍽️ Lista de Comidas y Precios
python
Copiar
Editar
comidas = {
    "tacos": 12,
    "tamales": 12,
    "arroz con pollo": 16,
    "carne en guiso": 20,
    "arroz": 5
}
📁 Estructura de Archivos
css
Copiar
Editar
RestaurantApp/
├── appmovil.py
├── images/
│   ├── main.png
│   └── arrow_down.png
└── README.md
✨ Notas
La ventana se establece en un tamaño fijo de 300x600 px.

La aplicación usa BoxLayout, GridLayout, ScrollView, Spinner, y Popup para su interfaz.

Puedes personalizar las comidas o los precios modificando el diccionario comidas en appmovil.py.

📝 Licencia
Este proyecto se distribuye bajo la licencia MIT.
