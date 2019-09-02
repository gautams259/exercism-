"""def convert(number):
    l=[ i for i in range(1,number+1) if number % i ==0]
    factor={3:'Pling',5:'Plang',7:'Plong'}
    output=""
    for i,j in factor.items():
        if i in l:
            output=output+j
    if len(output)==0:
        return str(number) 
    return output
 """       
def convert(number):
    result=""
    if number % 3 == 0:
        result = result+'Pling'
    if number % 5 == 0:
        result = result+'Plang'
    if number % 7 == 0:
        result = result+'Plong'
    if len(result) ==0:
        return str(number)
    else:
        return result
