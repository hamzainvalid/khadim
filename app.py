#/////////Sample/////////////

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

# import tkinter as tk
# from tkinter import ttk
# from tkinter import messagebox
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# from tkcalendar import DateEntry

# class InvoiceApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Invoice Generator")

#         # Set initial window size and make it resizable
#         self.root.geometry("600x400")
#         self.root.resizable(True, True)

#         # Creating frames
#         self.frame1 = ttk.Frame(root)
#         self.frame1.pack(padx=10, pady=10, fill='both', expand=True)
        

#         # Date
#         self.date_label = ttk.Label(self.frame1, text="Date:")
#         self.date_label.grid(row=0, column=0, sticky="w")
#         self.date_entry=DateEntry(self.frame1,selectmode='day')
#         self.date_entry.grid(row=0,column=1)

#         # Invoice Number
#         self.invoice_label = ttk.Label(self.frame1, text="Invoice No:")
#         self.invoice_label.grid(row=1, column=0, sticky="w")
#         self.invoice_entry = ttk.Entry(self.frame1)
#         self.invoice_entry.grid(row=1, column=1)

#         # Car Registration
#         self.car_reg_label = ttk.Label(self.frame1, text="Car Registration:")
#         self.car_reg_label.grid(row=2, column=0, sticky="w")
#         self.car_reg_entry = ttk.Entry(self.frame1)
#         self.car_reg_entry.grid(row=2, column=1)

#         # Car Model
#         self.car_model_label = ttk.Label(self.frame1, text="Car Model:")
#         self.car_model_label.grid(row=3, column=0, sticky="w")
#         self.car_model_entry = ttk.Entry(self.frame1)
#         self.car_model_entry.grid(row=3, column=1)

#         # Total Amount
#         self.total_amount_label = ttk.Label(self.frame1, text="Total Amount:")
#         self.total_amount_label.grid(row=4, column=0, sticky="w")
#         self.total_amount_entry = ttk.Entry(self.frame1)
#         self.total_amount_entry.grid(row=4, column=1)

#         # Advanced Amount
#         self.advanced_amount_label = ttk.Label(self.frame1, text="Advanced Amount:")
#         self.advanced_amount_label.grid(row=5, column=0, sticky="w")
#         self.advanced_amount_entry = ttk.Entry(self.frame1)
#         self.advanced_amount_entry.grid(row=5, column=1)

#         # Amount Handed Over
#         self.amount_handed_label = ttk.Label(self.frame1, text="Amount Handed Over:")
#         self.amount_handed_label.grid(row=6, column=0, sticky="w")
#         self.amount_handed_combo = ttk.Combobox(self.frame1, values=["Saim", "Ahad", "Mishal", "Abu Mishal"])
#         self.amount_handed_combo.grid(row=6, column=1)

#         # Type of Service
#         self.service_type_label = ttk.Label(self.frame1, text="Type of Service:")
#         self.service_type_label.grid(row=7, column=0, sticky="w")
#         self.service_type_combo = ttk.Combobox(self.frame1, values=["Mechanical work", "Technical Work", "Bodyshop"])
#         self.service_type_combo.grid(row=7, column=1)

#         # Description
#         self.description_label = ttk.Label(self.frame1, text="Description:")
#         self.description_label.grid(row=8, column=0, sticky="w")
#         self.description_entry = ttk.Entry(self.frame1)
#         self.description_entry.grid(row=8, column=1)

#         # Qty
#         self.qty_label = ttk.Label(self.frame1, text="Qty:")
#         self.qty_label.grid(row=9, column=0, sticky="w")
#         self.qty_entry = ttk.Entry(self.frame1)
#         self.qty_entry.grid(row=9, column=1)

#         # Generate button
#         self.generate_btn = ttk.Button(self.root, text="Generate Invoice", command=self.generate_invoice)
#         self.generate_btn.pack(pady=10)

#     def generate_invoice(self):
#         # Get input values
#         date = self.date_entry.get()
#         invoice_no = self.invoice_entry.get()
#         car_reg = self.car_reg_entry.get()
#         car_model = self.car_model_entry.get()
#         total_amount = self.total_amount_entry.get()
#         advanced_amount = self.advanced_amount_entry.get()
#         amount_handed = self.amount_handed_combo.get()
#         service_type = self.service_type_combo.get()
#         description = self.description_entry.get()
#         qty = self.qty_entry.get()

#         # Validate required fields
#         if not (date and invoice_no and car_reg and car_model and total_amount and advanced_amount and amount_handed and service_type and qty):
#             messagebox.showerror("Error", "Please fill in all required fields.")
#             return

#         # Generate PDF
#         filename = f"Invoice_{invoice_no}.pdf"
#         c = canvas.Canvas(filename, pagesize=letter)
#          # Add logo image
#         logo_path = "D:\Repositories\khadim\Logo.png"
#         c.drawImage(logo_path, 240, 750, width=120, height=60)
#         c.drawString(100, 750, "Invoice")
#         c.drawString(100, 730, f"Date: {date}")
#         c.drawString(100, 710, f"Invoice No: {invoice_no}")
#         c.drawString(100, 690, f"Car Registration: {car_reg}")
#         c.drawString(100, 670, f"Car Model: {car_model}")
#         c.drawString(100, 650, f"Total Amount: {total_amount}")
#         c.drawString(100, 630, f"Advanced Amount: {advanced_amount}")
#         c.drawString(100, 610, f"Amount Handed Over: {amount_handed}")
#         c.drawString(100, 590, f"Type of Service: {service_type}")
#         c.drawString(100, 570, f"Description: {description}")
#         c.drawString(100, 550, f"Qty: {qty}")

#         c.save()

#         messagebox.showinfo("Success", f"Invoice generated successfully: {filename}")

# def main():
#     root = tk.Tk()
#     app = InvoiceApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()



#////////////Test 3////////////

# import tkinter as tk
# from tkinter import ttk, messagebox
# from reportlab.lib.pagesizes import letter
# from reportlab.pdfgen import canvas
# import os

# class InvoiceApp:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("Invoice Generator")

#         # Set initial window size and make it resizable
#         self.root.geometry("600x400")
#         self.root.resizable(True, True)

#         # Creating frames
#         self.frame1 = ttk.Frame(root)
#         self.frame1.pack(padx=10, pady=10, fill='both', expand=True)

#         # Date
#         self.date_label = ttk.Label(self.frame1, text="Date:")
#         self.date_label.grid(row=0, column=0, sticky="w")
#         self.date_entry = ttk.Entry(self.frame1)
#         self.date_entry.grid(row=0, column=1)

#         # Invoice Number
#         self.invoice_label = ttk.Label(self.frame1, text="Invoice No:")
#         self.invoice_label.grid(row=1, column=0, sticky="w")
#         self.invoice_entry = ttk.Entry(self.frame1)
#         self.invoice_entry.grid(row=1, column=1)

#         # Car Registration
#         self.car_reg_label = ttk.Label(self.frame1, text="Car Registration:")
#         self.car_reg_label.grid(row=2, column=0, sticky="w")
#         self.car_reg_entry = ttk.Entry(self.frame1)
#         self.car_reg_entry.grid(row=2, column=1)

#         # Car Model
#         self.car_model_label = ttk.Label(self.frame1, text="Car Model:")
#         self.car_model_label.grid(row=3, column=0, sticky="w")
#         self.car_model_entry = ttk.Entry(self.frame1)
#         self.car_model_entry.grid(row=3, column=1)

#         # Total Amount
#         self.total_amount_label = ttk.Label(self.frame1, text="Total Amount:")
#         self.total_amount_label.grid(row=4, column=0, sticky="w")
#         self.total_amount_entry = ttk.Entry(self.frame1)
#         self.total_amount_entry.grid(row=4, column=1)

#         # Advanced Amount
#         self.advanced_amount_label = ttk.Label(self.frame1, text="Advanced Amount:")
#         self.advanced_amount_label.grid(row=5, column=0, sticky="w")
#         self.advanced_amount_entry = ttk.Entry(self.frame1)
#         self.advanced_amount_entry.grid(row=5, column=1)

#         # Amount Handed Over
#         self.amount_handed_label = ttk.Label(self.frame1, text="Amount Handed Over:")
#         self.amount_handed_label.grid(row=6, column=0, sticky="w")
#         self.amount_handed_combo = ttk.Combobox(self.frame1, values=["Saim", "Ahad", "Mishal", "Abu Mishal"])
#         self.amount_handed_combo.grid(row=6, column=1)

#         # Type of Service
#         self.service_type_label = ttk.Label(self.frame1, text="Type of Service:")
#         self.service_type_label.grid(row=7, column=0, sticky="w")
#         self.service_type_combo = ttk.Combobox(self.frame1, values=["Mechanical work", "Technical Work", "Bodyshop"])
#         self.service_type_combo.grid(row=7, column=1)

#         # Description
#         self.description_label = ttk.Label(self.frame1, text="Description:")
#         self.description_label.grid(row=8, column=0, sticky="w")
#         self.description_entry = ttk.Entry(self.frame1)
#         self.description_entry.grid(row=8, column=1)

#         # Qty
#         self.qty_label = ttk.Label(self.frame1, text="Qty:")
#         self.qty_label.grid(row=9, column=0, sticky="w")
#         self.qty_entry = ttk.Entry(self.frame1)
#         self.qty_entry.grid(row=9, column=1)

#         # Generate button
#         self.generate_btn = ttk.Button(self.frame1, text="Generate Invoice", command=self.generate_invoice)
#         self.generate_btn.grid(row=10, columnspan=2, pady=10)

#         # Print button
#         self.print_btn = ttk.Button(self.frame1, text="Print PDF", command=self.print_pdf)
#         self.print_btn.grid(row=11, columnspan=2, pady=10)

#         # Fetch PDF data button
#         self.fetch_data_btn = ttk.Button(self.frame1, text="Fetch PDF Data", command=self.fetch_pdf_data)
#         self.fetch_data_btn.grid(row=12, columnspan=2, pady=10)

#         # Adding Sizegrip for resizable window
#         ttk.Sizegrip(self.root).pack(side="bottom", fill="both")

#     def generate_invoice(self):
#         # Get input values
#         date = self.date_entry.get()
#         invoice_no = self.invoice_entry.get()
#         car_reg = self.car_reg_entry.get()
#         car_model = self.car_model_entry.get()
#         total_amount = self.total_amount_entry.get()
#         advanced_amount = self.advanced_amount_entry.get()
#         amount_handed = self.amount_handed_combo.get()
#         service_type = self.service_type_combo.get()
#         description = self.description_entry.get()
#         qty = self.qty_entry.get()

#         # Validate required fields
#         if not (date and invoice_no and car_reg and car_model and total_amount and advanced_amount and amount_handed and service_type and qty):
#             messagebox.showerror("Error", "Please fill in all required fields.")
#             return

#         # Generate PDF
#         filename = f"D:\Repositories\khadim\invoices-pdf\Invoice_{invoice_no}.pdf"
#         c = canvas.Canvas(filename, pagesize=letter)
#          # Add logo image
#         logo_path = "D:\Repositories\khadim\Logo.png"
#         c.drawImage(logo_path, 240, 750, width=120, height=60)
#         c.drawString(100, 750, "Invoice")
#         c.drawString(100, 730, f"Date: {date}")
#         c.drawString(100, 710, f"Invoice No: {invoice_no}")
#         c.drawString(100, 690, f"Car Registration: {car_reg}")
#         c.drawString(100, 670, f"Car Model: {car_model}")
#         c.drawString(100, 650, f"Total Amount: {total_amount}")
#         c.drawString(100, 630, f"Advanced Amount: {advanced_amount}")
#         c.drawString(100, 610, f"Amount Handed Over: {amount_handed}")
#         c.drawString(100, 590, f"Type of Service: {service_type}")
#         c.drawString(100, 570, f"Description: {description}")
#         c.drawString(100, 550, f"Qty: {qty}")

#         c.save()

#         messagebox.showinfo("Success", f"Invoice generated successfully: {filename}")

#     def print_pdf(self):
#         # Get the path to the generated PDF
#         pdf_path = "D:\Repositories\khadim\invoices-pdf"  # Replace with the actual path to your PDF

#         # Check if the PDF file exists
#         if not os.path.exists(pdf_path):
#             messagebox.showerror("Error", "PDF file not found.")
#             return

#         # Open the PDF file using the default PDF viewer
#         os.startfile(pdf_path, "print")

#     def fetch_pdf_data(self):
#         # Get the path to the generated PDF
#         pdf_path = "D:\Repositories\khadim\invoices-pdf"  # Replace with the actual path to your PDF

#         # Check if the PDF file exists
#         if not os.path.exists(pdf_path):
#             messagebox.showerror("Error", "PDF file not found.")
#             return

#         # Open the PDF file and read its contents
#         with open(pdf_path, "rb") as file:
#             # Use any PDF parsing library to extract data from the PDF
#             # For simplicity, let's assume the PDF contains text data
#             pdf_content = file.read()

#         # Populate entry fields with the fetched data
#         # For demonstration purposes, let's assume the PDF contains comma-separated values
#         data = pdf_content.decode().strip().split(",")

#         # Update entry fields with fetched data
#         self.date_entry.insert(0, data[0])
#         self.invoice_entry.insert(0, data[1])
#         self.car_reg_entry.insert(0, data[2])
#         self.car_model_entry.insert(0, data[3])
#         self.total_amount_entry.insert(0, data[4])
#         self.advanced_amount_entry.insert(0, data[5])
#         self.amount_handed_combo.set(data[6])
#         self.service_type_combo.set(data[7])
#         self.description_entry.insert(0, data[8])
#         self.qty_entry.insert(0, data[9])

# def main():
#     root = tk.Tk()
#     app = InvoiceApp(root)
#     root.mainloop()

# if __name__ == "__main__":
#     main()

#////////test 4- Fetch invoice info//////////

import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Toplevel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry
import json
import shutil

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
        self.date_entry=DateEntry(self.frame1,selectmode='day')
        self.date_entry.grid(row=0,column=1)

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
        self.generate_btn = ttk.Button(self.frame1, text="Generate Invoice", command=self.generate_invoice)
        self.generate_btn.grid(row=10, columnspan=2, pady=10)

        # Show invoices button
        self.show_invoices_btn = ttk.Button(self.root, text="Show Invoices", command=self.show_invoices)
        self.show_invoices_btn.pack(pady=10)

        # Adding Sizegrip for resizable window
        ttk.Sizegrip(self.root).pack(side="bottom", fill="both")

        # List to store invoice information
        self.invoices = []

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

        # Append invoice information to the list
        self.invoices.append({
            "Date": date,
            "Invoice No": invoice_no,
            "Car Registration": car_reg,
            "Car Model": car_model,
            "Total Amount": total_amount,
            "Advanced Amount": advanced_amount,
            "Amount Handed Over": amount_handed,
            "Type of Service": service_type,
            "Description": description,
            "Qty": qty
        })

        # Ask user to select directory
        directory = filedialog.askdirectory()
        if not directory:
            messagebox.showerror("Error", "No directory selected.")
            return

        # Generate PDF
        filename = f"{directory}/Invoice_{invoice_no}.pdf"
        c = canvas.Canvas(filename, pagesize=letter)
        logo_path = "logo\Logo.png"
        c.drawImage(logo_path, 240, 750, width=120, height=60)
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
        # Save invoices to a text file
        with open("db\invoices.txt", "a") as file:
            json.dump(self.invoices, file)

    def show_invoices(self):
        # Create a new window to display invoice information
        top = Toplevel(self.root)
        top.title("Invoices")

        # Load invoices from the text file
        try:
            with open("\invoices.txt", "r") as file:
                self.invoices = json.load(file)
        except FileNotFoundError:
            self.invoices = []

        def generate_invoice_pdf(invoice_data):
            # Ask user to select directory
            directory = filedialog.askdirectory()
            if not directory:
                messagebox.showerror("Error", "No directory selected.")
                return

            # Generate PDF
            filename = f"{directory}/Invoice_{invoice_data['Invoice No']}.pdf"
            c = canvas.Canvas(filename, pagesize=letter)
            c = canvas.Canvas(filename, pagesize=letter)
            logo_path = "logo\Logo.png"
            c.drawImage(logo_path, 240, 750, width=120, height=60)
            c.drawString(100, 750, "Invoice")
            c.drawString(100, 730, f"Date: {invoice_data['Date']}")
            c.drawString(100, 710, f"Invoice No: {invoice_data['Invoice No']}")
            c.drawString(100, 690, f"Car Registration: {invoice_data['Car Registration']}")
            c.drawString(100, 670, f"Car Model: {invoice_data['Car Model']}")
            c.drawString(100, 650, f"Total Amount: {invoice_data['Total Amount']}")
            c.drawString(100, 630, f"Advanced Amount: {invoice_data['Advanced Amount']}")
            c.drawString(100, 610, f"Amount Handed Over: {invoice_data['Amount Handed Over']}")
            c.drawString(100, 590, f"Type of Service: {invoice_data['Type of Service']}")
            c.drawString(100, 570, f"Description: {invoice_data['Description']}")
            c.drawString(100, 550, f"Qty: {invoice_data['Qty']}")
            c.save()

            messagebox.showinfo("Success", f"Invoice generated successfully: {filename}")

        # Create a frame to display invoice information
        frame = ttk.Frame(top)
        frame.pack(padx=10, pady=10)

        # Display invoice information and buttons
        for invoice_data in self.invoices:
            invoice_frame = ttk.Frame(frame, padding=(10, 5))
            invoice_frame.pack(fill="x")

            invoice_label = ttk.Label(invoice_frame, text=f"Invoice No: {invoice_data['Invoice No']}")
            invoice_label.pack(side="left", padx=(0, 10))

            generate_button = ttk.Button(invoice_frame, text="Generate PDF", command=lambda data=invoice_data: generate_invoice_pdf(data))
            generate_button.pack(side="right")

        # Add a scrollbar if there are many invoices
        # scrollbar = ttk.Scrollbar(frame, orient="vertical", command=top.yview)
        # scrollbar.pack(side="right", fill="y")

        # top.configure(yscrollcommand=scrollbar.set)

def main():
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

