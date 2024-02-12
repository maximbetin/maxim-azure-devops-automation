# Configuring the Infrastructure with Ansible

## Overview

This project leverages Ansible to automate the deployment and configuration of a Virtual Machine in Azure, transforming it into an efficient Reverse Proxy via Apache. This setup is designed to streamline web traffic management, directing requests to a designated backend server seamlessly.

## Prerequisites

- An Ubuntu VM (22.04) designated for Apache installation.
- Ansible installed on your control machine, facilitating automation. [Installation Guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html#pipx-install)
- SSH access configured for the Ubuntu VM, ensuring secure command execution.
- The IP address or hostname of your backend server, critical for reverse proxy setup.

## Getting Started

### 1. Install Ansible

First, ensure Ansible is installed on your control machine. This can typically be accomplished using your distribution's package manager. For Ubuntu/Debian systems:

```bash
sudo apt update
sudo apt install ansible
```

### 2. Configure Ansible Inventory

Next, prepare your inventory by creating a file named `inventory.ini` and populating it as follows:

```ini
[webserver]
your_vm_ip ansible_user=your_vm_ssh_user ansible_ssh_private_key_file=/path/to/your/private/key
```

Adjust `your_vm_ip`, `your_vm_ssh_user`, and `/path/to/your/private/key` to match your specific setup.

### 3. Develop the Ansible Playbook

This playbook is designed to automate the Apache installation and its configuration as a Reverse Proxy. Replace `http://your_vm_ip/` with your actual backend server's URL or IP address in the playbook's reverse proxy configuration section.

### 4. Execute the Playbook

Deploy the configuration by running the playbook with this command:

```bash
ansible-playbook -i inventory.ini setup-reverse-proxy.yml
```

This initiates the automation process, installing and configuring Apache on your Ubuntu VM as outlined in the playbook.

## Detailed Playbook Description

This playbook executes several key tasks to configure Apache as a Reverse Proxy on a Debian-based web server:

- **Install Apache**: Verifies and installs Apache (`apache2` package) if it's not already present, targeting Debian-based systems specifically.
- **Enable Apache Modules**: Automates the activation of `mod_proxy` and `mod_proxy_http` modules, essential for reverse proxy functionality.
- **Configure Apache Service**: Ensures Apache starts at boot and remains active, leveraging the `ansible.builtin.systemd` module for service management.
- **Apply Reverse Proxy Configuration**: Injects a predefined configuration block into `/etc/apache2/sites-available/000-default.conf`, directing HTTP requests to the specified backend server.
- **Restart Apache**: Utilizes a handler to restart Apache if configuration changes are made, applying the new settings immediately.

## Verification

Confirm the successful configuration by accessing your VM's IP address in a browser. The expected result is the content from your backend server being served through the Apache Reverse Proxy, demonstrating the playbook's effectiveness.

## Disclaimer

**Recommended Approach:** While executing the playbook, ensure that you have a secure connection to your Azure VM, preferably through a Jump/Bastion host or VPN to maintain security and efficiency. Direct SSH access from the public internet to your VM should be avoided to minimize security risks.