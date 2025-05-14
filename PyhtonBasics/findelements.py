
def findelement(lis, ele, ind):
    lis_len = len(lis)
    ele_ind = lis.index(ele)
    remin = (ind + ele_ind) % lis_len
    return lis[remin+1]
    
lis = ["Mon", "Tue", "Wed", "Thrus", "Fri", "Sat", "Sun"]
ele = "Sun"
ind = 16
    
x = findelement(lis=lis, ele=ele, ind=ind)
print(x)