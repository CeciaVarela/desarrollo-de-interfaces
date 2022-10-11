import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class YesWindow(Gtk.Window):
	label = Gtk.Label("Has acertado")
	def __init__(self):
		super().__init__(title="yes_window")
		self.add(self.label)
	

