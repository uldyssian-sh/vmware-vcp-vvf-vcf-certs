#!/usr/bin/env python3
"""
Advanced usage examples for VMware Certificate Manager
"""

import sys
import os
import json
import logging
from pathlib import Path
from datetime import datetime, timedelta, timezone

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import VMwareCertManager


class AdvancedCertManager(VMwareCertManager):
    """Extended certificate manager with advanced features"""
    
    def __init__(self, config=None):
        super().__init__(config)
        self.setup_advanced_logging()
    
    def setup_advanced_logging(self):
        """Setup advanced logging configuration"""
        # Create custom logger
        self.logger = logging.getLogger('advanced_cert_manager')
        self.logger.setLevel(logging.DEBUG)
        
        # Create file handler with rotation
        handler = logging.FileHandler('advanced-certs.log')
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        handler.setFormatter(formatter)
        self.logger.addHandler(handler)
    
    def get_certificate_status(self):
        """Get detailed certificate status information"""
        self.logger.info("Getting certificate status")
        
        # Mock certificate data - in real implementation, this would query vCenter
        certificates = [
            {
                'name': 'vCenter Server Certificate',
                'subject': 'CN=vcenter.example.com',
                'issuer': 'CN=VMware Certificate Authority',
                'valid_from': '2024-01-01T00:00:00Z',
                'valid_to': '2025-01-01T00:00:00Z',
                'status': 'valid',
                'days_until_expiry': 180
            },
            {
                'name': 'ESXi Host Certificate',
                'subject': 'CN=esxi01.example.com',
                'issuer': 'CN=VMware Certificate Authority',
                'valid_from': '2024-01-01T00:00:00Z',
                'valid_to': '2024-12-01T00:00:00Z',
                'status': 'expiring_soon',
                'days_until_expiry': 30
            }
        ]
        
        return certificates
    
    def generate_certificate_report(self):
        """Generate detailed certificate report"""
        self.logger.info("Generating certificate report")
        
        certificates = self.get_certificate_status()
        
        report = {
            'generated_at': datetime.now(timezone.utc).isoformat(),
            'total_certificates': len(certificates),
            'valid_certificates': len([c for c in certificates if c['status'] == 'valid']),
            'expiring_certificates': len([c for c in certificates if c['status'] == 'expiring_soon']),
            'expired_certificates': len([c for c in certificates if c['status'] == 'expired']),
            'certificates': certificates
        }
        
        return report
    
    def schedule_certificate_renewal(self, days_before_expiry=30):
        """Schedule automatic certificate renewal"""
        self.logger.info(f"Scheduling renewal for certificates expiring in {days_before_expiry} days")
        
        certificates = self.get_certificate_status()
        renewal_candidates = [
            c for c in certificates 
            if c['days_until_expiry'] <= days_before_expiry
        ]
        
        if renewal_candidates:
            self.logger.info(f"Found {len(renewal_candidates)} certificates for renewal")
            for cert in renewal_candidates:
                self.logger.info(f"Scheduling renewal for: {cert['name']}")
        else:
            self.logger.info("No certificates need renewal at this time")
        
        return renewal_candidates


def example_certificate_monitoring():
    """Example: Advanced certificate monitoring"""
    print("=== Advanced Certificate Monitoring ===")
    
    manager = AdvancedCertManager()
    
    # Get certificate status
    certificates = manager.get_certificate_status()
    
    print(f"Found {len(certificates)} certificates:")
    for cert in certificates:
        status_icon = "✅" if cert['status'] == 'valid' else "⚠️" if cert['status'] == 'expiring_soon' else "❌"
        print(f"  {status_icon} {cert['name']} - Expires in {cert['days_until_expiry']} days")
    
    return certificates


def example_certificate_reporting():
    """Example: Generate comprehensive certificate report"""
    print("\n=== Certificate Reporting ===")
    
    manager = AdvancedCertManager()
    
    # Generate report
    report = manager.generate_certificate_report()
    
    # Save report to file
    report_file = f"certificate_report_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    try:
        os.makedirs(os.path.dirname(report_file) or '.', exist_ok=True)
        with open(report_file, 'w') as f:
            json.dump(report, f, indent=2)
    except (IOError, OSError, PermissionError) as e:
        print(f"Error saving report: {e}")
        return None
    
    print(f"Certificate Report Generated: {report_file}")
    print(f"  Total Certificates: {report['total_certificates']}")
    print(f"  Valid: {report['valid_certificates']}")
    print(f"  Expiring Soon: {report['expiring_certificates']}")
    print(f"  Expired: {report['expired_certificates']}")
    
    return report


def example_automated_renewal():
    """Example: Automated certificate renewal workflow"""
    print("\n=== Automated Certificate Renewal ===")
    
    manager = AdvancedCertManager()
    
    # Schedule renewals for certificates expiring in 30 days
    renewal_candidates = manager.schedule_certificate_renewal(days_before_expiry=30)
    
    if renewal_candidates:
        print(f"Scheduled renewal for {len(renewal_candidates)} certificates:")
        for cert in renewal_candidates:
            print(f"  - {cert['name']} (expires in {cert['days_until_expiry']} days)")
        
        # Simulate renewal process
        print("\nExecuting renewal process...")
        success = manager.renew_certificates()
        print(f"Renewal result: {'✅ Success' if success else '❌ Failed'}")
    else:
        print("No certificates require renewal at this time")
    
    return renewal_candidates


def example_batch_operations():
    """Example: Batch certificate operations"""
    print("\n=== Batch Certificate Operations ===")
    
    manager = AdvancedCertManager()
    
    operations = [
        ('backup', manager.backup_certificates),
        ('validate', manager.validate_certificates),
        ('renew', manager.renew_certificates)
    ]
    
    results = {}
    
    for operation_name, operation_func in operations:
        print(f"Executing {operation_name}...")
        try:
            result = operation_func()
            results[operation_name] = result
            status = "✅ Success" if result else "❌ Failed"
            print(f"  {operation_name}: {status}")
        except Exception as e:
            results[operation_name] = False
            print(f"  {operation_name}: ❌ Error - {str(e)[:100]}")
            logger.error(f"Operation {operation_name} failed: {e}", exc_info=True)
    
    # Summary
    successful_ops = sum(1 for result in results.values() if result)
    total_ops = len(operations)
    
    print(f"\nBatch Operations Summary: {successful_ops}/{total_ops} successful")
    
    return results


def example_configuration_management():
    """Example: Dynamic configuration management"""
    print("\n=== Configuration Management ===")
    
    # Environment-specific configurations
    environments = {
        'development': {
            'vcenter': {
                'host': 'vcenter-dev.example.com',
                'verify_ssl': False
            },
            'logging': {
                'level': 'DEBUG'
            }
        },
        'production': {
            'vcenter': {
                'host': 'vcenter-prod.example.com',
                'verify_ssl': True
            },
            'logging': {
                'level': 'INFO'
            }
        }
    }
    
    # Select environment
    env = os.getenv('ENVIRONMENT', 'development')
    config = environments.get(env, environments['development'])
    
    print(f"Using configuration for environment: {env}")
    print(f"vCenter Host: {config['vcenter']['host']}")
    print(f"SSL Verification: {config['vcenter']['verify_ssl']}")
    print(f"Log Level: {config['logging']['level']}")
    
    # Initialize manager with environment-specific config
    try:
        manager = AdvancedCertManager(config=config)
    except Exception as e:
        print(f"Failed to initialize manager: {e}")
        return None
    
    return config


def main():
    """Run all advanced examples"""
    print("VMware Certificate Manager - Advanced Usage Examples")
    print("=" * 60)
    
    try:
        # Run advanced examples
        example_certificate_monitoring()
        example_certificate_reporting()
        example_automated_renewal()
        example_batch_operations()
        example_configuration_management()
        
        print("\n" + "=" * 60)
        print("✅ All advanced examples completed successfully")
        
    except Exception as e:
        print(f"\n❌ Advanced example failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())