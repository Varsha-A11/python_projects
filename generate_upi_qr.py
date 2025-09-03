import qrcode

upi_id=input("Enter ur upi id:")

# format-> upi://pay?pa=UPI_ID&pn=NAME&am=ACCOUNT&cu=CURRENCY&tn=MESSAGE

phonepe_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_url=f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create qr code 
phonepe_qr=qrcode.make(phonepe_url)
paytm_qr=qrcode.make(paytm_url)
google_qr=qrcode.make(google_url)

#save qr img optional
# phonepe_qr.save('phonepe_qr.png')

#display qr codes
phonepe_qr.show()
paytm_qr.show()
google_qr.show()