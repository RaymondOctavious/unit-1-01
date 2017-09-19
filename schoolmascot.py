# created by raymond octavious
# created on september 19, 2017
#created for ics3u
# created for daily assignment 
# this program displays the school and its mascot

import ui

def Mt_touch_up_inside(sender):
	view['Answer_label'].text = ('Mother Teresa \n Titan')

def Mark_touch_up_inside(sender):
	view['Answer_label'].text = ('Saint Marks \n Lions')	
	
def Joe_touch_up_inside(sender):
	view['Answer_label'].text = ('Saint Joe \n Jaguars')

view = ui.load_view()
view.present('sheet')
