from django.http import HttpResponse
import html
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.middleware.csrf import get_token
from django.shortcuts import render

def dumpdata(place, data) :
    retval = ""
    if len(data) > 0 :
        retval += '<p>Incoming '+place+' data:<br/>\n'
        for key, value in data.items():
            retval += html.escape(key) + '=' + html.escape(value) + '</br>\n'
        retval += '</p>\n'
    return retval

@csrf_exempt
def getform(request):
    response = """<p>Impossible GET guessing game...</p>
        <form>
        <p><label for="guess">Input Guess</label>
        <input type="text" name="guess" size="40" id="guess"/></p>
        <input type="hidden" name="csrfmiddlewaretoken" 
            value="token"/>
        <input type="submit"/>
        </form>"""

    token = get_token(request)
    response = response.replace('__token__', html.escape(token))

    response += dumpdata('POST', request.POST)
    return HttpResponse(response)


class GuessGameViev(View):
        def get(self, request):
            return render(request, 'game/game.html')

        def post(self, request):
            return HttpResponse("POST")

def cookie_view(request):
    username = request.GET.get('username')

    if username:
        response = HttpResponse(f"Hello, {username}! We've set your username as a cookie.")
        response.set_cookie('username', username, max_age=86400)
    elif 'username' in request.COOKIES:
        username = request.COOKIES['username']
        response = HttpResponse(f"Welcome back, {username}!")
    else:
        response = HttpResponse("Hello! Please provide your username as a GET parameter.")

    return response