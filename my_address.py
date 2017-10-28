# Created by: Roman Beya
# Created on: 12-Sep-2017
# Created for class: ICS3U
# This displays my address label on a user interface

import ui

def display_address_touch_up_inside(sender):
	view['address_label'].text = "Roman Beya\nOttawa\nOntario"

view = ui.load_view()
view.present('sheet')
