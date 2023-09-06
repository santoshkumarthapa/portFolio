ll = [1,2,5,3,7,9,5,4]



ll1 = []
for i in range(len(ll)-1):
    for j in range(len(ll)-i-1):
        if ll[i] < ll[j]:
            ll[j],ll[i] = ll[i], ll[j]

if __name__ == '__main__':
    print(ll)