def romanToInt(s: str) -> int:
        int_value = 0
        pre = 0
        for i in s:
            match i:
                case "I":
                    int_value += 1
                    print(int_value) 
                case "V":
                    if pre == "I":
                        int_value += 3
                    else:
                        int_value += 5
                    print(int_value)    
                case "X":
                    if pre == "I":
                        int_value += 8
                    else:
                        int_value += 10
                    print(int_value) 
                case "L":
                    if pre == "X":
                        int_value += 30
                    else:
                        int_value += 50
                    print(int_value) 
                case "C":
                    if pre == "X":
                        int_value += 80
                    else:
                        int_value += 100
                    print(int_value) 
                case "D":
                    if pre == "C":
                        int_value += 300
                    else:
                        int_value += 500
                    print(int_value) 
                case "M":
                    if pre == "C":
                        int_value += 800
                    else:
                        int_value += 1000
                        print(int_value) 
            pre = i
        return int_value

print(romanToInt("MCMXCIV"))        