import qrcode

url = input("Enter URL: ").strip()

# basic validation
if not url.startswith(("http://", "https://")):
    url = "https://" + url

img = qrcode.make(url)

# simple filename (avoid messy URLs as filenames)
img.save("qr_code.png")

img.show()