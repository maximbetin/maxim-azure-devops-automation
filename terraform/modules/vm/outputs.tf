output "vm_id" {
  description = "Virtual Machine ID."
  value       = "${azurerm_virtual_machine.vm.id}"
}

output "network_interface_ids" {
  description = "Network Interface ID."
  value       = "${azurerm_network_interface.vm.id}"
}

output "network_interface_private_ip" {
  description = "Private IP address of the Network Interface."
  value       = "${azurerm_network_interface.vm.private_ip_address}"
}
