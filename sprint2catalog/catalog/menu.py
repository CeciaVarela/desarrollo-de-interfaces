import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from cell import Cell

class Menu(Gtk.Window):
    def __init__(self, data_source):
        super().__init__(title="")
        self.set_size_request(250, 200)
        self.modify_bg(Gtk.STATE_NORMAL, Gtk.gdk.Color(6400, 6400, 6440))
        self.set_position(Gtk.WIN_POS_CENTER)
        
        mb = Gtk.MenuBar()
        
        filemenu = Gtk.Menu()
        filem = Gtk.MenuItem("Ayuda")
        filem.set_submenu(filemenu)
        
        mb.append(filem)

		#Creación del submenu
        imenu = Gtk.Menu()
        
        importm = Gtk.MenuItem("Acerca de")
        importm.set_submenu(imenu)
        
        inews = Gtk.MenuItem("Acerca del desarrollador")

        imenu.append(inews)
        
        filemenu.append(importm)

        vbox = Gtk.VBox(False, 2)
        vbox.pack_start(mb, False, False, 0)
        self.add(vbox)
		
		



