
from pyqrcode import QRCode

hello="https://tinyurl.com/y6wcc32b"

Gamtech=QRCode(hello ,version=None)

Gamtech.png('flyer.png', scale=4) 
