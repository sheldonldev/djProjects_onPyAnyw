from django.shortcuts import render
from django.http import HttpResponse


# https://docs.djangoproject.com/en/3.0/ref/request-response/#django.http.HttpRequest.COOKIES
# HttpResponse.set_cookie(key, value='', max_age=None, expires=None, path='/',
#     domain=None, secure=None, httponly=False, samesite=None)
def cookie(request):

    print(request.COOKIES)
    real_cookie = request.COOKIES.get('csrftoken')

    coursera_val = request.COOKIES.get('coursera', None)
    sakai_val = request.COOKIES.get('sakai', None)

    resp = HttpResponse()

    if coursera_val:
        resp.set_cookie('coursera', int(coursera_val) + 1)   # No expired date = until browser close
    else:
        resp.set_cookie('coursera', 1)                       # No expired date = until browser close

    resp.set_cookie('sakai', 42, max_age=1000)   # seconds until expire

    resp = HttpResponse(
        f"""
        csrftoken is given.\n\r\n\r
        coursera value is {str(coursera_val)}.\n\r\n\r
        sakai value is {str(sakai_val)}.\n\r\n\r
        """
    )
    return resp


# https://www.youtube.com/watch?v=Ye8mB6VsUHw
def visit_counter(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits

    # if num_visits > 4:
    #     del(request.session['num_visits'])

    return HttpResponse(f'visited {str(num_visits)} times')