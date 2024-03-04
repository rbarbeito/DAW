def potencia_r(base,exp):
  if exp==0:
    return 1

  if exp==1:
    return base
  
  return base * potencia_r(base,exp-1)


print(potencia_r(2,5))
