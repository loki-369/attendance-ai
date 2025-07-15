# Attendance Mailer AI 📧

This project automates sending department-wise student attendance reports via email using data from an Excel sheet.

---

## 🔧 Features

- Reads Excel sheet with student details
- Groups students by their department
- Sends attendance data to each department's email
- 100% free using Gmail SMTP + Python

---

## 📁 Folder Structure

attendance-ai/
├── send_attendance_email.py
├── requirements.txt
├── README.md
└── TinkerHub selection .xlsx ← (optional, for testing)



---

## ⚙️ Requirements

- Python 3.10+
- `pandas` and `openpyxl` libraries
- Gmail account with App Password enabled

Install dependencies:

```bash
pip install -r requirements.txt
📬 Setup Instructions
Enable 2-Step Verification in your Gmail

Go to App Passwords

Generate a 16-digit App Password for "Mail"

Edit the send_attendance_email.py file:

Replace sender_email with your Gmail

Replace app_password with the 16-digit password

Update department_emails with real department email addresses

Update column names if needed (e.g., "Full Name", "Department")

🚀 Run the Script
python send_attendance_email.py

🧠 Example Email Output
Subject: Attendance Report – B.C.A.

Dear HOD,

Here is the attendance list for your department:

- Anas Rahman – Present
- Fathima M – Absent
- Naufal KP – Present

Regards,  
TinkerHub Team
🛡️ Notes
Do NOT share your Gmail password or App Password publicly

Use a .gitignore to exclude .xlsx files if needed

💡 Author
Made with ❤️ by Ishal Ahammed
