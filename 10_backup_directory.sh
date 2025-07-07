#!/bin/bash

SOURCE_DIR="$HOME/devops-bash-scripts"
BACKUP_DIR="$HOME/backup"
mkdir -p "$BACKUP_DIR"

BACKUP_FILE="$BACKUP_DIR/backup-$(date +%F).tar.gz"
tar -czf "$BACKUP_FILE" "$SOURCE_DIR"

echo "Backup created: $BACKUP_FILE"
