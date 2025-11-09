# Configuration Guide

## Configuration Methods

The application supports multiple configuration methods:

1. **Configuration File** (`config/config.yml`)
2. **Environment Variables**
3. **Command Line Arguments**

## Configuration File

The main configuration file is located at `config/config.yml`:

```yaml
app:
  name: vmware-vcp-vvf-vcf-certs
  version: "1.0.0"
  debug: false
  environment: production

logging:
  level: INFO
  format: json
  file: vmware-certs.log

vcenter:
  host: "vcenter.example.com"
  username: "administrator@vsphere.local"
  password: "secure-password"
  port: 443
  verify_ssl: true
  timeout: 30

certificates:
  backup_path: "./backups"
  renewal_threshold_days: 30
  validation_interval_hours: 24

security:
  encryption_enabled: true
  audit_logging: true
  secure_storage: true
```

## Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `VCENTER_HOST` | vCenter Server hostname | - |
| `VCENTER_USERNAME` | vCenter username | - |
| `VCENTER_PASSWORD` | vCenter password | - |
| `VCENTER_PORT` | vCenter port | 443 |
| `DEBUG` | Enable debug mode | false |
| `LOG_LEVEL` | Logging level | INFO |

## Security Configuration

### SSL/TLS Settings

```yaml
vcenter:
  verify_ssl: true  # Verify SSL certificates
  ssl_cert_path: "/path/to/cert.pem"
  ssl_key_path: "/path/to/key.pem"
```

### Encryption

```yaml
security:
  encryption_enabled: true
  encryption_key: "your-encryption-key"
  secure_storage: true
```

## Advanced Configuration

### Custom Certificate Paths

```yaml
certificates:
  custom_paths:
    - "/opt/vmware/certs"
    - "/etc/ssl/vmware"
  exclude_patterns:
    - "*.tmp"
    - "backup_*"
```

### Notification Settings

```yaml
notifications:
  email:
    enabled: true
    smtp_server: "smtp.example.com"
    smtp_port: 587
    username: "notifications@example.com"
    password: "smtp-password"
  slack:
    enabled: false
    webhook_url: "https://hooks.slack.com/..."
```# Updated Sun Nov  9 12:50:33 CET 2025
# Updated Sun Nov  9 12:52:05 CET 2025
