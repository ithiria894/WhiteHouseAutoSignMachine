email=['jmosta.mos@hyperland.tools',
 'repiphanie.mosaw@gkcrhl.us',
 '1laian@gkcrhl.us',
 '1mario.mat@delawareheroinrehab.com',
 '6ra.iid.5l@buyu960.com',
 '9atl@yocxiphbi.shop',
 'brose.cat.16w@harnessmedia.dev',
 'wjaechul.shin.50d@fg2cj7.us',
 'mhamza.liyo.9t@feminineembodimentcourse.com',
 'wyas.mi@dousmakos.com']

v='1234567890qwertyuioplkjhgfdsazxcvbnmQWERTYUIOPLKJHGFDSAZXCVBNM@#$%^&*-_=+,./?;:'
 
def checkvalid(e):
    for i in e:
        if i not in v:
            print(i)
            return False
        return True

def checkall(email):    
    for m in email:
        checkvalid(m)

checkall(email)

while True:
    try:
        a=bool(random.getrandbits(1))
        if a == False:
            break
        else:
            continue
    except:
        print('sth wrong')
