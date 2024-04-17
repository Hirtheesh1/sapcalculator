from captcha.image import ImageCaptcha
import random
def generate_captcha(width, height, captcha_length=5):
    # Create an ImageCaptcha instance
    captcha = ImageCaptcha(width=width, height=height)

    # Generate random text for the CAPTCHA
    captcha_text = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(captcha_length))

    # Generate the CAPTCHA image
    captcha_image = captcha.generate(captcha_text)

    # Save the image to a file
    captcha_image_file = f'captcha_{captcha_text}.png'
    captcha.write(captcha_text, captcha_image_file)

    print(f"CAPTCHA generated and saved as '{captcha_image_file}'")

if __name__ == "__main__":
    # Set the dimensions of the CAPTCHA image
    width = 200
    height = 80

    # Generate and save the CAPTCHA
    generate_captcha(width, height)
