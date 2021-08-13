from django.http import HttpResponse, HttpResponseRedirect
from .models import WordListEntry
from django.shortcuts import render
from django.template import loader

def index(request):
    #min_id = WordListEntry.objects.all().order_by('id').first().id
    #entry = WordListEntry.objects.get(pk=min_id)
    #context = {'entry':entry,}
    #output = "/".join(str(w.pk) for w in entry)
    #return render(request,'MnemGen/index.html',context)
    #HttpResponse(output)
    if request.method == "POST":
        address = request.POST['ethAddress']
        try:
            intaddress = int(address)
        except ValueError:
            return render(request, 'MnemGen/index.html',
                          {'eth_Address': 'Address was invalid', })
        return render(request, 'MnemGen/index.html',
                      {'eth_Address': intaddress, })
    else:
        return render(request,'MnemGen/index.html',{})


def poseQuestion(request):
    return render(request,'MnemGen/index.html')

def about(request):
    return HttpResponse("The About Page. Explain the point of the website")
def share(request):
    return HttpResponse("A final share page with twitter and facebook sharing, just share the link to index")

