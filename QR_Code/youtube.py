
from pyqrcode import QRCode

#creating a youtube qr code

link="https://www.youtube.com/"

qrcode=QRCode(link)
    
qrcode.png('Qr_code2.png' , scale=8,)
    
