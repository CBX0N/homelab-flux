# Configure the DNS Provider
variable "key_secret" {
  type      = string
  sensitive = true
}

provider "dns" {
  update {
    server        = "192.168.0.25"
    key_name      = "cbxon.co.uk."
    key_algorithm = "hmac-sha256" #
    key_secret    = var.key_secret
  }
}