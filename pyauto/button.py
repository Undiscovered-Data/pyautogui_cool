import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from pyauto import lil_chut

the_state = "new"
the_number = 0

class ButtonWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Button Demo")
        self.set_border_width(10)
        self.the_state = "new"
        the_number = 1

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)

        button = Gtk.Button.new_with_label("Sort by N")
        button.connect("clicked", self.sort_by)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Too Short")
        button.connect("clicked", self.too_short)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("No Partial")
        button.connect("clicked", self.no_partial)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Poly A Tail")
        button.connect("clicked", self.poly_a)
        hbox.pack_start(button, True, True, 0)

        button = Gtk.Button.new_with_label("Plot Data")
        button.connect("clicked", self.data_plot)
        hbox.pack_start(button, True, True, 0)

    def sort_by(self, button):
        global the_state
        global the_number
        if the_state == "sort_state":
            the_number += 1
            lil_chut(0, the_number)
        else:
            the_number = 0
            the_state = "sort_state"
            lil_chut(0, the_number)

    def too_short(self, button):
        global the_state
        global the_number
        if the_state == "too_short":
            the_number += 1
            lil_chut(1, the_number)
        else:
            the_number = 0
            the_state = "too_short"
            lil_chut(1, the_number)

    def no_partial(self, button):
        global the_state
        global the_number
        if the_state == "no_partial":
            the_number += 1
            lil_chut(2, the_number)
        else:
            the_number = 0
            the_state = "no_partial"
            lil_chut(2, the_number)

    def poly_a(self, button):
        global the_state
        global the_number
        if the_state == "poly_a":
            the_number += 1
            lil_chut(3, the_number)
        else:
            the_number = 0
            the_state = "poly_a"
            lil_chut(3, the_number)

    def data_plot(self, button):
        global the_state
        global the_number
        if the_state == "plot_data":
            the_number += 1
            lil_chut(4, the_number)
        else:
            the_number = 0
            the_state = "plot_data"
            lil_chut(4, the_number)


win = ButtonWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()
