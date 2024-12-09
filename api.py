from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def process_url():
    input_url = request.args.get('url')
    if not input_url:
        return jsonify({'error': 'URL not provided'}), 400
    try:
        result = subprocess.run(
            ['python3', 'cpvod.py', input_url],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )
        if result.returncode != 0:
            return jsonify({'error': result.stderr}), 500
        return jsonify({'response': result.stdout.strip()})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)