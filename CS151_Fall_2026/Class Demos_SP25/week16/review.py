var_A = (2, 4, 8, )
var_B = (2*var_A, ('bits', ) )
var_C = var_B , ('K_byte','M_byte', 'G_byte', 'T_byte')
var_D = ("n",)
for v in var_C[1:]:
    var_D += v[:1]
print(type(var_D))

print(chr(101))

def puzzle(t): 
    def mystery(r,x): 
        x+=2 
        def enigma(s=0): 
            return r[s::x] 
        return enigma 
    x=1 
    y= mystery(t,x=x) 
    return y(x)+ y() + y(s=8)
print(puzzle("afslihdnya"))