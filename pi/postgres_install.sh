#!/bin/bash
set -e

# Required commands
REQUIRED_COMMANDS=("psql" "yq")

# Check for required commands
for cmd in "${REQUIRED_COMMANDS[@]}"; do
    if ! command -v "$cmd" >/dev/null 2>&1; then
        echo "$cmd could not be found"
        exit 1
    fi
done

# Confirm postgres user exists
if ! id "postgres" >/dev/null 2>&1; then
    echo "postgres service account could not be found"
    exit 1
fi

# Confirm script is being run as root
if [ "$EUID" -ne 0 ]; then
    echo "This script must be run as root or via sudo"
    exit 1
fi

#Check for secrets.yml
if [ ! -f "secrets.yml" ]; then
    echo "secrets.yml not found in current directory. Aborting."
    exit 1
fi

# Load values from secrets.yaml
DB_USER=$(yq '.db_user' secrets.yml | tr -d '"')
DB_PASSWORD=$(yq '.db_password' secrets.yml | tr -d '"')
DB_NAME=$(yq '.db_name' secrets.yml | tr -d '"')

echo "Creating database and user (if not exists)..."

sudo -u postgres psql <<EOF
DO \$\$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_catalog.pg_roles WHERE rolname = '$DB_USER'
   ) THEN
      CREATE ROLE $DB_USER LOGIN PASSWORD '$DB_PASSWORD';
   END IF;
END
\$\$;
EOF

echo "DB_USER: $DB_USER"

echo "Creating database if not exists..."
DB_EXISTS=$(sudo -u postgres psql -tAc "SELECT 1 FROM pg_database WHERE datname = '$DB_NAME'")

if [[ "$DB_EXISTS" != "1" ]]; then
  sudo -u postgres createdb -O "$DB_USER" "$DB_NAME"
  echo "Database '$DB_NAME' created."
else
  echo "Database '$DB_NAME' already exists."
fi

echo "PostgreSQL local setup complete."