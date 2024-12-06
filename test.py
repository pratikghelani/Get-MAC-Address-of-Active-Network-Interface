from getmac import get_mac_address

def get_active_mac_address():
    """
    Retrieve the MAC address of the active network interface.
    """
    mac = get_mac_address()
    if mac:
        print(f"MAC Address of active interface: {mac}")
    else:
        print("Could not retrieve MAC address. Ensure you're connected to a network.")

if __name__ == "__main__":
    get_active_mac_address()
