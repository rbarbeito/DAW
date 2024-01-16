my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]
#
# Escribe tu código aquí.
#

# list_unicos=[]
# for i in range(len(my_list)):
#     if my_list[i] not in list_unicos:
#         list_unicos.append(my_list[i])
        
# my_list=list_unicos        

print(my_list)
for i in range(len(my_list)-1,-1,-1):
    if my_list[i] in my_list[:i]:
        del my_list[i]

print(my_list)