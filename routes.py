import json
from flask import Flask, render_template

import detail
import log_parser

app = Flask(__name__)
app.debug = True
app.secret_key = "azertyuiop"


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/logs')
def logs():
    return render_template('logs.html', logs=log_parser.list_logs(), header=log_parser.logs_header())


@app.route('/logs/<int:id>')
def show_log(id):
    return render_template('log.html', ziped=zip(log_parser.logs_header(), log_parser.log_from_id(id)), id=id)


@app.route('/logs/<int:id>/ip')
def ip_detail(id):
    return render_template('ip.html', ip_data=detail.ip_detail(id), id=id)


@app.route('/logs/detail/date')
def date_chart():
    return render_template('detail/date.html', date_data=json.dumps(detail.date_data()))


@app.route('/logs/detail/ip')
def ip_chart():
    return render_template('detail/ip.html', ips=json.dumps(detail.ip_data()))