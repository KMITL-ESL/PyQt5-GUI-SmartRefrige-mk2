import gtts
import os
import time

tts = gtts.gTTS(text='ตู้เย็นอัจฉริยะสวัสดีค่ะรับอะไรดีคะ',lang='th')
tts.save('test.mp3')
os.system('test.mp3')
print('------------------------')
print('-    [Water]  [Cancle]   -')
print('------------------------')
choose1 = (input('>>>>>'))
if choose1 == "Water" :
    print('------------------------')
    print('-  Please enter amount of bottle you want   -')
    print('------------------------')

    water = int(input('>>>>>'))
    print('-------------------------------------------------------')
    print('-             amount of bottle'+ str(water)  +                '-')
    print('- if the amount at bettle is correct please confirm   -')
    print('-      [Confirm press 0]         [Cancle press 1]     -')
    print('-------------------------------------------------------')
    
    s = (input('>>>>>'))
    if s == "0" :
        error = 5
        while error > 2 :
            print('------------------------------------------')
            print('-        System is scanning your face       -')
            print('- please manage your face position in the square  -')
            print('-        [Sucessful press 0]    [Failed press 1]    -')
            print('------------------------------------------')
            scan = (input('>>>>>'))
            if scan == "0" :
                print('Successfully scanning')
                
                tts = gtts.gTTS(text='สวัสดีค่ะ คุณวัชราภรณ์',lang='th')
                tts.save('testscanfacetrue.mp3')
                os.system('testscanfacetrue.mp3')
                time.sleep(5)

                pay=water*10
                print('--------------------------------------------')
                print('-  Username : Watcharaporn Chatan             -')
                print('-  Quantity : '+str(water)+'            -')
                print('-  Total : '+str(pay) +' Baht     -')
                print('--------------------------------------------')
               
                tts = gtts.gTTS(text='โปรดตรวจสอบข้อมูล หากถูกต้องกดยืนยัน',lang='th')
                tts.save('testscanfacetrue.mp3')
                os.system('testscanfacetrue.mp3')

                print('--------------------------------')
                print('-  [Confirm press 0]   [Cancel press 1]  -')
                print('--------------------------------')
                choose2 = (input('>>>>'))
                errorpay = 5
                
                if choose2 == "0" :
                    print('--------------------------------')
                    print('-    System is processing the payment.    -')
                    print('--------------------------------')
                    account = 200
                    time.sleep(5)
                    if pay<account :
                        print('--------------------')
                        print('-    The payment is successful.   -')
                        print('--------------------')
                        print('--------------------')
                        print('-  Thank you for using the service  -')
                        print('--------------------')
                        tts = gtts.gTTS(text='ขอบคุณที่ใช้บริการ',lang='th')
                        tts.save('testscanfacefalse.mp3')
                        os.system('testscanfacefalse.mp3')
                        break
                    elif pay>account :
                        print('--------------------')
                        print('-  Payment failed   -')
                        print('--------------------')
                        tts = gtts.gTTS(text='เงินในบัญชีของท่านไม่เพียงพอ ตรวจสอบการทำรายการอีกครั้งค่ะ',lang='th')
                        tts.save('testscanfacetrue.mp3')
                        os.system('testscanfacetrue.mp3')
                        
                    else :
                        print('Try again.') 
                    
                elif choose2 == "1" :
                   error = 5
                                         
            elif scan == "1" :
               print('Undetecting face, please try again.')
               tts = gtts.gTTS(text='ลองใหม่อีกครั้งค่ะ',lang='th')
               tts.save('testscanfacefalse.mp3')
               os.system('testscanfacefalse.mp3')
               error = 5
    else :
        print('Thank you for using the service.')
        tts = gtts.gTTS(text='ขอบคุณที่ใช้บริการ',lang='th')
        tts.save('testscanfacefalse.mp3')
        os.system('testscanfacefalse.mp3')
elif choose1 == "Cancel" :
    print('Thank you for using the service.')
    tts = gtts.gTTS(text='ขอบคุณที่ใช้บริการ',lang='th')
    tts.save('testscanfacefalse.mp3')
    os.system('testscanfacefalse.mp3')
else :
    print('Please try again.')