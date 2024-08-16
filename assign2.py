total=int(input("Enter the total number of students :"))
cric=int(input("Enter the number of students playing cricket : "))
badminton=int(input("Enter the number of students playing badmintion : "))
football=int(input("Enter the number of students playing football :"))
cric_li=[]
bad_li=[]
foot_li=[]
print("Enter the roll no's of stdents playing cricket : ")
for i in range(cric):
    x=int(input())
    cric_li.append(x)
print("Enter the roll no's of stdents playing badminton : ")
for i in range(badminton):
    x=int(input())
    bad_li.append(x)
print("Enter the roll no's of stdents playing football : ")
for i in range(football):
    x=int(input())
    foot_li.append(x)
def union(li1,li2):
    li3=li1.copy()
    for i in range(len(li2)):
        if li2[i] not in li1:
            li3.append(li2[i])
    return li3
def intersection(li1,li2):
    li3=[]
    for i in range(len(li1)):
        for j in range(len(li2)):
            if li1[i]==li2[j]:
                li3.append(li2[j])
    return li3
def difference(li1,li2):
    li4=li1.copy()
    for i in range(len(li2)):
        if li2[i] in li1:
            li4.remove(li2[i])
    return li4
print("List of students who play both cricke and badminton ",intersection(cric_li,bad_li))
print("List of students who play either cricket or badminton but not both ",difference(union(cric_li,bad_li),intersection(cric_li,bad_li)))
print("Nuber of studnts who play neither cricket nor badminton ",total-len(union(cric_li,bad_li)))
print("Number of students who play cricket & football but not badminton ",difference(intersection(cric_li,foot_li),intersection(intersection(cric_li,foot_li),bad_li)))
print("Number of students who do no play any game ",total-len(union(union(cric_li,bad_li),foot_li)))
print("Number of students who play atleast one game ",len(union(union(cric_li,bad_li),foot_li)))
print("List of students who play all three games",intersection(intersection(cric_li,bad_li),foot_li))

      


