
   tour[0] = 0
   used[0] = true
   for i = 1 to n-1 :
      best = -1
      for j = 0 to n-1 :
         if not used[j] and (best = -1 or dist(tour[i-1],j) < dist(tour[i-1],best)) :
            best = j
      tour[i] = best
      used[best] = true
   return tour