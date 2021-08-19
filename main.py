from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/v1/sanitized/input/', methods=['POST'])
def result():
    if request.method == 'POST':
        req = request.json
        input = req["payload"]
        if input.isalnum():
            return jsonify({"result": "Sanitized"})
        else:
            return jsonify({"result": "Unsanitized"})


if __name__ == '__main__':
    app.run(debug=True)