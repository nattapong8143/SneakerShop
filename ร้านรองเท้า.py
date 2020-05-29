a = []
num = 0
while True:
    b = input('...........IRONFISH Sneaker Shop..........\n Nike [n]\n Adidas [a]\n Reebok [r]\n ตระกร้าสินค้า [x]\n')
    b = b.lower()
    if b =='n':
        c = input('..........Nike.........\n Nike Air Max 97 [n1]\n Nike Jordan 1 mid SE [n2]\n Nike Leborn 17 [n3]\n  ')
        c = c.lower()
        if c =='n1':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Nike Air Max 97','6100฿','20%','4880฿'))
            print('{0:-<100}'.format(""))    
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Nike Air Max 97:6100฿:20%:4880฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=4880
            elif d =='x':
                x = b
        elif c =='n2':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<20}{1:<20}{2:<20}{3:<20}'.format('Nike JOrdan 1 mid SE','4600฿','20%','3680฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Nike JOrdan 1 mid SE:4600฿:20%:3680฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=3680
            elif d =='x':
                x = b
        elif c =='n3':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Nike Leborn 17','7000฿','20%','5600฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Nike Leborn 17:7000฿:20%:5600฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=5600
            elif d =='x':
                x = b
        else:
            print('Not found!!!!')
            c = input('กลับเมนูหลัก กด [x]\n')
            c = b
    elif b =='a':
        c = input('..........Adidas.........\n Adidas Ultraboost Parley [a1]\n Adidas RS REPLICANT OZWEEGO [a2]\n Adidas ADILETTE BOOST[a3]\n  ')
        c = c.lower()
        if c =='a1':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Adidas Ultraboost Parley','6500฿','30%','4550฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Adidas Ultraboostx:6500฿:30%:4550฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=4550
            elif d =='x':
                x = b
        elif c =='a2':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Adidas RS REPLICANT OZWEEGO','16000฿','30%','11200฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Adidas RS REPLICANT OZWEEGO:16000฿:30%:11200฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=11200
            elif d =='x':
                x = b
        elif c =='a3':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Adidas ADILETTE BOOST','2300฿','30%','1610฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Adidas ADILETTE BOOST:23000฿:30%:1610฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=1610
            elif d =='x':
                x = b
        else:
            print('Not found!!!!')
            c = input('กลับเมนูหลัก กด [x]\n')
            c = b
    elif b =='r':
        c = input('..........Reebok.........\n Reebok Ahary Runner [r1]\n Reebok Realflex Train 5.0 [r2]\n Reebok Speed TR Flexweave[r3]\n  ')
        c = c.lower()
        if c =='r1':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Reebok Ahary Runner','3600฿','70%','1080฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Reebok Ahary Runner:3600฿:70%:1080฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=1080
            elif d =='x':
                x = b
        elif c=='r2':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Reebok Realflex Train 5.0','2990฿','70%','897฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Reebok Realflex Train 5.0:2990฿:70%:897฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=897
            elif d =='x':
                x = b
        elif c=='r3':
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
            print('{0:-<100}'.format(""))
            print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('Reebok Speed TR Flexweave','4200฿','70%','1260฿'))
            print('{0:-<100}'.format(""))
            d = input('หยิบใส่ตระกร้า กด [s]\n กลับเมนูหลัก กด [x]\n')
            if d =='s':
                a.append('Reebok Speed TR Flexweave:4200฿:70%:1260฿')
                print('.....ใส่ตระกร้าเรียบร้อย.....')
                num+=1260
            elif d =='x':
                x = b
    elif b =='x':
        print('{0:-<100}'.format(""))
        print('{0:<40}{1:<20}{2:<20}{3:<20}'.format('รุ่น','ราคา','ส่วนลด','รวมทั้งหมด'))
        print('{0:-<100}'.format(""))
        for t in a:
            e = t.split(":")
            print('{0[0]:<40}{0[1]:<20}{0[2]:<20}{0[3]:<20}'.format(e))
        print('{0:<80}{1:<20}'.format('All Price','%d ฿'%(num)))
        c = input('ชำะเงิน [p]\n กลับเมนูหลัก [x]\n')
        if c =='p':
            print('{0:-<100}'.format(""))
            print('{0:<80}'.format('BBL 5467256094 นายนัทธพงศ์ ถวิลการ'))
            print('{0:-<100}'.format(""))
            c = input('แจ่งสลิป [p]\n ยกเลิก [x]\n')
            if c =='p':
                print('{0:-<100}'.format(""))
                print('ชำระเรียบร้อย')
                print('{0:-<100}'.format(""))
            elif c =='x':
                continue
        elif c =='x':
            x = b