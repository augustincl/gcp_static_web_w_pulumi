import pulumi
from pulumi import ResourceOptions
from pulumi_gcp import compute
from pulumi_gcp import storage

#
#SOME KNOWN VAR (You might implement a yml reader to keep this!)
#
DOMAIN_NAME="[USE-YOUR-DOMAIN-NAME]" 

#step 1. create the website bucket
webbucket=storage.Bucket("official-web"
    ,website=storage.BucketWebsiteArgs(main_page_suffix="index.html")
    ,location='asia-east1')

accessctl=storage.DefaultObjectAccessControl("official-web-read"
    ,bucket=webbucket.name
    ,role="READER"
    ,entity="allUsers")

#step 2. create an external ip
access_addr=compute.GlobalAddress("addr-4-official-web")

#step 3. setup loadbalancer, ssl and CDN
backend_instance=compute.BackendBucket("backend-4-official-web"
    ,bucket_name=webbucket.name
    ,enable_cdn=True)

dedicated_ssl=compute.ManagedSslCertificate("ssl-4-official-web"
    ,managed=compute.ManagedSslCertificateManagedArgs(domains=[DOMAIN_NAME]))

web_routing=compute.URLMap("map-4-official-web"
    ,default_service=backend_instance.self_link)

target_proxy=compute.TargetHttpsProxy("proxy-4-official-web"
    ,url_map=web_routing
    ,ssl_certificates=[dedicated_ssl.self_link])

forward_rule=compute.GlobalForwardingRule("rule-4-official-web"
    ,load_balancing_scheme="EXTERNAL"
    ,ip_address=access_addr.address
    ,ip_protocol="TCP"
    ,port_range="443"
    ,target=target_proxy.self_link)

