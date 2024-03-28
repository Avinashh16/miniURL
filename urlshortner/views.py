from django.shortcuts import render,redirect
from django.http import HttpResponse, Http404
from django.utils import timezone
from .forms import urlForm
from .models import urlModel

# Create your views here.
def home(request):

    if request.method == 'POST':
        form = urlForm(request.POST) 
        if form.is_valid():
            original_url = form.cleaned_data['url']
            created_miniurl = form.cleaned_data['miniurl']
            time = timezone.now() 
            val = urlModel( url=  original_url , miniurl=created_miniurl,created_at=time)
            val.save()

            return redirect('success', created_miniurl)
    else:
        form = urlForm()
    
    return render(request, 'home.html', {'form': form})

def success(request, url):
    obj = urlModel.objects.filter(miniurl=url)
    if obj.exists():
        val = obj.first()
    return render(request,'created.html',{'val':val})

def miniurl(request,url):
    val = urlModel.objects.filter(miniurl=url)
    if val.exists():
        obj = val.first()
        target = obj.url
        print(target)

        return redirect(target)
    else:
        return render(request,'404.html')
    
def error_404_view(request,exception):
    return render(request, '404.html', status=404)