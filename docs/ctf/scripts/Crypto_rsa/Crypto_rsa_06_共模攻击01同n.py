import gmpy2
import binascii

n = 15944475431088053285580229796309956066521520107276817969079550919586650535459242543036143360865780730044733026945488511390818947440767542658956272380389388112372084760689777141392370253850735307578445988289714647332867935525010482197724228457592150184979819463711753058569520651205113690397003146105972408452854948512223702957303406577348717348753106868356995616116867724764276234391678899662774272419841876652126127684683752880568407605083606688884120054963974930757275913447908185712204577194274834368323239143008887554264746068337709465319106886618643849961551092377843184067217615903229068010117272834602469293571
e1 = 797
c1 = 11157593264920825445770016357141996124368529899750745256684450189070288181107423044846165593218013465053839661401595417236657920874113839974471883493099846397002721270590059414981101686668721548330630468951353910564696445509556956955232059386625725883038103399028010566732074011325543650672982884236951904410141077728929261477083689095161596979213961494716637502980358298944316636829309169794324394742285175377601826473276006795072518510850734941703194417926566446980262512429590253643561098275852970461913026108090608491507300365391639081555316166526932233787566053827355349022396563769697278239577184503627244170930

e2 = 521
c2 = 6699274351853330023117840396450375948797682409595670560999898826038378040157859939888021861338431350172193961054314487476965030228381372659733197551597730394275360811462401853988404006922710039053586471244376282019487691307865741621991977539073601368892834227191286663809236586729196876277005838495318639365575638989137572792843310915220039476722684554553337116930323671829220528562573169295901496437858327730504992799753724465760161805820723578087668737581704682158991028502143744445435775458296907671407184921683317371216729214056381292474141668027801600327187443375858394577015394108813273774641427184411887546849

assert gmpy2.gcd(e1, e2) == 1
s = gmpy2.gcdext(e1,e2)
m1 = gmpy2.powmod(c1,s[1],n)
m2 = gmpy2.powmod(c2,s[2],n)

m = (m1*m2)%n

print(binascii.unhexlify(hex(m)[2:]))

# method
def common_modulus(n, c1, e1, c2, e2):
    s = gmpy2.gcdext(e1, e2)
    m1 = gmpy2.powmod(c1, s[1], n)
    m2 = gmpy2.powmod(c2, s[2], n)
    m = (m1 * m2) % n
    unhexlify = binascii.unhexlify(hex(m)[2:])
    print(unhexlify)
    return unhexlify