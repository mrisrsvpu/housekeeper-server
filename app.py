import logging
from datetime import datetime, timedelta
from json import JSONDecodeError
from sys import stdout

import pytz
import requests
import sentry_sdk
from flask import Flask, Response, abort, request
from icalendar import Calendar, Event
from sentry_sdk.integrations.flask import FlaskIntegration

log = logging.getLogger(__name__)
log.addHandler(logging.StreamHandler(stdout))

try:
    sentry_sdk.init(
        dsn="https://3e7faf13b25a4104aa81c6e0b0cfbbd5:488995de1d394590bcf2077b4ec7489a@sentry-prod.mris.rsvpu.ru/2",
        integrations=[FlaskIntegration()]
    )
except:
    log.exception('Invalid sentry configuration')

app = Flask(__name__)

@app.route('/', methods=['POST'])
def get_housekeepere_event():
    log.info('Housekeeper: %s', request.json)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
