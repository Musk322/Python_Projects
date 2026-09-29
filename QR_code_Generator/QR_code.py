import qrcode

#Taking UPI ID AS a input 
upi_id = input("Enter your UPI ID = ")

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE
# pn = RECIPENT NAME
# am = AMOUNT
# tn = MESSAGE BOX(AFTER PAYMENT)
#DEFINING THE PAYMENT URL BASED ON THE UPI ID AND THE PAYMENT APP
#YOU CAN MODIFY THESE URLS BASED ON THE PAYMENT APPS YOU WANT TO SUPPORT

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name$mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name$mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name$mc=1234'

#create QR Codes for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save  the QR Code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the QR Codes(you may need to install PIL/PILLOW LIBRARY)
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
