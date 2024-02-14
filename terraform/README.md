# Provisioning Infrastructure with Terraform

## Overview

This project uses Terraform to provision a Virtual Machine in Azure, alongside necessary networking components.

## Prerequisites

- **Install [Terraform](https://www.terraform.io/downloads.html)**: Ensure you have Terraform installed on your machine (version >= 0.13 recommended).
- **Install [Azure CLI](https://docs.microsoft.com/en-us/cli/azure/install-azure-cli)**: Used for authenticating with Azure from your local machine.

## Project Structure

The project is organized into several key directories and files to facilitate easy management and scalability:

- **`main.tf`**: The entry point for Terraform configurations, containing provider setup and module invocations.
- **`variables.tf`**: Definitions of variables used across the project, including types and descriptions.
- **`outputs.tf`**: Defines outputs from the Terraform configurations that are important for the user or for downstream use.
- **`terraform.tfvars`**: Specifies values for the declared variables for a particular deployment (excluded from version control for sensitive data).
- **`versions.tf`**: Sets the required Terraform version and provider versions to ensure consistency across environments.
- **`modules/`**: Contains reusable modules for specific components like VMs, networking, etc.
    - Each module has its own `main.tf`, `variables.tf`, and `outputs.tf`.

## Variables and Sensitive Data Handling

Variables allow customization of the Terraform deployment without altering the main configuration files. Sensitive variables, such as passwords, are treated with additional care:

### Defining Variables

Variables are defined in `variables.tf` with possible descriptions and default values. Sensitive variables are marked with the `sensitive = true` flag to prevent their values from being displayed in logs or CLI output.

### Assigning Variable Values

- **For non-sensitive data**: The `tf.vars` holds the non-sensitive variable values.
- **For sensitive data**: Sensible variables are access through environment variables prefixed with `TF_VAR_`, e.g., `TF_VAR_admin_password`.

## Getting Started

### Step 1: Azure Authentication

1. **Login to Azure**:
   Open a terminal and use the Azure CLI to log in to your Azure account.

   ```bash
   az login
   ```

   A browser window will open for you to sign in to your Azure account.

2. **Set Subscription** (if you have multiple subscriptions):
   List your Azure subscriptions to find the subscription ID you want to use.

   ```bash
   az account list --query "[].{name:name, subscriptionId:id}"
   ```

   Set the subscription you want to use by replacing `YOUR_SUBSCRIPTION_ID` with the actual subscription ID.

   ```bash
   az account set --subscription YOUR_SUBSCRIPTION_ID
   ```

### Step 2: Configure Environment Variables

Set environment variables for sensitive data such as the admin password for the VM. Replace `YourSecurePasswordHere` with your actual password.

```bash
export TF_VAR_admin_password="YourSecurePasswordHere"
```

**Note**: For Windows Command Prompt, use `set` instead of `export`. For PowerShell, use `$env:TF_VAR_admin_password="YourSecurePasswordHere"`.

### Step 3: Initialize Terraform

Run the following command to initialize the Terraform workspace, which will download the necessary providers and set up the environment.

```bash
terraform init
```

### Step 4: Plan the Deployment

Generate and review an execution plan to see what Terraform will do before making any changes to your infrastructure.

```bash
terraform plan
```

### Step 5: Apply the Configuration

Apply the Terraform configuration to create resources in Azure. Terraform will prompt you for confirmation before proceeding.

```bash
terraform apply
```

Confirm the action by typing `yes` when prompted.

### Step 6: Access Your Resources

Once Terraform successfully applies your configuration, you can access and manage your Azure resources through the [Azure Portal](https://portal.azure.com) or using the Azure CLI.

## Managing State in Team Environments

In real-world scenarios, when working with Terraform in a team, it's essential to manage the state file in a way that promotes collaboration, prevents conflicts, and secures sensitive data.

### Remote State Backend

The recommended approach is to use a remote backend compatible with our cloud provider. This allows us to store the state file in a centralized, shared location, such as Azure Blob Storage.

### Configuration Example (Azure Blob Storage)

To configure Azure Blob Storage as the backend:

1. Create a storage account and container in Azure.
2. Add the backend configuration to your Terraform files:

    ```hcl
    terraform {
      backend "azurerm" {
        resource_group_name   = "MyResourceGroup"
        storage_account_name  = "mystorageaccount"
        container_name        = "tfstate"
        key                   = "terraform.tfstate"
      }
    }
    ```

3. Run `terraform init` to initialize the backend.

### State Locking and Security

- **State Locking**: Ensure your backend supports state locking to prevent concurrent state operations that could lead to conflicts.
- **Security**: Configure access controls to ensure only authorized team members can access the state file. Encrypt the backend to protect sensitive data contained in the state.

### Versioning

Enable versioning on your backend to keep a history of state changes, facilitating easier rollbacks if necessary.

### Best Practices

- **Access Control**: Use your cloud provider's access management tools to restrict access to the state file.
- **Sensitive Data**: Be mindful of sensitive data in your state file. Use encryption and secure access patterns.
- **Collaboration**: Use workspaces and modules to organize resources and collaborate effectively within your team.

For more detailed instructions and best practices, refer to the official [Terraform documentation](https://www.terraform.io/docs).

# TODO
Showcase the use of state files in backend?