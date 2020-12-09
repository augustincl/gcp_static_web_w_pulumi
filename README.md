# Setup an infrastructure for static web based on GCP 

This project will use google bucket as the web backend to serving a website.
The request will be served by CDN first, then the loadloadbalancer and bucket!

:triangular_flag_on_post: TLS with auto-updates by default!
:bulb: This implementation is used to show which are the necessary components for a static web site based on GCP. Of course, it also shows how to integrate all of them as your begining to create a web infra. You should take your customizations or concerns into considerations and modify codes, if any. 

## Prerequisite

* This project leverages GCP. Please setup your [gcloud SDK](https://cloud.google.com/sdk/docs/install#deb)
* You should leverage gcloud command to setup your application token
* Python **3.7+**. :warning: DO NOT USE VERSION 2.x
* [Pulumi](https://www.pulumi.com/docs/get-started/install/)

:mega: 
1. All the commands are based on **LINUX**
2. If you are a Windows user, please note that you might need to adjust some instructions!
3. Please refer to the official site for gcloud and pulumi for more details about the installation
4. Please leverage Anaconda to setup your python environment.

## Running the App

1. Download and initialize your environment

    :warning: 
    For Windows users, please leverage Anaconda to create your virtual environment. Then, use command to install requirements.txt

    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
    
2.  Create a new stack:

    ```
    $ pulumi stack init dev
    ```

3.  Configure the project:

    ```
    $ pulumi config set gcp:project YOURGOOGLECLOUDPROJECT
    $ pulumi config set gcp:zone asia-east1-a
    ```

4.  Edit the following variable in infrabase.py based on your domain

    ```
    DOMAIN_NAME="[USE-YOUR-DOMAIN-NAME]" 
    ```

5.  Run `pulumi up -y` to preview and deploy changes:

    ``` 
    Previewing update (dev)

    View Live: https://app.pulumi.com/augustincl/gcp_static_web_w_pulumi/dev/previews/0c5ef742-69d5-4616-b323-cd27227cb915

         Type                                       Name                         Plan       
     +   pulumi:pulumi:Stack                        gcp_static_web_w_pulumi-dev  create     
     +   ├─ gcp:compute:GlobalAddress               addr-4-official-web          create     
     +   ├─ gcp:storage:Bucket                      official-web                 create     
     +   ├─ gcp:compute:ManagedSslCertificate       ssl-4-official-web           create     
     +   ├─ gcp:compute:BackendBucket               backend-4-official-web       create     
     +   ├─ gcp:storage:DefaultObjectAccessControl  official-web-read            create     
     +   ├─ gcp:compute:URLMap                      map-4-official-web           create     
     +   ├─ gcp:compute:TargetHttpsProxy            proxy-4-official-web         create     
     +   └─ gcp:compute:GlobalForwardingRule        rule-4-official-web          create     
 
    Resources:
        + 9 to create

    Updating (dev)


    View Live: https://app.pulumi.com/augustincl/gcp_static_web_w_pulumi/dev/updates/1

        Type                                       Name                         Status      
     +   pulumi:pulumi:Stack                        gcp_static_web_w_pulumi-dev  created     
     +   ├─ gcp:compute:ManagedSslCertificate       ssl-4-official-web           created     
     +   ├─ gcp:storage:Bucket                      official-web                 created     
     +   ├─ gcp:compute:GlobalAddress               addr-4-official-web          created     
     +   ├─ gcp:storage:DefaultObjectAccessControl  official-web-read            created     
     +   ├─ gcp:compute:BackendBucket               backend-4-official-web       created     
     +   ├─ gcp:compute:URLMap                      map-4-official-web           created     
     +   ├─ gcp:compute:TargetHttpsProxy            proxy-4-official-web         created     
     +   └─ gcp:compute:GlobalForwardingRule        rule-4-official-web          created     
 
    Outputs:
        access_ip  : "34.120.152.39"
        bucket_name: "gs://official-web-51d6949"

    Resources:
        + 9 created

    Duration: 58s
    ```

6.  Upload your index.html!
    
    a. Go to [Google Console](https://console.cloud.google.com/) and open the created bucket (e.g. official-web-51d6949).
    b. upload your html file into it.

7.  Setup your domain name

    a. create an "A" Record to map your ip (e.g. 34.120.152.39) to [USE-YOUR-DOMAIN-NAME]
    b. You have to wait for a moment to let the dns setting be effective.

8. Now, you could find your web from [USE-YOUR-DOMAIN-NAME]!

9. Don't forget to clean up the infrastructure, if you just give it a try.

    ```
    $ pulumi destroy
    $ pulumi stack rm
    ```
