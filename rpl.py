s = []

def postfix(input):
    list = input.split()
    for i in range(len(list)):
        if list[i]!="+" and list[i]!="-" and list[i]!="*" and list[i]!="/":
            s.append(float(list[i]))
        else:
            right = s.pop()
            left = s.pop()
            if list[i]=="+":
                s.append(left+right)
            if list[i]=="-":
                s.append(left-right)
            if list[i]=="*":
                s.append(left*right)
            if list[i]=="/":
                s.append(left/right)
    return(s.pop())

def infix(input):
    output = ""
    list = input.split()
    print(list)
    for i in range(len(list)):
        if list[i]!="+" and list[i]!="-" and list[i]!="*" and list[i]!="/" and list[i]!="(" and list[i]!=")":
            output = output + list[i] + " "
        elif list[i]=="(":
            s.append(list[i])
        elif list[i]=="*" or list[i]=="/":
            while len(s)!=0 and (s[len(s)-1]=="*" or s[len(s)-1]=="/"):
                output = output + s.pop() + " "
            s.append(list[i])
        elif list[i]=="+" or list[i]=="-":
            while len(s)!=0:
                output = output + s.pop() + " "
            s.append(list[i])
        else:
            while len(s)!=0 and s[len(s)-1]!="(":
                output = output + s.pop() + " "
            s.pop()
    while len(s)!=0:
        output = output + s.pop() + " "
    return(output)

test = infix("6 + 2 * 3 / 4 - 1")
print(test)
s = []
print(postfix(test))





