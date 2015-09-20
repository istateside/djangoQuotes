from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from .models import Quote

class IndexView(generic.ListView):
    template_name = 'quotes/index.html'
    context_object_name = 'quotes'
    
    def get_queryset(self):
        """Return the last five published quotes"""
        return Quote.objects.order_by('-id')[:5]
        
class DetailView(generic.DetailView):
    model = Quote
    template_name = 'quotes/detail.html'

def update_quote(request, pk):
    quote = get_object_or_404(Quote, pk=pk)
    try:
        bodyText = request.POST['body'].strip()
        if len(bodyText) == 0:
            raise KeyError
    except (KeyError):
        return render(request, 'quotes/detail.html', {
            'quote': quote,
            'error_message': "No body? Maybe!"
        })
    else:
        quote.body = bodyText
        quote.save()
        return HttpResponseRedirect(reverse('quotes:detail', args=(quote.id,)))
    
    
    # return HttpResponse("You're editing quote %s." % quote_id)
    
def new_quote(request):
    return HttpResponse("This will be a form to create new quotes.")
    
def create_quote(request, params):
    return HttpResponse("I guess the create endpoint?")