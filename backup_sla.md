# Backup SLA
## 1. Database servers
This service provides reliable and effective storage and retrieval of data stored in them.

### 1.1 Backup coverage
Backup should contain all the database tables and records along with configured users and their priveleges.

### 1.2 Backup RPO
This service contains and stores user data. Backup that is being restored should not be older than 2 days.

### 1.3 Backup RTO
This service is a crucial component of main business process. It should be restored within 3 hours.

### 1.4 Backup frequency
Backup of this service has to be made every day. Every 7th backup is a full one, others are incremental.

### 1.5 Versioning and retention
2 versions of backup shoud be kept so that if newly introduced change to schema proves inefficient previous working state could be restored. Backup retention period is 4 days.

### 1.6 Usability 
#### 1.6.1 Database dump
This file should contain correct DML/DDL statements which can be verifyied with tools created for database administration. Also should contain up-to-date records. Their number can be verifyied by running query that counts number of rows.

### 1.7 Restoration criteria
This service should be restored in event of critical failure of the hardware(disk corruption etc.) or in event of security breach that results in data loss.

## 2. Monitoring servers
This group of services monitores state of different components of the infrastructure as well as state of the machines that host them.

### 2.1 Backup coverage
#### 2.1.1 Grafana dashboards
Dashboards that are meant for data visualization must be backuped.

#### 2.1.2 InfluxDB
Records for the past 24 hours must be retrieved from the database and archived.

### 2.2 Backup RPO
#### 2.2.1 Grafana dashboards
Dashboards should no be older than 31 days. 
#### 2.2.2 InfuxDB log records
Log loss worth of 4 hours is tolerable.

### 2.3 Backup RTO
Group of services must be restored within 3 hours.

### 2.4 Backup frequency
#### 2.4.1 Grafana dashboards
Backup of the dashboards should be made every first day of the month. Only full backups.
#### 2.4.2 InfluxDB log records
Log records must be archived every day.

### 2.5 Versioning and retention
#### 2.5.1 Dashboards
1 version: current dashboard set in use. Backups are stored for 60 days.
#### 2.5.2 Log records
Log records are stored for 180 days. One version per archive.

### 2.6 Usability
#### 2.6.1 Grafana
Dashborads are json files that most importantly contain database queries for metrics.
#### 2.6.2 InfluxDB log records
Archive contains records with timestamps in nanoseconds, messages, hostnames of machines where the log came from.

### 2.7 Restoration criteria
Component should be restored whenever it is mulfunctioning.

## 3. Ansible repository
Group of files that descrive what services are installed, on what machines and how they are configured.

### 3.1 Backup coverage
#### 3.1.1 Variable's files
These files contain all the important information for infrastructure configuration and therefore should be backuped.
#### 3.1.2 Roles and templates
Files that describe how services are installed and configuration templates/files must be backuped.
#### 3.1.3 Vault password
Password used for encryption of sensitive data should stored in a secure location.
#### 3.1.4 Playbooks
Configuration scenarios must be backuped.
#### 3.1.5 Ansible hosts file
Host file that contains ip addresses of machines and their roles in the infrastructure should be backuped.

### 3.2 Backup RPO
Backup of the repository should not be older than 30 days.

### 3.3 Backup RTO
Repository should be restored to working state within 24 hours.

### 3.4 Backup frequency
Backup of the repository should be made every 30 days.

### 3.5 Versioning and retention
2 backup versions: previously working repository and currently working repository. Backups are stored for 60 days.

### 3.6 Usability
#### 3.6.1 Variable's files
These files contain all the information relevent to current infrastructure: dns zone name, cnames, ip addresses, encrypted credentials for various services.
#### 3.6.2 Roles and templates
Roles directory contain main yaml file with relevant actions. Files and templates are of suitable format for service configuration. Templates must be Jinja2 templates.
#### 3.6.3 Vault password
This password should be able to decrypt encrypted user credentials from variable's files.
#### 3.6.4 Playbooks
These files are of yaml format and describe what services and where are installed.

### 3.7
Repository must be restored only when issues cannot be resolved at all.
