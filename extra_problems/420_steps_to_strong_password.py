# Solution from Ryan Logsdon (https://www.youtube.com/watch?v=aBu8T3YxQI0)
class Solution:
    MIN_LENGTH = 6
    MAX_LENGTH = 20

    def choose_best_character(self, password, index):
        filler = 'Z'                                                    # assume we should use an upper
        if not any(p.islower() for p in password):                      # if there are no lowers, use that
            filler = 'z'
        elif not any(p.isdigit() for p in password):                    # if there are no digits, use that
            filler = '9'
        if password[index] == filler:                                   # if the char at index is the same as filler, change Z->Y, z->y, 9->8 so we don't inadvertently repeat chars
            filler = chr(ord(filler) - 1)
        return filler

    def change_character(self, password, index):
        filler = self.choose_best_character(password, index)            # choose the best character to use for the given location

        temp = list(password)
        temp[index] = filler                                            # swap the character at index with the new filler character
        return ''.join(temp)

    def add_character(self, password, index):
        filler = self.choose_best_character(password, index)            # choose the best character to use for the given location
        return password[:index] + filler + password[index:]             # add in the filler at index

    def find_repeat_index(self, password):
        partitions = []                                                 # split the password up into groups of repeating chars, ex: 'aaabbbcd' -> ['aaa', 'bbb', 'c', 'd']
        previous_split = 0
        for i in range(1, len(password)):                               # start at the 2nd char and look back 1 to try to match
            if password[i-1] != password[i]:                            # if adjacent characters aren't matching
                partitions.append(password[previous_split:i])           # create a new partition
                previous_split = i
        partitions.append(password[previous_split:len(password)])       # remember to add the final section to the partition

        # print(partitions)

        max_length = max(len(partition) for partition in partitions)    # find the longest partition
        if max_length < 3:                                              # if there are no partitions of at least 3 repeating characters, return -1
            return -1
        
        mod1_index, mod2_index = -1, -1                                 # index of the first occurrances of repeating characters of length % 3 == 1 and length % 3 == 2
        index = 0
        for partition in partitions:
            length = len(partition)
            # print(f'partition: {partition}, length={length}')
            
            if length < 3:                                              # we're only targeting repeating partitions of 3 characters or greater
                index += length
                continue
            if length % 3 == 0:                                         # it's most efficient to target a repeating set of characters that divide evenly by 3
                return index
            if length % 3 == 1 and mod1_index == -1:
                mod1_index = index
            if length % 3 == 2 and mod2_index == -1:
                mod2_index = index
            index += length

        if mod1_index > -1:
            return mod1_index
        if mod2_index > -1:
            return mod2_index
        return 0

    def has_upper_lower_and_digit(self, password):
        has_upper = any(p.isupper() for p in password)
        has_lower = any(p.islower() for p in password)
        has_digit = any(p.isdigit() for p in password)

        if has_upper and has_lower and has_digit:
            return True
        return False

    def is_strong_password(self, password):
        if len(password) < self.MIN_LENGTH:
            return False

        if len(password) > self.MAX_LENGTH:
            return False

        if self.find_repeat_index(password) > -1:                               # the index of repeating characters is returned, -1 = no repeats
            return False

        if self.has_upper_lower_and_digit(password):
            return True

        return False

    def find_safe_index(self, password):
        for i in range(len(password)):                                          # find the first char in the password that isnt the only lower, upper, or digit in the password
            p = password[i]
            truncated_password = password[:i] + password[i+1:]                  # remove the i-th char from the password

            if p.isupper() and any(p.isupper() for p in truncated_password):    # if the i-th char is uppercase and there's still another uppercase char in the password, this is a safe char to remove
                return i
            if p.islower() and any(p.islower() for p in truncated_password):
                return i
            if p.isdigit() and any(p.isdigit() for p in truncated_password):
                return i
        return 0                                                                # only reach here if there are no alphanumeric chars in password

    def strongPasswordChecker(self, password: str) -> int:
        steps = 0

        print(f'{password} (starting at {len(password)})')

        while (True):
            repeat_index = self.find_repeat_index(password)
            # print(f'triple index: {repeat_index}')
            
            if len(password) < self.MIN_LENGTH:                                 # if the password is too short
                index = 0
                if repeat_index > -1:                                           # ...and there's a triple
                    index = repeat_index+2                                      # break up the triplicate character (2 index spaces after the start)
                password = self.add_character(password, index)                  # else just add a charact to the start to pad the length
            
            elif len(password) > self.MAX_LENGTH:                               # if the password is too long
                index = self.find_safe_index(password)                          # find an index where we know we wont remove the only upper, lower, or digit from the password
                if repeat_index > -1:                                           # ...and there's a triple
                    index = repeat_index+2
                password = password[:index] + password[index + 1:]

            else:                                                               # else the length isn't a problem
                if self.is_strong_password(password):
                    print(f'{password} is strong!')
                    break
                index = self.find_safe_index(password)                          # find an index where we know we wont remove the only upper, lower, or digit from the password
                if repeat_index > -1:
                    index = repeat_index+2                                      # the triplicate character (2 index spaces after the start)
                password = self.change_character(password, index)           
                

            steps += 1
            print(f'{password} ({len(password)})')

            if steps > 100:
                break
            
            if self.is_strong_password(password):
                # print(f'{password} is strong!')
                break

            

        return steps


if __name__ == '__main__':
    # password = 'ABABABABABABABABABAB1'                      # 2 steps
    # password = 'bbaaaaaaaaaaaaaaacccccc'                    # 8 steps
    # password = 'aaaabbbbccccddeeddeeddeedd'                 # 8 steps
    # password = 'FFFFFFFFFFFFFFF11111111111111111111AAA'     # 23 steps
    # password = 'a'                                          # 5 steps
    password = 'aA1'                                        # 3 steps
    # password = '1337C0d3'                                   # 0 steps
    # password = 'aaa1aaa'                                    # 2 steps
    # password = 'aaabb'                                      # 2 steps
    # password = 'aaa'                                        # 3 steps
    # password = 'aaaabb'                                     # 2 steps
    # password = 'aaaaBb'                                     # 1 step
    # password = 'aaaaaaaaaaa'                                # 3 steps
    # password = '...!!!'                                     # 3 steps
    # password = 'hoAISJDBVWD09232UHJEPODKNLADU1'             # 10 steps


    s = Solution()
    steps = s.strongPasswordChecker(password)
    print(f'steps = {steps}')