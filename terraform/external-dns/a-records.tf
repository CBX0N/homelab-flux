resource "cloudflare_dns_record" "root" {
  name    = "cbxon.co.uk"
  ttl     = 1
  type    = "A"
  zone_id = var.zone_id
  content = var.public_ip
}
