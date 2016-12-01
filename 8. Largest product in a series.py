"""The four adjacent digits in the 1000-digit number that have the greatest product are 9 × 9 × 8 × 9 = 5832.

73167176531330624919225119674426574742355349194934
96983520312774506326239578318016984801869478851843
85861560789112949495459501737958331952853208805511
12540698747158523863050715693290963295227443043557
66896648950445244523161731856403098711121722383113
62229893423380308135336276614282806444486645238749
30358907296290491560440772390713810515859307960866
70172427121883998797908792274921901699720888093776
65727333001053367881220235421809751254540594752243
52584907711670556013604839586446706324415722155397
53697817977846174064955149290862569321978468622482
83972241375657056057490261407972968652414535100474
82166370484403199890008895243450658541227588666881
16427171479924442928230863465674813919123162824586
17866458359124566529476545682848912883142607690042
24219022671055626321111109370544217506941658960408
07198403850962455444362981230987879927244284909188
84580156166097919133875499200524063689912560717606
05886116467109405077541002256983155200055935729725
71636269561882670428252483600823257530420752963450

Find the thirteen adjacent digits in the 1000-digit number that have the greatest product. What is the value of this product?"""

tot=0
top=0
s1="73167176531330624919225119674426574742355349194934"
for x in range(len(s1)-12):
    tot=int(s1[x])*int(s1[x+1])*int(s1[x+2])*int(s1[x+3])*int(s1[x+4])*int(s1[x+5])*int(s1[x+6])*int(s1[x+7])*int(s1[x+8])*int(s1[x+9])*int(s1[x+10])*int(s1[x+11])*int(s1[x+12])
    if(tot>top):
        top=tot
s2="96983520312774506326239578318016984801869478851843"
for x in range(len(s1)-12):
    tot=int(s2[x])*int(s2[x+1])*int(s2[x+2])*int(s2[x+3])*int(s2[x+4])*int(s2[x+5])*int(s2[x+6])*int(s2[x+7])*int(s2[x+8])*int(s2[x+9])*int(s2[x+10])*int(s2[x+11])*int(s2[x+12])
    if(tot>top):
        top=tot
s3="85861560789112949495459501737958331952853208805511"
for x in range(len(s1)-12):
    tot=int(s3[x])*int(s3[x+1])*int(s3[x+2])*int(s3[x+3])*int(s3[x+4])*int(s3[x+5])*int(s3[x+6])*int(s3[x+7])*int(s3[x+8])*int(s3[x+9])*int(s3[x+10])*int(s3[x+11])*int(s3[x+12])
    if(tot>top):
        top=tot
s4="12540698747158523863050715693290963295227443043557"
for x in range(len(s1)-12):
    tot=int(s4[x])*int(s4[x+1])*int(s4[x+2])*int(s4[x+3])*int(s4[x+4])*int(s4[x+5])*int(s4[x+6])*int(s4[x+7])*int(s4[x+8])*int(s4[x+9])*int(s4[x+10])*int(s4[x+11])*int(s4[x+12])
    if(tot>top):
        top=tot
s5="66896648950445244523161731856403098711121722383113"
for x in range(len(s1)-12):
    tot=int(s5[x])*int(s5[x+1])*int(s5[x+2])*int(s5[x+3])*int(s5[x+4])*int(s5[x+5])*int(s5[x+6])*int(s5[x+7])*int(s5[x+8])*int(s5[x+9])*int(s5[x+10])*int(s5[x+11])*int(s5[x+12])
    if(tot>top):
        top=tot
s6="62229893423380308135336276614282806444486645238749"
for x in range(len(s1)-12):
    tot=int(s6[x])*int(s6[x+1])*int(s6[x+2])*int(s6[x+3])*int(s6[x+4])*int(s6[x+5])*int(s6[x+6])*int(s6[x+7])*int(s6[x+8])*int(s6[x+9])*int(s6[x+10])*int(s6[x+11])*int(s6[x+12])
    if(tot>top):
        top=tot
s7="30358907296290491560440772390713810515859307960866"
for x in range(len(s1)-12):
    tot=int(s7[x])*int(s7[x+1])*int(s7[x+2])*int(s7[x+3])*int(s7[x+4])*int(s7[x+5])*int(s7[x+6])*int(s7[x+7])*int(s7[x+8])*int(s7[x+9])*int(s7[x+10])*int(s7[x+11])*int(s7[x+12])
    if(tot>top):
        top=tot
s8="70172427121883998797908792274921901699720888093776"
for x in range(len(s1)-12):
    tot=int(s8[x])*int(s8[x+1])*int(s8[x+2])*int(s8[x+3])*int(s8[x+4])*int(s8[x+5])*int(s8[x+6])*int(s8[x+7])*int(s8[x+8])*int(s8[x+9])*int(s8[x+10])*int(s8[x+11])*int(s8[x+12])
    if(tot>top):
        top=tot
s9="65727333001053367881220235421809751254540594752243"
for x in range(len(s1)-12):
    tot=int(s9[x])*int(s9[x+1])*int(s9[x+2])*int(s9[x+3])*int(s9[x+4])*int(s9[x+5])*int(s9[x+6])*int(s9[x+7])*int(s9[x+8])*int(s9[x+9])*int(s9[x+10])*int(s9[x+11])*int(s9[x+12])
    if(tot>top):
        top=tot
s10="52584907711670556013604839586446706324415722155397"
for x in range(len(s1)-12):
    tot=int(s10[x])*int(s10[x+1])*int(s10[x+2])*int(s10[x+3])*int(s10[x+4])*int(s10[x+5])*int(s10[x+6])*int(s10[x+7])*int(s10[x+8])*int(s10[x+9])*int(s10[x+10])*int(s10[x+11])*int(s10[x+12])
    if(tot>top):
        top=tot
s11="53697817977846174064955149290862569321978468622482"
for x in range(len(s1)-12):
    tot=int(s11[x])*int(s11[x+1])*int(s11[x+2])*int(s11[x+3])*int(s11[x+4])*int(s11[x+5])*int(s11[x+6])*int(s11[x+7])*int(s11[x+8])*int(s11[x+9])*int(s11[x+10])*int(s11[x+11])*int(s11[x+12])
    if(tot>top):
        top=tot
s12="83972241375657056057490261407972968652414535100474"
for x in range(len(s1)-12):
    tot=int(s12[x])*int(s12[x+1])*int(s12[x+2])*int(s12[x+3])*int(s12[x+4])*int(s12[x+5])*int(s12[x+6])*int(s12[x+7])*int(s12[x+8])*int(s12[x+9])*int(s12[x+10])*int(s12[x+11])*int(s12[x+12])
    if(tot>top):
        top=tot
s13="82166370484403199890008895243450658541227588666881"
for x in range(len(s1)-12):
    tot=int(s13[x])*int(s13[x+1])*int(s13[x+2])*int(s13[x+3])*int(s13[x+4])*int(s13[x+5])*int(s13[x+6])*int(s13[x+7])*int(s13[x+8])*int(s13[x+9])*int(s13[x+10])*int(s13[x+11])*int(s13[x+12])
    if(tot>top):
        top=tot
s14="16427171479924442928230863465674813919123162824586"
for x in range(len(s1)-12):
    tot=int(s14[x])*int(s14[x+1])*int(s14[x+2])*int(s14[x+3])*int(s14[x+4])*int(s14[x+5])*int(s14[x+6])*int(s14[x+7])*int(s14[x+8])*int(s14[x+9])*int(s14[x+10])*int(s14[x+11])*int(s14[x+12])
    if(tot>top):
        top=tot
s15="17866458359124566529476545682848912883142607690042"
for x in range(len(s1)-12):
    tot=int(s15[x])*int(s15[x+1])*int(s15[x+2])*int(s15[x+3])*int(s15[x+4])*int(s15[x+5])*int(s15[x+6])*int(s15[x+7])*int(s15[x+8])*int(s15[x+9])*int(s15[x+10])*int(s15[x+11])*int(s15[x+12])
    if(tot>top):
        top=tot
s16="24219022671055626321111109370544217506941658960408"
for x in range(len(s1)-12):
    tot=int(s16[x])*int(s16[x+1])*int(s16[x+2])*int(s16[x+3])*int(s16[x+4])*int(s16[x+5])*int(s16[x+6])*int(s16[x+7])*int(s16[x+8])*int(s16[x+9])*int(s16[x+10])*int(s16[x+11])*int(s16[x+12])
    if(tot>top):
        top=tot
s17="07198403850962455444362981230987879927244284909188"
for x in range(len(s1)-12):
    tot=int(s17[x])*int(s17[x+1])*int(s17[x+2])*int(s17[x+3])*int(s17[x+4])*int(s17[x+5])*int(s17[x+6])*int(s17[x+7])*int(s17[x+8])*int(s17[x+9])*int(s17[x+10])*int(s17[x+11])*int(s17[x+12])
    if(tot>top):
        top=tot
s18="84580156166097919133875499200524063689912560717606"
for x in range(len(s1)-12):
    tot=int(s18[x])*int(s18[x+1])*int(s18[x+2])*int(s18[x+3])*int(s18[x+4])*int(s18[x+5])*int(s18[x+6])*int(s18[x+7])*int(s18[x+8])*int(s18[x+9])*int(s18[x+10])*int(s18[x+11])*int(s18[x+12])
    if(tot>top):
        top=tot
s19="05886116467109405077541002256983155200055935729725"
for x in range(len(s1)-12):
    tot=int(s19[x])*int(s19[x+1])*int(s19[x+2])*int(s19[x+3])*int(s19[x+4])*int(s19[x+5])*int(s19[x+6])*int(s19[x+7])*int(s19[x+8])*int(s19[x+9])*int(s19[x+10])*int(s19[x+11])*int(s19[x+12])
    if(tot>top):
        top=tot
s20="71636269561882670428252483600823257530420752963450"
for x in range(len(s1)-12):
    tot=int(s20[x])*int(s20[x+1])*int(s20[x+2])*int(s20[x+3])*int(s20[x+4])*int(s20[x+5])*int(s20[x+6])*int(s20[x+7])*int(s20[x+8])*int(s20[x+9])*int(s20[x+10])*int(s20[x+11])*int(s20[x+12])
    if(tot>top):
        top=tot
print(top)
