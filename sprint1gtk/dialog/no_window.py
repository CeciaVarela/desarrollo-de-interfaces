import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class NoWindow(Gtk.Window):
	label = Gtk.Label("No has acertado")
	def __init__(self):
		super().__init__(title="no_window")
		self.add(self.label)

