import os
import re
import gzip
from datetime import datetime

LOG_DIRECTORY = "apache2/"


def logs_from_files(file_type):
    files = [f for f in os.listdir(LOG_DIRECTORY) if f.startswith(file_type + '.log')]
    files.sort(key=lambda x: int(x.split('.')[2]) if len(x.split('.')) > 2 else 0)

    logs = ""

    for file in files:
        if file.split('.')[-1] == 'gz':
            fo = gzip.open(LOG_DIRECTORY + file, 'rb')
        else:
            fo = open(LOG_DIRECTORY + file, 'rb')
        logs = fo.read().decode("utf-8") + logs
        fo.close()
    return logs


def list_logs():
    logs = logs_from_files('access')
    array_logs = []
    for line in logs.split('\n')[:-1]:
        list_log = list(re.match('^([(\d\.)|:]+) - (.*) \[(.*?)\] "(.*?)" (\d+) (\d+) "(.*?)" "(.*?)"$', line).groups())
        list_log[2] = datetime.strptime(list_log[2], '%d/%b/%Y:%H:%M:%S %z')
        array_logs.append(list_log)
    return array_logs

def logs_header():
    return (
        ['IP', 'ip'],
        ['Username', 'username'],
        ['Date', 'date'],
        ['Request', 'request'],
        ['Answer', 'answer'],
        ['User\'s port', 'usersport'],
        ['Manual request', 'manualrequest'],
        ['User\'s information', 'usersinformation']
    )

def log_from_id(id):
    return list_logs()[id]