alphabet = " ABCDEFGHIJKLMNOPQRSTUVWXYZ"
digits = "0123456789"
letter = "AZYXUTSRPMLKJHGEDCB"
weights = (9, 4, 5, 4, 3, 2)

def validate_checksum(letters:str, nums:str):
    val = []
    if len(nums) < 4:
        pad = 4 - len(nums)
        nums = nums.zfill(pad)
    for i in letters:
        for idx in range(len(letter)):
            if i == letter[idx]:
                val.append(idx)
    for x in nums:
        val.append(x)
    total = 0
    ## left with checksum calculations and return checksum letter
    
                

def is_plate_valid(letters:str, nums:int, checksum:str):
    letters = letters.upper()
    if letters[0:1] != 'S':
        return False
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
    return True

validate_checksum('NB', '9538')