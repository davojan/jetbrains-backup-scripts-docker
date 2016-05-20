# Helper Scripts for Managing Jetbrains Products Backups

Dockerized stateless helper scripts to manage backups of Jetbrains team products.

## Usage

Turn Upsource's ugly folder backups into gzipped archives with pretty names.

```bash
docker run --rm --volumes-from upsource davojan/jetbrains-backup-scripts archive-upsource-backup.py /data/backups/
```
