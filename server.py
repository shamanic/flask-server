# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""Entry point for the server application."""
"""
import os
import ssl
import json
import logging
import traceback
from datetime import datetime
from flask import Flask

#from .factory import create_app, create_user
#app = create_app(debug=True)
app = Flask(__name__)


# Other Options for run() params: threaded=True
def main():
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLSv1_2)
    ctx.load_cert_chain(os.path.join('flask_api/ssl', 'localhost.crt'), os.path.join('flask_api/ssl', 'localhost.key'))
    app.run(ssl_context=ctx, debug=False)
    app.logger.info('app started')
"""

from app import app
