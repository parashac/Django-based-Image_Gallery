from django.shortcuts import render, redirect
from gallery_app.models import Image
# Create your views here.
def gallery(request):
    images = Image.objects.all().order_by('-id')
    return render(request, 'gallery.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES.get('image')

        if title and image:
            Image.objects.create(title=title, image=image)
            return redirect('gallery')

    return render(request, 'upload.html')
