import tkinter as tk
from tkinter import ttk, filedialog, messagebox, Toplevel
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from tkcalendar import DateEntry
import json

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
        logo_path = "Logo.png"
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
        with open("invoices.txt", "a") as file:
            json.dump(self.invoices, file)

    def show_invoices(self):
        # Create a new window to display invoice information
        top = Toplevel(self.root)
        top.title("Invoices")

        # Load invoices from the text file
        try:
            with open("invoices.txt", "r") as file:
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

def main():
    root = tk.Tk()
    app = InvoiceApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()

