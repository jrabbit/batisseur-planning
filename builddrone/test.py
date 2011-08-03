from lengtche import leng_tche
import uuid

m = leng_tche(None, None) #Avoid Deamonizing

build_info = m.do_haikuport("joe")
for l in build_info[0][1].splitlines()[-2:]:
    if l[-4:] == '.zip':
        m.store_zip(l.split()[-1], build_info[1], "joe-"+uuid.uuid4().hex)

