import http.client


def check_url(url):
    conn = http.client.HTTPConnection(url.netloc)
    conn.request("HEAD", url.path)
    r = conn.getresponse()
    if r.status == 404:
        raise Exception('Connection aborted')