import imageio.v3 as iio

filename = ['1.jpg','2.jpg','3.jpg','4.jpg','5.jpg' ,'6.jpg','7.jpg', '8.jpg' , '9.jpg' , '10.jpg', '11.jpg','12.jpg','13.jpg','14.jpg','15.jpg' ,'16.jpg','17.jpg', '18.jpg' , '19.jpg' , '20.jpg', '21.jpg','22.jpg','23.jpg','24.jpg','25.jpg' ,'26.jpg','27.jpg', '28.jpg' , '29.jpg' , '30.jpg' , '41.jpg','42.jpg','43.jpg','44.jpg','45.jpg' ,'46.jpg','47.jpg', '48.jpg' , '49.jpg' , '50.jpg' , '51.jpg' ]

images = []

for file in filename:
    images.append(iio.imread(file))

iio.imwrite('team01.gif' , images , duration = 100 , loop = 0)

#grater duration more time it takes :)

