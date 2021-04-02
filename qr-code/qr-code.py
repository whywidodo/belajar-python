import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=2,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=20,
    border=4,
)
data = 'https://karyane.com'

qr.add_data(data)
qr.make(fit=True)
convert = qr.make_image(fill_color="black", back_color="white").convert('RGB')

convert.save("qr-code/hasil.png")
