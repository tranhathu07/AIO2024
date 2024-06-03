# -*- coding: utf-8 -*-
"""AIO2024

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1hFSI3ycPyGP9YlmUWWL_BESrCIWYUBnN

#Exercise 1:Precision, Recall, F1-Score"""
def classifi(tp,fp,fn):
  if type(tp) is not int:
    return("tp must be int")
  elif type(fp) is not int:
    return("fp must be int")
  elif type(fn) is not int:
    return("fn must be int")
  else:
    if not (tp > 0 and fp > 0 and fn > 0):
     print("tp and fp and fn must be greater than zero")
    else:
      precision=tp/(tp+fp)
      recall=(tp/(tp+fn))
      f1score= 2*(precision *recall)/(precision + recall)
      print(f'Precision ={precision}\nRecall = {recall}\nF1-Score={f1score}')

classifi(tp =2,fp ='a',fn =4)

"""#Exercise 2:Sigmoid,relu,elu"""

import math
def is_number ( n ) :
 try :
  float ( n ) # Type - casting the string to ‘float ‘.
 # If string is not a valid ‘float ‘ ,
 # it ’ll raise ‘ValueError ‘ exception
 except ValueError :
   return False
 return True
def sigmoid(x):
    ans= (1/(1 + math.exp(-x)))
    return ans
def relu(x):
  if x<=0:
    return 0
  else:
    return x
def elu(alpha,x):
  if x <=0:
   return(alpha*(math.exp(x)-1))
  else:
    return x
alpha = 0.01
x = input(("Nhập số:" ))
is_number(x)
if is_number(x) == False:
  print('x must be a number')
else:
  x=float(x)
  activation =['sigmoid','relu','elu']
  choice = input("Chọn 1 trong 3 mô hình sau:sigmoid,relu,elu :")
  if choice in activation:
    if choice == 'sigmoid':
      result = sigmoid(x)
      print(result)
    elif choice == 'relu':
      result = relu(x)
      print(result)
    else: # choice == 'elu'
      result = elu(alpha, x)
      elprint(result)
  else:
    print(f'{choice} is not supported')
"""#Exercise 3: MAE,MSE,RMSE để tính loss"""

import random
import math
n=input("Nhập số samples: ")
if n.isnumeric() == True:
 n=int(n)
 choice= input('Chọn 1 loss name trong MAE, MSE, RMSE: ')
 result =0
 mse = 0
 for i in range (1,n+1):
  y_hat = random.uniform(0.0,10.0)
  y = random.uniform(0.0,10.0)
  if choice =='MAE':
    result += (1/n) *abs(y_hat-y)
    print(f'loss name:{choice}, sample:{i}, predict:{y_hat}, target:{y},loss:{result}')
  elif choice == 'MSE':
    result += (1/n) *((y_hat-y)**2)
    print(f'loss name:{choice}, sample:{i}, predict:{y_hat}, target:{y},loss:{result}')
  elif choice == 'RMSE':
    result += (1/n) *((y_hat-y)**2)
    print(f'loss name:{choice}, sample:{i}, predict:{y_hat}, target:{y},loss:{math.sqrt(result)}')
else:
  print('number of samples must be an integer number')

"""#Exercise 4: Tính xấp xỉ"""

def giaithua(n):
    giaithua=1;
    if (n==0 or n==1):
        return giaithua;
    else:
        for i in range(2,n + 1):
            giaithua = giaithua*i;
        return giaithua
def appro_sinx(x,n):
  result = 0
  for i in range(n):
    sign = (-1) ** i
    term = x ** (2 * i + 1) / giaithua(2 * i + 1)
    result += sign * term
  return result

def appro_cosx(x,n):
  result = 0
  for i in range(n):
    sign = (-1) ** i
    term = x ** (2 * i) / giaithua(2 * i)
    result += sign * term
  return result


def appro_sinh(x,n):
  result = 0
  for i in range(n):
    term = x ** (2 * i + 1) / giaithua(2 * i + 1)
    result +=term
  return result

def appro_cosh(x,n):
  result = 0
  for i in range(n):
    term = x ** (2 * i) / giaithua(2 * i)
    result +=term
  return result

x = float(input("Nhập số radian muốn tính toán:"))
n = int(input("Số lần lặp để tính xấp xỉ:"))
if n<=0:
  print("Số lần lặp phải nguyên dương")
else:
  print(f'appro_sinx(x ={x},n={n})={appro_sinx(x,n)}\nappro_cosx(x={x},n={n})={appro_cosx(x,n)}\nappro_sinh(x ={x},n={n})={appro_sinh(x,n)}\nappro_cosh(x ={x},n={n})={appro_cosh(x,n)})')

"""#Exercise 5:Mean Difference of nth Root Error:"""

def md_nre(y,y_hat,n,p):
  result = ((y**(1/n))-(y_hat**(1/n)))**p
  return result
y=float(input("Nhập số target:"))
y_hat = float(input("Nhập số predict:"))
n= int(input("Nhập số căn bậc của target và predict:"))
p= int(input("Nhập bậc hàm loss:"))
print(f' md_nre(y={y},y_hat={y_hat},n={n},p={p})={md_nre(y,y_hat,n,p)}')
