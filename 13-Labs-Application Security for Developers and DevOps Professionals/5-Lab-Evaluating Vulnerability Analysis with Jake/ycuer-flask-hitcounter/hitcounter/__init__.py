"""
HitCounter Service
"""
from flask import Flask

app = Flask(__name__)

import hitcounter.routes
