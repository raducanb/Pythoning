import random

print(random.sample(range(1, 50), 6))

import zipfile
z = zipfile.ZipFile("new_archive.zip","w",zipfile.ZIP_DEFLATED) 
z.writestr("test.txt","some texts ...") 
z.writestr("/dir/a.txt","another text ...")
z.close()