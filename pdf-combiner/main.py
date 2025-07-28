import os
from tkinter import Tk, filedialog, messagebox
import pypdf


def combine_pdfs():
    root = Tk()
    root.withdraw()

    messagebox.showinfo("Select PDFs",
                        "Please select the PDF files you want to combine. You can select multiple files.")

    input_paths = filedialog.askopenfilenames(
        title="Select PDF files to combine",
        filetypes=[("PDF Files", "*.pdf")]
    )

    if not input_paths:
        messagebox.showwarning("Operation Canceled", "No files were selected. The program will now exit.")
        return

    # A alteração principal está aqui:
    pdf_writer = pypdf.PdfWriter()

    print("Selected files for merging (in order):")
    for path in input_paths:
        print(f"  - {os.path.basename(path)}")
        pdf_writer.append(path)

    output_path = filedialog.asksaveasfilename(
        title="Save Combined PDF as...",
        defaultextension=".pdf",
        filetypes=[("PDF File", "*.pdf")]
    )

    if not output_path:
        messagebox.showwarning("Operation Canceled", "No save location was chosen. The program will now exit.")
        pdf_writer.close()
        return

    try:
        with open(output_path, "wb") as f_out:
            pdf_writer.write(f_out)

        pdf_writer.close()

        print(f"\n✅ Success! Files combined and saved to: {output_path}")
        messagebox.showinfo("Success", f"PDFs combined successfully and saved as:\n{os.path.basename(output_path)}")

    except Exception as e:
        print(f"❌ Error while saving the file: {e}")
        messagebox.showerror("Error", f"An error occurred while saving the file:\n{e}")
        pdf_writer.close()


if __name__ == "__main__":
    combine_pdfs()