#!/usr/bin/env python3
"""
Basic usage examples for VMware Certificate Manager
"""

import sys
import os
from pathlib import Path

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import VMwareCertManager


def example_basic_validation():
    """Example: Basic certificate validation"""
    print("=== Basic Certificate Validation ===")
    
    # Initialize with default configuration
    try:
        manager = VMwareCertManager()
    except Exception as e:
        print(f"Failed to initialize certificate manager: {e}")
        return False
    
    # Validate certificates
    is_valid = manager.validate_certificates()
    
    if is_valid:
        print("✅ All certificates are valid")
    else:
        print("❌ Some certificates need attention")
    
    return is_valid


def example_custom_config():
    """Example: Using custom configuration"""
    print("\n=== Custom Configuration Example ===")
    
    # Custom configuration - use environment variables for credentials
    config = {
        'app': {
            'name': 'custom-cert-manager',
            'debug': True
        },
        'vcenter': {
            'host': os.getenv('VCENTER_HOST', 'vcenter.example.com'),
            'username': os.getenv('VCENTER_USERNAME', 'administrator@vsphere.local'),
            'password': os.getenv('VCENTER_PASSWORD', ''),
            'port': int(os.getenv('VCENTER_PORT', '443'))
        },
        'logging': {
            'level': 'DEBUG'
        }
    }
    
    # Initialize with custom config
    manager = VMwareCertManager(config=config)
    
    # Run validation
    result = manager.validate_certificates()
    print(f"Validation result: {result}")
    
    return result


def example_certificate_operations():
    """Example: Complete certificate operations workflow"""
    print("\n=== Complete Certificate Operations ===")
    
    try:
        manager = VMwareCertManager()
        
        # Step 1: Backup existing certificates
        print("1. Creating certificate backup...")
        backup_success = manager.backup_certificates()
        print(f"   Backup result: {'✅ Success' if backup_success else '❌ Failed'}")
        
        # Step 2: Validate certificates
        print("2. Validating certificates...")
        validation_success = manager.validate_certificates()
        print(f"   Validation result: {'✅ Valid' if validation_success else '❌ Invalid'}")
        
        # Step 3: Renew if needed
        if not validation_success:
            print("3. Renewing certificates...")
            renewal_success = manager.renew_certificates()
            print(f"   Renewal result: {'✅ Success' if renewal_success else '❌ Failed'}")
        else:
            print("3. Certificate renewal not needed")
            renewal_success = True
        
        # Return overall success
        return backup_success and validation_success and renewal_success
    except Exception as e:
        print(f"❌ Certificate operations failed: {e}")
        return False


def example_error_handling():
    """Example: Error handling and logging"""
    print("\n=== Error Handling Example ===")
    
    try:
        # Initialize with invalid configuration for testing
        config = {
            'vcenter': {
                'host': 'invalid-host.example.com',
                'username': os.getenv('TEST_USERNAME', 'test-user'),
                'password': os.getenv('TEST_PASSWORD', '')
            }
        }
        
        manager = VMwareCertManager(config=config)
        
        # This should fail gracefully
        result = manager.validate_certificates()
        print(f"Validation result: {result}")
        
    except Exception as e:
        print(f"Caught exception: {e}")
        print("Application handled the error gracefully")


def main():
    """Run all examples"""
    print("VMware Certificate Manager - Usage Examples")
    print("=" * 50)
    
    try:
        # Run examples
        results = []
        results.append(example_basic_validation())
        results.append(example_custom_config())
        results.append(example_certificate_operations())
        example_error_handling()
        
        if not all(r for r in results if r is not None):
            print("\n⚠️ Some examples had issues")
            return 1
        
        print("\n" + "=" * 50)
        print("✅ All examples completed successfully")
        
    except Exception as e:
        print(f"\n❌ Example failed: {e}")
        return 1
    
    return 0


if __name__ == "__main__":
    sys.exit(main())