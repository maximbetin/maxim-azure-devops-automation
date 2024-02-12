variable "prefix" {
  description = "Prefix for resource names."
  default     = "devops-automation"
}

variable "location" {
  description = "Azure region for all resources."
  default     = "West Europe"
  type        = string
}

variable "admin_username" {
  description = "Admin username for the VM."
  default     = "maxim"
  type        = string
}

variable "admin_password" {
  description = "The administrator password for the VM."
  sensitive   = true
  type        = string
}
