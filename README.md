# QR Code Generator

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python" alt="Python 3.8+" />
  <img src="https://img.shields.io/badge/QR-Code-1D9BF0?style=for-the-badge" alt="QR Code" />
</div>

A lightweight Python project that generates a QR code image from a URL using the `qrcode` library. The script creates a QR image in the current working directory and supports custom foreground and background colors.

## ✨ Features

- Generates QR codes from website URLs
- Automatically adds the `https://www.` prefix when needed
- Uses a clean, high-contrast color theme
- Saves the output as `qrcode.png`
- Easy to run and customize

## 🛠️ Tech Stack

- Python 3
- `qrcode` library

## 🚀 Installation

Install the required dependency:

```bash
pip install qrcode
```

## ▶️ Usage

Run the script:

```bash
python qrcode_generator.py
```

Then enter a website name such as:

```text
enter url: https://www.
```

Example input:

```text
enter url: github.com
```

The script will generate a QR code for:

```text
https://www.github.com
```

And save it as:

```text
qrcode.png
```

## 📁 Project Structure

```text
qrcode/
├── qrcode_generator.py
├── README.md
└── qrcode.png
```

## 🔧 Code Overview

The script:

1. Creates a QR code object with custom settings
2. Adds a URL as QR data
3. Builds the image with custom colors
4. Saves the result to `qrcode.png`

## 🧩 Example

```python
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
```

## 🤝 Contributing

Contributions are welcome. If you want to improve the project:

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push and open a pull request

## 📌 Notes

This project is intentionally simple and beginner-friendly, making it a great starting point for learning QR code generation with Python.

