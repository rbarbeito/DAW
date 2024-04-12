def solution(palabra):

    nueva_palabra = ""
    diff = ord("a")-ord("A")

    if ord(palabra[0]) >= ord("a") and ord(palabra[0]) <= ord("z"):
        nueva_palabra = chr(ord(palabra[0])-diff)

    for i in palabra[1:]:
        if ord(i) >= ord("a") and ord(i) <= ord("z"):
            nueva_palabra += i
        elif ord(i) >= ord("A") and ord(i) <= ord("Z"):
            nueva_palabra += chr(ord(i)+diff)
        else:
            continue

    return nueva_palabra


print(solution("ffhgajsYKJHhhl"))
