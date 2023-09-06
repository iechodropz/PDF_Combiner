import PyPDF2
import tkinter
from tkinter import filedialog


def merge_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

    if not file_paths:
        return

    pdf_writer = PyPDF2.PdfWriter()

    for file_path in file_paths:
        pdf_file = open(file_path, "rb")
        pdf_reader = PyPDF2.PdfReader(pdf_file)

        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

        pdf_file.close()

    merged_file_path = filedialog.asksaveasfilename(
        defaultextension=".pdf",
        filetypes=[("PDF files", "*.pdf")],
        initialfile="Merged PDF Files.pdf",
    )

    if not merged_file_path:
        return

    merged_pdf = open(merged_file_path, "wb")
    pdf_writer.write(merged_pdf)
    merged_pdf.close()


root = tkinter.Tk()
root.title("PDF Merger")

merge_button = tkinter.Button(root, text="Select PDFs", command=merge_pdfs)
merge_button.grid(row=0, column=0, padx=30, pady=30)

# Center the button within the grid cell
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
