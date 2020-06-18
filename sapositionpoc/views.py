from django.shortcuts import render
from django.http import HttpResponse
from .models import Sa
from .forms import SaForm, RawSaForm



# Create your views here.
def saquery(request):
    return render(request, 'sapositionpoc/saquery.html')

def saresult(request):
    if request.method == 'POST':
        search_id = request.POST.get('textfield', None)

        sabacklognum = Sa.objects.get(sa_number=search_id)
        #saforecastnum = Sa.objects.filter(sabacklognum)
        #return HttpResponse(search_id)
        return HttpResponse(sabacklognum)
        #return HttpResponse("it POSTS")
    else:
        return HttpResponse("it GETS")
        #return render(request, 'sapositionpoc/saquery.html')

#def saresult(request):
    #if request.method == 'POST':
#        search_id = request.POST.get('textfield', None)
#        try:
#                sabacklognum = Sa.objects.get(sa_number = searchid)
#                html = ("<H1>%s</H1>", sabacklognum)
#                return HttpResponse (html)
#            except Sa.DoesNotExist:
            #    return HttpResponse("no SA")
    #else:
        #return render(request,'sapositionpoc/saquery.html')

#form view
def sa_form_view(request):
    form = SaForm(request.POST or None)
    if form.is_valid():
        form.save()
        form = SaForm()
    context = {
        'form': form
    }
    return render(request, 'sapositionpoc/sa_form.html',context)

def index(request):
    #security_assessment = Sa.objects.all()
    obj = Sa.objects.get(id=1)
    #context = {
    #    'sa_number': obj.sa_number,
    #    'sa_position': obj.sa_position,
    #}
    context = {
        'object': obj
    }
    return render(request, 'sapositionpoc/sa_position.html',context)
    #'security_assessment':security_assessment
    #return HttpResponse("Hello, world. You're at the sapositionpoc index.")
def test(request):
    my_context = {
    "my_text": " This is about us",
    "this_is_true": True,
    "my_number": 123,
    "my_list": [123, 1235, 1236]
    }
    return render(request,'sapositionpoc/test.html', my_context)




#def sa_form_view(request):
    #print(request.GET)
    #print(request.POST)
#    if request.method == 'POST':
#        new_sa= request.POST.get('sa_number')
#        print(new_sa)
#    context = {}
#    return render(request, 'sapositionpoc/sa_form.html',context)

#def sa_form_view(request):
#    my_form = RawSaForm()
###        if my_form.is_valid():
    #        print(my_form.cleaned_data)
    #    else:
    #        print(my_form.errors)
    #context = {
    #    'form': my_form
#    }
#    return render(request, 'sapositionpoc/sa_form.html',context)
