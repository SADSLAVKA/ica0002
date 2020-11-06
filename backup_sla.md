# Backup SLA
## 1. Web servers
This service processes incoming network requests: serves HTML documents over HTTP and acts as a reverse proxy for App servers and Monitoring services.
### 1.1 Backup coverage
Only meaningful subject for backup is configuration file(s). No additional files required.

### 1.2 Backup RPO
Backup should contain latest configuration files that passed checks in testing environment.
### 1.3 Backup RTO
Service doesn't deal with user data directly although other services that do deal with user data and logs depend on the web servers. Service should be restored within 2 hours.
### 1.4 Versioning and retention
Service doesn't require sophisticated configuration so one version of the backup will be enough. Backup should be stored as until new configuration is approved for production environment.
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
Backup should contain latest source code and uWSGI configuration
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
2 versions of backup shoud be kept so that in event of unsuccessful database schema modification previous working state could be restored. Backup retention perioud is 4 days.
### 3.5 Usability 
#### 3.5.1 Configuration file
File of ini format. Contains a line that allows outside connections to database.
#### 3.5.2 Database dump
This file should contain correct DML/DDL statements which can be verifyied with tools created for database administration. Also should contain up-to-date records. Their number can be verifyied by running query that counts number of rows.
### 3.6 Restoration criteria
This service should be restored in event of critical failure of the hardware(disk corruption etc.) or in event of security breach that results in data loss.
