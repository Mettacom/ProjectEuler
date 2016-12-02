"""Counts of letters in each value. Minimal number of numbers"""
counts = {1:3, 2:3, 3:5, 4:4, 5:4, 6:3, 7:5, 8:5, 9:4, 10:3, 11:6, 12:6, 13:8, 14:8, 15:7, 16:7, 17:9, 18:8, 19:8, 20:6, 30:6, 40:5, 50:5, 60:5, 70:7, 80:6, 90:6, 100:10, 200:10, 300:12, 400:11, 500:11, 600:10, 700:12, 800:12, 900:11, 1000:11, 0:3}
"""Fill in the counts dictionary"""
for i in range(1, 1001):
    
    istr = str(i)
    
    if i not in counts:
        
        if len(istr) == 3:
                
            if int(istr[1]) != 0:
            
                counts[i] = counts[int(istr[0]+'00')] + counts[0] + counts[int(istr[1:])]
                
            
            else:
                
                counts[i] = counts[int(istr[0]+'00')] + counts[0] + counts[int(istr[2])]
        
        elif len(istr) == 2:
            
            counts[i] = counts[int(istr[0] + '0')] + counts[int(istr[1])]

    
print sum(counts.values()) - 3