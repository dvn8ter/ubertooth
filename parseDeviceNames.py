import pyshark

def extract_device_names(pcap_file):
    cap = pyshark.FileCapture(pcap_file, display_filter="btatt")
    device_names = set()

    for packet in cap:
        if hasattr(packet, 'bluetooth'):
            # Check for Scan Response or Advertisement Indication packets
            if packet.bluetooth.get_field_value('btcommon_eir_ad_entry_type') == '0x09': 
                device_name = packet.bluetooth.get_field_value('btcommon_eir_ad_entry_data')
                device_names.add(device_name)

    return device_names

pcap_file = 'capture_file.txt'  # Replace with your pcap file path
device_names = extract_device_names(pcap_file)
print("Found Bluetooth Device Names:")
for name in device_names:
    print(name)
