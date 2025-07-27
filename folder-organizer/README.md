# Python Folder Organizer 📂

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple Python script that automatically organizes files in a folder into subfolders based on their extensions. Ideal for cleaning up your "Downloads" folder or any other cluttered directory.

## ✨ Features

- **Extension-based Organization**: Moves `.pdf`, `.jpg`, `.docx`, `.zip` files, etc., into folders with their respective names (`pdf`, `jpg`, `docx`, `zip`).
- **Automatic Folder Creation**: Destination folders are created automatically if they don't already exist.
- **Graphical User Interface**: Uses a native OS window for you to easily and safely select the folder to organize.
- **Safe**: The script ignores subdirectories and its own file, preventing it from accidentally moving itself.
- **Lightweight & Portable**: Requires no external libraries. Works with a standard Python 3 installation.

## 🎬 Demo

Imagine you have a folder like this:

**Before:**
📁 Downloads/
├── invoice-2025.pdf
├── final-report.docx
├── company-logo.png
├── vacation-photo.JPG
└── presentation.pdf


After running the script and selecting the `Downloads` folder, it will look like this:

**After:**
📁 Downloads/
├── 📁 pdf/
│   ├── invoice-2025.pdf
│   └── presentation.pdf
│
├── 📁 docx/
│   └── final-report.docx
│
├── 📁 png/
│   └── company-logo.png
│
└── 📁 jpg/
└── vacation-photo.JPG


## 🚀 How to Use

1.  **Prerequisites**:
    - You must have **Python 3** installed on your computer. The required libraries (`Tkinter`, `os`, `shutil`, and `sys`) are included in the standard installation.

2.  **Download**:
    - Clone the entire repository to your local machine:
      ```bash
      git clone https://github.com/brenoocanha/python-automations.git
      ```
    - After cloning, navigate to the project's directory:
      ```bash
      cd python-automations/file-organizer
      ```

3.  **Execution**:
    - Open your terminal or command prompt.
    - Navigate to the directory where you saved the script.
    - Run the command:
      ```bash
      python your_script_name.py
      ```
    - A window will pop up for you to select the folder you want to organize.
    - The progress will be displayed in the terminal, and when it's done, your folder will be organized!

## ⚙️ How it Works

The script performs the following steps:
1.  Opens a dialog window (`tkinter.filedialog`) for the user to choose a directory.
2.  Lists all items in the selected directory (`os.listdir`).
3.  For each item, it checks if it's a file (`os.path.isfile`) and not the script itself.
4.  Extracts the file extension (e.g., `.pdf`).
5.  Creates a subfolder named after the extension (e.g., `pdf`) if it doesn't exist.
6.  Moves the file to the corresponding subfolder (`shutil.move`).

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
_Made with ❤️ by [Your Name or Username]_