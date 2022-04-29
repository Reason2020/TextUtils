#I have created this file - Reason Shrestha
from pickle import FALSE
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    # data = {
    #     'name': 'Reason Shrestha',
    #     'aspirant': 'AI Engineer'
    # }
    return render(request, 'index.html')

def analyze(request):
    #get the value from textarea of index page
    textvalue = request.POST['text']
    #get check box value
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charactercounter = request.POST.get('charactercounter', 'off')

    #check if any of the checkboxes are on
    if removepunc == 'on' or fullcaps == 'on' or newlineremover == 'on' or extraspaceremover == 'on':
        purpose = ""
        #check which checkbox is on
        if removepunc == 'on':
            updated = ""
            punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
            for char in textvalue:
                if char not in punctuations:
                    updated += char
            purpose += 'Removed Punctuations, '
            textvalue = updated
        if fullcaps == 'on':
            updated = ""
            for char in textvalue:
                updated += char.upper()
            purpose += 'Capitalized, '
            textvalue = updated
        if newlineremover == 'on':
            updated = ""
            for char in textvalue:
                if char != '\n' and char != '\r':
                    updated += char
            purpose += 'New Line Removed, '
            textvalue = updated
        if extraspaceremover == 'on':
            updated = ""
            for index, char in enumerate(textvalue):
                if textvalue[index] == " " and textvalue[index+1] == " ":
                    pass
                else:
                    updated += char
            purpose += 'Extra Space Removed, '
            textvalue = updated
        analyzed = updated
        params = {
            'purpose': purpose,
            'analyzed_text': analyzed
        }
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse('You have not selected what to do to your text')


#Just trying URL Routing
def capfirst(request):
    return HttpResponse('Capitalize First <a href="/">Back To Home</a>')

def newlineremove(request):
    return HttpResponse('Newline Remove <a href="/">Back To Home</a>')
    
def spaceremove(request):
    return HttpResponse('Space Remove <a href="/">Back To Home</a>')

def charcount(request):
    return HttpResponse('Char count <a href="/">Back To Home</a>')

def ex1(request):
    return render(request, 'navigator.html')