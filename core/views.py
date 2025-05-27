import os
import csv
from datetime import datetime
from django.shortcuts import render
from django.http import HttpResponse
from .forms import UploadExcelForm, UploadEMLForm
from .utils import extract_email_body, extract_rules


def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')


def eml_to_csv(request):
    """
    Handle EML file upload.
    """
    if request.method == 'POST':
        form = UploadEMLForm(request.POST, request.FILES)
        if form.is_valid():
            eml_instance = form.save()
            eml_path = eml_instance.file.path

            body = extract_email_body(eml_path)
            rules = extract_rules(body)

            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"rules_{timestamp}.csv"

            response = HttpResponse(content_type='text/csv')
            response['Content-Disposition'] = f'attachment; filename="{filename}"'
            writer = csv.writer(response)
            writer.writerow(['Rule Description', 'Values'])
            for row in rules:
                writer.writerow([row[0], ', '.join(row[1:])])

            if os.path.exists(eml_path):
                os.remove(eml_path)
                eml_instance.delete()
            return response
    else:
        form = UploadEMLForm()
    return render(request, 'core/eml_to_csv.html', {'form': form})
