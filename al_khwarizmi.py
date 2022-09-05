def al_khwarizmi(x,y):

    if y==1:
        return x*y

    result=0
    if y%2==0:
         result = al_khwarizmi(x,int(y/2))

         return 2*result
    else:
        result = al_khwarizmi(x,int(y/2))

        return x+2*result

    return result


result = al_khwarizmi(13,11)

print(f"### Result---- {result}")