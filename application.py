#from flask import Flask, jsonify
from flask import Flask

# pimoroni imports
# particulate sensor
from pms5003 import PMS5003, ReadTimeoutError
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("app started")

pms5003 = PMS5003()

#######

application = Flask(__name__)

@application.route("/particulates")
def particulates():
    #try:
        #readings = pms5003.read()
        #logging.info(readings)
    logging.info("message received")
    #except ReadTimeoutError:
        #pms5003 = PMS5003()

  #return jsonify({"ButtonPress":"Success"})
    #return readings
    return "hello world", 200

if __name__ == "__main__":
  application.run(debug=True, host='0.0.0.0')

