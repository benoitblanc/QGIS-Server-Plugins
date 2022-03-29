import os

# Cache duration in seconds
cache_ttl = 60

# Debug mode prints messages and raises SQL errors
debug = True

# The Secret Key to decode the JWT in case of Bearer authentication
jwt_secret_key = os.environ.get('JWT_SECRET_KEY', '******')

# The Environement variable that contains the user name (e.g. REMOTE_USER, CAS-User, ...)
user_env_var = 'REMOTE_USER'

# The default user for anonymous connections (should have less permissions than any others)
default_user = 'siglc'

# SQL query to get user permissions on a schema
# We expect this query to take 2 named parameters
#    %(user)s   - The user name
#    %(schema)s - The schema name
# and to return 5 columns in the following order:
#    0 - table name, text
#    1 - select permission, bool
#    2 - insert permission, bool
#    3 - update permission, bool
#    4 - delete permission, bool
perms_sql = "SELECT t.tablename, has_table_privilege(%(user)s, t.schemaname || '.' || t.tablename, 'SELECT') as canRead, has_table_privilege(%(user)s, t.schemaname || '.' || t.tablename, 'INSERT') as canInsert, has_table_privilege(%(user)s, t.schemaname || '.' || t.tablename, 'UPDATE') as canUpdate, has_table_privilege(%(user)s, t.schemaname || '.' || t.tablename, 'DELETE') as canDelete FROM pg_catalog.pg_tables t WHERE t.schemaname = %(schema)s"
role_sql = "SELECT rolname FROM pg_roles WHERE rolname=%(user)s"
