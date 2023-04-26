import qrcode
img = qrcode.make("Hello")
img.save("qrcode.png")
