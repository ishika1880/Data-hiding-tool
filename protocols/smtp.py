import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import base64

def hide_data_smtp(email, data, data_type, smtp_server, smtp_port, username, password):
    try:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = username
        msg['To'] = email
        msg['Subject'] = 'Hidden Data'

        if data_type == 'text':
            hidden_data = "Hidden Text: " + data
            msg.attach(MIMEText(hidden_data, 'plain'))
        elif data_type == 'image':
            hidden_data = "Hidden Image Data"
            msg.attach(MIMEText(hidden_data, 'plain'))

            # Decode base64 image data and attach
            try:
                image_data = base64.b64decode(data)
                image_attachment = MIMEBase('application', 'octet-stream')
                image_attachment.set_payload(image_data)
                encoders.encode_base64(image_attachment)
                image_attachment.add_header('Content-Disposition', 'attachment; filename="hidden_image.jpg"')
                msg.attach(image_attachment)
            except Exception as img_e:
                return f"Error handling image data: {str(img_e)}"
        else:
            return "Unsupported data type for SMTP"

        # Send the email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(username, password)
            server.send_message(msg)

        return "Data sent successfully over SMTP"
    except Exception as e:
        return f"SMTP Error: {str(e)}"
