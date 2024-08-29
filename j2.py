from qrcode import *
import qrcode

data = input("what is your data for img qrcode: ")


image_qr = qrcode.make(data)
image_qr.save("qrcode.png")