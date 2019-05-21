import json
import urllib

def post_message_to_slack(data, web_hook_url):
    method = 'POST'
    request_headers = {'Content-Type': 'application/json; charset=utf-8'}
    body = json.dumps(data).encode("utf-8")
    request = urllib.request.Request(
        url=web_hook_url,
        data=body,
        method=method,
        headers=request_headers
    )
    urllib.request.urlopen(request)
