#from flask import Flask, jsonify
from flask import Flask

# pimoroni imports
# particulate sensor
import pms5003 import PMS5003, ReadTimeoutError
import logging

logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

pms5003 = PMS5003()

#######

application = Flask(__name__)

@application.route("/particulates")
def particulates():
    try:
        readings = pms5003.read()
        logging.info(readings)
    except ReadTimeoutError:
        pms5003 = PMS5003()

  #return jsonify({"ButtonPress":"Success"})
  return readings

if __name__ == "__main__":
  application.run(debug=True)
