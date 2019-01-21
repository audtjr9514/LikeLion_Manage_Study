from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def result(request):
    text = request.GET['fulltext']
    
    length = list(text)
    count = length.count(' ')
    for x in range(0,count):
        length.remove(' ')
    words = text.split()
    word_dictionary = {}

    for word in words:
        if word in word_dictionary:
            word_dictionary[word] += 1
        else:
            word_dictionary[word] = 1

    return render(request, 'result.html', {'full': text, 'total' : len(words), 'dictionary': word_dictionary.items(), 'textlength': len(length),'totaltextlength': len(text) })
    
def count(request):
    full_text = request.GET['fulltext']
    word_list = full_text.split()

    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'total': len(word_list) })