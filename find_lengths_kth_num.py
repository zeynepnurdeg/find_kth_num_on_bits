def findKthBit(length, k):
    S = "0"
    for i in range(2,length+1):
        invert = ""
        for j in range(len(S)):
            if S[j] == "1":
                invert += "0"
            else:
                invert += "1"

        S = S + "1" + invert[::-1]
            
    print(S) #optional, just to see the whole string
    return S[k - 1]

bit = int(input("Enter the num of bit (1-20 pls): "))
k = int(input("Enter the k (as to find the kth num of bit lenght): "))

print(findKthBit(bit,k))