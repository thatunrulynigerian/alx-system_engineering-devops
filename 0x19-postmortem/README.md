# Issue Summary
Duration of the Outage: September 15, 2024, 3:00 PM - 4:00 PM EAT

# Impact: 
The web application was down for one hour, and 80% of users could not access the platform. Users saw "503 Service Unavailable" errors.

# Root Cause: 
A database migration was set up incorrectly, making the database unreachable for the application.

# Timeline
3:00 PM: Monitoring alerts showed high error rates for the application.
3:05 PM: Users started reporting problems accessing the site.
3:10 PM: The engineering team looked into the application logs for errors.
3:20 PM: Initial checks showed no errors in the application, but issues with the database were suspected.
3:30 PM: Further investigation found that the migration script had an incorrect endpoint, causing the database connection failure.
3:45 PM: The migration script was fixed, and the database connection was restored.
4:00 PM: The application was back online, and users could access it again.
Root Cause and Resolution
Root Cause: The migration script had an incorrect endpoint, which prevented the application from connecting to the database.

# Resolution: 
The correct endpoint was added to the migration script, and it was re-run, allowing the application to reconnect to the database.

# Improvements:
Set up a staging environment to test migration scripts before they go live.
Improve monitoring to alert the team about database connection issues.
Task List:
Create a staging environment for testing database migrations.
Add a monitoring check that alerts when the database is unreachable.

# Example Migration Check Script
#!/usr/bin/env bash

#check if the database is reachable
if ! nc -z localhost 5432; then
  echo "Database is not reachable!"
  exit 1
fi
echo "Database is reachable."

This postmortem will help us learn from the outage and prevent similar issues in the future.

## Corresponding Image
![Error 503 Service Unavailable](https://media.geeksforgeeks.org/wp-content/uploads/20221230125712/Fix-HTTP-Error-503-Service-Unavailable.png)
