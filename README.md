# Udacity Project: Logs Analysis

Logs analysis project is a project from Full Stack Web Developer Nanodegree Program on Udacity.


This project aims to strengthen SQL database skills by giving an opportunity practice interacting with a live database both from the command line and codeas well as exploring a large database with over a million rows.


## So what is being reported, anyway?
1. What are the most popular three articles of all time?


2. Who are the most popular article authors of all time? 


3. On which days did more than 1% of requests lead to errors? 


## Downloading Software
1. Download VirtualBox. 
VritualBox is the software that actually runs the virtual machine. It can be downloaded from virtualbox.org, [here](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1).


2. Install Vagrant. Vagrant is the software that configures the VM and lets sharing files between host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). 


3. Download the VM configuration. Fork and clone the repository [https://github.com/udacity/fullstack-nanodegree-vm](https://github.com/udacity/fullstack-nanodegree-vm). Change directory to the vagrant directory and run the command 'vagrant up'. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!


4. The PostgreSQL database. The PostgreSQL database server will automatically be started inside the VM. You sould check that server is running and works fine via 'psql' command-line tool and run some test SQL statements.


5. Also, please make sure you have installed Python 2.7 as well as psycopg2 library.


6. Troubleshooting. If some errors occurred [stackoverflow](http://stackoverflow.com) is a place where answers for most questions can be found either already answered or being asked by you.



## Getting Started

1. Bring virtual machine online using 'vagrant up'


2. Log in to your virtual machine via 'vagrant ssh'


3. Download the data needed for the project from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)


4. Put this file into the '/vagrant' directory and unzip


5. Load downladed data in '/vagrant' directory into your local database via following command 'psql -d news -f newsdata.sql.' (being in '/vagrant' directory)


6. Run this code via 'python code.py'


## All about VIEWS

This solution uses following code for VIEW creation for question #3. 
    
    DROP VIEW IF EXISTS status_count;


    CREATE VIEW status_count AS
    SELECT log_record.time::date AS date,
    SUM(CASE WHEN log_record.status NOT LIKE '200 OK' THEN 1 ELSE 0 END)
    AS  error_status,
    COUNT(*) AS total_status
    FROM log AS log_record
    GROUP BY date;

However, you do not need to create anything manually before running 'code.py' since all views are already included in the solution of question 3 itself.

## Answers

You can see program output in 'answers.txt'


