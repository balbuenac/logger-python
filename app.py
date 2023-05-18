from flask import Flask
from flask import request, jsonify
import logging
from datadoglog import DatadogFormatter

app = Flask(__name__)

# Init Logging
logger = logging.getLogger()
file_handler = logging.FileHandler('logs.log')
file_handler.setFormatter(DatadogFormatter())
logger.addHandler(file_handler)

@app.route('/api')
def api():
    num_arg = request.args.get('num')
    logger.setLevel(logging.INFO)
    logger.info(num_arg)
    try:
        val = int(num_arg)
        if val == 5:
            raise AttributeError("Atribute Error") 
        elif val == 3:
            raise NotImplementedError("NotImplemented Error")
    except Exception as e:
        logger.setLevel(logging.ERROR)
        logger.error(e)
        return jsonify(Result="Fail"), 500
    return jsonify(Result="Success"), 200

if __name__ == "__main__":
    app.run(debug=True, port=6000)

# !pip install datadog-log