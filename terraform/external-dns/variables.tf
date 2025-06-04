variable "cloudflare_api_token" {
  type      = string
  sensitive = true
}

variable "public_ip" {
  type = string
}

variable "zone_id" {
  type = string
}
