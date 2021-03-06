#!/usr/bin/env python
# -*- coding:utf-8 -*-


from flask import Flask

app = Flask(__name__)
app.config.from_object('config')

from view import *

if __name__ == '__main__':
    app.run()