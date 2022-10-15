# u-boot-mdb-output-to-file

Convert U-Boot mdb command output as a TEXT/ASCII file

# Example:

Try to load the text file from filesystem to memory

```ruby
U-Boot> ext4load mmc 0:2 0x0200000 /etc/passwd 
547 bytes read in 3 ms (177.7 KiB/s)
U-Boot>
```

Note down the size info . (Here 547 bytes means in hex 0x223)

Now display the content from that memory address using "md.b" command
```ruby
U-Boot> md.b 0x0200000 0x223
00200000: 72 6f 6f 74 3a 78 3a 30 3a 30 3a 72 6f 6f 74 3a  root:x:0:0:root:
00200010: 2f 72 6f 6f 74 3a 2f 62 69 6e 2f 73 68 0a 64 61  /root:/bin/sh.da
00200020: 65 6d 6f 6e 3a 78 3a 31 3a 31 3a 64 61 65 6d 6f  emon:x:1:1:daemo
00200030: 6e 3a 2f 75 73 72 2f 73 62 69 6e 3a 2f 62 69 6e  n:/usr/sbin:/bin
.......
```
Copy this result to a text file or capture log in a file. 
For testing purpose I copied a log file which is output of md.b command in this repo.

Download this script "uboot_mdb_to_textfile.py"
```ruby
$ git clone https://github.com/DevendraDevadiga/u-boot-mdb-output-to-file.git
$ cd u-boot-mdb-output-to-file
$ chmod 777 uboot_mdb_to_textfile.py
```
Now check usage of this command:
```ruby
$ python3 uboot_mdb_to_textfile.py 
Usage: python3  uboot_mdb_to_textfile.py logfilename [outputfilname]
```

So provide log file as input and provide file name (optional)
In this example I loaded /etc/pswd file. So output name used as pswd.
```ruby
$ python3 uboot_mdb_to_textfile.py pswd-md-output.log pswd
```

Now check the content of 'pswd' file.
```ruby
$ cat pswd
root:x:0:0:root:/root:/bin/sh
daemon:x:1:1:daemon:/usr/sbin:/bin/false
bin:x:2:2:bin:/bin:/bin/false
sys:x:3:3:sys:/dev:/bin/false
sync:x:4:100:sync:/bin:/bin/sync
mail:x:8:8:mail:/var/spool/mail:/bin/false
www-data:x:33:33:www-data:/var/www:/bin/false
operator:x:37:37:Operator:/var:/bin/false
nobody:x:65534:65534:nobody:/home:/bin/false
dhcpcd:x:1000:1000:dhcpcd user:/:/bin/false
sshd:x:1001:1001:SSH drop priv user:/var/empty:/bin/false
tee:x:1002:1002:TEE user:/:/bin/sh
test:x:1003:1005:Test user, may run TEE client applications:/:/bin/sh
```
