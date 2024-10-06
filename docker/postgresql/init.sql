DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'notifications-db'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE "notifications-db"');
   END IF;
END
$do$;
