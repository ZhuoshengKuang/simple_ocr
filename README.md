# Simple OCR Project Using Tesseract

This project demonstrates a basic implementation of Optical Character Recognition (OCR) using Tesseract to extract text from PDF files. It's designed as a simple web application that allows users to upload PDF files, after which the server processes these files to extract and display the text content. This project aims to illustrate the foundational concepts of applying OCR technology to real-world applications.

## Features

- Upload PDF files through a web interface.
- Extract text from uploaded PDF files using Tesseract OCR.
- Download the extracted text as a `.txt` file.

## Prerequisites

Before you can run this project, you'll need to have the following installed on your system:

- Python 3.x
- Tesseract OCR

### Installing Tesseract OCR

Tesseract needs to be installed separately from this project. Installation instructions vary depending on your operating system:

- **For Ubuntu/Debian:**

  ```bash
  sudo apt update
  sudo apt install tesseract-ocr
  sudo apt install libtesseract-dev
  ```
- **For Windows:**

Download the installer from the [official Tesseract GitHub repository](https://github.com/tesseract-ocr/tesseract) and follow the installation instructions.

- **For macOS:**

  ```bash
  brew install tesseract
  ```
  
### Setup
#### 1. Clone the repository to your local machine.
  ```bash
  git clone https://github.com/ZhuoshengKuang/simple_ocr.git
  ```
#### 2. Navigate to the project directory.
  ```bash
  cd OCR
  ```
#### 3. Create a virtual environment and activate it.
  ```bash
  python -m venv venv
  source venv/bin/activate
  ```
#### 4. Install the required Python packages.
  ```bash
  pip install -r requirements.txt
  ```
## Running the Application
From within the project directory, run the Flask application with the following command:
  ```bash
  python app.py
  ```
This will start a web server on localhost (usually http://127.0.0.1:5000/). Open your web browser and navigate to this address to access the application.
## Usage
#### 1. On the homepage, click the "Choose File" button and select a PDF file you wish to extract text from.
#### 2. Click the "Extract Text" button to upload the file and start the OCR process.
#### 3. After processing, the extracted text will be displayed on the page, with an option to download it as a text file.

## Contributing
Contributions to this project are welcome. Please feel free to fork the repository, make your changes, and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE).
  ```less
  https://github.com/ZhuoshengKuang/simple_ocr.git`
  ````

This README provides all necessary instructions for getting started with your project, setting it up, and how to use it.
