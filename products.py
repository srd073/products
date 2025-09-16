products=[]
while True:
	name=input('請輸入商品名稱(q離開):')
	if name=='q':
		break
	price=input('請輸入商品價格：')

	# p=[]
	# p.append(name)
	# p.append(price)
	#p = [name, price]    ＃程式寫法,效果同上面三行
    
	#products.append(p)
	products.append([name,price]) 

print(products)

for p in products:
	print(p)

for p in products:
	print(p[0],'的價格是',p[1])

# 字串可以合併 ＋,*
# 'abc' + '123'  --> 'abc123'
# 'abc' *  3     --> 'abcabcabc'

with open('products.csv','w') as f:
	for p in products:
		f.write(p[0]+','+p[1]+'\n') 




