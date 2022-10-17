import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk, GdkPixbuf
from cell import Cell

class MainWindow(Gtk.Window):
	image1 = Gtk.Image()
	image2 = Gtk.Image()
	image3 = Gtk.Image()
	image4 = Gtk.Image()
	image5 = Gtk.Image()
	
	def __init__(self):
		super().__init__(title="Catálogo")
		self.connect("destroy", Gtk.main_quit)
		self.set_border_width(15)
		self.set_default_size(400, 400)
		
		#Definir el títlo de la página
		header = Gtk.HeaderBar(title="Animales")
		header.set_subtitle("Catálogo 2022")
		header.props.show_close_button = True
		
		self.set_titlebar(header)
		
		scrolled = Gtk.ScrolledWindow()
		scrolled.set_policy(Gtk.PolicyType.NEVER, Gtk.PolicyType.AUTOMATIC)
		scrolled.add(self.image1)
		scrolled.add(self.image2)
		scrolled.add(self.image3)
		scrolled.add(self.image4)
		scrolled.add(self.image5)
		self.add(scrolled)
	

		#Añadir imágenes
		pixbuf1 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Imagen1.jpg", 200, 200, False)
		pixbuf2 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Imagen2.jpg", 200, 200, False)
		pixbuf3 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Imagen3.jpg", 200, 200, False)
		pixbuf4 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Imagen4.jpg", 200, 200, False)
		pixbuf5 = GdkPixbuf.Pixbuf.new_from_file_at_scale("data/unedited/Imagen5.jpg", 200, 200, False)
		self.image1.set_from_pixbuf(pixbuf1)
		self.image2.set_from_pixbuf(pixbuf2)
		self.image3.set_from_pixbuf(pixbuf3)
		self.image4.set_from_pixbuf(pixbuf4)
		self.image5.set_from_pixbuf(pixbuf5)
		
				
		
		
		
		
