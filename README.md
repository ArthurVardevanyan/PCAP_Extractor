This Program Extracts the Requested Information from the Wireshark/Tshark Generated PCAP File.



tshark -i XNetworkDeviceX -w /XXXX/tshark.pcap -q -B 2000 -f "port XXXX" -b filesize:25000 -s 50

This Command creates the PCAP File with the specified capture commands from Tshark. In My case, I am Monitoring traffic across a certain port, and storing it into a file.
TShark Documentation: https://www.wireshark.org/docs/man-pages/tshark.html


TODO:
Add Log File Support
General Code Maintenance and Cleanup

