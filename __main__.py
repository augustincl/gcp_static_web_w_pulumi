import pulumi
import infrabase

# Export the DNS name of the bucket
pulumi.export('bucket_name', infrabase.webbucket.url)
pulumi.export('access_ip',infrabase.access_addr.address)