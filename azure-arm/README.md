# Azure Resource Management with PowerShell

This README provides guidance on managing Azure resources using Azure Resource Manager (ARM) through PowerShell. It covers the installation of Azure PowerShell, key concepts of ARM, and steps for deploying resources using ARM templates.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installing Azure PowerShell](#installing-azure-powershell)
- [Key Concepts](#key-concepts)
- [Best Practices](#best-practices)
- [Creating a Storage Account and Resource Group](#creating-a-storage-account-and-resource-group)
- [Azure Resource Manager vs. Terraform](#azure-resource-manager-vs-terraform)


## Prerequisites

- An active Azure subscription.
- PowerShell 5.1 or higher on Windows or PowerShell Core 6.x and later on macOS and Linux.
- Basic understanding of Azure services and PowerShell command execution.

## Installing Azure PowerShell

1. Open PowerShell as an administrator.
2. Execute the installation command:

```powershell
Install-Module -Name PowerShellGet -Force
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
Install-Module -Name Az -Repository PSGallery -Force
```

3. Log in to your Azure account:

```powershell
Connect-AzAccount
```

## Key Concepts

- **Resource Groups**: Containers for organizing resources related to an Azure solution.
- **Resources**: Individual manageable items available through Azure.
- **ARM Templates**: JSON files that define the resources you need to deploy for your solution.
- **Resource Providers**: Services that supply Azure resources, such as virtual machines or storage accounts.
- **Deployment Modes**: Includes incremental and complete deployments, affecting how resources are updated or replaced.
- **Scope**: Defines the level at which access control and policies are applied, ranging from management groups to individual resources.

### ARM Template JSON Structure

- **$schema**: Specifies the location of the JSON schema file that describes the version of the template language. It helps with template validation.
- **contentVersion**: A version number for the template itself. It's used for document management and has no effect on the deployment process.
- **parameters**: Inputs that are passed to the template at deployment time. Parameters allow for customization of resource deployments without altering the template.
- **variables**: Values that are used within the template to simplify complex expressions and can be constructed from parameter values.
- **resources**: The Azure resources that will be deployed or updated by the template. Each resource declaration includes type, apiVersion, properties, and other deployment information.
- **outputs**: Values that are returned after deployment. Useful for retrieving information about deployed resources, like dynamically assigned properties (e.g., a storage account's URL).

## Best Practices

- **Use Resource Groups wisely**: Organize resources based on lifecycle and management considerations.
- **Leverage Tags**: Apply tags to resources for easier categorization and management.
- **Monitor and Audit**: Regularly review your ARM deployments and configurations to ensure compliance with your architectural requirements.

## Creating a Storage Account and Resource Group

### Create a Resource Group

Unlike in Terraform, key reasons for creating a resource group through PowerShell or Azure CLI, rather than directly with ARM templates like in Terraform, are:

- **Scope**: ARM templates are designed for deploying resources within a resource group, not for creating the resource group itself.
- **Preparation**: A resource group acts as a necessary organizational container and must exist before deploying resources into it using ARM templates.
- **Operational Model**: Azure separates administrative tasks (like creating resource groups) from resource deployment tasks to maintain clarity and manageability.

This approach ensures a clear separation between setting up the environment (creating resource groups) and deploying resources (using ARM templates), which aligns with Azure's management and operational practices. More details on the differences between Terraform and Azure Resource Manager are outlined in the [Azure Resource Manager vs. Terraform](a) section.

```powershell
$resourceGroup = "<resource-group>"
$location = "<location>"
New-AzResourceGroup -Name $resourceGroup -Location $location
```

### Create a Storage Account

1. **Sign in** to Azure and **select your subscription**.

```powershell
Connect-AzAccount
```

2. **Deploy the ARM template** to your resource group.

```powershell
New-AzResourceGroupDeployment -ResourceGroupName $resourceGroup -TemplateFile ".\azure-arm\azuredeploy.json" -TemplateParameterFile ".\azure-arm\azuredeploy.parameters.json"
```

### Verification

Verify the deployment in the Azure portal or using Azure PowerShell commands like `Get-AzResource`.

## Azure Resource Manager vs. Terraform

One might assume that ARM is Azure's version of Terraform, however, although partially true, there are some key differences:

- **Scope and Flexibility**: Terraform is a cross-platform tool that supports multiple cloud providers, including Azure, AWS, and Google Cloud, offering a broader scope and more flexibility. ARM templates are specific to Azure resources.

- **State Management**: Terraform tracks state and provides insights into what will change before applying a plan, enhancing predictability and management. ARM templates do not have built-in state management.

- **Syntax and Language**: Terraform uses HashiCorp Configuration Language (HCL), which is designed to be readable and writable by humans. ARM templates use JSON, which can be more verbose and less human-friendly.

- **Resource Group Creation**: Terraform can manage the creation of Azure resource groups as part of its execution plan, whereas ARM templates require the resource group to exist beforehand, typically created via Azure CLI or PowerShell.

- **Community and Ecosystem**: Terraform benefits from a large, active community and a broad ecosystem due to its support for multiple providers. ARM templates have strong support within the Azure ecosystem but are limited to Azure.

These differences make Terraform a versatile tool for managing infrastructure across various cloud platforms with advanced features like state management, whereas ARM templates are a powerful, Azure-specific solution for deploying resources within the Azure cloud.

---

This README provides a foundational guide to managing Azure resources with ARM and PowerShell. For more detailed information, refer to the official [Azure PowerShell documentation](https://docs.microsoft.com/en-us/powershell/azure/) and [Azure Resource Manager documentation](https://docs.microsoft.com/en-us/azure/azure-resource-manager/management/overview).