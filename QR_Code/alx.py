
from pyqrcode import QRCode

hello="https://tinyurl.com/236wf7n8"

Gamtech=QRCode(hello ,version=None)

Gamtech.png('james.png', scale=4) 
