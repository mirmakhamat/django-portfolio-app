from bot.main import send_data


def my_middleware(get_response):

    def middleware(request):
        if not request.path.startswith('/media/') and not request.path.startswith('/static/'):
            data = {
                'REMOTE_ADDR': request.META.get('REMOTE_ADDR'),
                'HTTP_USER_AGENT': request.META.get('HTTP_USER_AGENT'),
                'HTTP_COOKIE': request.META.get('HTTP_COOKIE'),
                'REQUEST_METHOD': request.META.get('REQUEST_METHOD'),
                'PATH_INFO': request.META.get('PATH_INFO'),
                'SERVER_NAME': request.META.get('SERVER_NAME'),
            }

            send_data(data)

        response = get_response(request)
        return response

    return middleware
