#i have creatd this file-shrinkhala

from django.http import HttpResponse
from django.shortcuts import render

def home(request):
     return render(request,'index2.html')

def analyze(request):
    #get the text
    textdj=request.POST.get('text','default')

    removepunc=request.POST.get('removepunc','off')
    fullcaps=request.POST.get('fullcaps','off')
    newlineremover = request.POST.get('newlineremover', 'off')
    removespace= request.POST.get('removespace', 'off')
    charcount = request.POST.get('charcount', 'off')

    #check punchuation
    if removepunc=="on":
        puntuations='''!@~`$#%^&*()_+=-|}{\][":?><';/.,'''
        analyzed=" "
        for char in textdj:
            if char not in puntuations:
                analyzed=analyzed+char
        params={'purpose':'removed punctuations','analyzed_text':analyzed}
        textdj=analyzed
        
    #change uppercase
    if fullcaps=="on":
        analyzed=" "
        for char in textdj:
            analyzed=analyzed+char.upper()
        params={'purpose':'change to uppercase','analyzed_text':analyzed}
        textdj = analyzed
        #return render(request,'analyze2.html',params)

     #remove new line
    if newlineremover=="on":
        analyzed = " "
        for char in textdj:
            if char !="\n" and char!="\r":
               analyzed=analyzed+char
        params = {'purpose': 'remove new lines','analyzed_text': analyzed}
        textdj = analyzed

    #remove extra space
    if removespace == "on":
        analyzed = " "
        for index,char in enumerate(textdj):
            if not(textdj[index]== " " and textdj[index+1]==" "):
                 analyzed = analyzed +char
        params = {'purpose': 'remove new lines', 'analyzed_text': analyzed}
        textdj = analyzed

    #count all character
    if charcount == "on":
        count=0
        for char in textdj:
            if not(char==" "):
                count=count+1
        params = {'purpose': 'count all characters','analyzed_text':textdj,'character':count}

    if(removepunc!="on" and fullcaps!="on" and newlineremover!="on" and removespace != "on" and charcount != "on"):
        return HttpResponse("<h3>please select any operation and try again!!</h3>")

    return render(request, 'analyze2.html', params)

