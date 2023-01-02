from django.shortcuts import render

# Create your views here.
def operations2(request):
    d={'a':100,'b':200,'c':300}
    return render(request,'operations2.html',d)