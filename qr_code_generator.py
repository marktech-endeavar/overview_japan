import qrcode

# Replace with your PDF's public URL
pdf_url = "https://github.com/marktech-endeavar/overview_japan/blob/main/MARKTECH%20-%20One%20Pager.pdf"

# Generate QR code
qr = qrcode.QRCode(version=1, box_size=10, border=5)
qr.add_data(pdf_url)
qr.make(fit=True)

# Create and save the QR code image
img = qr.make_image(fill_color="black", back_color="white")
img.save("overview_japan_qr_code.png")

print("✅ QR code saved as pdf_qrcode.png")
