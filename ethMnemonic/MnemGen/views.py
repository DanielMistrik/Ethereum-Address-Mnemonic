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
    """
    Converts the provided ethereum address into a mnemonic
    :param hexs: The hexadecimal version of the ethereum address with 0x prefix
    :return: Returns the mnemonic that was converted from the ethereum address from hexs
    """
    hexs = hexs[2:]
    returnVar = []
    for i in range(0, len(hexs), 3):
        if i + 3 >= len(hexs):
            returnVar.append(WordListEntry.objects.get(pk=(int(hexs[i:], 16))).word)
        else:
            returnVar.append(WordListEntry.objects.get(pk=(int(hexs[i:i + 3], 16))).word)
    return "-".join(returnVar)

def decrypt(mnemonic):
    """
    Converts the provided mnemonic into a EIP-55 abiding ethereum address
    :param mnemonic: The mnemonic, String, to be converted
    :return: A String that represents the hexadecimal ethereum address with 0x prefix
    """
    returnhex = ''
    workArray = mnemonic.split("-")
    for word in workArray:
        returnhex=returnhex+hex(WordListEntry.objects.get(word=word).pk)[2:]
    return "0x"+makeEthAddress(returnhex)

def makeEthAddress(address):
    """
    Converts an all lowercase address into an EIP-55 abiding one
    :param address: The lowercase address to be modified without 0x prefix
    :return: The EIP-55 abiding ethereum address without 0x prefix
    """
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
    """
    Renders the main html page
    """
    return render(request,'MnemGen/index.html',{})


def about(request):
    """
    Renders the about page
    """
    return render(request,'MnemGen/about.html')

def EthtoMnem(request):
    """
    Processes an ajax request and converts the provided ethereum address into a mnemonic
    :param request: Ajax request containing the ethereum address to be converted
    :return: Json response containing the converted mnemonic
    """
    if request.is_ajax():
        addrss = request.POST.get('addrss', None)
        try:
            returnVar = encrypt(addrss)
        except Exception:
            returnVar = "Error"
        if addrss: #cheking if first_name and last_name have value
            response = {
                         'msg':returnVar
            }
            return JsonResponse(response) # return response as JSON

def MnemtoEth(request):
    """
    Processes an ajax request and converts the provided mnemonic into a EIP-55 abiding ethereum address
    :param request: Ajax request with the mnemonic to be converted
    :return: Json response that contains the EIP-55 abiding converted ethereum address
    """
    if request.is_ajax():
        mnemonic = request.POST.get('mnem', None)
        try:
            returnVar = decrypt(mnemonic)
        except Exception:
            returnVar = "Error"
        if mnemonic:
            response = {
                         'msg':returnVar
            }
            return JsonResponse(response)

def MnemChecker(request):
    """
    Processes an ajax request and determines if the provided mnemonic is valid
    :param request: Ajax request with the corresponding mnemonic
    :return: Returns a JSON response with the verdict of whether the mnemonic is valid, outputs "Valid", or invalid, outputs "Invalid"
    """
    if request.is_ajax():
        mnemonic = request.POST.get('mnem',None)
        isValid = False
        if not mnemonic is None:
            words = mnemonic.split('-')
            if len(words) == 14:
                for i in range(14):
                    try:
                        WordListEntry.objects.get(word=words[i])
                        if i==13:
                            isValid = True
                    except Exception:
                        break;
        response = {
            'msg':"Valid" if isValid else "Invalid"
        }
        print(response)
        return  JsonResponse(response)
