Python generation of QR codes
-----------------------------

Notes and links - work in process

```
https://pypi.org/project/PyQRCode/
https://stackoverflow.com/questions/45481990/how-to-insert-logo-in-the-center-of-qrcode-in-python
https://stackoverflow.com/questions/2563822/how-do-you-composite-an-image-onto-another-image-with-pil-in-python
https://www.geeksforgeeks.org/python-generate-qr-code-using-pyqrcode-module/


 pip install pyqrcode
 pip install pypng


#####
>>> import pyqrcode
>>> url = pyqrcode.create('https://blogs.cisco.com/developer/tetration-for-security')
>>> url.png('code.png', scale=5)
>>> quit()


# Import QRCode from pyqrcode 
import pyqrcode 
from pyqrcode import QRCode 


# String which represent the QR code 
s = "www.geeksforgeeks.org"

# Generate QR code 
url = pyqrcode.create(s) 

# Create and save the png file naming "myqr.png" 
url.svg("myqr.svg", scale = 8) 


>>> url = pyqrcode.create('http://uca.edu')
>>> with open('code.png', 'w') as fstream:
...     url.png(fstream, scale=5)
>>> # same as above
>>> url.png('code.png', scale=5)
>>> # in-memory stream is also supported
>>> buffer = io.BytesIO()
>>> url.png(buffer)
>>> # do whatever you want with buffer.getvalue()
>>> print(list(buffer.getvalue())

```

