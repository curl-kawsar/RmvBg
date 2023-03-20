from rembg import remove
from PIL import Image
import easygui as eg
input_path = eg.fileopenbox(title='Your Image')
output_path = eg.filesavebox(title='Enter Your Path Here')
input = Image.open(input_path)
output = remove(input)
output.save(output_path)