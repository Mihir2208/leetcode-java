class Solution:
    def lemonadeChange(self, bills: list[int]) -> bool:
        five_counter = 0
        ten_counter = 0
        balance = 0

        for i in range(len(bills)):
            if bills[i] == 5:
                five_counter += 1
                balance += bills[i]

            elif bills[i] == 10:
                if five_counter > 0:
                    ten_counter += 1
                    balance += bills[i]
                    balance -= 5
                    five_counter -= 1
                else:
                    return False    

            if bills[i] == 20:
                if ten_counter > 0 and five_counter > 0:
                    ten_counter -= 1
                    five_counter -= 1
                elif five_counter >= 3:
                    five_counter -= 3
                else:
                    return False 
         

        return True   

