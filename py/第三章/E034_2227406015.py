names=["张飞","李大刀","李墨白","王老虎","雷小米"]
advanced_mathematics=[78,92,84,50,99]
linear_algebra=[75,67,88,50,98]
summation=[]
def helper(s):
    return [s[1],s[2]]
for i in range(5):
    summation.append([names[i],advanced_mathematics[i],linear_algebra[i]])
summation.sort(key=helper,reverse=True)
print(summation)