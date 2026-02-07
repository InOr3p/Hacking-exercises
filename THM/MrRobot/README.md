# Mr Robot

- **NMAP scan**

Starting Nmap 7.95 ( https://nmap.org ) at 2026-01-31 11:59 CET
Not shown: 997 filtered tcp ports (no-response)
PORT    STATE SERVICE  VERSION
22/tcp  open  ssh      OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   3072 cc:ba:aa:ae:a7:8d:86:ea:3a:69:56:85:76:96:59:25 (RSA)
|   256 6c:b7:e7:22:9b:3d:1b:ab:10:8e:26:08:60:50:20:78 (ECDSA)
|_  256 83:4c:c5:07:ef:f6:a4:14:71:df:84:cd:e9:6b:38:6e (ED25519)
80/tcp  open  http     Apache httpd
|_http-title: Site doesn't have a title (text/html).
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
|_http-server-header: Apache
443/tcp open  ssl/http Apache httpd
| http-methods:
|_  Supported Methods: GET HEAD POST OPTIONS
| ssl-cert: Subject: commonName=www.example.com
| Issuer: commonName=www.example.com
| Public Key type: rsa
| Public Key bits: 1024
| Signature Algorithm: sha1WithRSAEncryption
| Not valid before: 2015-09-16T10:45:03
| Not valid after:  2025-09-13T10:45:03
| MD5:   3c16:3b19:87c3:42ad:6634:c1c9:d0aa:fb97
|_SHA-1: ef0c:5fa5:931a:09a5:687c:a2c2:80c4:c792:07ce:f71b
|_http-title: Site doesn't have a title (text/html).
|_http-favicon: Unknown favicon MD5: D41D8CD98F00B204E9800998ECF8427E
|_http-server-header: Apache
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

- **gobuster scan**

===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/.hta                 (Status: 403) [Size: 213]
/.hta.asp             (Status: 403) [Size: 217]
/.hta.aspx            (Status: 403) [Size: 218]
/.hta.bak             (Status: 403) [Size: 217]
/.hta.txt             (Status: 403) [Size: 217]
/.hta.php             (Status: 403) [Size: 217]
/.hta.html            (Status: 403) [Size: 218]
/.htaccess            (Status: 403) [Size: 218]
/.htaccess.php        (Status: 403) [Size: 222]
/.htaccess.html       (Status: 403) [Size: 223]
/.htaccess.asp        (Status: 403) [Size: 222]
/.htaccess.bak        (Status: 403) [Size: 222]
/.htaccess.aspx       (Status: 403) [Size: 223]
/.htaccess.txt        (Status: 403) [Size: 222]
/.htpasswd            (Status: 403) [Size: 218]
/.htpasswd.php        (Status: 403) [Size: 222]
/.htpasswd.html       (Status: 403) [Size: 223]
/.htpasswd.asp        (Status: 403) [Size: 222]
/.htpasswd.aspx       (Status: 403) [Size: 223]
/.htpasswd.bak        (Status: 403) [Size: 222]
/.htpasswd.txt        (Status: 403) [Size: 222]
/0                    (Status: 301) [Size: 0] [--> http://10.80.160.110/0/]
/admin                (Status: 301) [Size: 235] [--> http://10.80.160.110/admin/]
/atom                 (Status: 301) [Size: 0] [--> http://10.80.160.110/feed/atom/]
/audio                (Status: 301) [Size: 235] [--> http://10.80.160.110/audio/]
/blog                 (Status: 301) [Size: 234] [--> http://10.80.160.110/blog/]
/cgi-bin/.html        (Status: 403) [Size: 222]
/css                  (Status: 301) [Size: 233] [--> http://10.80.160.110/css/]
/dashboard            (Status: 302) [Size: 0] [--> http://10.80.160.110/wp-admin/]
/favicon.ico          (Status: 200) [Size: 0]
/feed                 (Status: 301) [Size: 0] [--> http://10.80.160.110/feed/]
/image                (Status: 301) [Size: 0] [--> http://10.80.160.110/image/]
/Image                (Status: 301) [Size: 0] [--> http://10.80.160.110/Image/]
/images               (Status: 301) [Size: 236] [--> http://10.80.160.110/images/]
/index.html           (Status: 200) [Size: 1188]
/index.php            (Status: 301) [Size: 0] [--> http://10.80.160.110/]
/index.html           (Status: 200) [Size: 1188]
/index.php            (Status: 301) [Size: 0] [--> http://10.80.160.110/]
/intro                (Status: 200) [Size: 516314]
/js                   (Status: 301) [Size: 232] [--> http://10.80.160.110/js/]
/license              (Status: 200) [Size: 309]
/license.txt          (Status: 200) [Size: 309]
/login                (Status: 302) [Size: 0] [--> http://10.80.160.110/wp-login.php]
/page1                (Status: 301) [Size: 0] [--> http://10.80.160.110/]
/phpmyadmin           (Status: 403) [Size: 94]
/rdf                  (Status: 301) [Size: 0] [--> http://10.80.160.110/feed/rdf/]
/readme               (Status: 200) [Size: 64]
/readme.html          (Status: 200) [Size: 64]
/robots               (Status: 200) [Size: 41]
/robots.txt           (Status: 200) [Size: 41]
/robots.txt           (Status: 200) [Size: 41]
/rss                  (Status: 301) [Size: 0] [--> http://10.80.160.110/feed/]
/rss2                 (Status: 301) [Size: 0] [--> http://10.80.160.110/feed/]
/sitemap              (Status: 200) [Size: 0]
/sitemap.xml          (Status: 200) [Size: 0]