# VCP-VCF Sample Questions

## Question 1
**What is the primary function of SDDC Manager in VMware Cloud Foundation?**

A) Virtual machine management  
B) Lifecycle management and automation  
C) Network security policies  
D) Storage provisioning  

**Answer:** B  
**Explanation:** SDDC Manager is the central component for lifecycle management, automation, and orchestration of the entire VCF stack.

## Question 2
**Which components are part of the Management Domain?**

A) Only vCenter Server  
B) vCenter Server and NSX Manager  
C) vCenter Server, NSX Manager, vRealize Suite, and SDDC Manager  
D) Only SDDC Manager  

**Answer:** C  
**Explanation:** The Management Domain contains all core management components including vCenter, NSX Manager, vRealize Suite, and SDDC Manager.

## Question 3
**What is the minimum number of ESXi hosts required for a VCF Management Domain?**

A) 2 hosts  
B) 3 hosts  
C) 4 hosts  
D) 6 hosts  

**Answer:** C  
**Explanation:** VCF requires a minimum of 4 ESXi hosts for the Management Domain to ensure proper redundancy and availability.

## Question 4
**Which network is used for vSAN traffic in VCF?**

A) Management Network  
B) vMotion Network  
C) vSAN Network  
D) Overlay Network  

**Answer:** C  
**Explanation:** vSAN has its own dedicated network segment for storage traffic to ensure optimal performance and isolation.

## Question 5
**What happens during a VCF workload domain creation?**

A) Only vCenter is deployed  
B) New ESXi hosts are automatically discovered  
C) A new vCenter instance and cluster are created  
D) Existing workloads are migrated  

**Answer:** C  
**Explanation:** Creating a workload domain involves deploying a new vCenter instance and creating a new cluster for that domain.

## Question 6
**Which tool is used to validate VCF hardware compatibility?**

A) vSphere Client  
B) VMware Compatibility Guide  
C) SDDC Manager  
D) vRealize Log Insight  

**Answer:** B  
**Explanation:** The VMware Compatibility Guide (VCG) is the official tool to verify hardware compatibility with VCF.

## Question 7
**What is the purpose of Network Pools in VCF?**

A) Load balancing network traffic  
B) Providing IP address ranges for VCF components  
C) Creating network security policies  
D) Managing virtual switches  

**Answer:** B  
**Explanation:** Network Pools define IP address ranges that VCF uses to assign addresses to various components during deployment.

## Question 8
**Which certificate authority is recommended for VCF production deployments?**

A) Self-signed certificates  
B) VMware Certificate Authority (VMCA)  
C) Enterprise Certificate Authority  
D) Public Certificate Authority  

**Answer:** C  
**Explanation:** For production environments, an Enterprise Certificate Authority is recommended for better security and management.

## Question 9
**What is the default backup schedule for SDDC Manager?**

A) Daily  
B) Weekly  
C) Monthly  
D) No default schedule  

**Answer:** D  
**Explanation:** SDDC Manager backups must be manually configured and scheduled by the administrator.

## Question 10
**Which port is used for SDDC Manager web interface?**

A) 443  
B) 80  
C) 8080  
D) 9443  

**Answer:** A  
**Explanation:** SDDC Manager web interface uses standard HTTPS port 443 for secure access.