from panos.firewall import Firewall
from panos.errors import PanDeviceError


##################### ___Network Management Utilities___#####################

def create_panos_connection(request):
    """Create a PAN-OS connection based on the form data."""
    host = request.POST.get('host')
    username = request.POST.get('username')
    password = request.POST.get('password')
    api_key = request.POST.get('api_key')

    if not host or not username:
        raise ValueError("Host and Username are required.")

    try:
        if api_key:
            fw = Firewall(host, api_key)
        else:
            fw = Firewall(host, username, password)
        fw.refresh_system_info()
        return fw
    except PanDeviceError as e:
        raise ValueError(f"Failed to connect to the firewall: {str(e)}")
