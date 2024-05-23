# Import the necessary modules
from gimpfu import *
import time
import gtk, gimpui

def debugMessage(Message):
    dialog = gtk.MessageDialog(None, 0, gtk.MESSAGE_INFO, gtk.BUTTONS_OK, Message)
    dialog.run()
    dialog.hide()
# Function to extract path coordinates
def extract_path_coordinates(image,drawable):
    vectors = pdb.gimp_image_get_active_vectors(image)
    nstrokes, strokes = pdb.gimp_vectors_get_strokes(vectors)
    stroke_type, n_points, cpoints, closed = pdb.gimp_vectors_stroke_get_points(vectors, strokes[0])
    print(str(cpoints))
    time.sleep(60)
    
    

# Register the Python-fu function in GIMP
register(
    "python_fu_extract_path_coordinates",
    "Extract Path Coordinates",
    "Extracts the coordinates of points from a path in GIMP",
    "Your Name",
    "Your Copyright",
    "Year",
    "<Image>/Filters/Extract Path Coordinates",
    "*",
    [],
    [],
    extract_path_coordinates,
)

# Main function to run GIMP's main loop
main()
