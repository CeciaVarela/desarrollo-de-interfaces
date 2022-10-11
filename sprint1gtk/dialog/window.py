import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MainWindow(Gtk.Window):
	box1 = Gtk.Box(orientation=Gtk.Orientation.VERTICAL)
	label = Gtk.Label("¿Es París la capital de Francia?")
	box2 = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL)
	button1 = Gtk.Button(label="Si")
	button2 = Gtk.Button(label="No")
	
	def __init__(self):
		super().__init__(title="Main")
		self.connect("destroy", Gtk.main_quit)
		self.box1.pack_start(self.label, True, True, 0)
		self.box1.pack_start(self.box2, True, True, 0)
		
		self.add(self.box1)		
		self.button1.connect("clicked", self.on_button1_clicked)
		self.button2.connect("clicked", self.on_button2_clicked)
		self.box2.pack_start(self.button1, True, True, 0)
		self.box2.pack_start(self.button2, True, True, 0)
	
				
	def on_button1_clicked(self, widget):
		from yes_window import YesWindow
		yes = YesWindow()
		yes.show_all()
				
			
	def on_button2_clicked(self, widget):
		from no_window import NoWindow
		no = NoWindow()
		no.show_all()
		
