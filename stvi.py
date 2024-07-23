from PIL import Image

def encode_message(image_path, message, output_image_path):
    # Load the image
    image = Image.open(image_path.strip('"').strip("'"))
    pixels = image.load()

    # Convert the message to binary
    binary_message = ''.join(format(ord(char), '08b') for char in message)
    binary_message += '1111111111111110'  # Adding a delimiter to signify end of message

    # Debug: Print the binary message to be encoded
    print("Binary message to encode:", binary_message)

    # Variables to keep track of which pixel and which bit we're at
    message_index = 0
    message_length = len(binary_message)

    for y in range(image.height):
        for x in range(image.width):
            if message_index < message_length:
                # Get the pixel
                r, g, b = image.getpixel((x, y))

                # Modify the LSB of each color channel if there are still bits to encode
                r = (r & 0xFE) | int(binary_message[message_index])
                message_index += 1
                if message_index < message_length:
                    g = (g & 0xFE) | int(binary_message[message_index])
                    message_index += 1
                if message_index < message_length:
                    b = (b & 0xFE) | int(binary_message[message_index])
                    message_index += 1

                # Update the pixel with the new values
                pixels[x, y] = (r, g, b)

    # Save the new image
    image.save(output_image_path.strip('"').strip("'"))
    print(f"Message encoded and saved to {output_image_path}")

def decode_message(image_path):
    # Load the image
    image = Image.open(image_path.strip('"').strip("'"))
    binary_message = ""
    pixels = image.load()

    for y in range(image.height):
        for x in range(image.width):
            r, g, b = image.getpixel((x, y))

            # Extract the LSB of each color channel and add it to the binary message
            binary_message += str(r & 1)
            binary_message += str(g & 1)
            binary_message += str(b & 1)

    # Debug: Print the extracted binary message
    print("Extracted binary message:", binary_message[:64])  # Print first 64 bits for brevity

    # Split by 8-bit chunks, stop at the delimiter
    message = ""
    for i in range(0, len(binary_message), 8):
        byte = binary_message[i:i+8]
        if byte == "11111111":
            break
        message += chr(int(byte, 2))

    return message

if __name__ == "__main__":
    choice = input("Do you want to encode or decode a message? (e/d): ").lower()
    if choice == 'e':
        image_path = input("Enter the path of the image to encode: ")
        message = input("Enter the message to encode: ")
        output_image_path = input("Enter the path to save the encoded image: ")
        encode_message(image_path, message, output_image_path)
    elif choice == 'd':
        image_path = input("Enter the path of the image to decode: ")
        message = decode_message(image_path)
        print("Decoded message:", message)
    else:
        print("Invalid choice. Please choose 'e' for encoding or 'd' for decoding.")
