import smtplib
from email.message import EmailMessage
from logger import log_info, log_error

EMAIL_ADDRESS = "abdullahakmaldar@gmail.com"
EMAIL_PASSWORD = "lifa pxcd vons bjxk"

receiver_email = "saimaakmal1708@gmail.com"

subject = "Sales Report"
body = "Please find attached the latest sales report."

file_path = "sales_summary.txt"

try:

    msg = EmailMessage()
    msg["Subject"] = subject
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg.set_content(body)

    with open(file_path, "rb") as file:
        file_data = file.read()
        file_name = file.name

    msg.add_attachment(
        file_data,
        maintype="application",
        subtype="octet-stream",
        filename=file_name
    )

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        smtp.send_message(msg)

    print("Email sent successfully")
    log_info("Email sent successfully")

except Exception as error:

    print("Error sending email:", error)
    log_error(str(error))