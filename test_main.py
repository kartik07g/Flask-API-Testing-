import unittest
from flask import request, jsonify
class test_result(unittest.TestCase):
    def test_result(self):
        if request.method == 'POST':
            req = request.json
            input = req["payload"]
            if input.isalnum():
                return jsonify({"result": "Sanitized"})
            else:
                return jsonify({"result": "Unsanitized"})


if __name__ == '__main__':
    unittest.main()
    