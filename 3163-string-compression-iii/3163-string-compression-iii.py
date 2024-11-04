class Solution:
    def compressedString(self, word: str) -> str:
      h = {}
      comp = []
      prv = word[0]
      
      for c in word:
        if c == prv:
          if c in h:
            h[c] = h[c] + 1
          else:
            h[c] = 1
          if h[c] == 9:
            comp.append(str(h[c])+c)
            h[c]= 0
        else:
          if h[prv] !=0 :
            comp.append(str(h[prv])+prv)
          h[prv]= 0
          h[c] = 1
        prv = c
          
      for k,v in h.items():
        if v != 0:
          comp.append(str(v)+k)
      
      return ''.join(x for x in comp)
        