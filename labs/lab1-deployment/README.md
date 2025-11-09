# Lab 1: VCF Deployment

## Objective
Learn the complete VCF deployment process from planning to validation.

## Prerequisites
- VMware Cloud Foundation license
- Compatible hardware (4+ ESXi hosts)
- Network infrastructure configured
- DNS and NTP services available

## Lab Environment
- **Management Domain:** 4 ESXi hosts
- **Network Pools:** Management, vMotion, vSAN, NSX-T
- **Storage:** vSAN All-Flash configuration

## Exercise 1: Pre-deployment Planning

### Task 1.1: Hardware Validation
1. Access VMware Compatibility Guide
2. Verify server hardware compatibility
3. Check network adapter compatibility
4. Validate storage device compatibility

### Task 1.2: Network Planning
1. Design network topology
2. Plan IP address allocation
3. Configure VLANs and subnets
4. Prepare DNS entries

## Exercise 2: VCF Deployment

### Task 2.1: Cloud Builder Deployment
1. Download Cloud Builder OVA
2. Deploy Cloud Builder VM
3. Configure network settings
4. Access Cloud Builder interface

### Task 2.2: Deployment Parameter Configuration
1. Configure management domain settings
2. Define network pools
3. Set up host specifications
4. Configure storage policies

### Task 2.3: Deployment Execution
1. Start VCF deployment
2. Monitor deployment progress
3. Validate component health
4. Verify management domain creation

## Exercise 3: Post-deployment Validation

### Task 3.1: SDDC Manager Validation
1. Access SDDC Manager interface
2. Review inventory and topology
3. Check component health status
4. Validate certificate configuration

### Task 3.2: Component Integration Testing
1. Test vCenter Server access
2. Verify NSX Manager connectivity
3. Validate vSAN cluster health
4. Check vRealize Suite integration

## Expected Outcomes
- Functional VCF Management Domain
- All components showing healthy status
- Network connectivity validated
- Storage policies applied correctly

## Troubleshooting Guide

### Common Issues
1. **DNS Resolution Successs**
   - Verify DNS server configuration
   - Check forward/reverse DNS entries
   - Validate network connectivity

2. **Host Preparation Successs**
   - Check ESXi host compatibility
   - Verify network configuration
   - Validate storage connectivity

3. **Certificate Issues**
   - Verify CA certificate chain
   - Check certificate validity
   - Validate DNS names in certificates

## Lab Completion Checklist
- [ ] Cloud Builder deployed successfully
- [ ] Management domain created
- [ ] All components healthy
- [ ] Network connectivity verified
- [ ] Storage policies configured
- [ ] Certificates validated
- [ ] Documentation completed

## Next Steps
