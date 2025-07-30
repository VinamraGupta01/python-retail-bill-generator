🧾 Retail Billing System
A full-featured desktop billing application built with Python and Tkinter, designed for small retail stores. This GUI-based software supports billing for multiple product categories, automated tax calculation (GST), printing and saving bills, and even sending invoices via email—all packed into a single offline app.

🚀 Features
✅ Easy-to-use graphical interface
✅ Auto item-wise price and GST calculation
✅ Categories supported: 1) Cosmetics, 2) Grocery, 3) Beverages
✅ Customer details input (Name, Phone Number)
✅ Generates formatted printable receipts
✅ Email support: Send invoices from the app
✅ Save and search previous bills by bill number
✅ Clean/reset form functionality
✅ Setup script for easy installation

🧱 Technologies Used
Tool	Purpose
Python 3.x	Main programming language
Tkinter	GUI development
smtplib	Email sending
tempfile & os	File handling for printing and saving
setup.py	To package the application

📁 File Structure
bash
Copy
Edit
Retail-Billing-System/
│
├── Billing.py          # Main GUI application
├── setup.py            # Setup script for installation
├── bills/              # Auto-generated folder to store saved bill files
├── icon.ico            # Optional application icon
├── README.md           # Project documentation


🖥 Installation
📦 Option 1: Run Directly
Make sure Python 3.x is installed.

Install any required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Launch the app:

bash
Copy
Edit
python Billing.py

🛠 Option 2: Install with setup.py
bash
Copy
Edit
python setup.py install

📸 Screenshots
(You can add images here of your GUI interface)
![App Screenshot](screenshots/app-main.png)
Example:

css
Copy
Edit
🧪 Example Use Case
Perfect for:

Retail shopkeepers needing a quick offline billing tool

College mini projects (Python GUI)

Anyone learning real-world Tkinter development

❗ Notes
Ensure internet is active while using the email feature.

Set up "App Password" in Gmail if using two-factor authentication.

📬 Contact
Made by [Your Name]
📧 [youremail@example.com]
🔗 LinkedIn

