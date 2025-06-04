resource "cloudflare_dns_record" "guacamole" {
  name    = "guacamole.cbxon.co.uk"
  ttl     = 1
  type    = "CNAME"
  zone_id = var.zone_id
  content = "cbxon.co.uk"
}

resource "cloudflare_dns_record" "grafana" {
  name    = "grafana.cbxon.co.uk"
  ttl     = 1
  type    = "CNAME"
  zone_id = var.zone_id
  content = "cbxon.co.uk"
}