from django.shortcuts import render

# Create your views here.
def Bharath(request):
    d={'a':4567,'b':7289,'c':1789}
    return render(request,'Bharath.html',context=d)