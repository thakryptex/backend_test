import re
import time
import json
from datetime import datetime
from .models import UrlAdminModel as Model
from django.http import Http404, HttpResponse
from threading import Thread

""" allows to use python2 and python3 """
try:
    from urllib.request import urlopen, URLError
    from queue import Queue
except ImportError:
    from urllib2 import urlopen, URLError
    from Queue import Queue


parsing = False  # 'True' if parsing process is working
upload_queue = Queue()  # Thread-safe queue that collect data that needs to be send to the client
threads = []  # list of threads


# initialize parsing process
def start(request):
    if request.is_ajax():
        global parsing
        parsing = True

        data = Model.objects.filter(success=False).order_by('timeshift').values()

        # transfer to dictionary where key = 'timeshift', value = 'url', like this: {1: [urls], 2: [urls], 3: [urls]}
        timeshifts = {d['timeshift']: [a['url'] for a in data if a['timeshift'] == d['timeshift']] for d in data}

        thread = Thread(target=parse, args=(timeshifts,))
        thread.start()

        return HttpResponse(status=200)  # tells the client that parsing process initiated
    else:
        raise Http404


# send new info from the queue to the client
def refresh(request):
    if request.is_ajax() and parsing:
        if not upload_queue.empty():
            data = []
            while not upload_queue.empty():  # get data until queue becomes empty
                data.append(upload_queue.get())
            json_data = json.dumps(data)
            return HttpResponse(json_data, content_type='application/json')  # send new data to the client
        else:
            return HttpResponse(status=204)  # if there is no new data, send status 204 = 'No content'
    else:
        raise Http404  # if request is not from ajax or parsing process isn't initiated, then error


# called by 'start' method, works according timeshift of URLs
def parse(timeshifts):
    passed = 0
    for shift in sorted(timeshifts):
        time.sleep(shift - passed)  # sleeps according to its timeshift
        passed += shift

        thread = Thread(target=parse_list, args=(timeshifts[shift],))  # parse list of URLs with the same timeshift
        thread.start()
        threads.append(thread)  # add this thread to the list of threads

    for t in threads:  # join all threads
        t.join()

    time.sleep(3)
    global parsing
    parsing = False  # parsing is over


# called by 'parse' method, parse sites one-by-one from the list of URL with equal timeshift
def parse_list(urls):
    for url in urls:
        data = Model.objects.filter(url=url).values()[0]
        try:
            parsed = parse_url(url)  # if some errors occurs, we save parsing result as 'error'
        except URLError:
            parsed = {'success': False, 'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
        data.update(parsed)  # add new data to the dictionary
        global upload_queue
        upload_queue.put(data)

        thread = Thread(target=update_db, args=(data,))
        thread.start()
        threads.append(thread)


# called by 'parse_list' method, parse one exact URL and return collected data
def parse_url(url):
    time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    html = str(urlopen(url, timeout=3).read().decode('utf-8', 'ignore'))  # waits for 3 seconds to get an answer
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


# called by 'parse_list' method, save collected data to database by updating
def update_db(data):
    Model.objects\
        .filter(url=data['url'])\
        .update(title=data['title'], h1=data['h1'], charset=data['charset'], success=data['success'], time=data['time'])
