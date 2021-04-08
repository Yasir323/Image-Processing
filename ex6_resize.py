import cv2
import os
from rich.console import Console 

console = Console()


def resize_image(file, i):
	img = cv2.imread(file)
	# print(file)
	# print(f"Original shape: {img.shape}")
	original_width = img.shape[1]
	original_height = img.shape[0]
	new_width = 640
	scale_factor = new_width / original_width
	new_height =  scale_factor * original_height
	new_shape = (new_width, int(new_height))
	# print(f"New shape: {new_shape}")
	imgResize = cv2.resize(img, new_shape)
	file_name = "data/image1" + str(i) + ".jpg"
	cv2.imwrite(file_name, imgResize)
	# print(f"Image {i} resized successfully!")


# files = os.listdir(os.path.join(os.getcwd(), 'data'))
files = []
for i in range(10):
	file = "image" + str(i) + ".jpg"
	files.append(file)

i = 0
with console.status('[bold green]Resizing files...') as status:
	for file in files:
		file = os.path.join('data', file)
		resize_image(file, i)
		console.log(f'[green]Finished resizing file[/green] {i + 1}')
		i += 1
		console.log(f'[bold red]Done!')

