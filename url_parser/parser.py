import re
import json
import datetime
from .models import UrlAdminModel as Model
from django.http import Http404, HttpResponse

try:
    from urllib.request import urlopen, URLError
    from _thread import start_new_thread
except ImportError:
    from urllib2 import urlopen, URLError
    from thread import start_new_thread


def parse(request):
    if request.is_ajax():
        urls = Model.objects.filter(success=False).order_by('timeshift').values()
        list_urls = [entry for entry in urls]

        for url in list_urls:
            try:
                parsed = parse_url(url['url'])
            except URLError:
                parsed = {'success': False, 'time': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
            url.update(parsed)
            start_new_thread(update_db, (url,))

        json_data = json.dumps(list_urls)
        return HttpResponse(json_data, content_type='application/json')
    else:
        raise Http404


def parse_url(url):
    time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = str(urlopen(url).read().decode('utf-8', 'ignore'))
    title = re.findall(r'<title>(.*?)</title>', html)
    h1 = re.findall(r'<h1>(.*?)</h1>', html)
    charset = re.findall(r'<meta.*charset=(.*?)[" ]', html)

    parse_result = {
        'title': title[0] if len(title) > 0 else None,
        'h1': h1[0] if len(h1) > 0 else None,
        'charset': charset[0] if len(charset) > 0 else None,
        'time': time,
        'success': True,
    }
    return parse_result


def update_db(data):
    Model.objects\
        .filter(url=data['url'])\
        .update(title=data['title'], h1=data['h1'], charset=data['charset'], success=data['success'], time=data['time'])
