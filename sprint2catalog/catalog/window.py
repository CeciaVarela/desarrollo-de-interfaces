import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class MainWindow(Gtk.Window):
	flowbox = Gtk.FlowBox()
	
	def __init__(self, data_source):
		super().__init__(title="Catálogo")
		self.connect("destroy", Gtk.main_quit)
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_border_width(15)
		self.set_default_size(700, 600)
		
		#Definir el título de la página
		header = Gtk.HeaderBar(title="Animales")
		header.set_subtitle("Catálogo 2022")
		header.props.show_close_button = True
		
		self.set_titlebar(header)

		#Permitir el movimiento horizontal o vertical	
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.flowbox)
		self.add(scrolled)
	
		#Añadir imágenes
		for item in data_source:
			cell = Cell(item.get("name"), item.get("gtk_image"))
			self.flowbox.add(cell)

			mb = Gtk.MenuBar()
		
			filemenu = Gtk.Menu()
			filem = Gtk.MenuItem("Ayuda")
			filem.set_submenu(filemenu)
		
			label = Gtk.Label()
		
			mb.append(filem)

			#Creación del submenu
			imenu = Gtk.Menu()
		
			importm = Gtk.MenuItem("Acerca de")
			importm.set_submenu(imenu)
		
			label.set_text("El desarrollador es una persona")
			inews = Gtk.MenuItem("Acerca del desarrollador", label)
			imenu.append(inews)
		
			filemenu.append(importm)
		
			vbox = Gtk.VBox(False, 2)
			vbox.pack_start(mb, False, False, 0)
			self.add(vbox)
	
