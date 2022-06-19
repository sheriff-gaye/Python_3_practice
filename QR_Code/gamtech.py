
from pyqrcode import QRCode

link="https://chat.whatsapp.com/LuS7AcWrqZX1NHGRk7W8Lv"

img=QRCode(link)

img.png('whatsapp.png',scale=8)