s=str(input())
A=list(s.lower())
B=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
k=14
k1=0
k2=0
k3=0
k4=0
k5=0
k6=0
k7=0
k8=0
k9=0
k10=0
k11=0
k12=0
k13=0
k14=0
k15=0
k16=0
k17=0
k18=0
k19=0
k20=0
k21=0
k22=0
k23=0
k24=0
k25=0
k26=0
k27=0
k28=0
k29=0
k30=0
k31=0
k32=0
k33=0
for i in range (len(A)):
    if A[i]=='а':
        k1=k1+1
    elif A[i] == 'б':
        k2=k2+1
    elif A[i] == 'в':
        k3=k3+1
    elif A[i] == 'г':
        k4=k4+1
    elif A[i]=='д':
        k5=k5+1
    elif A[i]=='е':
        k6=k6+1
    elif A[i]=='ё':
        k7=k7+1
    elif A[i]=='ж':
        k8=k8+1
    elif A[i]=='з':
        k9=k9+1
    elif A[i]=='и':
        k10=k10+1
    elif A[i]=='й':
        k11=k11+1
    elif A[i]=='к':
        k12=k12+1
    elif A[i]=='л':
        k13=k13+1
    elif A[i]=='м':
        k14=k14+1
    elif A[i]=='н':
        k15=k15+1
    elif A[i]=='о':
        k16=k16+1
    elif A[i]=='п':
        k17=k17+1
    elif A[i]=='р':
        k18=k18+1
    elif A[i]=='с':
        k19=k19+1
    elif A[i]=='т':
        k20=k20+1
    elif A[i]=='у':
        k21=k21+1
    elif A[i]=='ф':
        k22=k22+1
    elif A[i]=='х':
        k23=k23+1
    elif A[i]=='ц':
        k24=k24+1
    elif A[i]=='ч':
        k25=k25+1
    elif A[i]=='ш':
        k26=k26+1
    elif A[i]=='щ':
        k27=k27+1
    elif A[i]=='ъ':
        k28=k28+1
    elif A[i]=='ы':
        k29=k29+1
    elif A[i]=='ь':
        k30=k30+1
    elif A[i]=='э':
        k31=k31+1
    elif A[i]=='ю':
        k32=k32+1
    elif A[i]=='я':
        k33=k33+1
print('%а: ', (k1/len(A))*100,
          '%б: ', (k2/len(A))*100,
          '%в: ', (k3 / len(A)) * 100,
          '%г: ', (k4 / len(A)) * 100,
          '%д: ', (k5 / len(A)) * 100,
          '%е: ', (k6 / len(A)) * 100,
          '%ё: ', (k7 / len(A)) * 100,
          '%ж: ', (k8 / len(A)) * 100,
          '%з: ', (k9 / len(A)) * 100,
          '%и: ', (k10 / len(A)) * 100,
          '%й: ', (k11 / len(A)) * 100,
          '%к: ', (k12 / len(A)) * 100,
          '%л: ', (k13 / len(A)) * 100,
          '%м: ', (k14 / len(A)) * 100,
          '%н: ', (k15 / len(A)) * 100,
          '%о: ', (k16 / len(A)) * 100,
          '%п: ', (k17 / len(A)) * 100,
          '%р: ', (k18 / len(A)) * 100,
          '%с: ', (k19 / len(A)) * 100,
          '%т: ', (k20 / len(A)) * 100,
          '%у: ', (k21 / len(A)) * 100,
          '%ф: ', (k22 / len(A)) * 100,
          '%х: ', (k23 / len(A)) * 100,
          '%ц: ', (k24 / len(A)) * 100,
          '%ч: ', (k25 / len(A)) * 100,
          '%ш: ', (k26 / len(A)) * 100,
          '%щ: ', (k27 / len(A)) * 100,
          '%ъ: ', (k28 / len(A)) * 100,
          '%ы: ', (k29 / len(A)) * 100,
          '%ь: ', (k30 / len(A)) * 100,
          '%э: ', (k31 / len(A)) * 100,
          '%ю: ', (k32 / len(A)) * 100,
          '%я: ', (k33 / len(A)) * 100)