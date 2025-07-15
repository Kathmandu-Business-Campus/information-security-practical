# !/bin/bash

rm -rf md5_collision_demo

mkdir md5_collision_demo && cd md5_collision_demo

# use .exe from same site for windows
wget https://www.mscs.dal.ca/~selinger/md5collision/hello
wget https://www.mscs.dal.ca/~selinger/md5collision/erase

# run hello.exe and erase.exe directly. noo need for this step
chmod +x ./hello
chmod +x ./erase

# Show hash
md5sum hello
md5sum erase

sha256sum hello
sha256sum erase

# Verify difference in file
cmp hello erase

./hello
./erase
