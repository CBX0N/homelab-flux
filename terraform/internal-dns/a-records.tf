resource "dns_a_record_set" "hercules" {
  addresses = ["192.168.0.160"]
  name      = "hercules"
  zone      = "cbxon.co.uk."
}

resource "dns_a_record_set" "atlas" {
  addresses = ["192.168.0.249"]
  name      = "atlas"
  zone      = "cbxon.co.uk."
}

resource "dns_a_record_set" "raptor" {
  addresses = ["192.168.0.95"]
  name      = "raptor"
  zone      = "cbxon.co.uk."
}

resource "dns_a_record_set" "truenas" {
  addresses = ["192.168.0.250"]
  name      = "truenas"
  zone      = "cbxon.co.uk."
}

resource "dns_ptr_record" "raptor" {
  name = "0.95"
  ptr  = "raptor.cbxon.co.uk."
  zone = "168.192.in-addr.arpa."
}