terraform {
  
  # The version of Terraform to use
  required_providers {
    azurerm = {
      source = "hashicorp/azurerm"
      version = "3.91.0"
    }
  }
}

# The name of the provider to use
provider "azurerm" {
    features {}
}