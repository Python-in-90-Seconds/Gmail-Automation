import smtplib, ssl

sender = "your@gmail.com"
password = "your_app_password"  # Not your normal password!
receiver = "friend@example.com"

subject = "No Login Needed"
body = "This email was sent using Python and an app password."

msg = f"Subject: {subject}\n\n{body}"

context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(sender, password)
    server.sendmail(sender, receiver, msg)
