import socket
import requests

def hide_data_tcp(host, data, data_type):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
            sock.connect((host, 5000))  # Assuming the server is running on port 5000
            
            if data_type == 'text':
                hidden_data = f"Hidden Text: {data}"
            elif data_type == 'image':
                hidden_data = f"Hidden Image Data: {data}"  # Placeholder for actual image handling
            else:
                raise ValueError("Unsupported data type for TCP")

            sock.sendall(hidden_data.encode('utf-8'))
        return "Data sent successfully over TCP"
    except Exception as e:
        return f"TCP Error: {str(e)}"