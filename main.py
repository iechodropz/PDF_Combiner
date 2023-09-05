import PyPDF2
import tkinter
from tkinter import filedialog


def merge_pdfs():
    file_paths = filedialog.askopenfilenames(filetypes=[("PDF files", "*.pdf")])

    if not file_paths:
        return


root = tkinter.Tk()
root.title("PDF Merger")

merge_button = tkinter.Button(root, text="Merge PDFs", command=merge_pdfs)
merge_button.grid(row=0, column=0, padx=30, pady=30)

# Center the button within the grid cell
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

root.mainloop()
