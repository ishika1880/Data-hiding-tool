from flask import Flask, request, jsonify
from protocols.tcp import hide_data_tcp
from protocols.udp import hide_data_udp
from protocols.http import hide_data_http
from protocols.ftp import hide_data_ftp
from protocols.dns import hide_data_dns
from protocols.smtp import hide_data_smtp

app = Flask(__name__)

# Mapping protocols to their handlers
PROTOCOL_HANDLERS = {
    'tcp': hide_data_tcp,
    'udp': hide_data_udp,
    'http': hide_data_http,
    'ftp': hide_data_ftp,
    'dns': hide_data_dns,
    'smtp': hide_data_smtp,
}

@app.route('/hide', methods=['POST'])
def hide_data():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'Request must be in JSON format'}), 400

        protocol = data.get('protocol')
        hidden_data = data.get('data')
        data_type = data.get('data_type')
        target = data.get('target')

        # Validate required fields
        missing_fields = [field for field in ['protocol', 'data', 'data_type', 'target'] if field not in data]
        if missing_fields:
            return jsonify({'error': f'Missing required fields: {", ".join(missing_fields)}'}), 400

        # Validate data type
        if data_type not in ['text', 'image']:
            return jsonify({'error': 'Unsupported data type. Please use "text" or "image".'}), 400

        # Retrieve the handler for the specified protocol
        handler = PROTOCOL_HANDLERS.get(protocol)
        if not handler:
            return jsonify({'error': f'Invalid protocol: {protocol}'}), 400

        # Call the handler
        try:
            result = handler(target, hidden_data, data_type)
        except Exception as e:
            return jsonify({'error': f'Error in protocol handler: {str(e)}'}), 500

        return jsonify({'result': result})

    except Exception as e:
        return jsonify({'error': f'Internal server error: {str(e)}'}), 500

if __name__ == '__main__':
    app.run(debug=True)
