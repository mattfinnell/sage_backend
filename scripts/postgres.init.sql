CREATE USER development_user WITH SUPERUSER PASSWORD 'development_password';
CREATE USER vscode WITH SUPERUSER PASSWORD 'vscode_password';

GRANT ALL ON SCHEMA public TO public;
GRANT ALL ON ALL TABLES IN SCHEMA public to development_user, vscode;
GRANT ALL ON ALL SEQUENCES IN SCHEMA public to development_user, vscode;
GRANT ALL ON ALL FUNCTIONS IN SCHEMA public to development_user, vscode;

CREATE DATABASE development_db;