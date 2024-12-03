import socket
import requests

def hide_data_udp(host, data, data_type):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as sock:
            if data_type == 'text':
                hidden_data = f"Hidden Text: {data}"
            elif data_type == 'image':
                hidden_data = f"Hidden Image Data: {data}"  # Placeholder for actual image handling
            else:
                raise ValueError("Unsupported data type for UDP")

            sock.sendto(hidden_data.encode('utf-8'), (host, 5000))  # Send to port 5000
        return "Data sent successfully over UDP"
    except Exception as e:
        return f"UDP Error: {str(e)}"