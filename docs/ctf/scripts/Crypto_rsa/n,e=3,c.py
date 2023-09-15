# 解题思路： 题中e=3相对于n，c来说极小，故可知是低加密指数攻击。
# ①当 m^3<n 时, c=m^3，直接将c开三次方即可得到m
# ②当 m^3>n 时, c=m^3−i∗n，只要找到i，使得c+in能够开三次方即可得到m。当m^3>n时，c=m^3-i*n，只要找到i，使得c+in能够开三次方即可得到m。当m
#3
#>n时，c=m
#3
#−i∗n，只要找到i，使得c+in能够开三次方即可得到m。

import gmpy2,binascii,libnum,time
n=47966708183289639962501363163761864399454241691014467172805658518368423135168025285144721028476297179341434450931955275325060173656301959484440112740411109153032840150659
e=3
res=0
c=10968126341413081941567552025256642365567988931403833266852196599058668508079150528128483441934584299102782386592369069626088211004467782012298322278772376088171342152839
print( time.asctime())
for i in range(200000000):
    if gmpy2.iroot(c+n*i,3)[1]==1:
        res=gmpy2.iroot(c+n*i,3)[0]
        print( i,res)
        print( libnum.n2s(int(res)))
        print( time.asctime())
        break