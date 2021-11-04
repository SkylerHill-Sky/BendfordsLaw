from django.shortcuts import render


# Create your views here.
from main.forms import TextFileForm
from main.models import TextFile


def upload_file(request):
    """ Uploads a File """
    context_data = {
        'title': 'Upload File',
        'number': 4,
        'form': TextFileForm,
    }
    if request.method == 'POST':
        form = TextFileForm(request.POST, request.FILES)
        context_data['form'] = form
        if form.is_valid():
            form.save()
            context_data['success'] = True
        else:
            context_data['success'] = False

    return render(request, 'upload_file.html', context_data)


def index_view(request):
    """ Index view for the site """
    all_files = TextFile.objects.all()
    context_data = {
        'title': 'Index',
        'all_files': all_files,
    }
    return render(request, 'index.html', context_data)