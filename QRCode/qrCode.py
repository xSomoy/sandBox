import qrcode
import Image
img = qrcode.make("Hello")
img.save("hello.jpg")