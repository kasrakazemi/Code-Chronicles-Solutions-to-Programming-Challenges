class Solution:
    def intToRoman(self, num: int) -> str:
        divide_list =  [1, 4, 5, 9, 10, 40, 50, 90,
		100, 400, 500, 900, 1000]
        divide_list.reverse()
        output_str=''
        roman_dic = {
           1:     'I'  ,
              5:  'V'    ,
                10:'X'      ,
                50:'L'      ,
                100:'C'       ,
             500:   'D'        ,
                1000: 'M'         ,
              4:     'IV'  ,
              9:  'IX'    ,
                40:'XL'      ,
                90:'XC'      ,
                400:'CD'       ,
             900:   'CM'      
        }
        for i in divide_list:
      
            divide = num//i

            num = num%i
            output_str += divide * roman_dic[i]
              


        return output_str