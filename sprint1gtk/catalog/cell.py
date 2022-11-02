import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Cell(Gtk.EventBox):
	name = None
	
	def __init__(self, name, image):
		super().__init__()
		self.name = name
		self.image = image
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=4)
		box.pack_start(Gtk.Label(label=name), False, False, 0)
		box.pack_start(image, True, True, 0)
		self.add(box)
		self.connect("button-release-event", self.on_click)
		
	def on_click(self, widget, event):
		label = Gtk.Label()
		label2 = Gtk.Label()
		imagen = Gtk.Image().set_from_pixbuf(self.image.get_pixbuf())
		
		
		if self.name == "Mapaches":			
			label.set_text(self.name)
			label2.set_text("Son unos animales muy bonitos")
			imagen = Gtk.Image().set_from_pixbuf(self.image1.get_pixbuf())
			
		elif self.name == "Ardilla":
			label.set_text(self.name)
			label2.set_text("Las ardillas comen bellotas")
			imagen = Gtk.Image().set_from_pixbuf(self.image2.get_pixbuf())
			
		elif self.name == "Mariquita":
			label.set_text(self.name)
			label2.set_text("Las mariquitas tienen puntitos")
			imagen = Gtk.Image().set_from_pixbuf(self.image3.get_pixbuf())
			
		elif self.name == "Perro":
			label.set_text(self.name)
			label2.set_text("Los perros son muy cariñosos")
			imagen = Gtk.Image().set_from_pixbuf(self.image4.get_pixbuf())
			
		elif self.name == "Hamster":
			label.set_text(self.name)
			label2.set_text("Los hamsters tienen la cara gordita")
			imagen = Gtk.Image().set_from_pixbuf(self.image5.get_pixbuf())
			
		

		from detail_window import DetailWindow
		detWin = DetailWindow(label, imagen, label2)
		detWin.show_all()	
		
