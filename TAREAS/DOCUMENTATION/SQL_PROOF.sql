select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [rdsadmin];
SELECT option_name, major_engine_version, port, lifecycle, change_state, install_start_epoch, install_end_epoch FROM rds_option_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT family_guid, rds_sequence_id, file_epoch, database_name FROM rdsadmin.dbo.log_backup_manifest 
WHERE lifecycle = 'EXTRACTED'
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT COUNT(*) FROM sys.dm_exec_connections WITH(NOLOCK) WHERE encrypt_option = 'TRUE' AND net_transport = 'TCP';
go

USE [master];
SELECT value_in_use FROM sys.configurations WITH(NOLOCK) WHERE NAME = 'Database Mail XPs';
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE master;
SELECT sys.fn_varbintohexstr(sid) AS 'SID' FROM sys.server_principals WHERE name = 'BUILTIN\Administrators';
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [rdsadmin];
SELECT option_name, major_engine_version, port, lifecycle, change_state, install_start_epoch, install_end_epoch FROM rds_option_info
go

USE [rdsadmin];
SELECT option_name, major_engine_version, port, lifecycle, change_state, install_start_epoch, install_end_epoch FROM rds_option_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
DECLARE @max_days_to_retain int;                                                                             
                                                                                                             
-- Get maximum days to retain information from rds_configuration                                             
SET @max_days_to_retain = COALESCE((SELECT CAST([value] AS INT) from [rdsadmin].[dbo].[rds_configuration]    
WHERE  [name] = 'customer tasks retention'), 36);                                                            
                                                                                                             
-- Delete all the tasks that meet the criteria                                                               
DELETE FROM [rdsadmin].[dbo].[rds_customer_tasks]                                                            
WHERE DATEDIFF(DAY, [last_updated], GETUTCDATE()) > @max_days_to_retain                                      
AND [task_type] IN ('SSIS_DEPLOY_PROJECT') AND [task_id] not in                                                        
(select [task_id] from (SELECT [task_id], rank() over (partition by database_name order by task_id desc)     
as 'ranking' from [rdsadmin].[dbo].[rds_customer_tasks] where task_type in ('RESTORE_DB_NORECOVERY',         
'RESTORE_DB_LOG_NORECOVERY', 'RESTORE_DB_DIFFERENTIAL_NORECOVERY') and lifecycle = 'SUCCESS') RankedDatabaseName where ranking = 1)
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
DECLARE @max_days_to_retain int;                                                                             
                                                                                                             
-- Get maximum days to retain information from rds_configuration                                             
SET @max_days_to_retain = COALESCE((SELECT CAST([value] AS INT) from [rdsadmin].[dbo].[rds_configuration]    
WHERE  [name] = 'customer tasks retention'), 36);                                                            
                                                                                                             
-- Delete all the tasks that meet the criteria                                                               
DELETE FROM [rdsadmin].[dbo].[rds_customer_tasks]                                                            
WHERE DATEDIFF(DAY, [last_updated], GETUTCDATE()) > @max_days_to_retain                                      
AND [task_type] IN ('BACKUP_DB', 'RESTORE_DB', 'HA_RESTORE_DB', 'BACKUP_DB_DIFFERENTIAL', 'RESTORE_DB_DIFFERENTIAL', 'RESTORE_DB_LOG', 'RESTORE_DB_DIFFERENTIAL_NORECOVERY', 'RESTORE_DB_LOG_NORECOVERY', 'RESTORE_DB_NORECOVERY', 'RESTORE_TDE_CERTIFICATE', 'BACKUP_TDE_CERTIFICATE', 'DOWNLOAD_FROM_S3', 'UPLOAD_TO_S3', 'DELETE_FILES_ON_DISK', 'LIST_FILES_ON_DISK', 'COPY_TLOG_BACKUP_TO_S3') AND [task_id] not in                                                        
(select [task_id] from (SELECT [task_id], rank() over (partition by database_name order by task_id desc)     
as 'ranking' from [rdsadmin].[dbo].[rds_customer_tasks] where task_type in ('RESTORE_DB_NORECOVERY',         
'RESTORE_DB_LOG_NORECOVERY', 'RESTORE_DB_DIFFERENTIAL_NORECOVERY') and lifecycle = 'SUCCESS') RankedDatabaseName where ranking = 1)
go

SELECT family_guid, rds_sequence_id, file_epoch, database_name FROM rdsadmin.dbo.log_backup_manifest 
WHERE lifecycle = 'EXTRACTED'
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

USE [rdsadmin];
SELECT option_name, major_engine_version, port, lifecycle, change_state, install_start_epoch, install_end_epoch FROM rds_option_info
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

            SELECT SP2.name
            FROM sys.server_role_members SRM WITH (NOLOCK) 
            INNER JOIN sys.server_principals SP1 WITH (NOLOCK) ON SRM.role_principal_id = SP1.principal_id
            INNER JOIN sys.server_principals SP2 WITH (NOLOCK) ON SRM.member_principal_id = SP2.principal_id
            WHERE SP1.type_desc ='SERVER_ROLE' AND SP1.is_fixed_role = 1
            AND SP1.name IN
                (
                'sysadmin',
                'securityadmin',
                'serveradmin',
                'diskadmin',
                'dbcreator',
                'bulkadmin'
                )
            AND SP2.name NOT LIKE CONVERT(nvarchar(128),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')) + '\Administrator'
            AND SP2.type_desc NOT IN ('CERTIFICATE_MAPPED_LOGIN')
            UNION ALL 
            SELECT SP.name
            FROM sys.server_principals SP WITH (NOLOCK)
            INNER JOIN sys.server_permissions SSP WITH (NOLOCK) ON SP.principal_id = SSP.grantee_principal_id
            WHERE 
            (
                -- Server Permissions that are not allowed for customer
                SSP.permission_name IN
                (
                    'ALTER ANY AVAILABILITY GROUP',
                    'ALTER ANY EVENT NOTIFICATION',
                    'ALTER RESOURCES',
                    'ALTER SETTINGS',
                    'AUTHENTICATE SERVER',
                    -- We are not checking 'CONNECT ANY DATABASE' because [NT SERVICE\SQLTELEMETRY] has this permission and currently we do not protect 
                    -- this login, so customer can re-create that. However, this permission alone is not insecure and other privileges are checked
                    -- for every login.
                    --   'CONNECT ANY DATABASE',
                    'CONTROL SERVER',
                    'CREATE AVAILABILITY GROUP',
                    'CREATE DDL EVENT NOTIFICATION',
                    'CREATE ENDPOINT',
                    'CREATE TRACE EVENT NOTIFICATION',
                    'EXTERNAL ACCESS ASSEMBLY',
                    'SHUTDOWN',
                    'UNSAFE ASSEMBLY'
                ) 
                AND state_desc IN ('GRANT','GRANT_WITH_GRANT_OPTION')
            )
            AND SP.name NOT LIKE CONVERT(nvarchar(128),SERVERPROPERTY('ComputerNamePhysicalNetBIOS')) + '\Administrator'
            AND SP.type_desc NOT IN ('CERTIFICATE_MAPPED_LOGIN')
go
DECLARE @max_days_to_retain int;                                                                             
                                                                                                             
-- Get maximum days to retain information from rds_configuration                                             
SET @max_days_to_retain = COALESCE((SELECT CAST([value] AS INT) from [rdsadmin].[dbo].[rds_configuration]    
WHERE  [name] = 'customer tasks retention'), 36);                                                            
                                                                                                             
-- Delete all the tasks that meet the criteria                                                               
DELETE FROM [rdsadmin].[dbo].[rds_customer_tasks]                                                            
WHERE DATEDIFF(DAY, [last_updated], GETUTCDATE()) > @max_days_to_retain                                      
AND [task_type] IN ('SSAS_DEPLOY_PROJECT', 'SSAS_BACKUP_DB', 'SSAS_RESTORE_DB', 'SSAS_ADD_DB_ADMIN_MEMBER') AND [task_id] not in                                                        
(select [task_id] from (SELECT [task_id], rank() over (partition by database_name order by task_id desc)     
as 'ranking' from [rdsadmin].[dbo].[rds_customer_tasks] where task_type in ('RESTORE_DB_NORECOVERY',         
'RESTORE_DB_LOG_NORECOVERY', 'RESTORE_DB_DIFFERENTIAL_NORECOVERY') and lifecycle = 'SUCCESS') RankedDatabaseName where ranking = 1)
go

USE [master];
SELECT * FROM sys.tables WHERE name = 'rds_database_tracking'
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

            SELECT d.database_id AS DatabaseId,
                   d.name AS Name, 
                   d.state_desc AS [State],
                   d.user_access_desc AS UserAccess,
                   d.recovery_model_desc AS RecoveryModel,
                   d.create_date AS CreateDate,
                   d.is_encrypted AS IsEncrypted,
                   d.is_read_only AS IsReadOnly,
                   d.replica_id AS ReplicaId,
                   d.group_database_id AS GroupDatabaseId,
                   rdt.rds_db_unique_id as RdsDbUniqueId,
                   rdt.lifecycle as RdsLifecycle
            FROM sys.databases d WITH (NOLOCK)
            LEFT OUTER join master.dbo.rds_database_tracking rdt WITH (NOLOCK)
			ON d.name = rdt.database_name
        
go

SELECT          d.name,
            map.family_guid,
            d.recovery_model_desc,
            d.is_auto_close_on,
            d.state_desc
FROM            sys.databases d
JOIN        rdsadmin..db_mappings map
ON  map.database_name = d.name
WHERE           d.name != 'tempdb'
go


SELECT * FROM rdsadmin..db_awaiting_snapshot
go
SELECT name, is_disabled FROM sys.server_triggers WITH (nolock)
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
SELECT 1
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go

SELECT 1
go

SELECT sqlserver_start_time FROM sys.dm_os_sys_info
go
select *, HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle)) as sql_id,     HASHBYTES('SHA2_256', CONCAT(sql_text, sql_handle, plan_handle)) as handle_id,     HASHBYTES('SHA2_256', CONCAT(plan_handle, query_plan_hash)) as plan_id     from (select s.session_id,     db_name(s.database_id) as db,     s.program_name,     s.login_name,      s.host_name,       r.sql_handle,      r.query_hash,      substring(t.text, (r.statement_start_offset/2)+1, ((CASE r.statement_end_offset WHEN -1 THEN DATALENGTH(t.TEXT) ELSE r.statement_end_offset END - r.statement_start_offset)/2)+1) sql_text,     r.wait_type,        r.plan_handle,       r.query_plan_hash     from sys.dm_exec_sessions s,          sys.dm_exec_requests r           outer apply sys.dm_exec_sql_text(r.sql_handle) t     where s.session_id = r.session_id           and s.session_id != @@SPID) f
go
