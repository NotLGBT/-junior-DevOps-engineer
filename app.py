from flask import Flask, jsonify, render_template, request
import monitoring as monitor

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('index.html')

@app.route('/monitoring/test/api', methods=['GET'])
def api_request():
    method_stat = request.args.get('method_stat', 'Memory')
    pattern = request.args.get('pattern', 'firefox')
    interval = int(request.args.get('interval', 20))

    try:
        payload = monitor.stat_extract(method_stat, pattern, interval)
        return jsonify(payload)
    except ValueError as e:
        return jsonify({"error": str(e)}), 400
    except Exception as e:
        return jsonify({"error": f"Unexpected error: {str(e)}"}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)