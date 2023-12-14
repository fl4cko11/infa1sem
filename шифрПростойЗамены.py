s=str(input())
A=list(s.lower())
B=['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р', 'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
for i in range (len(A)):
    if A[i]=='а':
        A[i]='п'
    elif A[i] == 'б':
        A[i] = 'т'
    elif A[i] == 'в':
        A[i] = 'х'
    elif A[i] == 'г':
        A[i] = 'и'
    elif A[i]=='д':
        A[i] = 'ё'
    elif A[i]=='е':
        A[i] = 'ш'
    elif A[i]=='ё':
        A[i] = 'ц'
    elif A[i]=='ж':
        A[i] = 'р'
    elif A[i]=='з':
        A[i] = 'ы'
    elif A[i]=='и':
        A[i] = 'я'
    elif A[i]=='й':
        A[i] = 'з'
    elif A[i]=='к':
        A[i] = 'э'
    elif A[i]=='л':
        A[i] = 'ч'
    elif A[i]=='м':
        A[i] = 'д'
    elif A[i]=='н':
        A[i] = 'ж'
    elif A[i]=='о':
        A[i] = 'в'
    elif A[i]=='п':
        A[i] = 'ф'
    elif A[i]=='р':
        A[i] = 'г'
    elif A[i]=='с':
        A[i] = 'м'
    elif A[i]=='т':
        A[i] = 'у'
    elif A[i]=='у':
        A[i] = '?'
    elif A[i]=='ф':
        A[i] = 'ю'
    elif A[i]=='х':
        A[i] = 'ь'
    elif A[i]=='ц':
        A[i] = 'о'
    elif A[i]=='ч':
        A[i] = 'к'
    elif A[i]=='ш':
        A[i] = 'с'
    elif A[i]=='щ':
        A[i] = 'е'
    elif A[i]=='ъ':
        A[i] = 'щ'
    elif A[i]=='ы':
        A[i] = 'й'
    elif A[i]=='ь':
        A[i] = 'б'
    elif A[i]=='э':
        A[i] = 'а'
    elif A[i]=='ю':
        A[i] = 'н'
    elif A[i]=='я':
        A[i] = 'л'
    print(A[i], sep='', end='')
