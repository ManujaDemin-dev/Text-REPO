import imageio.v3 as iio

filename = ['picture011.png' , 'picture2.png']

images = []

for file in filename:
    images.append(iio.imread(file))

iio.imwrite('team.gif' , images , duration = 500 , loop = 0)

