from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'login_info'
db = MySQL(app)
# cursor = db.connection.cursor(MySQLdb.cursors.DictCursor)



class Inject():
    def check(self, u, p):
        self.u = u
        self.p = p
        cursor = db.connection.cursor()
        if cursor is not None:
            cursor.execute("SELECT * FROM `info` WHERE `username` = '%s' AND `pass` = '%s'" % (u, p))
            account = cursor.fetchall()
            print(cursor.rowcount)
            if account:
                return 1
            else:
                return 0
        else:
            return o


@app.route('/v1/sanitized/input/', methods=['POST'])
def result():
    if request.method == 'POST':
        req = request.json
        user = req["username"]
        password = req["password"]
        c1 = Inject()
        if c1.check(user, password):
            return jsonify({"result": "Sanitized"})
        else:
            return jsonify({"result": "Unsanitized"})


if __name__ == '__main__':
    app.run(debug=True)
