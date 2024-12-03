from ftplib import FTP
from io import StringIO

def hide_data_ftp(host, data, data_type, username='', password=''):
    try:
        ftp = FTP(host)
        ftp.login(username, password)  # Accept credentials dynamically

        if data_type == 'text':
            hidden_data = "Hidden Text: " + data
        elif data_type == 'image':
            hidden_data = "Hidden Image Data: " + data
        else:
            return "Unsupported data type for FTP"

        # Use StringIO to simulate a file-like object
        hidden_file = StringIO(hidden_data)
        ftp.storlines('STOR hidden_data.txt', hidden_file)
        ftp.quit()
        return "Data sent successfully over FTP"
    except Exception as e:
        return f"FTP Error: {str(e)}"