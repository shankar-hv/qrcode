import qrcode
def qrcodegenerator(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(url)
    qr.make(fit=True)

    img = qr.make_image(back_color=(66, 209, 245), fill_color=(218, 245, 66))
    img.save('qrcode.png')

entry_point="https://www."
url = input("enter url: https://www.")
final_url = entry_point + url
qrcodegenerator(final_url)