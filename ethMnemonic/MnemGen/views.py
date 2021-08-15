from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.urls import reverse
from django.views import View
import sha3
from .models import WordListEntry
from django.shortcuts import render
from django.template import loader

def encrypt(hexs):
    hexs = hexs[2:]
    returnVar = []
    for i in range(0, len(hexs), 3):
        if i + 3 >= len(hexs):
            returnVar.append(WordListEntry.objects.get(pk=(int(hexs[i:], 16))).word)
        else:
            returnVar.append(WordListEntry.objects.get(pk=(int(hexs[i:i + 3], 16))).word)
    return "-".join(returnVar)

def decrypt(mnemonic):
    returnhex = ''
    workArray = mnemonic.split("-")
    for word in workArray:
        returnhex=returnhex+hex(WordListEntry.objects.get(word=word).pk)[2:]
    return "0x"+makeEthAddress(returnhex)

def makeEthAddress(address):
    kck = sha3.keccak_256()
    kck.update(address.encode('ascii'))
    hash = kck.hexdigest()
    returnAddress = ''
    for i in range(len(address)):
        if address[i].isalpha():
            if int(hash[i],16) >= 8:
                returnAddress += address[i].upper()
                continue
        returnAddress += address[i]
    return returnAddress

def index(request):
    if request.method == "POST":
        if 'ethAddress' in request.POST:
            address = request.POST['ethAddress']
            try:
                returnVar = encrypt(address)
            except ValueError:
                return render(request, 'MnemGen/index.html',
                              {'eth_Address': 'Address was invalid', })
            return render(request, 'MnemGen/index.html',
                          {'eth_Address': returnVar, })
        else:
            mnemonic = request.POST['mnemonic']
            try:
                returnVar = decrypt(mnemonic)
            except ObjectDoesNotExist:
                return render(request, 'MnemGen/index.html',
                              {'eth_mnemonic': 'Address was invalid', })
            return render(request, 'MnemGen/index.html',
                          {'eth_mnemonic': returnVar, })
    else:
        return render(request,'MnemGen/index.html',{})


def about(request):
    return render(request,'MnemGen/about.html')
def share(request):
    return render(request,'MnemGen/share.html')

def EthtoMnem(request):
    if request.is_ajax():
        first_name = request.POST.get('first_name', None) # getting data from first_name input
        try:
            returnVar = encrypt(first_name)
        except ValueError:
            returnVar = "Error"
        if first_name: #cheking if first_name and last_name have value
            response = {
                         'msg':returnVar
            }
            return JsonResponse(response) # return response as JSON

def MnemtoEth(request):
    if request.is_ajax():
        mnemonic = request.POST.get('mnem', None) # getting data from first_name input
        try:
            returnVar = decrypt(mnemonic)
        except ValueError:
            returnVar = "Error"
        if mnemonic:
            response = {
                         'msg':returnVar
            }
            return JsonResponse(response)