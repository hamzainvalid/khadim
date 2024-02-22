# from tkinter import *

# page = Tk()

# Label(page, text = 'Date', font = ('Arial', 14)).grid(row=0)
# Entry(page).grid(row=0, column=2)

# Label(page, text = 'Invoice no', font = ('Arial', 14)).grid(row=1)
# Entry(page).grid(row=1, column=2)

# Label(page, text = 'Car registration', font = ('Arial', 14)).grid(row=2)
# Entry(page).grid(row=2, column=2)

# Label(page, text = 'Car Model', font = ('Arial', 14)).grid(row=3)
# Entry(page).grid(row=3, column=2)

# Label(page, text = 'Total Amount', font = ('Arial', 14)).grid(row=4)
# Entry(page).grid(row=4, column=2)

# Label(page, text = 'Advanced Amount', font = ('Arial', 14)).grid(row=5)
# Entry(page).grid(row=5, column=2)

# Label(page, text = 'Description', font = ('Arial', 14)).grid(row=6)
# Entry(page).grid(row=6, column=2)

# Label(page, text = 'Qty', font = ('Arial', 14)).grid(row=7)
# Entry(page).grid(row=7, column=2)

# Button(page, text='Submit').grid(row=9, sticky=E, pady=10)


# page.mainloop()

# ////////// TEST ///////////

# import tkinter as tk
# from tkinter import messagebox
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter

# def generate_pdf():
#     name = name_entry.get()
#     age = age_entry.get()
#     profession = profession_entry.get()

#     if not name or not age or not profession:
#         messagebox.showerror("Error", "Please fill in all fields")
#         return

#     pdf_file = f"{name}_info.pdf"
#     c = canvas.Canvas(pdf_file, pagesize=letter)
#     c.drawString(100, 750, "Name: " + name)
#     c.drawString(100, 730, "Age: " + age)
#     c.drawString(100, 710, "Profession: " + profession)
#     c.save()
#     messagebox.showinfo("Success", f"PDF generated: {pdf_file}")

# # Create the main window
# root = tk.Tk()
# root.title("PDF Generator")

# # Create input fields
# tk.Label(root, text="Name:").grid(row=0, column=0, sticky="w")
# name_entry = tk.Entry(root)
# name_entry.grid(row=0, column=1)

# tk.Label(root, text="Age:").grid(row=1, column=0, sticky="w")
# age_entry = tk.Entry(root)
# age_entry.grid(row=1, column=1)

# tk.Label(root, text="Profession:").grid(row=2, column=0, sticky="w")
# profession_entry = tk.Entry(root)
# profession_entry.grid(row=2, column=1)

# # Button to generate PDF
# generate_button = tk.Button(root, text="Generate PDF", command=generate_pdf)
# generate_button.grid(row=3, column=0, columnspan=2)

# # Start the application
# root.mainloop()

#//////////////Test 2/////////////////

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry

class InvoiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Invoice Generator")

        # Set initial window size and make it resizable
        self.root.geometry("600x400")
        self.root.resizable(True, True)

        # Creating frames
        self.frame1 = ttk.Frame(root)
        self.frame1.pack(padx=10, pady=10, fill='both', expand=True)
        

        # Date
        self.date_label = ttk.Label(self.frame1, text="Date:")
        self.date_label.grid(row=0, column=0, sticky="w")
        cal=DateEntry(self.frame1,selectmode='day')
        cal.grid(row=0,column=1)

        # Invoice Number
        self.invoice_label = ttk.Label(self.frame1, text="Invoice No:")
        self.invoice_label.grid(row=1, column=0, sticky="w")
        self.invoice_entry = ttk.Entry(self.frame1)
        self.invoice_entry.grid(row=1, column=1)

        # Car Registration
        self.car_reg_label = ttk.Label(self.frame1, text="Car Registration:")
        self.car_reg_label.grid(row=2, column=0, sticky="w")
        self.car_reg_entry = ttk.Entry(self.frame1)
        self.car_reg_entry.grid(row=2, column=1)

        # Car Model
        self.car_model_label = ttk.Label(self.frame1, text="Car Model:")
        self.car_model_label.grid(row=3, column=0, sticky="w")
        self.car_model_entry = ttk.Entry(self.frame1)
        self.car_model_entry.grid(row=3, column=1)

        # Total Amount
        self.total_amount_label = ttk.Label(self.frame1, text="Total Amount:")
        self.total_amount_label.grid(row=4, column=0, sticky="w")
        self.total_amount_entry = ttk.Entry(self.frame1)
        self.total_amount_entry.grid(row=4, column=1)

        # Advanced Amount
        self.advanced_amount_label = ttk.Label(self.frame1, text="Advanced Amount:")
        self.advanced_amount_label.grid(row=5, column=0, sticky="w")
        self.advanced_amount_entry = ttk.Entry(self.frame1)
        self.advanced_amount_entry.grid(row=5, column=1)

        # Amount Handed Over
        self.amount_handed_label = ttk.Label(self.frame1, text="Amount Handed Over:")
        self.amount_handed_label.grid(row=6, column=0, sticky="w")
        self.amount_handed_combo = ttk.Combobox(self.frame1, values=["Saim", "Ahad", "Mishal", "Abu Mishal"])
        self.amount_handed_combo.grid(row=6, column=1)

        # Type of Service
        self.service_type_label = ttk.Label(self.frame1, text="Type of Service:")
        self.service_type_label.grid(row=7, column=0, sticky="w")
        self.service_type_combo = ttk.Combobox(self.frame1, values=["Mechanical work", "Technical Work", "Bodyshop"])
        self.service_type_combo.grid(row=7, column=1)

        # Description
        self.description_label = ttk.Label(self.frame1, text="Description:")
        self.description_label.grid(row=8, column=0, sticky="w")
        self.description_entry = ttk.Entry(self.frame1)
        self.description_entry.grid(row=8, column=1)

        # Qty
        self.qty_label = ttk.Label(self.frame1, text="Qty:")
        self.qty_label.grid(row=9, column=0, sticky="w")
        self.qty_entry = ttk.Entry(self.frame1)
        self.qty_entry.grid(row=9, column=1)

        # Generate button
        self.generate_btn = ttk.Button(self.root, text="Generate Invoice", command=self.generate_invoice)
        self.generate_btn.pack(pady=10)

    def generate_invoice(self):
        # Get input values
        date = self.date_entry.get()
        invoice_no = self.invoice_entry.get()
        car_reg = self.car_reg_entry.get()
        car_model = self.car_model_entry.get()
        total_amount = self.total_amount_entry.get()
        advanced_amount = self.advanced_amount_entry.get()
        amount_handed = self.amount_handed_combo.get()
        service_type = self.service_type_combo.get()
        description = self.description_entry.get()
        qty = self.qty_entry.get()

        # Validate required fields
        if not (date and invoice_no and car_reg and car_model and total_amount and advanced_amount and amount_handed and service_type and qty):
            messagebox.showerror("Error", "Please fill in all required fields.")
            return

        # Generate PDF
        filename = f"Invoice_{invoice_no}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        c.drawString(100, 750, "Invoice")
        c.drawString(100, 730, f"Date: {date}")
        c.drawString(100, 710, f"Invoice No: {invoice_no}")
        c.drawString(100, 690, f"Car Registration: {car_reg}")
        c.drawString(100, 670, f"Car Model: {car_model}")
        c.drawString(100, 650, f"Total Amount: {total_amount}")
        c.drawString(100, 630, f"Advanced Amount: {advanced_amount}")
        c.drawString(100, 610, f"Amount Handed Over: {amount_handed}")
        c.drawString(100, 590, f"Type of Service: {service_type}")
        c.drawString(100, 570, f"Description: {description}")
        c.drawString(100, 550, f"Qty: {qty}")

        c.save()

        messagebox.showinfo("Success", f"Invoice generated successfully: {filename}")

def main():
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

