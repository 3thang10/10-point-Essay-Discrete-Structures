def cal_modulo_inverse(n, m):
    def cal_gcd(n, m):
        if n == 1 or m == 1:
            return None
        x = 0
        y = 1
        x_trunggian = 1
        y_trunggian = 0

        while m != 0:

            q = n // m

            r = n % m
            n = m
            m = r

            x_moi = x_trunggian - q * x
            x_trunggian = x
            x = x_moi

            y_moi = y_trunggian - q * y
            y_trunggian = y
            y = y_moi

        gcd = n

        return gcd, x_trunggian, y_trunggian
    if cal_gcd(n, m) == None:
        print ("không tồn tại")
    else:  
        gcd = list(cal_gcd(n,m))[0]
        x = list(cal_gcd(n,m))[1]

        if gcd != 1:
            print("không tồn tại")

        else:
            print(x % m , "là nghịch đảo của",n, "modulo",m)

#testcase1: n = 7, m = 5 
cal_modulo_inverse(7,5)

# #testcase2: n = 0, m = 11
cal_modulo_inverse(0,11)

# #testcase3: n = 15, m = 0 
cal_modulo_inverse(15,0)

# #testcase4: n = 1, m = 1
cal_modulo_inverse(1,1)

# #testcase5: n = 17, m = 17 
cal_modulo_inverse(17, 17)

# #testcase6: n = 20, m = 30
cal_modulo_inverse(20,30)

# #testcase7: n = 12, m = 5 
cal_modulo_inverse(12,5)

# #testcase8: n = 28, m = 15
cal_modulo_inverse(28, 15)

# #testcase9: n = 9, m = 4 
cal_modulo_inverse(9, 4)

# #testcase10: n = 16, m = 9
cal_modulo_inverse(16,9)




