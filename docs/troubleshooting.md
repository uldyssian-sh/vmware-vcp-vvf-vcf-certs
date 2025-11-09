# Troubleshooting Guide

## Common Issues

### Connection Issues

#### Problem: Cannot connect to vCenter Server
**Symptoms:**
- Connection timeout errors
- SSL certificate errors
- Authentication failures

**Solutions:**
1. Verify vCenter server hostname/IP address
2. Check network connectivity: `ping vcenter-server.domain.com`
3. Verify port accessibility: `telnet vcenter-server.domain.com 443`
4. Check SSL certificate validity
5. Verify credentials and permissions

#### Problem: SSL Certificate Verification Failed
**Symptoms:**
- SSL verification errors
- Certificate chain issues

**Solutions:**
1. Disable SSL verification (not recommended for production):
   ```yaml
   vcenter:
     verify_ssl: false
   ```
2. Add custom CA certificate to trust store
3. Update system certificate store

### Authentication Issues

#### Problem: Authentication Failed
**Symptoms:**
- Login failures
- Permission denied errors

**Solutions:**
1. Verify username and password
2. Check user permissions in vCenter
3. Ensure user has certificate management privileges
4. Try using administrator@vsphere.local account

### Certificate Issues

#### Problem: Certificate Validation Fails
**Symptoms:**
- Certificate expiration warnings
- Invalid certificate errors

**Solutions:**
1. Check certificate expiration dates
2. Verify certificate chain integrity
3. Ensure proper certificate format
4. Check certificate permissions

#### Problem: Certificate Renewal Fails
**Symptoms:**
- Renewal process errors
- Backup creation failures

**Solutions:**
1. Ensure sufficient disk space for backups
2. Verify write permissions to backup directory
3. Check certificate service status
4. Review renewal logs for specific errors

### Configuration Issues

#### Problem: Configuration File Not Found
**Symptoms:**
- Config file not found errors
- Default configuration used

**Solutions:**
1. Verify config file path: `config/config.yml`
2. Check file permissions
3. Use absolute path if needed
4. Copy from example: `cp config/config.yml.example config/config.yml`

#### Problem: Invalid Configuration Format
**Symptoms:**
- YAML parsing errors
- Configuration validation failures

**Solutions:**
1. Validate YAML syntax: `python -c "import yaml; yaml.safe_load(open('config/config.yml'))"`
2. Check indentation (use spaces, not tabs)
3. Verify required fields are present
4. Review configuration documentation

## Debugging

### Enable Debug Mode

```bash
# Command line
python main.py --debug validate

# Environment variable
export DEBUG=true
python main.py validate

# Configuration file
debug: true
```

### Log Analysis

Check log files for detailed error information:

```bash
# View recent logs
tail -f vmware-certs.log

# Search for errors
grep -i error vmware-certs.log

# View specific time range
grep "2024-01-01" vmware-certs.log
```

### Verbose Output

Enable verbose logging:

```yaml
logging:
  level: DEBUG
  format: detailed
```

## Performance Issues

### Problem: Slow Certificate Operations
**Symptoms:**
- Long response times
- Timeout errors

**Solutions:**
1. Increase timeout values:
   ```yaml
   vcenter:
     timeout: 60
   ```
2. Check network latency to vCenter
3. Verify vCenter server performance
4. Reduce concurrent operations

### Problem: High Memory Usage
**Symptoms:**
- Out of memory errors
- System slowdown

**Solutions:**
1. Process certificates in batches
2. Increase system memory
3. Optimize certificate processing logic
4. Monitor memory usage patterns

## Getting Help

### Log Collection

Before reporting issues, collect relevant logs:

```bash
# Create support bundle
tar -czf support-bundle.tar.gz \
  vmware-certs.log \
  config/config.yml \
  /var/log/vmware/ \
  ~/.vmware/
```

### Issue Reporting

When reporting issues, include:

1. **Environment Information:**
   - Operating system and version
   - Python version
   - VMware vCenter version
   - Application version

2. **Error Details:**
   - Complete error messages
   - Stack traces
   - Log files
   - Configuration (sanitized)

3. **Steps to Reproduce:**
   - Exact commands used
   - Configuration settings
   - Expected vs actual behavior

### Support Channels

- **GitHub Issues**: [Create Issue](https://github.com/uldyssian-sh/vmware-vcp-vvf-vcf-certs/issues/new)
- **Documentation**: [Project Wiki](https://github.com/uldyssian-sh/vmware-vcp-vvf-vcf-certs/wiki)
- **Community**: [Discussions](https://github.com/uldyssian-sh/vmware-vcp-vvf-vcf-certs/discussions)# Updated Sun Nov  9 12:50:33 CET 2025
# Updated Sun Nov  9 12:52:05 CET 2025
# Updated Sun Nov  9 12:57:00 CET 2025
