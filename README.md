How to work? 

Systemd:
sudo mv flask_test.service flask_test.timer /etc/systemd/system/
sudo systemctl enable flask_test.timer

Flask: 
flask run
open pop up link at browser 

Logging 
tail /var/log/monitoring.log (create a new one, if do not have)

That's all - lol 
