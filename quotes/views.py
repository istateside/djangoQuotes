from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
# from django.template import RequestContext, loader

from .models import Quote


def index(request):
    latest_quotes_list = Quote.objects.order_by('-id')[:5]
    context = { 'quotes': latest_quotes_list }
    return render(request, 'quotes/index.html', context)

def detail(request, quote_id):
    quote = get_object_or_404(Quote, pk=quote_id)
    return render(request, 'quotes/detail.html', { 'quote': quote })
    
def quote_author(request, quote_id):
    response = "You're looking at the author of quote %s."
    return HttpResponse(response % quote_id)
    
def edit_quote(request, quote_id):
    return HttpResponse("You're editing quote %s." % quote_id)