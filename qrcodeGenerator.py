import qrcode
import image

qr = qrcode.QRCode(
    version=10, # version shows high the number bigger the code image and complicated image
    box_size=6, # size of the box where qr code will be displayed 
    border=3, # white part of image
)
data = "https://wordpress.com/post/yesshecreates.art.blog/11"

qr.add_data(data)
qr.make(fit= True)
img = qr.make_image(fill="black", back_color = "white")
img.save("test.png")
