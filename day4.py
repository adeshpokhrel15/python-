def target_sum(l,target):
    for ind,num in enumerate(l):
        if num>target:
            continue
        for nextindex in range(ind+1,len(l)):
            secondnum=l[nextindex]
            if num+secondnum==target:
                return (num,secondnum)
one,two=target_sum([0,2,4,3,5,8],8)
print(one,two)

#another program
def adjacent_greater(l):
    length = len(l)
    for ind in length(l,length-1):

        curr=l[i]
        prev=l[i-1]
        next_item=l[i+1]
        if(prev>curr and next_item>curr):
            result.append()


#stack
def 
opening_braces=['(','{','[']
closing_braces=[')','}',']']
braces=list()
s='[{()}]'
for b in s:
    if b in opening_braces:
        braces.append(b)
    elif b in closing_braces:
        to_compare=b.pop()
        if b==')' and to_compare == '(':
            pass
        elif b=='}' and to_compare == '{':
            pass
        elif b==']' and to_compare == '[':
            pass
        else:
            return False
if len(braces)==0:
    return True 
else:
    return False






















