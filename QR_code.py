import qrcode
data  = input("Enter the text or URL: ").strip()
Filename = input("Enter the filename: ").strip()

img = qrcode.make(data)
type(img)
img.save(Filename)
print(f"QR Code saved as {Filename}")
