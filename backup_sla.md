# Backup SLA
## 1. Web servers
This service processes incoming network requests: serves HTML documents over HTTP and acts as a reverse proxy for App servers and Monitoring services.
### 1.1 Backup coverage
Only meaningful subject for backup is configuration file(s). No additional files required.

### 1.2 Backup RPO
Backup should contain latest configuration files that worked in production environment.
### 1.3 Backup RTO
This service is one of the main components of the infrastructure and other services rely on it. Service should be restored within 2 hours.
### 1.4 Versioning and retention
Service doesn't require sophisticated configuration so one version of the backup will be enough. Backup should be stored for 120 days (effectively until new configuration is approved for production environment if it does).
### 1.5 Usability
#### 1.5.1 Syntax
Syntax of the backup files should be verified using command line tools.
#### 1.5.2 Reverse proxies
Configuration file(s) should contain reverse proxies to all relevant services.
### 1.6 Restoration criteria
It will be easier to reinstall the service completely rather than trying to troubleshoot it. Whenever it is determined that service is malfunctioning it should be restored.

## 2. App servers
This service handles the main business process. It is a simple web application that interracts with a database.
### 2.1 Backup coverage
#### 2.1.1 uWSGI configuration
uWSGI requires manual configuration and is crutial for the operation of the web application. Therefore configuration must be backuped.
#### 2.1.2 App dependecies
Should the list of web application dependencies ever grow it should be immeadiatly documented. This will allow restoration of the service to the latest version of the app.
#### 2.1.3 Source code
Application isn't compiled so there is no build files that need to be stored. Only source code that passed testing.
### 2.2 Backup RPO
Backup should contain latest source code and uWSGI configuration that worked in production environment.
### 2.3 Backup RTO
This service directly interacts with customers therefore it should be restored within 3 hours
### 2.4 Versioning and retention
#### 2.4.1 uWSGI
Configuration file is relatively simple and isn't a subject to frequent changes. One version of backup should exists at a time. Backup should be stored until new configuration is approved for production environmetn.
#### 2.4.2 Source code
This component is very important and more complex therefore there are 2 versions: current working code and previously working code. Development process is continious so backup is retained for 30 days.
### 2.5 Usability
#### 2.5.1 uWSGI configuration
Backup should be a file of ini format and contain following data: connection to database along with correct user credentials. Also it should contain basic configuration for web application
#### 2.5.2 Source code of application
Backup should be a working(parses and runs without errors) file that contains Python code.
### 2.6 Restoration criteria
Backup should be restored when newly deployed version of the application fails in the production environment or when uWSGI fails.

## 3. Database servers
This service provides reliable and effective storage and retrieval of data stored in them.
### 3.1 Backup coverage
Backup should contain all the database tables and records along with configured users and their priveleges. Also configuration file(s) should be included in the backup.
### 3.2 Backup RPO
This service contains and stores user data. Backup that is being restored should be no older than 24 hours.
### 3.3 Backup RTO
This service is a crucial component of main business process. It should be restored within 3 hours.
### 3.4 Versioning and retention
2 versions of backup shoud be kept so that if newly introduced change to schema proves inefficient previous working state could be restored. Backup retention perioud is 4 days.
### 3.5 Usability 
#### 3.5.1 Configuration file
File of ini format. Contains a line that allows outside connections to database.
#### 3.5.2 Database dump
This file should contain correct DML/DDL statements which can be verifyied with tools created for database administration. Also should contain up-to-date records. Their number can be verifyied by running query that counts number of rows.
### 3.6 Restoration criteria
This service should be restored in event of critical failure of the hardware(disk corruption etc.) or in event of security breach that results in data loss.

## 4. DNS servers
This service resolves ip addresses to human readable names that appear in configuration files and monitoring applications.
### 4.1 Backup coverage
Backup should contain up-to-date configuration of the service along with description of the zone.
### 4.2 Backup RPO
Backup should contain latest configuration files that worked in production environment.
### 4.3 Backup RTO
Service is crucial to the entire infrustructure operation. It should be restored within 2 hours.
### 4.4 Versioning and retention
2 versions of backups should be kept so that reverting to previous settings after some time would be possible. Backup should be stored for 120 days (effectively until new configuration is approved for production environment if it does).
### 4.5 Usability
#### 4.5.1 Configuration file
File should be of conf format. It should contain relevant acl entries and forwarders that. It should also contain lines that expose statistics for monitoring.
#### 4.5.2 Zone file
This file contains up-to-date information about zone and admin email. It also includes translation for all machines in the network and their aliases.
### 4.6 Restoration criteria
This service should be restored to working state after it is determined that it is mulfunctioning.

## 5. Monitoring servers
This group of services monitores state of different components of the infrastructure as well as state of the machines that host them.
### 5.1 Backup coverage
#### 5.1.1 Prometheus
This component relies on 2 configuration files: arguments for the service itself and prometheus configuration.
#### 5.1.2 Node and service exporters
These components rely on reverse proxy configuration for nginx. Service exporters require additional configuration: exposing statistics channel of monitored service, special configuration file, deamon file for service creation.
#### 5.1.3 Grafana
This service's configuration file must be backuped as well as dashboards that are meant for data visualization.
#### 5.1.3 InfluxDB and Telegraf
Configuration files of the services must be backuped. Records for the past 2 weeks must be retrieved from the database and archived.
### 5.2 Backup RPO
Backup must contain all the config files. Log loss worth of 4 hours is tolerable.
### 5.3 Backup RTO
Group of services must be restored within 3 hours.
### 5.4 Versioning and retention
#### 5.4.1 Configuration files
2 versions: previously working configration and current working configuration. Backups are stored for 60 days.
#### 5.4.2 Log records
Log records are stored for 180 days. One version per archive.
### 5.5 Usability
#### 5.5.1 Prometheus configuration file
It is a file of yaml format and contains all the jobs relevant to the current infrastructure.
#### 5.5.2 Grafana
Configuration file is of format ini. Dashborads are json files that most importantly contain database queries.
#### 5.5.3 InfluxDB and Telegraf
Configuration files are of conf format.
### 5.6 Restoration criteria
Component should be restored whenever it is mulfunctioning.

## 6. Ansible repository
Group of files that descrive what services are installed, on what machines and how they are configured.
### 6.1 Backup coverage
#### 6.1.1 Variable's files
These files contain all the important information for infrastructure configuration and therefore should be backuped.
#### 6.1.2 Roles
Files that describe how services are installed and configuration templates/files must be backuped.
#### 6.1.3 Vault password
Password used for encryption of sensitive data should stored in a secure location.
#### 6.1.4 Playbooks
Configuration scenarios must be backuped.
### 6.2 Backup RPO
Backup should contain latest working repository
### 6.3 Backup RTO
Repository should be restored to working state within 24 hours.
### 6.4 Versioning and retention
2 backup versions: previously working repository and currently working repository. Backups are stored for 60 days.
### 6.5 Usability
#### 6.5.1 Variable's files
These files contain all the information relevent to current infrastructure: dns zone name, cnames, ip addresses, encrypted credentials for various services.
#### 6.5.2 Roles
Roles directory contain main yaml file with relevant actions. Files and templates are of suitable format for service configuration. Templates must be Jinja2 templates.
#### 6.5.3 Vault password
This password should be able to decrypt encrypted user credentials from variable's files.
#### 6.5.4 Playbooks
These files are of yaml format and describe what services and where are installed.
### 6.6
Repository must be restored only when issues cannot be resolved at all.
