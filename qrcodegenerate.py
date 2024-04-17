import qrcode as q 

upi_id = input("Enter your UPI Id")
url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=0123'
qr_code = q.make(url)

qr_code.save('qr_code.jpg') 
qr_code.show()