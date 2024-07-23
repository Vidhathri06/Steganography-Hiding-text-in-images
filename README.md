# Steganography-Hiding-text-in-images

Types of Steganography Techniques Used
Least Significant Bit (LSB) Method:

What It Is: This method hides text in the smallest bits of the image's pixel values, making the changes invisible to the human eye.
How It Works: Each pixel in an image has color values (red, green, blue). By changing the least significant bit (the smallest bit) of these color values, we can embed the binary representation of a text message into the image without noticeably altering it.

Python Libraries Used in the Code
PIL (Python Imaging Library):
What It Does: PIL, now known as Pillow, is a library for opening, manipulating, and saving many different image file formats in Python.
How It's Used: In this project, PIL is used to load the image, access and modify its pixel values, and save the modified image.

