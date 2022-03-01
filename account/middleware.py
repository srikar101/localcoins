from django.shortcuts import redirect


def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        print('middleware')
        r = request.session.get('user')
        print(r)
        if r is None:
            redirect('/login/')

        response = get_response(request)

        return response

    return middleware