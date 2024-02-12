module "vm" {
  source = "./modules/vm"

  prefix         = var.prefix
  location       = var.location
  admin_username = var.admin_username
}