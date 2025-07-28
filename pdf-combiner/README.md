# PDF Combiner 🔀

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A simple Python automation that lets you quickly and easily combine multiple PDF files into a single document using a friendly graphical interface.

---

## ✨ Features

- **Graphical Interface**: Select the files you want to merge and choose the final location and filename, all through your operating system's native windows.
- **Flexible**: Combine files from different folders without needing to move them to a specific location first.
- **Modern Library**: Uses `pypdf`, the modern and actively maintained successor to `PyPDF2`, compatible with the latest versions.
- **User Feedback**: Displays success, cancellation, or error messages for a clearer experience.

---

## 🚀 How to Use

### 1. Prerequisites
- You must have **Python 3** installed.
- This automation has an external dependency. Install it with the following command in your terminal:
  ```bash
  pip install pypdf
  ```

### 2. Installation

- Clone the repository to your local machine:

    ```bash
    git clone [https://github.com/brenoocanha/python-automations.git](https://github.com/brenoocanha/python-automations.git)
    ```

- Navigate to the project directory:

    ```bash
    cd python-automations/pdf-combiner
    ```

### 3. Execution

- Once you are inside the project's directory, run the script:

    ```bash
    python main.py
    ```

- Follow the instructions in the windows that appear: first, select the PDFs you want to merge; then, choose where to save the final file.

---

## ⚙️ How it Works

1. The script uses tkinter.filedialog.askopenfilenames to open a window where the user can select multiple .pdf files.

2. It checks if any files were selected.

3. It uses the pypdf library to create a PdfWriter object.

4. It adds each of the selected PDFs to the PdfWriter object using the .append() method.

5. It uses tkinter.filedialog.asksaveasfilename to ask the user where to save the new combined PDF file.

6. It writes the result to the specified location and displays a success message.

---

## 📜 License

This project is licensed under the MIT License. For more details, create a LICENSE file in the project with the license text.

---

Made with ❤️ by Breno Ocanha