N = input().split()
MS = set(N[:2])
TK = set(N[2:4])

game = {'P':'S','R':'P','S':'R'}

if len(MS) == 2 and len(TK) == 2 :
   print('?')
elif len(MS) == 1 and len(TK) == 1 :
   if game[list(MS)[0]] in TK :
      print('TK')
   elif game[list(TK)[0]] in MS :
      print('MS')
   else :
      print('?')
elif len(MS) < 2 :
   if game[list(MS)[0]] in TK :
      print('TK')
   else :
      print('?')
elif len(TK) < 2 :
   if game[list(TK)[0]] in MS :
      print('MS')
   else :
      print('?')