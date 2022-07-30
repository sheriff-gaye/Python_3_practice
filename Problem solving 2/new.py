mod = 10**9 + 7
def  getPalindromesCount(s):
    O = I = OO = OI = IO = II = OOx = OIx = IOx = IIx = Oyxy = Iyxy = zyxyz = 0
    for c in s:
        if c == '0':
            zyxyz += Oyxy
            Iyxy += IOx
            Oyxy += OOx
            IIx += II
            IOx += IO
            OIx += OI
            OOx += OO
            IO += I
            OO += O
            O += 1
        else:
            zyxyz += Iyxy
            Iyxy += IIx
            Oyxy += OIx
            IIx += II
            IOx += IO
            OIx += OI
            OOx += OO
            II += I
            OI += O
            I += 1
    return zyxyz % mod
print(getPalindromesCount('0100110'))