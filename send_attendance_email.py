import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Load Excel file
df = pd.read_excel("excel .xlsx")

# Department emails (replace with your real emails)
department_emails = {
    "B.C.A. – Bachelor of Computer Applications": "bca@gmail.com",
    "B.Com Finance (Self-Financing)": "bcomsself@gmail.com"
    # add emails as needed
}


# Gmail config
sender_email = "sender@gmail.com"
app_password = "app password"

# SMTP setup
server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login(sender_email, app_password)

# Group by department and send
for Department, group_df in df.groupby("Department"):
    if Department in department_emails:
        receiver_email = department_emails[Department]

        # Prepare message
        student_list = "\n".join(group_df["Name"].tolist())
        message_body = f"Dear HOD,\n\nHere is the attendance list for your department:\n\n{student_list}\n\nRegards,\nTinkerHub Team"

        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Attendance Report – {Department}"
        message.attach(MIMEText(message_body, "plain"))

        server.sendmail(sender_email, receiver_email, message.as_string())
        print(f"✅ Sent email to {receiver_email}")
    else:
        print(f"⚠️ No email found for department: {department}")

server.quit()
