# I have created this file - Abhishek
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    params = {'name': 'Abhishek', 'Place': 'Nagpur'}
    return render(request, 'index.html', params)


def analyze(request):
    djtext = request.POST.get('text', 'default')
    remove = request.POST.get('remove', 'OFF')
    upper = request.POST.get('upper','OFF')
    newlineremover = request.POST.get('newlineremover','OFF')
    extraspaceremover=request.POST.get('extraspaceremover','OFF')
    punctuations = '''[]{}-!"#$%&'()*+,./:;<=>?@\^_`\|'''
    analyze=""

    print(len(djtext))
    if remove == 'on' and len(djtext)>0:
        for char in djtext:
            if char not in punctuations:
                analyze = analyze + char
        params = {'Purpose': 'Remove Punctuation', 'AnalyzedText': analyze}
        djtext=analyze

    if upper == 'on' and len(djtext) > 0:
        analyze = djtext.upper()
        params = {'Purpose': 'Change To Upper Case', 'AnalyzedText': analyze}
        djtext=analyze
        # return render(request,'analyze.html',params)

    if newlineremover=='on' and len(djtext)>0:
        analyze=""
        for char in djtext:
            if char!='\n' and char!='\r':
                analyze=analyze+char
        params = {'Purpose': 'New line Remover', 'AnalyzedText': analyze}
        djtext=analyze

    if extraspaceremover=='on' and len(djtext)>0:
        analyze=""
        for index , char in enumerate(djtext):
            print(char)
            if djtext[index] == ' ' and djtext[index+1]==' ':
                pass
            else:
                analyze=analyze+char
        params = {'Purpose': 'New line Remover', 'AnalyzedText': analyze}

    if remove != 'on' and upper != 'on' and newlineremover !='on' and extraspaceremover!='on':
        return HttpResponse('Try to check options mentioned')

    return render(request, 'analyze.html', params)

