import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class Lab(Gtk.Window):
	label = Gtk.Label("El desarrollador es una persona")
	def __init__(self):
		super().__init__(title="lab")
		self.add(self.label)
	