#!/bin/bash

while true; do
read -p $'\nWelcome! Choose an option:\n1. Public IP\n2. Private IP\n3. MAC Address\n4. CPU Usage (Top 5)\n5. Memory Usage\n6. Active Services\n7. Top 10 Largest Files\n8. Exit\n\nEnter your choice: ' project

case $project in
#Identify the system's public IP:
1) echo "The systems public ip is $(curl -s ifconfig.me)"
;;
#Identify the private IP address assigned to the system's network interface:
2) echo "The systems private address is $(ifconfig | grep broadcast| awk '{print $2}')"
;;
# Display the MAC address (masking sensitive portions for security):
3) echo "the mac address of my system is $(ifconfig | grep ether | awk '{print $2}')"
;;
#Display the percentage of CPU usage for the top 5 processes:
4) echo "The percentage of CPU usage for the top 5 processes 
$(ps aux --sort=-%cpu| awk '{print $1, $2, $3 }'| head -n 6)"
;;
# Display memory usage statistics: total and available memory:
5) echo "This is the memory usage statstic for the total and available memory 
$(free -h| head -n 2| awk '{print $(NF-5), $(NF)}' )"
;;
#List active system services with their status:
6)echo " The active system services with their status are $(systemctl list-units --type=service --state=running)"
;;
#Locate the Top 10 Largest Files in /home:
7)echo "The top ten largest files in home are $(sudo find /home -type f -exec du -h {} + | sort -rh | head -n 10)"
;;
8)echo "Exiting ..";break;;
*)echo " invalid input ";;
esac
read -p "
press enter to continue ..."

done
