resource "dns_a_record_set" "k8s" {
  addresses = [ "192.168.0.243" ]
  name = "k8s"
  zone = "cbxon.co.uk."
}

resource "dns_ptr_record" "k8s" {
  name = "0.243"
  ptr = "k8s.cbxon.co.uk."
  zone = "168.192.in-addr.arpa."
}