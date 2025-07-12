and_ = 3
dico1 = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
dico2 = ['eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
dico3 = ['twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'ninety']

thousand = 8
hundred = 7
ten = 3

def make_dico(dico):
    res = {}

    for word in dico:
        res[word] = len(word)
    
    return res

dico1 = make_dico(dico1)
dico2 = make_dico(dico2)
dico3 = make_dico(dico3)

one_to_nine = 0
for val in dico1.values():
    one_to_nine+=val

eleven_to_nineteen = 0
for val in dico2.values():
    eleven_to_nineteen+=val

one_to_ninety_nine = one_to_nine + eleven_to_nineteen + ten
for val in dico3.values():
    one_to_ninety_nine+=(val*10+one_to_nine)


one_to_thousand = one_to_ninety_nine+thousand+len('one')
for val in dico1.values():
    one_to_thousand+=((val+hundred)+(val+hundred+and_)*99+one_to_ninety_nine)

answer=one_to_thousand
#print(f"Problème 17 : {answer}")