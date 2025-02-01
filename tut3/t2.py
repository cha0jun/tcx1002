alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
letter = "AZYXUTSRPMLKJHGEDCB"
weights = (9, 4, 5, 4, 3, 2)

def validate_checksum(letters:str, nums:str):
    val = []
    if len(nums) < 4:
        nums = nums.zfill(4)
    for i in letters:
        if i == '0':
            val.append(int(i))
        for idx in range(len(alphabet)):
            if i == alphabet[idx]:
                val.append(idx)
    for x in nums:
        val.append(int(x))
    print(val)
        
    total = 0
    udx = 0
    for k in val:
        total = total + (k*weights[udx])
        udx += 1
        
    remainder = total % 19
    
    checkval = letter[remainder]
    
    return checkval
                

def is_plate_valid(letters:str, nums:int, checksum:str):
    letters = letters.upper()
    ##if letters[0:1] != 'S':
    ##    return False
    if ('I' or 'O') in letters:
        return False
    nums = str(nums)
    if len(nums) > 4:
        return False
    if nums[0:1] == '0':
        return False
    if len(checksum)>1:
        return False
    if checksum.upper() in ('F' or 'I' or 'N' or 'O' or 'Q' or 'V' or 'W'):
        return False
    checkinput = ''
    
    if len(letters) == 3:
        checkinput = letters[1:]
    elif len(letters) == 2:
        checkinput = letters
    elif len(letters) == 1:
        checkinput = letters.zfill(2)
        
    if checksum != validate_checksum(checkinput,nums):
        return False
        
    return True

print(is_plate_valid('SNB',9538,'E'))