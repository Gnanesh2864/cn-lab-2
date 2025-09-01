import smtplib
import logging
from email.mime.text import MIMEText

logging.basicConfig(filename="smtp_log.txt", level=logging.INFO)

smtp_server = "smtp.gmail.com"
port = 587
sender_email = "devratharaisersalaar@gmail.com"
password = "qhkoqbyorzqdavbz"   # <-- use App Password here
receiver_email = "koushik_2301me25@iitp.ac.in"
for i in range(50):
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(sender_email, password)

        msg = MIMEText("test for smtp")
        msg["Subject"] = "hi"
        msg["From"] = sender_email
        msg["To"] = receiver_email

        server.sendmail(sender_email, receiver_email, msg.as_string())
        logging.info("Email sent successfully")
        print("✅ Email sent successfully!")
        server.quit()

    except Exception as e:
        logging.error(f"SMTP error: {e}")
        print("❌ Error:", e)
