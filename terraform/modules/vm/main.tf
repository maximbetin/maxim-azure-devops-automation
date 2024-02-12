# Resource Group Configuration
resource "azurerm_resource_group" "rg" {
  name     = "${var.prefix}-resources"
  location = "West Europe"
}

# Virtual Network Configuration
resource "azurerm_virtual_network" "vnet" {
  name                = "${var.prefix}-vnet"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name
  address_space       = ["10.0.0.0/16"] # TODO: Explain CIDR
}

# Subnet Configuration
resource "azurerm_subnet" "subnet" {
    name                 = "${var.prefix}-subnet"
    resource_group_name  = azurerm_resource_group.rg.name
    virtual_network_name = azurerm_virtual_network.vnet.name
    address_prefixes     = ["10.0.1.0/24"] # TODO: Explain CIDR
  
}

# Network Interface Configuration
resource "azurerm_network_interface" "interface" {
  name                = "${var.prefix}-interface"
  location            = azurerm_resource_group.rg.location
  resource_group_name = azurerm_resource_group.rg.name

  ip_configuration {
    name                          = "${var.prefix}-ip-config"
    subnet_id                     = azurerm_subnet.subnet.id
    private_ip_address_allocation = "Dynamic"
  }
}

# VM Configuration
resource "azurerm_virtual_machine" "vm" {
  name                  = "${var.prefix}-vm"
  location              = azurerm_resource_group.rg.location
  resource_group_name   = azurerm_resource_group.rg.name
  network_interface_ids = [azurerm_network_interface.interface.id]
  vm_size               = "Standard_DS1_v2"

  # Delete the OS and data disks when the VM is deleted
  delete_os_disk_on_termination = true
  delete_data_disks_on_termination = true

  # Define the operating system image
  storage_image_reference {
    publisher = "Canonical"
    offer     = "0001-com-ubuntu-server-jammy"
    sku       = "22_04-lts"
    version   = "latest"
  }

  # Define the operating system disk
  storage_os_disk {
    name              = "${var.prefix}-os-disk"
    caching           = "ReadWrite"
    create_option     = "FromImage"
    managed_disk_type = "Standard_LRS"
  }

  # Define the Linux Configuration
  os_profile {
    computer_name  = "${var.prefix}-vm"
    admin_username = "${var.admin_username}"
    admin_password = "Password1234!"
  }

  # Define the SSH Configuration
  os_profile_linux_config {
    disable_password_authentication = false

    ssh_keys {
        path     = "/home/${var.admin_username}/.ssh/authorized_keys"
        key_data = file("~/.ssh/id_rsa.pub")
    }
  }

  tags = {
    environment = "staging"
  }
}