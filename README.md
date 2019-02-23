This Program Extracts the Requested Information from the Wireshark/Tshark Generated PCAP File.<br/>



tshark -i XNetworkDeviceX -w /XXXX/tshark.pcap -q -B 2000 -f "port XXXX" -b filesize:5000 -s 50<br/>
Pcap_Extractor.py is Run once a half hour via a cron job on my system.
This Command creates the PCAP File with the specified capture commands from Tshark. In My case, I am Monitoring traffic across a certain port, and storing it into a file.<br/>
TShark Documentation: https://www.wireshark.org/docs/man-pages/tshark.html<br/>


TODO:
Add Log File Support<br/>
Better Expection Cathingt<br/>
Add the ablity to create create MYSQL From scratch instead of making it before ever runing the program<br/>
Don't drop the table to update the table. <br/>
General Code Maintenance and Cleanup<br/>

