with open("input3") as f:
    data = f.read().splitlines()

# def maxpower(s):
#     nums = list(s)
#     ans = 0
#     for a in nums:
#         pos = nums.index(a)
#         a = int(a)
#         for b in nums[pos+1:]:
#             b = int(b)
#             maybe = (a*10)+b
#             if maybe>ans:
#                 ans = maybe
#     return(ans)
def maxpower(s):
    nums = [int(num)for num in s]
    slice1 = nums[:-11]
    num1 = max(slice1)
    pos1 = slice1.index(num1)
    print(pos1)
    slice2 = nums[pos1+1:-10]
    num2 = max(slice2)
    pos2 = pos1 + 1 + slice2.index(num2)
    print(pos2)
    slice3 = nums[pos2+1:-9]
    num3 = max(slice3)
    pos3 = pos2 + 1 + slice3.index(num3)
    print(pos3)
    slice4 = nums[pos3+1:-8]
    num4 = max(slice4)
    pos4 = pos3 + 1 + slice4.index(num4)
    print(pos4)
    slice5 = nums[pos4+1:-7]
    num5 = max(slice5)
    pos5 = pos4 + 1 + slice5.index(num5)
    print(pos5)
    slice6 = nums[pos5+1:-6]
    num6 = max(slice6)
    pos6 = pos5 + 1 + slice6.index(num6)
    print(pos6)
    slice7 = nums[pos6+1:-5]
    num7 = max(slice7)
    pos7 = pos6 + 1 + slice7.index(num7)
    print(pos7)
    slice8 = nums[pos7+1:-4]
    num8 = max(slice8)
    pos8 = pos7 + 1 + slice8.index(num8)
    print(pos8)
    slice9 = nums[pos8+1:-3]
    num9 = max(nums[pos8+1:-3])
    pos9 = pos8 + 1 + slice9.index(num9)
    print(pos9)
    slice10 = nums[pos9+1:-2]
    num10 = max(slice10)
    pos10 = pos9 + 1 + slice10.index(num10)
    print(pos10)
    slice11 = nums[pos10+1:-1]
    num11 = max(slice11)
    pos11 = pos10 + 1 + slice11.index(num11)
    print(pos11)
    num12 = max(nums[pos11+1:])
    ans = num1*100000000000+num2*10000000000+num3*1000000000+num4*100000000+num5*10000000+num6*1000000+num7*100000+num8*10000+num9*1000+num10*100+num11*10+num12
    return(ans)
# print(maxpower(data[0]))
# print(data[0])
# print(data)
anslist = []
for l in data:
    val = maxpower(l)
    anslist.append(val)
print(anslist)
print(sum(anslist))