# API Reference

## Command Line Interface

### Main Commands

#### validate
Validate VMware certificates

```bash
python main.py validate [OPTIONS]
```

**Options:**
- `--config PATH`: Configuration file path
- `--debug`: Enable debug mode
- `--help`: Show help message

**Example:**
```bash
python main.py validate --config config/production.yml
```

#### renew
Renew VMware certificates

```bash
python main.py renew [OPTIONS]
```

**Options:**
- `--force`: Force renewal even if not expired
- `--backup`: Create backup before renewal
- `--config PATH`: Configuration file path

**Example:**
```bash
python main.py renew --backup --config config/production.yml
```

#### backup
Backup VMware certificates

```bash
python main.py backup [OPTIONS]
```

**Options:**
- `--output PATH`: Backup output directory
- `--compress`: Compress backup files
- `--config PATH`: Configuration file path

**Example:**
```bash
python main.py backup --output /backups --compress
```

#### run
Run the certificate manager

```bash
python main.py run [OPTIONS]
```

**Options:**
- `--daemon`: Run as daemon
- `--config PATH`: Configuration file path
- `--debug`: Enable debug mode

## Python API

### VMwareCertManager Class

```python
from vmware_certs import VMwareCertManager

# Initialize with default config
manager = VMwareCertManager()

# Initialize with custom config
config = {
    'vcenter': {
        'host': 'vcenter.example.com',
        'username': 'admin',
        'password': 'password'
    }
}
manager = VMwareCertManager(config=config)
```

#### Methods

##### validate_certificates()
Validate all VMware certificates

**Returns:** `bool` - True if all certificates are valid

```python
is_valid = manager.validate_certificates()
```

##### renew_certificates()
Renew expiring certificates

**Returns:** `bool` - True if renewal successful

```python
success = manager.renew_certificates()
```

##### backup_certificates()
Create backup of certificates

**Returns:** `bool` - True if backup successful

```python
success = manager.backup_certificates()
```

## Configuration API

### Loading Configuration

```python
from vmware_certs.config import ConfigManager

config_manager = ConfigManager()
config = config_manager.load_config('config/config.yml')
```

### Environment Variables

```python
import os
from vmware_certs.config import get_env_config

# Get configuration from environment
env_config = get_env_config()
```

## Error Handling

### Exception Types

- `VMwareCertError`: Base exception for certificate operations
- `ConnectionError`: vCenter connection issues
- `AuthenticationError`: Authentication failures
- `CertificateValidationError`: Certificate validation failures

### Example Error Handling

```python
from vmware_certs import VMwareCertManager
from vmware_certs.exceptions import VMwareCertError

try:
    manager = VMwareCertManager()
    manager.validate_certificates()
except VMwareCertError as e:
    print(f"Certificate error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```# Updated Sun Nov  9 12:50:33 CET 2025
