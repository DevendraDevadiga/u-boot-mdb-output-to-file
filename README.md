# u-boot-mdb-output-to-file
Convert U-Boot mdb command output as a TEXT/ASCII file

#Example:
Try to load the text file from filesystem to memory
```ruby
U-Boot> ext4load mmc 0:2 0x0200000 /etc/passwd 
547 bytes read in 3 ms (177.7 KiB/s)
U-Boot>
```

Note down the size info . ()

