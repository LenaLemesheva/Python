# Дан список, вывести отдельно буквы и цифры.
# a = ( ‘1’, "a", 'b', '2', '3' ,'c') 
# b = ( 'a' , 'b' , 'c')
# c = ( '1', '2', '3')

lst = ['1', 'a', 'b', '2', '3', 'c']
print([i for i in lst if i.isdigit()]) # isidigit - если все символы цифры
print([i for i in lst if i.isalpha()]) # isalpha - если все символы буквы
