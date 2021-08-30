#!/bin/bash
while true; do
   echo -e "\n"
   echo "Hostname"
   curl http://localhost:23333/info/host
   echo -e "\n"
   echo "Uptime"
   curl http://localhost:23333/info/uptime
   echo -e "\n"
   echo "Load Average"
   curl http://localhost:23333/info/load
   echo -e "\n"
   sleep 0.5
   echo "Endpoints being called"
done