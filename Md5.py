import getpass
import hashlib
p = getpass.getpass()
print hashlib.md5(p).hexdigest()