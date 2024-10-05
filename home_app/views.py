from django.http import HttpResponse

def home_app(request):
    content = '<h1> Home <h1>'\
            '<ul>'\
            '  <li> <a href="/hello/vic"> Hello </a> </li>'\
            '  <li> <a href="/calc/10/10" > Calc </a> </li>'\
            '</ul>'
    return  HttpResponse(content)
