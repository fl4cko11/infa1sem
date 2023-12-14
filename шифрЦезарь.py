s=str(input())
A=list(s.lower())
B=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
k=14
for i in range (len(A)):
    if A[i]=='а':
        A[i]=B[(B.index('а')+k)%len(B)]
    elif A[i] == 'б':
        A[i] = B[(B.index('б') + k) % len(B)]
    elif A[i] == 'в':
        A[i] = B[(B.index('в') + k) % len(B)]
    elif A[i] == 'г':
        A[i] = B[(B.index('г') + k) % len(B)]
    elif A[i]=='д':
        A[i]=B[(B.index('д')+k)%len(B)]
    elif A[i]=='е':
        A[i]=B[(B.index('е')+k)%len(B)]
    elif A[i]=='ё':
        A[i]=B[(B.index('ё')+k)%len(B)]
    elif A[i]=='ж':
        A[i]=B[(B.index('ж')+k)%len(B)]
    elif A[i]=='з':
        A[i]=B[(B.index('з')+k)%len(B)]
    elif A[i]=='и':
        A[i]=B[(B.index('и')+k)%len(B)]
    elif A[i]=='й':
        A[i]=B[(B.index('й')+k)%len(B)]
    elif A[i]=='к':
        A[i]=B[(B.index('к')+k)%len(B)]
    elif A[i]=='л':
        A[i]=B[(B.index('л')+k)%len(B)]
    elif A[i]=='м':
        A[i]=B[(B.index('м')+k)%len(B)]
    elif A[i]=='н':
        A[i]=B[(B.index('н')+k)%len(B)]
    elif A[i]=='о':
        A[i]=B[(B.index('о')+k)%len(B)]
    elif A[i]=='п':
        A[i]=B[(B.index('п')+k)%len(B)]
    elif A[i]=='р':
        A[i]=B[(B.index('р')+k)%len(B)]
    elif A[i]=='с':
        A[i]=B[(B.index('с')+k)%len(B)]
    elif A[i]=='т':
        A[i]=B[(B.index('т')+k)%len(B)]
    elif A[i]=='у':
        A[i]=B[(B.index('у')+k)%len(B)]
    elif A[i]=='ф':
        A[i]=B[(B.index('ф')+k)%len(B)]
    elif A[i]=='х':
        A[i]=B[(B.index('х')+k)%len(B)]
    elif A[i]=='ц':
        A[i]=B[(B.index('ц')+k)%len(B)]
    elif A[i]=='ч':
        A[i]=B[(B.index('ч')+k)%len(B)]
    elif A[i]=='ш':
        A[i]=B[(B.index('ш')+k)%len(B)]
    elif A[i]=='щ':
        A[i]=B[(B.index('щ')+k)%len(B)]
    elif A[i]=='ъ':
        A[i]=B[(B.index('ъ')+k)%len(B)]
    elif A[i]=='ы':
        A[i]=B[(B.index('ы')+k)%len(B)]
    elif A[i]=='ь':
        A[i]=B[(B.index('ь')+k)%len(B)]
    elif A[i]=='э':
        A[i]=B[(B.index('э')+k)%len(B)]
    elif A[i]=='ю':
        A[i]=B[(B.index('ю')+k)%len(B)]
    elif A[i]=='я':
        A[i]=B[(B.index('я')+k)%len(B)]
    print(A[i], sep='', end='')