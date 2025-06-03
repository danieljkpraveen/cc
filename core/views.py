from .utils import (
    create_panos_connection
)
from .forms import (
    FirewallConnectForm,
)
import xml.etree.ElementTree as ET

from django.shortcuts import render

from .models import FirewallCredential


def index(request):
    """
    Render the index page.
    """
    return render(request, 'index.html')


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
        if request.POST.get('version'):
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
