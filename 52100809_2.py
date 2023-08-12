
from sympy import isprime

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def modinv(n, m):
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
        raise ValueError('Nghịch đảo modulo không tồn tại')
    else:  
        gcd = list(cal_gcd(n,m))[0]
        x = list(cal_gcd(n,m))[1]
        if gcd != 1:
            raise ValueError('Nghịch đảo modulo không tồn tại')
        else:
            return x % m
        
def tinhkhoa(p, q):
    if not (isprime(p) and isprime(q)):
        raise ValueError('Hai số p và q phải là số nguyên số')
    elif p == q:
        raise ValueError('p và q không được bằng nhau')
    n = p * q
    phi = (p - 1) * (q - 1)
    for e in range(phi // 3, phi):
        g = gcd(e, phi)
        if g == 1:
            d = modinv(e, phi)
            return ((n, e), (n, d))
    raise ValueError('Lỗi không tìm được e')

def mahoa(pk, td):
    n, e = pk
    ma = [pow(ord(char), e, n) for char in td]
    return ma

def giaima(pk, td_ma):
    n, d = pk
    ma_td = [chr(pow(char, d, n)) for char in td_ma]
    return ''.join(ma_td)

# testcase 1:
# p = 10
# q = 41

# testcase 2:
# p = 97
# q = 41
# thongdiep = ""

# testcase 3:
p = 97
q = 41
thongdiep = "hí hí"
if(thongdiep == ""):
    print("thông điệp rỗng")
else:
    print("Khóa công khai: ", list(tinhkhoa(p, q))[0])
    print("Khóa bí mật: ", list(tinhkhoa(p, q))[1])
    td_mh = mahoa(list(tinhkhoa(p, q))[0], thongdiep)
    print("Thông điệp đã mã hóa: ", td_mh)
    td_gm = giaima(list(tinhkhoa(p, q))[1], td_mh)
    print("Giải mã thông điệp: ", td_gm)