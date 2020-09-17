from flask import Flask

# pimoroni imports
# particulate sensor
from pms5003 import PMS5003, ReadTimeoutError
import logging
########

application = Flask(__name__)

######
logging.basicConfig(
    format='%(asctime)s.%(msecs)03d %(levelname)-8s %(message)s',
    level=logging.INFO,
    datefmt='%Y-%m-%d %H:%M:%S')

logging.info("app started")

pms5003 = PMS5003()
#######

@application.route("/particulates")
def particulates():
    global pms5003

    try:
        readings = pms5003.read()
        logging.info(readings)
    except ReadTimeoutError:
        # TODO probably don't need to do this as it's from the example loop
        # should definitely print out the error though
        # QUESTION: should we handle the other possible errors
        pms5003 = PMS5003()

    detailsToReturn = {"PM1.0":readings.pm_ug_per_m3(1.0),
                       "PM2.5":readings.pm_ug_per_m3(2.5),
                       "PM10":readings.pm_ug_per_m3(10),
                       "PM1.0a":readings.pm_ug_per_m3(1.0, True),
                       "PM2.5a":readings.pm_ug_per_m3(2.5, True),
                       "PM10a":readings.pm_ug_per_m3(None, True),
                       ">0.3":readings.pm_per_1l_air(0.3),
                       ">0.5":readings.pm_per_1l_air(0.5),
                       ">1.0":readings.pm_per_1l_air(1.0),
                       ">2.5":readings.pm_per_1l_air(2.5),
                       ">5.0":readings.pm_per_1l_air(5.0),
                       ">10.0":readings.pm_per_1l_air(10.0)}

    # QUESTION: do we want to use jsonify?
    return detailsToReturn

if __name__ == "__main__":
  application.run(debug=True, host='0.0.0.0')


