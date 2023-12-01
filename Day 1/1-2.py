total = 0
toadd = 0
with open('input.txt', 'r', encoding="utf-8") as f:
    lines = f.readlines()
    nums = []
    coords = []
    total = 0
    lineno = 1
    textnums = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7, "eight": 8, "nine": 9}
    x = 0
    y = 1

    for line in lines:
        while y < len(line):
            test = (line[x:y])
            #print(test)
            if any(chr.isdigit() for chr in test):
                nums.append(test[-1])
                x = y
            else:
                for key, value in textnums.items():
                    if key in line[x:y]:
                        nums.append(str(value))
                        x = y-1
            y = y+1
        y=0
        x=0
        #print(nums)
           
        chars = len(nums)
        if chars < 1:
            print("No Ints")
        elif chars == 1:
            toadd = int((nums[0]) + (nums[0]))
            total = total + toadd
        else:
            toadd = int((nums[0]) + (nums[chars-1]))
            total = total + toadd
        #print(f"{lineno}: {line} = {nums} -> {toadd}")
        #o.write(str(toadd) + "\n")    
        nums = []
        toadd = 0
        lineno = lineno + 1


print(total)