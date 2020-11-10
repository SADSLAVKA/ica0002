# Backup SLA
## 1. Database servers
This service provides reliable and effective storage and retrieval of data stored in them.

### 1.1 Backup coverage
Backup should contain all the database tables and records along with configured users and their priveleges. Also configuration file(s) should be included in the backup.

### 1.2 Backup RPO
This service contains and stores user data. Backup that is being restored should be no older than 24 hours.

### 1.3 Backup RTO
This service is a crucial component of main business process. It should be restored within 3 hours.

### 1.4 Versioning and retention
2 versions of backup shoud be kept so that if newly introduced change to schema proves inefficient previous working state could be restored. Backup retention perioud is 4 days.

### 1.5 Usability 
#### 1.5.1 Configuration file
File of ini format. Contains a line that allows outside connections to database.
#### 1.5.2 Database dump
This file should contain correct DML/DDL statements which can be verifyied with tools created for database administration. Also should contain up-to-date records. Their number can be verifyied by running query that counts number of rows.

### 1.6 Restoration criteria
This service should be restored in event of critical failure of the hardware(disk corruption etc.) or in event of security breach that results in data loss.

## 2. Monitoring servers
This group of services monitores state of different components of the infrastructure as well as state of the machines that host them.

### 2.1 Backup coverage
#### 2.1.1 Grafana
Dashboards that are meant for data visualization must be backuped.
#### 2.1.2 InfluxDB
Records for the past 2 weeks must be retrieved from the database and archived.
### 2.2 Backup RPO
Backup must contain all dashboards. Log loss worth of 4 hours is tolerable.
### 2.3 Backup RTO
Group of services must be restored within 3 hours.
### 2.4 Versioning and retention
#### 2.4.1 Dashboards
1 version: current dashboard set in use. Backups are stored for 60 days.
#### 2.4.2 Log records
Log records are stored for 180 days. One version per archive.
### 2.5 Usability
#### 2.5.1 Grafana
Dashborads are json files that most importantly contain database queries.
#### 2.5.2 InfluxDB log records
Records contain syslog format messages.
### 2.6 Restoration criteria
Component should be restored whenever it is mulfunctioning.

## 3. Ansible repository
Group of files that descrive what services are installed, on what machines and how they are configured.

### 3.1 Backup coverage
#### 3.1.1 Variable's files
These files contain all the important information for infrastructure configuration and therefore should be backuped.
#### 3.1.2 Roles
Files that describe how services are installed and configuration templates/files must be backuped.
#### 3.1.3 Vault password
Password used for encryption of sensitive data should stored in a secure location.
#### 3.1.4 Playbooks
Configuration scenarios must be backuped.

### 3.2 Backup RPO
Backup should contain latest working repository

### 3.3 Backup RTO
Repository should be restored to working state within 24 hours.

### 3.4 Versioning and retention
2 backup versions: previously working repository and currently working repository. Backups are stored for 60 days.

### 3.5 Usability
#### 3.5.1 Variable's files
These files contain all the information relevent to current infrastructure: dns zone name, cnames, ip addresses, encrypted credentials for various services.
#### 3.5.2 Roles
Roles directory contain main yaml file with relevant actions. Files and templates are of suitable format for service configuration. Templates must be Jinja2 templates.
#### 3.5.3 Vault password
This password should be able to decrypt encrypted user credentials from variable's files.
#### 3.5.4 Playbooks
These files are of yaml format and describe what services and where are installed.

### 3.6
Repository must be restored only when issues cannot be resolved at all.
