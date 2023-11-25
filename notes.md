## ubertooth one ##

``sudo apt-get install gcc-arm-none-eabi cmake build-essential libusb-1.0-0-dev libbluetooth-dev wireshark ubertooth kismet dfu-programmer dfu-util``

This command will display the current firmware version.

``ubertooth-util -v``

``cd firmware``
``make``
``cd /home/dcanale/kali/ubertooth/firmware/bluetooth_rxtx``
``ubertooth-dfu -d bluetooth_rxtx.dfu -r``

Firmware version: git-e0fd34d (API:1.07)

Capturing Bluetooth Packets\
``sudo ubertooth-btle -f``
Capture Bluetooth Packets to .pcap\
``sudo ubertooth-btle -f -c capture_file.pcap``
``pip install pyshark``
Capturing BLE in Wireshark
- Run the command: ``mkfifo /tmp/pipe``

- Open Wireshark

- Click Capture -> Options

- Click “Manage Interfaces” button on the right side of the window

- Click the “New” button

- In the “Pipe” text box, type “/tmp/pipe”

- Click Save, then click Close

- Click “Start”

- In a terminal, run ubertooth-btle:

``ubertooth-btle -f -c /tmp/pipe``
