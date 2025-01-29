import qrcode
import art
print(art.logo)

data = input("Enter the data to be stored in the QR code: ").strip()
filename = input("Enter the filename of the QR code: ").strip()

qr=qrcode.QRCode(box_size=10, border=5)
qr_data = qr.add_data(data)
img = qr.make_image(fill_color="black", back_color="white")
img.save(filename+".png")
print(f"QR code saved as: {filename}")