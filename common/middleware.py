from .forms import GetInTouchForm

from bot.main import send_getintouch, send_data

def my_middleware(get_response):

    def middleware(request):
        if not request.path.startswith('/media/') and not request.path.startswith('/static/'):
            data = {
                'REMOTE_ADDR': request.META['REMOTE_ADDR'],
                'HTTP_USER_AGENT': request.META['HTTP_USER_AGENT'],
                'HTTP_COOKIE': request.META['HTTP_COOKIE'],
                'REQUEST_METHOD': request.META['REQUEST_METHOD'],
                'PATH_INFO': request.META['PATH_INFO'],
                'SERVER_NAME': request.META['SERVER_NAME'],
            }
            
            send_data(data)
        if request.method == "POST":
            get_in_touch_form = GetInTouchForm(request.POST)
            if get_in_touch_form.is_valid():
                get_in_touch_form.save()
                name = get_in_touch_form.data['name']
                email = get_in_touch_form.data['email']
                message = get_in_touch_form.data['message']
                send_getintouch(name, email, message)

        response = get_response(request)
        return response

    return middleware
