total = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    nums = []
    coords = []
    total = 0
    lineno = 1

    for line in lines:
        for i, v in enumerate(line):
            if v.isnumeric():
                nums.append(v)
        #print(nums)        
        chars = len(nums)
        if chars == 1:
            total = total + int((nums[0]) + (nums[0]))
            #print(f"{lineno}: {total}")
        else:
            total = total + int((nums[0]) + (nums[chars-1]))
            #print(f"{lineno}: {total}")
        nums = []
        lineno = lineno + 1


print(total)

