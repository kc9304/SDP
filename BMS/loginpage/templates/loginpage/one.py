import qrcode

url = "https://www.example.com"

qr = qrcode.make(url)
qr.save('website_qr_code.png')
