from .utils import (
    extract_email_body,
    extract_rules,
    create_panos_connection
)
from .forms import (
    UploadExcelForm,
    UploadEMLForm,
    FirewallConnectForm,
    VersionSelectForm,
    ConfigUploadForm
)
import os
import csv
from datetime import datetime
import xml.etree.ElementTree as ET
import tempfile

from django.shortcuts import render
from django.http import HttpResponse
from panos.updater import SoftwareUpdater

from .models import FirewallCredential


def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')


############## _____Automation Views_____##############
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
            writer.writerow(['Tasks', 'Results'])
            for row in rules:
                writer.writerow([row[0], ', '.join(row[1:])])

            if os.path.exists(eml_path):
                os.remove(eml_path)
                eml_instance.delete()
            return response
    else:
        form = UploadEMLForm()
    return render(request, 'core/eml_to_csv.html', {'form': form})


############## _____Network Management Views_____##############
def check_firewall_connection(request):
    """
    Handle firewall connection form submission.
    """
    if request.method == 'POST':
        fw = create_panos_connection(request)
        return render(request, 'core/firewall_connection.html', {'firewall': fw})
    else:
        form = FirewallConnectForm()
    return render(request, 'core/firewall_connection.html', {'form': form})


def connect_and_fetch_panos_version(request):
    """
    Connect to the PAN-OS device and fetch the version.
    """
    if request.method == 'POST':
        global HOSTNAME, PASSWORD, USERNAME, API_KEY
        if request.POST.get('version'):
            print(f"Host: {HOSTNAME}")
            version = request.POST.get('version')
            # print(
            #     f"Selected PAN-OS version: {version}\nFirewall host: {FW.host}")
            return render(request, 'core/panos_versions.html')
        fw = create_panos_connection(request)
        fw_credential = FirewallCredential(
            host=request.POST.get('host'),
            username=request.POST.get('username'),
            password=request.POST.get('password'),
            api_key=request.POST.get('api_key')
        )
        fw_credential.save()

        software_info = fw.op("request system software info", xml=True)

        info_tree = ET.fromstring(software_info)
        versions = []
        for entry in info_tree.findall(".//entry"):
            version = entry.find("version").text
            # downloaded = entry.find("downloaded").text
            # versions.append((version, downloaded))
            versions.append(version)
        return render(request, 'core/panos_versions.html', {'versions': versions})
    else:
        form = FirewallConnectForm()
    return render(request, 'core/panos_versions.html', {'form': form})


# def install_selected_version(request):
#     """
#     Install the selected PAN-OS version.
#     """
#     if request.method == 'POST':
#         version = request.POST.get('version')
#         fw = create_panos_connection(request)
