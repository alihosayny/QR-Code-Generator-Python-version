
import qrcode

print("Choose QR Code type:")
print("1 - URL")
print("2 - Text")
print("3 - Image URL")

choice = input("Enter your choice: ")

if choice == "1":
    data = input("Enter your URL: ")

elif choice == "2":
    data = input("Enter your text: ")

elif choice == "3":
    data = input("Enter your image URL: ")

else:
    print("Invalid choice!")
    exit()

# you can change code qrCode here
file_path = "C:\\Users\\HP\\Desktop\\tp\\pyTp\\qrCode\\codeQr.png"

qr = qrcode.QRCode()
qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color="white")
img.save(file_path)

print("Your QR Code was generated :)")
