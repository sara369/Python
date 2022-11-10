#pip3 install qrcode
#pip3 install image


import qrcode
import image

qr = qrcode.QRCode(
    version = 15, # the version of the qr code, the high the number the code image and complication will be higher
    box_size = 10, #qrcode display box size
    border = 5 # the white borders of the image
)


data = "test the qrcode" #you can type anything here, or post url, cv .. etc.

qr.add_data(data)
qr.make(fit = True)

image = qr.make_image(fill = "black", back_color = "white")

image.save("test.png")



#code was written by following "Techie Coder" tutorial on YouTube :)