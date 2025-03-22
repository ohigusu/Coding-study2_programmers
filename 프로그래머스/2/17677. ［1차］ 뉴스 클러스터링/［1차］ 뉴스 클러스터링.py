import re
from collections import Counter
def solution(str1, str2):
    str1,str2 = str1.lower(),str2.lower()
    
    def make_pairs(s):
        pairs = []
        for i in range(len(s)-1):
            temp = s[i:i+2]
            if re.fullmatch("[a-z]{2}", temp): 
                pairs.append(temp)
        return pairs
    
    s1,s2 = make_pairs(str1),make_pairs(str2)
    
    counter1 = Counter(s1)
    counter2 = Counter(s2)
    
    gyo = counter1 & counter2  
    hab = counter1 | counter2 
    
    inter = sum(gyo.values())
    union = sum(hab.values())
    
    
    if union == 0:
        return 65536
    
    return int((inter / union) * 65536)