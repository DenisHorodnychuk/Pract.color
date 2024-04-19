from django.shortcuts import render

def index(request):
    if 'count' not in request.session:
        request.session['count'] = 1
    else:
        request.session['count'] += 1

    background_colors = ['#ffccff', '#ffcccc', '#ffffcc', '#ccffcc', '#ccffff', '#ccccff']
    background_color = background_colors[request.session['count'] % len(background_colors)]

    return render(request, 'index.html', {'background_color': background_color})

# Create your views here.
