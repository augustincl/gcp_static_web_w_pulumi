# 使用 Pulumi 與 GCP 建置靜態網站 

將採用 Google Bucket 來存放靜態網頁，並且提供給使用者瀏覽。Bucket 前端會放置負載均衡器與 CDN 來提供最佳的瀏覽體驗。

:triangular_flag_on_post: 預設使用 Google 所提供的受管憑證，來自動提供 TLS 保護!<br/><br/>

:bulb: 整個專案一方面展現透過 GCP 建置靜態網站所需要的必要元件外，另一方面則採用 Pulumi 來進行自動化建置。整個專案可以作為建置屬於你自己的網站的起點，但如果有任何安全的考量與客製，也請大膽修改成你所考慮的樣子。當然，你也可以建議或者是貢獻你的配置到本專案中!

## Prerequisite

* 此專案是基於 Google 的雲端服務，為了完成整個佈署，請安裝 [gcloud SDK](https://cloud.google.com/sdk/docs/install#deb)
* Python 3.7+ :warning: 請勿安裝2.x的版本
* [Pulumi](https://www.pulumi.com/docs/get-started/install/)

:mega: 
1. 本專案所有操作都是基於 **LINUX**。
2. 如果是 Windows 的使用者，一些操作指令可能不適用! 請稍加調適。
3. gcloud與pulumi的設置請參考官網，而Python則請用anaconda建立執行環境

## Running the App

1. 下載並且初始你的環境

    :warning:
    Windows 使用者請利用 Anaconda 建立虛擬環境，再利用指令安裝 requirements.txt 即可!

    ```
    $ python3 -m venv venv
    $ source venv/bin/activate
    $ pip3 install -r requirements.txt
    ```
    
2.  建立一個新的堆疊:

    ```
    $ pulumi stack init dev
    ```

3.  設定專案組態屬性:

    ```
    $ pulumi config set gcp:project YOURGOOGLECLOUDPROJECT
    $ pulumi config set gcp:zone asia-east1-a
    ```

4.  打開 infrabase.py 檔案，並且將已申請好的域名指派給如下的域名變數

    ```
    DOMAIN_NAME="[USE-YOUR-DOMAIN-NAME]" 
    ```

5.  執行 `pulumi up -y` 來預覽整個基礎設施的配置，並且進行佈署:

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

6.  上傳你的預設首頁!
    
    a. 前往 [Google Console](https://console.cloud.google.com/)，並且打開建立好的 bucket (e.g. official-web-51d6949).
    b. 上傳 index.html.

7.  進行域名設置

    a. 開啟域名伺服器的設定工具，並且建立 A 紀錄，將 ip (e.g. 34.120.152.39) 對應至 [USE-YOUR-DOMAIN-NAME]
    b. 等待一段時間，讓域名進行傳播並且生效

8. 現在你可以透過 [USE-YOUR-DOMAIN-NAME] 來瀏覽你的網站!

9. 如果你只是進行測試，別忘記在測試完畢後，將所有資源刪除，以避免不必要的帳單!

    ```
    $ pulumi destroy
    $ pulumi stack rm
    ```
