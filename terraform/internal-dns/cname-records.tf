resource "dns_cname_record" "k8s" {
  depends_on = [dns_cname_record.k8s]
  cname      = "raptor.cbxon.co.uk."
  name       = "k8s"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "jellyfin" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "jellyfin"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "jellyseerr" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "jellyseerr"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "radarr" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "radarr"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "sonarr" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "sonarr"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "prowlarr" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "prowlarr"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "qbittorrent" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "qbittorrent"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "grafana" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "grafana"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "guacamole" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "guacamole"
  zone       = "cbxon.co.uk."
}

resource "dns_cname_record" "authentik" {
  depends_on = [dns_cname_record.k8s]
  cname      = "k8s.cbxon.co.uk."
  name       = "authentik"
  zone       = "cbxon.co.uk."
}