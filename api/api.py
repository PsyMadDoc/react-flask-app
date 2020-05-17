import time
from flask import Flask

app = Flask(__name__)

# Responds to /time URL with a JSON payload sush as:
# {"time": 1581527730.5866282}


@app.route('/time')
def get_current_time():
    return {'time': time.time()}
