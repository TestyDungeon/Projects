def romanToInt(s: str) -> int:
        int_value = 0
        for i in s:
            match i:
                case "I":
                    int_value += 1
                case "V":
                    int_value += 5
                case "X":
                    int_value += 10
                case "L":
                    int_value += 50
                case "C":
                    int_value += 100
                case "D":
                    int_value += 500
                case "M":
                    int_value += 1000
        return int_value

print(romanToInt("IV"))        