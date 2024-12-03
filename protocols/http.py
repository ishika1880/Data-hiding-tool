import requests
import socket

def hide_data_http(url, data, data_type):
    try:
        if data_type == 'text':
            hidden_data = {"hidden": f"Hidden Text: {data}"}
        elif data_type == 'image':
            hidden_data = {"hidden": f"Hidden Image Data: {data}"}  # Placeholder for actual image handling
        else:
            raise ValueError("Unsupported data type for HTTP")

        response = requests.post(url, json=hidden_data)
        response.raise_for_status()  # Ensure HTTP errors are caught
        return f"HTTP Response: {response.text}"
    except requests.RequestException as e:
        return f"HTTP Error: {str(e)}"
    except Exception as e:
        return f"General Error: {str(e)}"