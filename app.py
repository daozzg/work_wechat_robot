#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
@version: 1.0.0
@author: zheng guang
@contact: zg.zhu@daocloud.io
@time: 2019/7/4 4:56 PM
"""

from flask import Flask, request, Response
import requests
import arrow
import logging
import json
import os

LOG = logging.getLogger(__name__)
app = Flask(__name__)

WECAHT_API = os.getenv('WECAHT_API', "https://qyapi.weixin.qq.com/cgi-bin/webhook/send?key={}")
KEY = os.getenv('ROBOT_KEY', '')
ALEAT_MANAGER_URL = os.getenv('ALEAT_MANAGER_URL', '')


def send_wechat_msg(key, message):
    data = {
        "msgtype": "markdown",
        "markdown": {
            "content": message
        }
    }
    if not key and KEY:
        key = KEY
    if not isinstance(message, str):
        data = message
    LOG.debug("send wechat msg: %s", data)
    respose = requests.post(WECAHT_API.format(key), json=data)
    LOG.info("send message result: %s:%s", respose.status_code, respose.text)
    if respose.status_code == 200:
        return True
    else:
        return False


def try_get_value(data_dict, keys, default_value=""):
    for key in keys:
        if data_dict.get(key):
            return data_dict.get(key)
    return default_value


@app.route('/prometheus_webhook', methods=['POST'])
def prometheus_webhook():
    bearer_token = request.headers.get('Authorization', 'bearer_token ').split(" ")
    if len(bearer_token) != 2:
        get_result(error="bearer_token can not null")
    receiver = bearer_token[1]

    data = request.get_json()
    LOG.debug("receive msg: %s", data)
    msg = ""
    for alert in data.get('alerts'):
        status = alert.get('status')
        status_color = 'warning' if status == 'firing' else 'info'
        status = '告警' if status == 'firing' else '已恢复'
        labels = alert.get('labels', {})
        annotations = alert.get('annotations', {})
        resource_name = try_get_value(labels,
                                      ["resource_name", "deployment", "daemonset", "statefulset", "pod", "pod_name",
                                       "instance"], 'cluster')
        resource = "{namespace}{resource_name}".format(
            namespace="{}/".format(labels.get("namespace")) if labels.get("namespace") else '',
            resource_name=resource_name)

        message = try_get_value(annotations, ["message", "description"], "")
        action = annotations.get("Action", '')
        runbook_url = annotations.get("runbook_url", '')
        action_msg = ""
        if action:
            if runbook_url:
                action_msg = ">处理建议: <font color=\"comment\"> {}</font> [more]({})  ".format(action, runbook_url)
            else:
                action_msg = '''>处理建议: <font color="comment">{}</font>  '''.format(action)

        msg = '''
<font color="{_status_color}">{_status}</font>: [{_title}]({_alert_namager_url})  
>级别: <font color="comment">{_severity}</font>  
>资源: <font color="comment">{_resource}</font> [监控源]({_source})  
>描述: <font color="comment">{_message}</font> 
{_action_msg}  
\n
'''.format(_title=labels.get("alertname", ' '), _resource=resource, _status_color=status_color, _status=status,
           _message=message, _source=annotations.get('generatorURL'), _action_msg=action_msg,
           _severity=try_get_value(labels, ["Severity", "severity"], "critical"),
           _alert_namager_url=ALEAT_MANAGER_URL if ALEAT_MANAGER_URL else alert.get('externalURL', ' '))

        result = send_wechat_msg(receiver, msg)

    return get_result(error=result)


def get_result(text='', receiver='', error=""):
    if isinstance(error, bool):
        if error:
            error = ""
        else:
            error = "send alert failed"
    result = {
        "receiver": receiver,
        "text": text,
    }
    if error:
        return Response(json.dumps({"error": error}), mimetype='application/json', status=400)
    return Response(json.dumps(result), mimetype='application/json')


if __name__ == '__main__':
    logging.basicConfig(level=logging.getLevelName(os.getenv('LOG_LEVEL', 'DEBUG')),
                        format='%(asctime)s %(name)s %(levelname)-8s %(message)s')
    LOG.info("app started")
    app.run('0.0.0.0', '8080')
