import qrcode

def generate_qr_code(data, file_name='qrcode.png'):
    # Create QR code instance
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=50,
        border=6,
    )
    
    # Add data to the QR code
    qr.add_data(data)
    qr.make(fit=True)
    
    # Create an image from the QR code instance
    img = qr.make_image(fill_color="purple", back_color="yellow")
    
    # Save the image to a file
    img.save(file_name)
    
    print(f"QR code saved as {file_name}")

if __name__ == "__main__":
    # Example: Generate a QR code for a URL
    data_to_encode = "https://www.youtube.com/@indiansnackseuu9926"
    generate_qr_code(data_to_encode)
