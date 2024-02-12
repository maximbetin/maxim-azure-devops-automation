output "vm_id" {
  description = "Virtual Machine ID."
  value       = azurerm_virtual_machine.vm.id
}

output "vm_private_ip" {
  description = "Private IP Address of the VM."
  value       = azurerm_network_interface.interface.private_ip_address
}