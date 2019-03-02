This Program Extracts the Requested Information from the Wireshark/Tshark Generated PCAP File.<br/>



tshark -i XNetworkDeviceX -w /XXXX/tshark.pcap -q -B 2000 -f "port XXXX" -b filesize:5000 -s 50<br/>
Pcap_Extractor.py is Run once a half hour via a cron job on my system.
This Command creates the PCAP File with the specified capture commands from Tshark. In My case, I am Monitoring traffic across a certain port, and storing it into a file.<br/>
TShark Documentation: https://www.wireshark.org/docs/man-pages/tshark.html<br/>

API KEY Needed from  https://ipinfo.io/ in order to get IpData<br/>

Required Libraries:<br/>
OS<br/>
datetime<br/>
socket<br/>

GLOB<br/>
pymysql<br/>
ipinfo<br/>

TODO:
Add Log File Support<br/>
Better Expection Cathingt<br/>
General Code Maintenance and Cleanup<br/>

Sample MYSQL DataBase Output<br/>

Enpoint Data:<br/>

| Address         | Packets | Bytes      | Tx_Packets | Tx_Bytes  | Rx_Packets | Rx_Bytes   | First_Seen       | Last_Seen        | Organization      | Country       | Region     | City          |
|-----------------|---------|------------|------------|-----------|------------|------------|------------------|------------------|-------------------|---------------|------------|---------------|
| 104.131.144.157 |       1 |         60 |          1 |        60 |          0 |          0 | 2019-03-02 16:28 | 2019-03-02 16:28 | DigitalOcean, LLC | United States | California | San Francisco |
| 192.168.0.9     |  530612 |  537598919 |     198933 |  34844727 |     331679 |  502754192 | 2019-03-02 16:28 | 2019-03-02 17:53 | Server            | Internal      | NULL       | NULL          |
| 192.168.0.8     |    2409 |    1077428 |       1064 |    427607 |       1345 |     649821 | 2019-03-01 15:25 | 2019-03-02 16:28 | NULL              | Internal      | NULL       | NULL          |
| 192.168.0.7     |   11481 |   12957579 |       2696 |    310850 |       8785 |   12646729 | 2019-03-01 15:26 | 2019-03-02 16:28 | NULL              | Internal      | NULL       | NULL          |
| 192.168.0.6     |  111510 |   66094672 |      46818 |  22189931 |      64692 |   43904741 | 2019-03-01 15:25 | 2019-03-02 17:53 | Arthur-Hp         | Internal      |            |               |
| 192.168.0.5     |   14140 |   14606656 |       5441 |   5788198 |       8699 |    8818458 | 2019-03-01 15:26 | 2019-03-02 17:53 | Nexus 5x          | Internal      |            |               |
| 192.168.0.4     |    9698 |   12342691 |       1353 |    154325 |       8345 |   12188366 | 2019-03-01 15:26 | 2019-03-02 16:28 | NULL              | Internal      | NULL       | NULL          |
| 192.168.0.3     |    2092 |     589865 |       1043 |    129204 |       1049 |     460661 | 2019-03-01 15:25 | 2019-03-02 17:53 | NULL              | Internal      | NULL       | NULL          |
| 192.168.0.2     | 1210155 | 1733804267 |      66190 |   7755584 |    1143965 | 1726048683 | 2019-03-01 15:25 | 2019-03-01 15:26 | NULL              | Internal      | NULL       | NULL          |
| 192.168.0.1     |  478587 |  503409034 |     310276 | 491952777 |     168311 |   11456257 | 2019-03-01 15:25 | 2019-03-02 17:53 | NULL              | Internal      | NULL       | NULL          |


Conversation Data:

| Address_A       | Address_B     | Packets_A_B | Bytes_A_B  | Packets_B_A | Bytes_B_A | Packets | Bytes      | First_Seen       | Last_Seen        |
|-----------------|---------------|-------------|------------|-------------|-----------|---------|------------|------------------|------------------|
| 192.168.0.1     | 192.168.0.2   |       46818 |   22189931 |       64692 |  43904741 |  111510 |   66094672 | 2019-03-01 15:25 | 2019-03-02 17:53 |
| 192.168.0.6     | 192.168.0.1   |     1143965 | 1726048683 |       66190 |   7755584 | 1210155 | 1733804267 | 2019-03-01 15:25 | 2019-03-01 15:26 |
| 192.168.0.7     | 192.168.0.1   |        8699 |    8818458 |        5441 |   5788198 |   14140 |   14606656 | 2019-03-01 15:25 | 2019-03-02 17:53 |
| 192.168.0.9     | 192.168.0.1   |      168311 |   11456257 |      310276 | 491952777 |  478587 |  503409034 | 2019-03-01 15:25 | 2019-03-02 17:53 |
| 192.168.0.6     | 192.168.0.1   |        1049 |     460661 |        1043 |    129204 |    2092 |     589865 | 2019-03-01 15:25 | 2019-03-02 17:53 |
| 192.168.0.4     | 192.168.0.1   |        8785 |   12646729 |        2696 |    310850 |   11481 |   12957579 | 2019-03-01 15:26 | 2019-03-02 16:28 |
| 192.168.0.8     | 192.168.0.1   |        8345 |   12188366 |        1353 |    154325 |    9698 |   12342691 | 2019-03-01 15:26 | 2019-03-02 16:28 |
| 104.131.144.157 | 192.168.0.1   |           0 |          0 |           1 |        60 |       1 |         60 | 2019-03-02 16:28 | 2019-03-02 16:28 |

