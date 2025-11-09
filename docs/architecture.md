# VMware Cloud Foundation Architecture

## Overview

VMware Cloud Foundation (VCF) is a unified SDDC platform that bundles compute, storage, networking, and management into a single integrated solution.

## Core Components

### 1. SDDC Manager
- **Purpose:** Centralized lifecycle management
- **Functions:**
  - Automated deployment
  - Configuration management
  - Patch and update orchestration
  - Certificate management

### 2. Management Domain
- **Components:**
  - vCenter Server
  - NSX Manager
  - vRealize Suite
  - SDDC Manager
- **Purpose:** Manages the entire VCF environment

### 3. Workload Domains
- **VI Workload Domain:** vSphere-based workloads
- **NSX-T Workload Domain:** Micro-segmented applications
- **Custom Domains:** Specialized workload requirements

## Architecture Layers

### Physical Layer
- **Servers:** ESXi hosts with VCF compatibility
- **Networking:** ToR switches, spine-leaf topology
- **Storage:** vSAN or external storage arrays

### Virtualization Layer
- **Compute:** vSphere ESXi hypervisor
- **Storage:** vSAN distributed storage
- **Networking:** NSX-T software-defined networking

### Management Layer
- **SDDC Manager:** Lifecycle automation
- **vCenter:** Compute management
- **NSX Manager:** Network management
- **vRealize Suite:** Operations management

### Application Layer
- **Kubernetes:** Tanzu Kubernetes Grid
- **VMs:** Traditional virtual machines
- **Containers:** Cloud-native applications

## Exam Focus Areas

### VCP-VCF Topics
1. VCF architecture components (15%)
2. Management domain concepts (20%)
3. Workload domain types (25%)
4. Integration points (40%)

### Key Concepts to Master
- SDDC Manager functionality
- Domain relationships
- Network pools and IP allocation
- Certificate management workflows
- Backup and recovery procedures# Updated Sun Nov  9 12:50:33 CET 2025
# Updated Sun Nov  9 12:52:05 CET 2025
# Updated Sun Nov  9 12:57:00 CET 2025
