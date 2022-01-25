class Solution:
    def intToRoman(self, num: int) -> str:
        
        dict_base1 =  {
            "0": "",
            "1": "I",
            "2": "II",
            "3": "III",
            "4": "IV",
            "5": "V",
            "6": "VI",
            "7": "VII",
            "8": "VIII",
            "9": "IX"
        }
        dict_base2 = {
            "0": "",
            "1": "X",
            "2": "XX",
            "3": "XXX",
            "4": "XL",
            "5": "L",
            "6": "LX",
            "7": "LXX",
            "8": "LXXX",
            "9": "XC"
        }
        dict_base3 = {
            "0": "",
            "1": "C",
            "2": "CC",
            "3": "CCC",
            "4": "CD",
            "5": "D",
            "6": "DC",
            "7": "DCC",
            "8": "DCCC",
            "9": "CM"
        }
        dict_base4 = {
            "1": "M",
            "2": "MM",
            "3": "MMM"
        }
        num = str(num)
        dicts_list = [dict_base1, dict_base2, dict_base3,dict_base4]
        res = ""
        for i in range(len(num)):
            res += dicts_list[len(num)-i -1][num[i]]

        return res

        
        
    
