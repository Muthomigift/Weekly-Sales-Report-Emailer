import smtplib, os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

def send_html_report(to, data):
    html_body = (
        '<html><body style="font-family: Arial, sans-serif;">'
        '<h2 style="color: #1F4E79;">Weekly Sales Report</h2>'
        '<table border="1" cellpadding="8" style="border-collapse:collapse;">'
        '<tr style="background:#1F4E79; color:white;"><th>County</th><th>Orders</th><th>Revenue (KES)</th></tr>'
        f'<tr><td>Nairobi</td><td>{data["nairobi_orders"]}</td><td>{data["nairobi_revenue"]:,}</td></tr>'
        f'<tr><td>Mombasa</td><td>{data["mombasa_orders"]}</td><td>{data["mombasa_revenue"]:,}</td></tr>'
        '</table></body></html>'
    )
    msg = MIMEMultipart("alternative")
    msg["Subject"] = "Weekly Sales Report"
    msg["From"] = os.getenv("GMAIL_ADDRESS")
    msg["To"] = to
    msg.attach(MIMEText(html_body, "html"))

    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(
            os.getenv("GMAIL_ADDRESS"),
            os.getenv("GMAIL_APP_PASSWORD")
        )
        server.send_message(msg)
        print(f"Sent to {to}")

send_html_report("ybrysonnie@gmail.com", {"nairobi_orders": 120, "nairobi_revenue": 485000, "mombasa_orders": 85, "mombasa_revenue": 312500})