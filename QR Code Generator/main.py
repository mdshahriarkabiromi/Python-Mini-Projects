
import qrcode
from colorama import Fore, init
init()

data = input("Enter the data to be stored in the QR code: ").strip()
filename = input("\nEnter the filename for the QR code (no spaces or special characters): ").strip()

# Error detection - requires at least 10x10 QR code with default parameters
qr = qrcode.QRCode(box_size=10, border=5)

# Add encoding information - using 'qr.version' to indicate supported version based on module count
encoding_info = f"Encoding Information:\n"
encoding_info += f"Number of QR Code modules used: {qr.version}\n"
print(encoding_info)

def get_color(spec):
    return r'\x1b[' + spec + 'm■'

# Example usage
fill_colors = [
    get_color('32'),     # Green
    get_color('40')      # White on black
]

# Generate the QR code
qr.add_data(data)
qr.make(fit=True)
img = qr.make_image(fill_color="black", back_color="white")

# Save the QR code image
img.save(filename + ".png")

print(Fore.GREEN + f"QR code generated successfully! It is saved as: {filename}.png")
