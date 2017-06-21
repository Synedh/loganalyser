import requests

import log_parser


def ip_detail(id):
    if type(id) == int:
        ip = log_parser.log_from_id(id)[0]
    else:
        ip = id
    response = requests.get('http://ipinfo.io/' + ip + '/json')
    if response.status_code != 200:
        print("Error " + " : " + str(response))
    return response.json()


def date_data():
    logs = log_parser.list_logs()
    dates = [log[2].strftime('%Y-%m-%d') for log in logs]
    sumed_dates = []
    for date in dates:
        for sumed_date in sumed_dates:
            if date == sumed_date['date']:
                sumed_date['value'] += 1
                break
        else:
            sumed_dates.append({'date': date, 'value': 1})
    return sumed_dates


def ip_data():
    ips = [log[0] for log in log_parser.list_logs() if log[0] != '::1']
    summed_ips = []
    for ip in ips:
        for summed_ip in summed_ips:
            if ip == summed_ip['ip']:
                summed_ip['value'] += 1
                break
        else:
            summed_ips.append({'ip': ip, 'value': 1})
    return summed_ips
