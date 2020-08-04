from PIL import Image, ImageDraw

source = Image.open('test.jpg')
width, heigth = source.size 

ratio = 1920 / 1080

if (width/heigth<=ratio):
	new_width = int(ratio * heigth)
	new_image = Image.new('RGBA', (new_width, heigth), (0,0,0,255))
	coordinates = (int(new_width / 2 - width / 2), 0)
	new_image.paste(source, coordinates)
	new_image.save('new_image.png')
else:
	print('Скорее всего изображение и так подходит для обоев')	

	
