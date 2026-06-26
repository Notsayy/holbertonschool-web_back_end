# MySQL Advanced

This project focuses on advanced MySQL features: constraints, indexes, stored procedures, functions, views, and triggers. All scripts are executed on **Ubuntu 20.04 LTS** with **MySQL 8.0**.

## Requirements

- All SQL keywords must be in **UPPERCASE**
- Every query must have a comment just above it describing what it does
- Each file must start with a comment describing the task
- All files must end with a new line

## Setup

```bash
# Install MySQL 8.0
sudo apt update
sudo apt install mysql-server -y
sudo service mysql start

# Connect
sudo mysql -uroot
```

## Tasks

### 0. We are all unique! — `0-uniq_users.sql`

Creates a `users` table with the following columns:

| Column  | Type         | Constraints                           |
| ------- | ------------ | ------------------------------------- |
| `id`    | INT          | NOT NULL, AUTO_INCREMENT, PRIMARY KEY |
| `email` | VARCHAR(255) | NOT NULL, UNIQUE                      |
| `name`  | VARCHAR(255) | —                                     |

The script uses `CREATE TABLE IF NOT EXISTS` so it won't fail if the table already exists.
The `UNIQUE` constraint on `email` is enforced at the database level, preventing duplicate entries regardless of the application layer.

**Usage:**

```bash
cat 0-uniq_users.sql | mysql -uroot -p holberton
```

## Repository

- **GitHub:** `holbertonschool-web_back_end`
- **Directory:** `MySQL_Advanced`

# Author

[Notsayy](https://github.com/Notsayy)
