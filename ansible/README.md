# Configuring Infrastructure with Ansible

## Overview

This project uses Ansible to automate the deployment and configuration of a Virtual Machine in Azure, setting it up as an Apache-based Reverse Proxy. This setup is designed to efficiently manage web traffic by directing requests to a designated backend server.

## Prerequisites

- **Ansible Installation**: Ensure Ansible is installed on your machine. [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html).
- **SSH Access**: Configured for the Ubuntu VM to ensure secure command execution.
- **Azure CLI Installation**: Useful for managing Azure resources directly if necessary. [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli).

## Project Structure

The project is organized for easy management and scalability, featuring:

- **`ansible.cfg`**: Configuration file for Ansible, defining global settings.
- **`inventories/`**: 
  - Contains inventory files for different environments (e.g., staging).
  - **`staging/`**: 
    - **`hosts`**: Defines VMs in the staging environment.
    - **`group_vars/`**: Contains variables applicable to groups of hosts.
    - **`host_vars/`**: Stores variables specific to individual hosts.
- **`playbooks/`**: 
  - Holds Ansible playbooks, such as `setup-reverse-proxy.yml` for configuring Apache as a Reverse Proxy.
- **`roles/`**: 
  - Houses reusable roles for specific tasks, including the `apache-reverse-proxy` role with tasks, templates, default variables, and variable descriptions.

## Variables and Sensitive Data Handling

Variables enable playbook customization without altering main configurations, with sensitive data handled securely:

### Defining Variables

- **`roles/apache-reverse-proxy/defaults/main.yml`**: Specifies default values for the role.
- **`roles/apache-reverse-proxy/vars/main.yml`**: (For demonstration) Includes block comments describing possible scenarios for variable usage.
- **`group_vars/`** and **`host_vars/`**: Define environment or host-specific variables to fine-tune role behavior without direct playbook modifications.

### Handling Sensitive Data

- **Ansible Vault**: Encrypts sensitive variables (e.g., backend server URLs, SSH keys) to secure them within your project.

## Getting Started

### 1. Configure SSH Access

Set up your SSH keys and configure `known_hosts` for secure connections to Azure VMs.

### 2. Review and Update Inventory

Adjust `inventories/staging/hosts` with the IP addresses and SSH details of your Azure VMs.

### 3. Set Environment Variables (If Necessary)

If encountering issues with `ansible.cfg` not being recognized, set the `ANSIBLE_ROLES_PATH` environment variable:

```bash
export ANSIBLE_ROLES_PATH=$(pwd)/roles
```

This command temporarily sets the roles path for the current terminal session. For persistent changes, add it to your shell profile (e.g., `.bashrc` or `.zshrc`).

### 4. Execute the Playbook

```bash
ansible-playbook -i inventories/staging/hosts playbooks/setup-reverse-proxy.yml
```

This command configures your VM as an Apache Reverse Proxy according to the playbook specifications.

### 5. Verify the Configuration

Access your VM's IP address or domain name in a web browser to confirm the reverse proxy setup.

## Collaboration and Best Practices

- **Version Control**: Use Git to track and manage changes.
- **Ansible Best Practices**: Follow guidelines for playbook and role development to ensure project maintainability and scalability.
- **Sensitive Data Management**: Secure sensitive data with Ansible Vault and avoid embedding secrets directly in playbooks or inventory files.

Refer to the [Ansible Documentation](https://docs.ansible.com/ansible/latest/index.html) for comprehensive instructions and best practices.