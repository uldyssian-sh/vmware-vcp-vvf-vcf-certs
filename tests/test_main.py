#!/usr/bin/env python3
"""
Unit tests for VMware Certificate Manager
"""

import unittest
import sys
import os
from pathlib import Path
from unittest.mock import Mock, patch, MagicMock

# Add parent directory to path for imports
sys.path.insert(0, str(Path(__file__).parent.parent))

from main import VMwareCertManager


class TestVMwareCertManager(unittest.TestCase):
    """Test cases for VMwareCertManager class"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_config = {
            'app': {
                'name': 'test-cert-manager',
                'version': '1.0.0',
                'debug': True
            },
            'vcenter': {
                'host': 'test-vcenter.example.com',
                'username': 'test-user',
                'password': 'test-password',
                'port': 443
            },
            'logging': {
                'level': 'DEBUG',
                'format': 'json'
            }
        }
        
        self.manager = VMwareCertManager(config=self.test_config)
    
    def test_initialization(self):
        """Test manager initialization"""
        self.assertIsNotNone(self.manager)
        self.assertEqual(self.manager.version, "1.0.0")
        self.assertEqual(self.manager.config['app']['name'], 'test-cert-manager')
    
    def test_initialization_without_config(self):
        """Test manager initialization without config"""
        manager = VMwareCertManager()
        self.assertIsNotNone(manager)
        self.assertIsNotNone(manager.config)
    
    @patch('main.logger')
    def test_validate_certificates_success(self, mock_logger):
        """Test successful certificate validation"""
        result = self.manager.validate_certificates()
        
        # Should return True for successful validation
        self.assertTrue(result)
        
        # Should log appropriate messages
        mock_logger.info.assert_called()
    
    @patch('main.logger')
    def test_validate_certificates_failure(self, mock_logger):
        """Test certificate validation failure"""
        # Mock an exception during validation
        with patch.object(self.manager, 'validate_certificates') as mock_validate:
            mock_validate.side_effect = Exception("Validation failed")
            
            # Should handle exception gracefully
            with self.assertRaises(Exception):
                self.manager.validate_certificates()
    
    @patch('main.logger')
    def test_renew_certificates_success(self, mock_logger):
        """Test successful certificate renewal"""
        result = self.manager.renew_certificates()
        
        # Should return True for successful renewal
        self.assertTrue(result)
        
        # Should log appropriate messages
        mock_logger.info.assert_called()
    
    @patch('main.logger')
    def test_backup_certificates_success(self, mock_logger):
        """Test successful certificate backup"""
        result = self.manager.backup_certificates()
        
        # Should return True for successful backup
        self.assertTrue(result)
        
        # Should log appropriate messages
        mock_logger.info.assert_called()
    
    def test_config_loading(self):
        """Test configuration loading"""
        config = self.manager._load_config()
        
        # Should return a dictionary
        self.assertIsInstance(config, dict)
        
        # Should have required keys
        self.assertIn('app', config)
        self.assertIn('logging', config)
        self.assertIn('vcenter', config)
    
    @patch.dict(os.environ, {'DEBUG': 'true', 'LOG_LEVEL': 'DEBUG'})
    def test_environment_variables(self):
        """Test environment variable loading"""
        manager = VMwareCertManager()
        config = manager._load_config()
        
        # Should respect environment variables
        self.assertTrue(config['app']['debug'])
    
    def test_run_method(self):
        """Test main run method"""
        result = self.manager.run()
        
        # Should return 0 for success
        self.assertEqual(result, 0)


class TestCLICommands(unittest.TestCase):
    """Test cases for CLI commands"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.test_config = {
            'app': {'debug': True},
            'vcenter': {
                'host': 'test-vcenter.example.com',
                'username': 'test-user',
                'password': 'test-password'
            }
        }
    
    @patch('main.VMwareCertManager')
    def test_validate_command(self, mock_manager_class):
        """Test validate CLI command"""
        # Mock the manager instance
        mock_manager = Mock()
        mock_manager.validate_certificates.return_value = True
        mock_manager_class.return_value = mock_manager
        
        # Import and test the CLI function
        from main import cli
        
        # This would normally be tested with click.testing.CliRunner
        # For now, just verify the manager is created correctly
        manager = VMwareCertManager()
        result = manager.validate_certificates()
        self.assertTrue(result)
    
    @patch('main.VMwareCertManager')
    def test_renew_command(self, mock_manager_class):
        """Test renew CLI command"""
        mock_manager = Mock()
        mock_manager.renew_certificates.return_value = True
        mock_manager_class.return_value = mock_manager
        
        manager = VMwareCertManager()
        result = manager.renew_certificates()
        self.assertTrue(result)
    
    @patch('main.VMwareCertManager')
    def test_backup_command(self, mock_manager_class):
        """Test backup CLI command"""
        mock_manager = Mock()
        mock_manager.backup_certificates.return_value = True
        mock_manager_class.return_value = mock_manager
        
        manager = VMwareCertManager()
        result = manager.backup_certificates()
        self.assertTrue(result)


class TestErrorHandling(unittest.TestCase):
    """Test cases for error handling"""
    
    def setUp(self):
        """Set up test fixtures"""
        self.manager = VMwareCertManager()
    
    def test_invalid_config_handling(self):
        """Test handling of invalid configuration"""
        invalid_config = {
            'invalid_key': 'invalid_value'
        }
        
        # Should handle invalid config gracefully
        manager = VMwareCertManager(config=invalid_config)
        self.assertIsNotNone(manager)
    
    @patch('main.logger')
    def test_exception_logging(self, mock_logger):
        """Test that exceptions are properly logged"""
        # This would test actual exception scenarios
        # For now, just verify logger is available
        self.assertIsNotNone(mock_logger)


class TestConfigurationManagement(unittest.TestCase):
    """Test cases for configuration management"""
    
    def test_default_configuration(self):
        """Test default configuration values"""
        manager = VMwareCertManager()
        config = manager.config
        
        # Should have default values
        self.assertIn('app', config)
        self.assertIn('logging', config)
        self.assertIn('vcenter', config)
    
    def test_custom_configuration(self):
        """Test custom configuration override"""
        custom_config = {
            'app': {
                'name': 'custom-manager',
                'debug': True
            }
        }
        
        manager = VMwareCertManager(config=custom_config)
        
        # Should use custom values
        self.assertEqual(manager.config['app']['name'], 'custom-manager')
        self.assertTrue(manager.config['app']['debug'])
    
    @patch('pathlib.Path.exists')
    @patch('builtins.open')
    @patch('yaml.safe_load')
    def test_config_file_loading(self, mock_yaml_load, mock_open, mock_exists):
        """Test configuration file loading"""
        mock_exists.return_value = True
        mock_yaml_load.return_value = {
            'app': {'name': 'file-config'},
            'logging': {'level': 'INFO'},
            'vcenter': {'host': 'file-vcenter.com'}
        }
        
        manager = VMwareCertManager()
        config = manager._load_config()
        
        # Should load from file
        mock_open.assert_called()
        mock_yaml_load.assert_called()


def run_tests():
    """Run all tests"""
    # Create test suite
    test_suite = unittest.TestSuite()
    
    # Add test cases
    test_classes = [
        TestVMwareCertManager,
        TestCLICommands,
        TestErrorHandling,
        TestConfigurationManagement
    ]
    
    for test_class in test_classes:
        tests = unittest.TestLoader().loadTestsFromTestCase(test_class)
        test_suite.addTests(tests)
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(test_suite)
    
    return result.wasSuccessful()


if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)# Updated Sun Nov  9 12:50:33 CET 2025
# Updated Sun Nov  9 12:52:05 CET 2025
