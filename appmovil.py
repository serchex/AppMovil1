from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.spinner import Spinner
from kivy.uix.label import Label
from kivy.uix.scrollview import ScrollView
from kivy.uix.gridlayout import GridLayout
from kivy.core.window import Window
from kivy.uix.popup import Popup
from kivy.graphics import Color, Rectangle
from kivy.uix.image import Image

Window.size = (300,600)

comidas={
    "tacos":12,
    "tamales":12,
    "arroz con pollo":16,
    "carne en guiso":20,
    "arroz": 5
}

def mostrar_popup(lista_layout):
    comidas_seleccionadas=[child.text for child in lista_layout.children]
    total = sum(int(comida.split("-")[1]) for comida in comidas_seleccionadas)
    
    layout_popup = BoxLayout(orientation='vertical',padding=10,spacing=10,)
    label_total = Label(
        text=f"El total a pagar es {total}",
        height=30,
        color=(0,0,0,1)    
    )
    layout_popup.add_widget(label_total)

    popup=Popup(
        title='Factura de comida',
        content=layout_popup,
        size_hint=(0.8,0.8),
    )
    
    cerrar_boton=Button(
        text='Cerrar',
        height=40,
        size_hint_y=None
    )
    layout_popup.add_widget(cerrar_boton)
    cerrar_boton.bind(on_press=popup.dismiss)
    
    popup.open()
    
def eliminar_ultima_comida(lista_layout):
    if len(lista_layout.children) > 0:
        lista_layout.remove_widget(lista_layout.children[0])

def agregar_comida(comida_seleccionada, lista_layout):
    if comida_seleccionada:
        comida_label = Label(
            text=f"{comida_seleccionada} - {comidas[comida_seleccionada]}",
            size_hint_y=None,
            height=40,
            font_size=16,
            color=(0,0,0,1)
        )
        
        lista_layout.add_widget(comida_label)

def construir_interfaz_grafica():
    layout_principal=BoxLayout(
        orientation='vertical',
        padding=[10,100,10,10],
        spacing=10
    )
    
    with layout_principal.canvas.before:
        layout_principal.bg_rect = Rectangle(
            source="images\main.png",#fondo
            size=Window.size,
            pos=layout_principal.pos
        )
        
    def update_bg_rect(instance, value):
        layout_principal.bg_rect.size = layout_principal.size
        layout_principal.bg_rect.pos = layout_principal.pos
    
    layout_principal.bind(size=update_bg_rect, pos=update_bg_rect)
    
    spinner_layout=BoxLayout(
        orientation='horizontal',
        size_hint=(1,0.1),
        spacing=5
    )
    
    comida_spinner = Spinner(
        text="Selecciona una comida",
        values=list(comidas.keys()),
        size_hint=(0.92,1),
        color=(1,1,1,1),
        font_size=16
    )
    
    spinner_icon=Image(
        source='images/arrow_down.png',
        size_hint=(0.08,1)
    )
    
    spinner_layout.add_widget(comida_spinner)
    spinner_layout.add_widget(spinner_icon)
    
    layout_principal.add_widget(spinner_layout)
    
    with spinner_layout.canvas.before:
        Color(0.8,0.8,0.8,1),
        spinner_layout.bg_rect=Rectangle(
            size=spinner_layout.size,
            pos=spinner_layout.pos
        )
        
    def update_bg_rect_spinner(instance, value):
        spinner_layout.bg_rect.size = spinner_layout.size
        spinner_layout.bg_rect.pos = spinner_layout.pos
        
    spinner_layout.bind(size=update_bg_rect_spinner, pos=update_bg_rect_spinner)
    
    agregar_button = Button(
        text="Agregar comida",
        size_hint=(1,0.1),
        font_size=16
    )
    
    layout_principal.add_widget(agregar_button)
    
    eliminar_button = Button(
        text="Eliminar comida",
        size_hint=(1,0.1),
        font_size=16
    )
    
    layout_principal.add_widget(eliminar_button)
    
    show_popup_button = Button(
        text='Mostrar resumen',
        size_hint=(1, 0.1),
        font_size=16,
    )
    layout_principal.add_widget(show_popup_button)
    
    scroll_view = ScrollView(size_hint=(1, 0.5))
    comida_list_layout = GridLayout(cols=1, size_hint_y=None)

    scroll_view.add_widget(comida_list_layout)
    layout_principal.add_widget(scroll_view)
    
    agregar_button.bind(on_press=lambda instance: agregar_comida(comida_spinner.text, comida_list_layout))
    eliminar_button.bind(on_press=lambda instance: eliminar_ultima_comida(comida_list_layout))
    show_popup_button.bind(on_press=lambda instance: mostrar_popup(comida_list_layout))
    
    return layout_principal

class RestaurantApp(App):
    def build(self):
        return construir_interfaz_grafica()
    
RestaurantApp().run()