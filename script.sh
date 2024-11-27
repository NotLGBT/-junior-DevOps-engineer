#!/bin/bash

method_stat="CPU"
process="python"
interval=5

result=$(ps hf -C "$process" | awk '{ print $3; exit }')
restart=$(ps xhf -C "$process" | awk '{ print $4; exit }')



if [[ "$result" =~ ^R|S ]]; then
  response=$(curl -s -o /dev/null -w "%{http_code}" "http://127.0.0.1:5000/monitoring/test/api?method_stat=$method_stat&pattern=$process&interval=$interval")
  if [[ "$response" -eq 200 ]]; then 
    echo "200 status"
  else 
    echo "Status is $response" >> /var/log/monitoring.log
  fi
elif [[ "$restart" == "0:00" ]]; then 
  echo "$process is in none-runnning state" >> /var/log/monitoring.log
else 
  exit
fi

