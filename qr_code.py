
# import qrcode as qr


# img = make("https://www.youtube.com/watch?v=sRxrwjOtIag&list=RDic8j13piAhQ&index=2")
# img.save("alltoowell.png")
import qrcode
from PIL import Image
import qrcode.constants

qr=qrcode.QRCode(version=1,
                 error_correction=qrcode.constants.ERROR_CORRECT_H,
                 box_size=10,border=4,)

qr.add_data("https://www.youtube.com/watch?v=FOGRHBp6lvM&t=35s")
qr.make(fit=True)
img=qr.make_image(fill_color="green",back_color="blue")
img.save("wscube.png")
