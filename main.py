import pyscreenshot as ImageGrab


def take_screenshot():
    print("taking screenshot")
    image_name = "screenshot"
    screenshot = ImageGrab.grab()

    filepath = f"./screenshots/{image_name}.png"

    screenshot.save(filepath)

    print("screenshot taken")

    return filepath

def main():
    take_screenshot()

if __name__ == '__main__':
    main()