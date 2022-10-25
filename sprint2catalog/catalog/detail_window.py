import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class DetailWindow(Gtk.Window):
	
	def __init__(self, label, image, label2):
		box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
		super().__init__(title="Catálogo")
		self.set_position(Gtk.WindowPosition.CENTER)
		self.set_default_size(400, 400)
		self.add(box)
		box.pack_start(label, True, True, 0)
		box.pack_start(image, True, True, 0)
		box.pack_start(label2, True, True, 0)
		
		
		
