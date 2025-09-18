# Installation Guide

## Prerequisites

- Python 3.8 or higher
- VMware vCenter Server access
- Administrative privileges for certificate management

## Installation Methods

### Method 1: Direct Installation

```bash
# Clone the repository
git clone https://github.com/uldyssian-sh/vmware-vcp-vvf-vcf-certs.git
cd vmware-vcp-vvf-vcf-certs

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### Method 2: Docker Installation

```bash
# Build Docker image
docker build -t vmware-certs .

# Run container
docker run -v $(pwd)/config:/app/config vmware-certs
```

## Configuration

1. Copy the example configuration:
   ```bash
   cp config/config.yml.example config/config.yml
   ```

2. Edit the configuration file with your VMware environment details:
   ```yaml
   vcenter:
     host: "your-vcenter-server.domain.com"
     username: "administrator@vsphere.local"
     password: "your-password"
   ```

3. Set environment variables (optional):
   ```bash
   export VCENTER_HOST="your-vcenter-server.domain.com"
   export VCENTER_USERNAME="administrator@vsphere.local"
   export VCENTER_PASSWORD="your-password"
   ```

## Verification

Run the application to verify installation:

```bash
python main.py --help
```

## Troubleshooting

### Common Issues

1. **Connection Error**: Verify vCenter credentials and network connectivity
2. **Permission Error**: Ensure user has certificate management privileges
3. **SSL Error**: Check SSL certificate configuration

For more help, see [Troubleshooting Guide](troubleshooting.md).