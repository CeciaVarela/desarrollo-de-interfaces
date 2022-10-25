import gi
import requests, threading, shutil
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GLib
from window import MainWindow

class LoadWindow(Gtk.Window):
    label = Gtk.Label("Cargando elementos...")
    spinner = Gtk.Spinner()
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=20)

    def __init__(self):
        super().__init__(title="")
        self.connect("destroy", Gtk.main_quit)
        self.set_position(Gtk.WindowPosition.CENTER)
        self.set_border_width(60)
        self.set_default_size(200, 200)
        self.set_resizable(False)
        self.spinner.props.active = True

        self.box.pack_start(self.label, False, False, 0)
        self.box.pack_start(self.spinner, False, False, 0)
        self.add(self.box)
        #self.load_json()
        self.launch_load()

    def start_main_window(self, loaded_items_list):
        win = MainWindow(loaded_items_list)
        win.show_all()
        self.disconnect_by_func(Gtk.main_quit)
        self.close()    
    
    def launch_load(self):
        thread = threading.Thread(target=self.load_json, args=())
        thread.start()

    def load_json(self):
        response = requests.get('https://raw.githubusercontent.com/CeciaVarela/desarrollo-de-interfaces/main/API-REST/catalog.json')
        json_list = response.json() # We assume the request went OK. This'll crash otherwise

        #Inicializamos la lista que almacena los resultados
        result = []
        
        for json_item in json_list:
            #Almacenamos en estas variables los valores de los datos que están en el JSON
            name = json_item.get("name")
            description = json_item.get("description")
            image_url = json_item.get("image_url")
            #Descargamos la imagen y la almacenamos en un archivo temporal
            r = requests.get(image_url, stream=True)
            with open("temp.png", 'wb') as f:
                shutil.copyfileobj(r.raw, f)
            #Creamos un Gtk.Image y lo añadimos a un diccionario. Y ese diccionario es añadido a la lista "result"
            image = Gtk.Image.new_from_file("temp.png")
            result.append({"name": name, "description": description, "gtk_image": image})
        GLib.idle_add(self.start_main_window,  result)
