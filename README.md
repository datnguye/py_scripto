# py-scripto
This is to run SQL script or file script in an instance of sql server

Installation:
```
python -m pip install py_scripto
```

### Version used
```
SQL Server 2019
Python 3.7.5
```

## DEPENDENCIES

### DbExec stored procedure
1. Download from https://github.com/datnguye/SQL-Server/blob/master/maintenance/DbExec.sql

2. Compile it to master database

### xp_cmdshell need enabling on SQL instance
```
EXEC sp_configure 'show advanced option', 1
RECONFIGURE
GO
EXEC sp_configure 'xp_cmdshell', 1
RECONFIGURE
GO
```

## USAGE

```
from py_scripto import sqlserver
sqlserver.run_file_script(server="DAVID\DAVID", uid="py-scripto", pwd="py-scripto", connect_to_db="IMPORT", script_path="D:\\Downloads\\test.sql")
sqlserver.run_script(server="DAVID\DAVID", uid="py-scripto", pwd="py-scripto", connect_to_db="IMPORT", sql="SELECT * FROM Test WITH (NOLOCK)")
```