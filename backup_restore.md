# Restoration of services
Restoration process of many services involves running commands from ansible repository. In that case part of the command prompt should look similar to this:  
  
```conf  
*user*@*name-of-computer*:*current-directory*$
```  
Where `current-directory` should be name of the ansible reporsitory or path to it. 

After successful service restoration make sure to do the steps from `Backup` part of this document which is in the very end.  

## 1. Core services  
These are the services that maintain the business process. 

### 1.1 Domain name server (DNS)  
To restore this service run command from ansible repository. Following command will install the service:  

```conf  
ansible-playbook lab07_grafana.yaml -t dns  
```  

### 1.2 Web server(Nginx)  
To restore this service run command
from ansible repository. Following command will install the webserver:  

```conf
ansible-playbook lab07_grafana.yaml -t nginx
```  

You may need to do this step when restoring other services: exporters for dns, mysql metrics.  

### 1.3 Web application (AGAMA) and uWSGI 
To restore this service run command from ansible repository. Following command will install the application itself along with necessary components:  

```conf
ansible-playbook lab07_grafana.yaml -t webapp 
```  

To restore users' data turn to part `1.4.2` of this document.

### 1.4 App database (MySQL)
#### 1.4.1 Restoration of the service itself  
Run this command from ansible repository:  

```conf 
ansible-playbook lab07_grafana.yaml -t db 
```  

#### 1.4.2 Restoration of users' data from backup
First ensure that the service is running with the following command:  

```conf  
sudo service mysql status  
```  

You should see `active (running)` in the output. The next step is to ensure that we can connect to the database using command prompt and that database schema is intact. Run following command, using MySQL user's agama credentials: 

```conf 
mysql --user=agama --password=*agama-password* --database=agama --execute "show tables;"  
```
If the output is empty or as follows(you can ignore the warning):  

```conf
+-----------------+
| Tables_in_agama |
+-----------------+
| item            |
+-----------------+
```  
You can proceed. If command returns an error, run the commands from part `1.4.1` of this document.  

Next step is to get the backup from the backup server. For that, run these commands as `root` user:  

```conf
su backup 
```  
This will make you a `backup` user.  

```conf  
duplicity --no-encryption restore  rsync://SADSLAVKA@backup.verysorry.io//home/SADSLAVKA/agama /home/backup/restore/agama.dump  
```
This will download the backup to `/home/backup/restore` under the name of `agama.dump`.  

```conf  
exit  
```  
This will turn you back to `root` user.  

Now we are ready to restore users data. Run following command, using MySQL user's `agama` credentials: 

```conf 
mysql --user=agama --password=*agama-password* --database=agama < /home/backup/restore/agama.dump    
```  

After that ensure that schema has been restore using this command:  

```conf 
mysql --user=agama --password=*agama-password* --database=agama --execute "show tables;"  
```  

And ensure that user data is present with this command:  

```conf  
mysql --user=agama --password=*agama-password* --database=agama --execute "select * from item;"  
```  

## 2. Monitoring services  
This is a group of services that provides machines' and services' health monitoring as well as log aggregation. Almost all of these services require that steps in the part `2.1.1` of this document were done.

### 2.1 Metrics exporters   
#### 2.1.1 Machine metrics exporter (node exporter)  
To restore this service run command from ansible repository. Following command will install the webserver along with node exporter:  

```conf
ansible-playbook lab07_grafana.yaml -t nginx 
```  

You may need to do this step when restoring other services: exporters for dns, mysql metrics.   

#### 2.1.2 Web server metrics exporter
To restore this service run command from ansible repository. Following command will install the webserver metrics exporter:  

```conf 
ansible-playbook lab07_grafana.yaml -t web-metrics  
```   

#### 2.1.3 DNS server metrics exporter  
To restore this service run command from ansible repository. Following command will install the DNS metrics exporter:  

```conf 
ansible-playbook lab07_grafana.yaml -t dns-metrics  
```   

#### 2.1.4 MySQL server metrics exporter  
To restore this service run command from ansible repository. Following command will install the webserver metrics exporter:  

```conf 
ansible-playbook lab07_grafana.yaml -t db-metrics  
```   

### 2.2 Metrics aggregator server 
To restore this service run command from ansible repository. Following command will install the metrics aggregator server:  

```conf 
ansible-playbook lab07_grafana.yaml -t prometheus  
```   

### 2.3 Log aggregator service 
To restore this service run command from ansible repository. Following command will install log aggregation service and configure other machines to send logs to it:  

```conf 
ansible-playbook lab08_logging.yaml   
```   

### 2.4 Metrics visualization service   
#### 2.4.1 Restoration of the service itself  
To restore this service run command from ansible repository. Following command will install metrics visualization service:  

```conf 
ansible-playbook lab07_grafana.yaml -t grafana   
```   

#### 2.4.2 Restoration of the dashboards  
First step is to download dashboard files form the backup server with following commands. Execute following commands as user `root`:  

```conf
su backup 
```  
This will make you a `backup` user.  

```conf  
duplicity --no-encryption restore rsync://SADSLAVKA@backup.verysorry.io//home/SADSLAVKA/dashboards /home/backup/restore/  
```
This will download the dashboards to `/home/backup/restore` as `.json` files. Their names will correspond to their function.  

```conf  
exit  
```  
This will turn you back to `root` user.  

For the next step you are going to need a connection to the network where machines are located. On the connected machine open a web browser and type the following in the address bar(assuming that DNS is operational):  

```conf  
grafana.verysorry.io/grafana  
```  
You will be greeted with a login screen. To login in use standard credentials(user: `admin`, password: `admin`) if no other configured user is present (don't forget to document the password after changing it).  

After logging in navigate to the taskbar on the left and hover your mouse over plus sign. In the popup press on the `Import` option. Then use the following command to get the dashboard file contents on the machine where backups are located:  

```conf 
cat /home/backup/restore/*name-of-dashboard*.json  
```  

Copy the contents of the file into the `Import via panel json` field on the `Import` page. Repeat the process until all desired dashboards are restored.  

## 3. Backups 
Run the following command from ansible repository to schedule future backups:  

```conf  
ansible-playbook lab10_backups.yaml  
```

