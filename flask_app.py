from flask import Flask
from flask import request
from flask import jsonify
import db_worker as dat
app = Flask(__name__)


@app.route('/activate/', methods=['POST','GET'])
def accept():
    db = dat.database('prod.db')
    akey = request.args.get("akey")
    skey = request.args.get("skey")
    if db.get_apikey(akey) == []:
        return('500')
    else:
        if db.get_settings(skey) == []:
            return('500')
        else:
            return (db.get_settings(skey)[1])


