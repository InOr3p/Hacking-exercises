# Leviathan

## Level 0 -> Level 1

- Run `ls -al` inside `/home/leviathan0` and find `.backup/` folder, which contains `bookmarks.html`.

- By running `cat bookmarks.html | grep leviathan` I got:

```html
<DT><A HREF="http://leviathan.labs.overthewire.org/passwordus.html | This will be fixed later, the password for leviathan1 is 3QJ3TgzHDq" ADD_DATE="1155384634" LAST_CHARSET="ISO-8859-1" ID="rdf:#$2wIU71">password to leviathan1</A>
```

## Level 1 -> Level 2

- Running strings on check file, I noticed the usage of `strcmp@GLIBC_2.0`.

- Hence, I run `ltrace`, to check what calls are made using strcmp and found out:

`strcmp("ciao", "sex")` 

- After inserting sex as password, we login as leviathan2 and can fetch the real leviathan2's password (by going to `/etc/leviathan_pass` and reading the content of leviathan2): `NsN1HwFoyN`


## Level 2 -> Level 3

- The printfile is using `access()` function, which uses the real user ID (and not the effective one) to run the specified file. Printfile has the **SUID** set, hence if I run `./printfile /etc/leviathan_pass/leviathan3`, it should print the content of leviathan3 as it would be runned by leviathan3 user. But since access() uses the real user ID, it runs the password file as leviathan2 (who I really am). 

- To bypass access() (which basically run `cat`) I can create a file called `tmp1.txt tmp2.txt`, then create another file `tmp2.txt` which is a link to 
`/etc/leviathan_pass/leviathan3` (with `ln -s /etc/leviathan_pass/leviathan3 tmp2.txt`). Then I can run `./printfile "tmp1.txt tmp2.txt"`: by doing so, access() checks the tmp1.txt privileges (and there's no error, because it's been created and runned by leviathan2) and so cat command will try to print the content of tmp1.txt and tmp2.txt (which contains the password): `f0n8h2iWLP`


## Level 3 -> Level 4

- The same as **Level 1 -> Level 2**

- Password: `WG1egElCvO`

## Level 4 -> Level 5

- Running the hidden file bin I got a binary string, which I passed to Cyberchef and converted to ASCII to get the password: `0dyxT7F4QD`


## Level 5 -> Level 6

- Running the leviathan5 file, I noticed it tries to print the content of the /tmp/file.log file. But it doesn't exist. Hence, I create it as a file linked to the password file in this way: `ln -s /etc/leviathan_pass/leviathan6 /tmp/file.log`. After running again leviathan5, I get the password: `szo7HDB88w`

## Level 6 -> Level 7

- The file asks to insert a 4 digits strings. Hence, I bruteforce it with the following code: `for i in {0..10000}; do echo "trying $i"; ./leviathan6 $i | grep -v "Wrong"; sleep 0.005; done`.

- The final password is: `qEs5Io5yM8`