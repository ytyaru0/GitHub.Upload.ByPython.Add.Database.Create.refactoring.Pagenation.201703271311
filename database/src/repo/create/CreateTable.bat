@echo off
set sqlite=sqlite3.exe
set sql_dir=%~dp0res/sql/create/
set db=%~dp0res/db/GitHub.Repositories.sqlite3
"%sqlite%" "%db%" < "%sql_dir%Repositories.sql"
"%sqlite%" "%db%" < "%sql_dir%Counts.sql"
"%sqlite%" "%db%" < "%sql_dir%Languages.sql"
