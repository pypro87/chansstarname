for i in range(11):
  if i<4:
    for j in range(i, 4):
      print(" ", end=" ")
  else:
    if i<8:
      for j in range(1):
        print(" ", end=" ")
    else:
      for j in range(6,i):
        print(" ", end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<3:
    if i>0:
      for l in range(0, 2*i):
        print(" ", end=" ")
    for k in range(3):
      print("*", end=" ")
    for l in range(i,3):
      print(" ",end=" ")
  else:
    if i<8:
      for l in range(9):
        print(" ",end=" ")
    else:
      for l in range(i,10):
        print(" "," ",end=" ");
      for k in range(3):
        print("*",end=" ")
      for l in range(7,i):
        print(" ",end=" ")
#H
  for j in range(3):
    print("*",end=" ")
  if i<4 or i>6:
    for l in range(5):
      print(" ",end=" ")
  else:
    for k in range(5):
      print("*",end=" ")
  for j in range(3):
    print("*",end=" ")
  print(" ",end=" ")
#A
  for j in range(i,3):
    print(" ",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<4:
    for l in range(0,2*i):
      print(" ",end=" ")
  else:
    if i>3 and i<7 or i>8:
      for l in range(6):
        print(" ",end=" ")
    else:
      for l in range(6):
        print("*",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<3:
    for j in range(i,4):
      print(" ",end=" ")
  else:
      print(" ",end=" ")
#N
  for j in range(3):
    print("*",end=" ")
  if i<3:
    for k in range(0,i):
      print("*",end=" ")
  else:
    for l in range(0,i-3):
      print(" ",end=" ")
    for j in range(3):
      print("*",end=" ")
  for l in range(i,7):
    print(" ",end=" ")
  if i<8:
    for j in range(3):
      print("*",end=" ")
  else:
    for j in range(i,10):
      print("*",end=" ")
  print(" ",end=" ")
#D
  for j in range(3):
    print("*",end=" ")
  if i<1:
    for j in range(3):
      print("*",end=" ")
    for l in range(5):
       print(" ",end=" ")
  else:
    if i<3:
      for k in range(0,i+1):
       print(" ",end=" ")
      for j in range(3):
       print("*",end=" ")
      for l in range(i+1,5):
       print(" ",end=" ")
    else:
      if i<8:
        for k in range(4):
          print(" ",end=" ")
        for j in range(3):
          print("*",end=" ")
        print(" ",end=" ")
      else:
        if i<10:
          for k in range(i,11):
            print(" ",end=" ")
          for j in range(3):
            print("*",end=" ")
          for l in range(6,i):
            print(" ",end=" ")
        else:
          for j in range(3):
            print("*",end=" ")
          for l in range(5):
            print(" ",end=" ")
#A
  for j in range(i,3):
    print(" ",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<4:
    for l in range(0,2*i):
      print(" ",end=" ")
  else:
    if i>3 and i<7 or i>8:
      for l in range(6):
        print(" ",end=" ")
    else:
      for l in range(6):
        print("*",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<3:
    for j in range(i,4):
      print(" ",end=" ")
  else:
      print(" ",end=" ")
#N
  for j in range(3):
    print("*",end=" ")
  if i<3:
    for k in range(0,i):
      print("*",end=" ")
  else:
    for l in range(0,i-3):
      print(" ",end=" ")
    for j in range(3):
      print("*",end=" ")
  for l in range(i,7):
    print(" ",end=" ")
  if i<8:
    for j in range(3):
      print("*",end=" ")
  else:
    for j in range(i,10):
      print("*",end=" ")
  print(" ",end=" ")
#A
  for j in range(i,3):
    print(" ",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<4:
    for l in range(0,2*i):
      print(" ",end=" ")
  else:
    if i>3 and i<7 or i>8:
      for l in range(6):
        print(" ",end=" ")
    else:
      for l in range(6):
        print("*",end=" ")
  for k in range(3):
    print("*",end=" ")
  if i<3:
    for j in range(i,4):
      print(" ",end=" ")
  else:
      print(" ",end=" ")
  print()