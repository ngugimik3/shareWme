from flask import Flask, request, send_file, jsonify
import os
from file_handler import save_file, get_file_path, delete_file, list_files

app = Flask(__name__)

@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        file = request.files.get('file')
        if not file:
            raise ValueError('No file provided')
        metadata = save_file(file)
        return jsonify({'message': 'File uploaded successfully', 'metadata': metadata}), 200
    except ValueError as e:
        return jsonify({'error': str(e)}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/download/<filename>', methods=['GET'])
def download_file(filename):
    try:
        file_path = get_file_path(filename)
        return send_file(file_path, as_attachment=True)
    except FileNotFoundError as e:
        return jsonify({'error': str(e)}), 404

@app.route('/delete/<filename>', methods=['DELETE'])
def delete_file_route(filename):
    if delete_file(filename):
        return jsonify({'message': f'{filename} deleted successfully'}), 200
    return jsonify({'error': f'{filename} not found'}), 404

@app.route('/list', methods=['GET'])
def list_files_route():
    return jsonify({'files': list_files()}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

