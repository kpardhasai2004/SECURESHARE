from django.shortcuts import render, redirect
from django.http import FileResponse
from django.shortcuts import get_object_or_404
from .models import SharedFile
from django.utils import timezone
# Create your views here.

def file_list(request):
    files = SharedFile.objects.all()
    return render(request, 'file_list.html', {'files': files})

def upload_file(request):
    if request.method == 'POST':
        title = request.POST['title']
        file = request.FILES['file']
        expiration_time = request.POST.get('expiration_time')  # Get expiration time from the form
        
        # Set expiration time if provided
        if expiration_time:
            expiration_time = timezone.now() + expiration_time
        
        shared_file = SharedFile.objects.create(title=title, file=file, expiration_time=expiration_time)
        return redirect('share_file', access_code=shared_file.access_code)
    return render(request, 'upload_file.html')



def access_file(request, access_code):
    try:
        file = SharedFile.objects.get(access_code=access_code)
        now = timezone.now()
        if file.expiration_time and now > file.expiration_time:
            return render(request, 'expired_file.html', {'file': file})
        return render(request, 'access_file.html', {'file': file})
    except SharedFile.DoesNotExist:
        return render(request, 'access_error.html')

def receive_function(request):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        if access_code:
            try:
                file = SharedFile.objects.get(access_code=access_code)
                return redirect('access_file', access_code=access_code)
            except SharedFile.DoesNotExist:
                return render(request, 'receive_error.html', {'error_message': 'Invalid access code'})
        else:
            return render(request, 'receive_error.html', {'error_message': 'Access code is required'})
    return render(request, 'receive_function.html')

def share_file(request, access_code):
    try:
        file = SharedFile.objects.get(access_code=access_code)
        return render(request, 'share_file.html', {'file': file})
    except SharedFile.DoesNotExist:
        return render(request, 'access_error.html')
