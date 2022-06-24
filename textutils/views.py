# I have created this file -- Sachin Singh

 
from django.http import HttpResponse
from django.shortcuts import render
import re

def index(request):
    return render(request,'index.html')

def analyse(request):
    text_analyse = request.POST.get('text','default')

    remo_punc = request.POST.get('removepunc','off')
    capital = request.POST.get('capitalise','off')
    lower = request.POST.get('lowercase','off')
    removespace = request.POST.get('space_remover','off')
    removenewlines = request.POST.get('remnwlines','off')
    char_count = request.POST.get('charcount','off')

    ans = ''
    temp_text = text_analyse

    punctuations = '''!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~'''
    if remo_punc == 'on':
        for char in temp_text:
            if char not in punctuations:
                ans+=char
        temp_text=ans
     
    if capital == 'on':
        ans = temp_text.upper()
        temp_text = ans

    if lower == 'on':
        ans = temp_text.lower()
        temp_text = ans

    if removespace =='on':
        ans = re.sub(' +',' ',temp_text)
        temp_text = ans
         
    if removenewlines == 'on':
        ans=""
        for char in temp_text:
            if char != "\n" and char != "\r": # why we are writing here 'char != "\r" '
                ans+=char
        temp_text = ans

     
    count=0
    if char_count == 'on':
        for char in temp_text:
            if char!=' ':
                count+=1
    
    if temp_text == text_analyse:
        ans = temp_text

    params = {'rslt':ans,'char':count}
    return render(request,'analyse.html',params)