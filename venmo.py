import qrcode

# Venmo
data = "https://account.venmo.com/u/QueenoftheHarpies"
img = qrcode.make(data)

path = "./content/images/venmo.png"

img.save(path)
print(f"Saved qr code to {path}")

# Cash app
data = "https://cash.app/$queenoftheharpies"
img = qrcode.make(data)

path = "./content/images/cash.png"

img.save(path)
print(f"Saved qr code to {path}")
