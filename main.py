import PyPDF2
import tkinter
from tkinter import filedialog


def merge_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

    if not file_paths:
        return

    pdf_writer = PyPDF2.PdfFileWriter()

    for file_path in file_paths:
        pdf_file = open(file_path, "rb")
        pdf_reader = PyPDF2.PdfFileReader(pdf_file)

        for page_num in range(pdf_reader.numPages):
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        pdf_file.close()


root = tkinter.Tk()
root.title("PDF Merger")

merge_button = tkinter.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.grid(row=0, column=0, padx=30, pady=30)

# Center the button within the grid cell
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
