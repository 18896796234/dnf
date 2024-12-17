import serial #line:1
import time #line:2
import numpy as np #line:3
import random #line:4
import threading #line:6
class CH9329 :#line:9
    def __init__ (OOO000O0OOOO0O0OO ,OOOOO00OO0O0OOO0O ):#line:10
        OOO000O0OOOO0O0OO .__O00000OO000O00000 =serial .Serial (OOOOO00OO0O0OOO0O ,baudrate =9600 ,timeout =0.2 )#line:11
        OOO000O0OOOO0O0OO .__O00OO0O0OOO0O0O0O =threading .Lock ()#line:12
        OOO000O0OOOO0O0OO .__O00OOO0O00O000000 ={'shiftkey':6 ,'shift':6 ,'controlkey':7 ,'ctrl':7 ,'menu':5 ,'alt':5 ,'lwin':4 ,'rwin':1 ,}#line:22
        OOO000O0OOOO0O0OO .__OO0OOO000000OO0O0 ={'left':7 ,'right':6 ,'middle':5 }#line:28
        OOO000O0OOOO0O0OO .__OO0OO0OO00OO000O0 ={'~':'35','!':'1E','@':'1F','#':'20','$':'21','%':'22','^':'23','&':'24','*':'25','(':'26',')':'27','_':'2D','+':'2E','{':'2F','}':'30','|':'38',':':'33','"':'34','<':'36','>':'37','?':'38','Q':'14','W':'1A','E':'08','R':'15','T':'17','Y':'1C','U':'18','I':'0C','O':'12','P':'13','A':'04','S':'16','D':'07','F':'09','G':'0A','H':'0B','J':'0D','K':'0E','L':'0F','Z':'1D','X':'1B','C':'06','V':'19','B':'05','N':'11','M':'10',}#line:78
        OOO000O0OOOO0O0OO .__OO00OOOOOO0OOOOOO ={'tab':'2B','`':'35','1':'1E','2':'1F','3':'20','4':'21','5':'22','6':'23','7':'24','8':'25','9':'26','0':'27','-':'2D','=':'2E','q':'14','w':'1A','e':'08','r':'15','t':'17','y':'1C','u':'18','i':'0C','o':'12','p':'13','[':'2F',']':'30','a':'04','s':'16','d':'07','f':'09','g':'0A','h':'0B','j':'0D','k':'0E','l':'0F',';':'33','\'':'34','z':'1D','x':'1B','c':'06','v':'19','b':'05','n':'11','m':'10',',':'36','.':'37','/':'38','capital':'39','shang':'52','xia':'51','zuo':'50','you':'4F','up':'52','down':'51','left':'50','right':'4F','esc':'29','enter':'28','space':'2C',' ':'2C','f10':'43','f5':'3E','f11':'44','f12':'45','back':'2A','del':'4C','delete':'4C','f1':'3A','f2':'3B','f3':'3C','f4':'3D','f5':'3E','f6':'3F','f7':'40','f8':'41','f9':'42',}#line:147
        OOO000O0OOOO0O0OO .__O000O0O0OO0000OO0 =["57","AB","00","02","08"]#line:149
        OOO000O0OOOO0O0OO .__OO00OOO0OO0O0O00O =['57','AB','00','04','07','02']#line:150
        OOO000O0OOOO0O0OO .__OO00OO0O000OOO00O =['57','AB','00','05','05','01']#line:151
        OOO000O0OOOO0O0OO .__O00OO00O00O00O0OO =['00','00','00','00','00','00']#line:153
        OOO000O0OOOO0O0OO .__O0O0O0O00O00O0OOO =['0','0','0','0','0','0','0','0']#line:155
        OOO000O0OOOO0O0OO .__OO00OO00OOOO0OOO0 =['0','0','0','0','0','0','0','0']#line:157
    def __O0OO0OOOO0OOO000O (OOOOO00OO0OOO000O ,OO0000OO0000O0OO0 ):#line:160
        try :#line:161
            with OOOOO00OO0OOO000O .__O00OO0O0OOO0O0O0O :#line:162
                O0O0O0O0O000O0O00 =bytes .fromhex (OO0000OO0000O0OO0 )#line:163
                OOOOO00OO0OOO000O .__O00000OO000O00000 .write (O0O0O0O0O000O0O00 )#line:164
                time .sleep (random .uniform (0.005 ,0.012 ))#line:165
        except serial .SerialException as OOOOOO0O00O00OO0O :#line:173
            print ("串口通信发生异常:",OOOOOO0O00O00OO0O )#line:174
            OOOOO00OO0OOO000O .reset ('all')#line:175
    def close_serial (OO0O0O0OO0OO0O0O0 ):#line:179
        OO0O0O0OO0OO0O0O0 .__O00000OO000O00000 .close ()#line:180
    def reset (OO00OO00O0O0OO00O ,type ='key'):#line:183
        if type =='key':#line:184
            OO00OO00O0O0OO00O .key_reset ()#line:185
        elif type =='mouse':#line:186
            OO00OO00O0O0OO00O .mouse_reset ()#line:187
        elif type =='all':#line:188
            OO00OO00O0O0OO00O .key_reset ()#line:189
            OO00OO00O0O0OO00O .mouse_reset ()#line:190
    def key_reset (OOO00O00OOOOO0000 ):#line:193
        OOO00O00OOOOO0000 .__O00OO00O00O00O0OO =['00','00','00','00','00','00']#line:195
        OOO00O00OOOOO0000 .__O0O0O0O00O00O0OOO =['0','0','0','0','0','0','0','0']#line:196
        OOO00O00OOOOO0000 .__O0OO0OOOO0OOO000O ('57AB00020800000000000000000C')#line:198
    def mouse_reset (OO000OOOOO0OO0OO0 ):#line:201
        OO000OOOOO0OO0OO0 .__OO00OO00OOOO0OOO0 =['0','0','0','0','0','0','0','0']#line:203
        OO000OOOOO0OO0OO0 .__O0OO0OOOO0OOO000O ('57AB000407020000000000000F')#line:204
        OO000OOOOO0OO0OO0 .__O0OO0OOOO0OOO000O ('57AB00050501000000000D')#line:205
    def __OO0O00000000OO000 (O0000OO00000OOO0O ,OO000O000O0O0O0O0 ):#line:209
        OO00OOOO000O0OOOO =0 #line:210
        for O0O0O0O00OOO000O0 in OO000O000O0O0O0O0 :#line:211
            OO00OOOO000O0OOOO +=int (O0O0O0O00OOO000O0 ,16 )#line:212
        O0O0O000000OO0OO0 =hex (OO00OOOO000O0OOOO )[-2 :]#line:213
        return O0O0O000000OO0OO0 #line:214
    def __OOOO0000OOO00000O (O0OO000OOOO00OOOO ,O0OO0OOO0OO00OOO0 ):#line:219
        OO0OO0O00OOOO0OOO =int (O0OO0OOO0OO00OOO0 ,2 )#line:220
        OO00OO0O00O000O0O =format (OO0OO0O00OOOO0OOO ,'02X')#line:221
        return [OO00OO0O00O000O0O ]#line:222
    def keyDown (O00OO0OO00O0O0O0O ,O0O00OO0000OO0O00 ):#line:225
        if O0O00OO0000OO0O00 !='':#line:227
            if O0O00OO0000OO0O00 in O00OO0OO00O0O0O0O .__OO00OOOOOO0OOOOOO :#line:228
                if O00OO0OO00O0O0O0O .__OO00OOOOOO0OOOOOO [O0O00OO0000OO0O00 ]in O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO :#line:229
                    return #line:230
                else :#line:231
                    for O00OO00OOO00000OO ,OOO0000O0OOOOO000 in enumerate (O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO ):#line:232
                        if OOO0000O0OOOOO000 =='00':#line:233
                            O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO [O00OO00OOO00000OO ]=O00OO0OO00O0O0O0O .__OO00OOOOOO0OOOOOO [O0O00OO0000OO0O00 ]#line:234
                            break #line:235
            elif O0O00OO0000OO0O00 in O00OO0OO00O0O0O0O .__O00OOO0O00O000000 :#line:238
                if O00OO0OO00O0O0O0O .__O0O0O0O00O00O0OOO [O00OO0OO00O0O0O0O .__O00OOO0O00O000000 [O0O00OO0000OO0O00 ]]=="1":#line:240
                    return #line:241
                else :#line:242
                    O00OO0OO00O0O0O0O .__O0O0O0O00O00O0OOO [O00OO0OO00O0O0O0O .__O00OOO0O00O000000 [O0O00OO0000OO0O00 ]]="1"#line:243
            elif O0O00OO0000OO0O00 in O00OO0OO00O0O0O0O .__OO0OO0OO00OO000O0 :#line:246
                O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO =['00','00','00','00','00','00']#line:247
                O00OO0OO00O0O0O0O .__O0O0O0O00O00O0OOO [6 ]="1"#line:248
                O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO [0 ]=O00OO0OO00O0O0O0O .__OO0OO0OO00OO000O0 [O0O00OO0000OO0O00 ]#line:249
            O00OO0OO00O0O0O0O .__O0OO0O0O0OO000OOO =O00OO0OO00O0O0O0O .__OOOO0000OOO00000O (''.join (O00OO0OO00O0O0O0O .__O0O0O0O00O00O0OOO ))#line:252
            O00O0O00O00OO000O =O00OO0OO00O0O0O0O .__OO0O00000000OO000 (O00OO0OO00O0O0O0O .__O000O0O0OO0000OO0 +O00OO0OO00O0O0O0O .__O0OO0O0O0OO000OOO +O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO )#line:255
            O00OO0OO00O0O0O0O .__OOO0000OO00OO000O =''.join (O00OO0OO00O0O0O0O .__O000O0O0OO0000OO0 )#line:258
            O00OO0OO00O0O0O0O .__O0O0OOO0OO0O0O00O =O00OO0OO00O0O0O0O .__O0OO0O0O0OO000OOO [0 ]#line:259
            O00OO0OO00O0O0O0O .__OOOOO000OOOOO00O0 =''.join (O00OO0OO00O0O0O0O .__O00OO00O00O00O0OO )#line:260
            OOOOOO00OOO0OO000 =O00OO0OO00O0O0O0O .__OOO0000OO00OO000O +O00OO0OO00O0O0O0O .__O0O0OOO0OO0O0O00O +'00'+O00OO0OO00O0O0O0O .__OOOOO000OOOOO00O0 +O00O0O00O00OO000O #line:261
            O00OO0OO00O0O0O0O .__O0OO0OOOO0OOO000O (OOOOOO00OOO0OO000 )#line:264
    def keyUp (O0OOO0OO000O000O0 ,O0O00000O0OOOOOOO ):#line:267
        if O0O00000O0OOOOOOO !='':#line:270
            if O0O00000O0OOOOOOO in O0OOO0OO000O000O0 .__OO00OOOOOO0OOOOOO :#line:271
                for O0OOO0OO0O00000O0 ,O00OO00O00O0O0O00 in enumerate (O0OOO0OO000O000O0 .__O00OO00O00O00O0OO ):#line:273
                    if O00OO00O00O0O0O00 ==O0OOO0OO000O000O0 .__OO00OOOOOO0OOOOOO [O0O00000O0OOOOOOO ]:#line:274
                        O0OOO0OO000O000O0 .__O00OO00O00O00O0OO [O0OOO0OO0O00000O0 ]='00'#line:275
            elif O0O00000O0OOOOOOO in O0OOO0OO000O000O0 .__O00OOO0O00O000000 :#line:277
                if O0OOO0OO000O000O0 .__O0O0O0O00O00O0OOO [O0OOO0OO000O000O0 .__O00OOO0O00O000000 [O0O00000O0OOOOOOO ]]=="0":#line:278
                    return #line:279
                else :#line:280
                    O0OOO0OO000O000O0 .__O0O0O0O00O00O0OOO [O0OOO0OO000O000O0 .__O00OOO0O00O000000 [O0O00000O0OOOOOOO ]]="0"#line:281
                pass #line:282
            elif O0O00000O0OOOOOOO in O0OOO0OO000O000O0 .__OO0OO0OO00OO000O0 :#line:284
                O0OOO0OO000O000O0 .__O00OO00O00O00O0OO =['00','00','00','00','00','00']#line:285
                O0OOO0OO000O000O0 .__O0O0O0O00O00O0OOO [6 ]="0"#line:286
            O0OOO0OO000O000O0 .__O0OO0O0O0OO000OOO =O0OOO0OO000O000O0 .__OOOO0000OOO00000O (''.join (O0OOO0OO000O000O0 .__O0O0O0O00O00O0OOO ))#line:289
            O0OO0000OO000OO0O =O0OOO0OO000O000O0 .__OO0O00000000OO000 (O0OOO0OO000O000O0 .__O000O0O0OO0000OO0 +O0OOO0OO000O000O0 .__O0OO0O0O0OO000OOO +O0OOO0OO000O000O0 .__O00OO00O00O00O0OO )#line:292
            O0OOO0OO000O000O0 .__OOO0000OO00OO000O =''.join (O0OOO0OO000O000O0 .__O000O0O0OO0000OO0 )#line:295
            O0OOO0OO000O000O0 .__O0O0OOO0OO0O0O00O =O0OOO0OO000O000O0 .__O0OO0O0O0OO000OOO [0 ]#line:296
            O0OOO0OO000O000O0 .__OOOOO000OOOOO00O0 =''.join (O0OOO0OO000O000O0 .__O00OO00O00O00O0OO )#line:297
            OO000OOOOOO0OOOOO =O0OOO0OO000O000O0 .__OOO0000OO00OO000O +O0OOO0OO000O000O0 .__O0O0OOO0OO0O0O00O +'00'+O0OOO0OO000O000O0 .__OOOOO000OOOOO00O0 +O0OO0000OO000OO0O #line:298
            O0OOO0OO000O000O0 .__O0OO0OOOO0OOO000O (OO000OOOOOO0OOOOO )#line:301
    def press (O0OO000OOO0OO00OO ,OOO0O000OOO0000OO ):#line:305
        O0OO000OOO0OO00OO .keyDown (OOO0O000OOO0000OO )#line:306
        time .sleep (random .uniform (0.05 ,0.12 ))#line:307
        O0OO000OOO0OO00OO .keyUp (OOO0O000OOO0000OO )#line:308
    def input_keys (O0O0000000O0OOO00 ,O0000O0O0O0OOO000 ):#line:311
        for O00O000O0O00OOO00 in O0000O0O0O0OOO000 :#line:312
            O0O0000000O0OOO00 .press (O00O000O0O00OOO00 )#line:313
    def mouse_keyDown (O00O0000O0O0OO000 ,keyname ='left'):#line:318
        if keyname in O00O0000O0O0OO000 .__OO0OOO000000OO0O0 :#line:320
            O00O0000O0O0OO000 .__OO00OO00OOOO0OOO0 [O00O0000O0O0OO000 .__OO0OOO000000OO0O0 [keyname ]]='1'#line:321
            O00O0000O0O0OO000 .__O00OO0OO0O0O0000O =O00O0000O0O0OO000 .__OOOO0000OOO00000O (''.join (O00O0000O0O0OO000 .__OO00OO00OOOO0OOO0 ))#line:323
            O0000000O0000O0OO =O00O0000O0O0OO000 .__OO0O00000000OO000 (O00O0000O0O0OO000 .__OO00OO0O000OOO00O +O00O0000O0O0OO000 .__O00OO0OO0O0O0000O )#line:326
            O00O0000O0O0OO000 .__O000OO0O0000OO000 =''.join (O00O0000O0O0OO000 .__OO00OO0O000OOO00O )#line:329
            O00O0000O0O0OO000 .__O00OO00000O0OOOOO =O00O0000O0O0OO000 .__O00OO0OO0O0O0000O [0 ]#line:330
            O0000OO00O0O0O0O0 =O00O0000O0O0OO000 .__O000OO0O0000OO000 +O00O0000O0O0OO000 .__O00OO00000O0OOOOO +'000000'+O0000000O0000O0OO #line:331
            O00O0000O0O0OO000 .__O0OO0OOOO0OOO000O (O0000OO00O0O0O0O0 )#line:334
    def mouse_keyUp (O0000O000OOOO00O0 ,keyname ='left'):#line:337
        if keyname in O0000O000OOOO00O0 .__OO0OOO000000OO0O0 :#line:339
            O0000O000OOOO00O0 .__OO00OO00OOOO0OOO0 [O0000O000OOOO00O0 .__OO0OOO000000OO0O0 [keyname ]]='0'#line:340
            O0000O000OOOO00O0 .__O00OO0OO0O0O0000O =O0000O000OOOO00O0 .__OOOO0000OOO00000O (''.join (O0000O000OOOO00O0 .__OO00OO00OOOO0OOO0 ))#line:342
            O0OO0000OO00OO0OO =O0000O000OOOO00O0 .__OO0O00000000OO000 (O0000O000OOOO00O0 .__OO00OO0O000OOO00O +O0000O000OOOO00O0 .__O00OO0OO0O0O0000O )#line:345
            O0000O000OOOO00O0 .__O000OO0O0000OO000 =''.join (O0000O000OOOO00O0 .__OO00OO0O000OOO00O )#line:348
            O0000O000OOOO00O0 .__O00OO00000O0OOOOO =O0000O000OOOO00O0 .__O00OO0OO0O0O0000O [0 ]#line:349
            OOOO0OOOOOO0OOO00 =O0000O000OOOO00O0 .__O000OO0O0000OO000 +O0000O000OOOO00O0 .__O00OO00000O0OOOOO +'000000'+O0OO0000OO00OO0OO #line:350
            O0000O000OOOO00O0 .__O0OO0OOOO0OOO000O (OOOO0OOOOOO0OOO00 )#line:353
    def leftClick (O0OO0OO0OO0O0OOO0 ):#line:356
        O0OO0OO0OO0O0OOO0 .mouse_keyDown ('left')#line:357
        time .sleep (random .uniform (0.05 ,0.12 ))#line:358
        O0OO0OO0OO0O0OOO0 .mouse_keyUp ('left')#line:359
    def rightClick (O0OO0000O000000OO ):#line:362
        O0OO0000O000000OO .mouse_keyDown ('right')#line:363
        time .sleep (random .uniform (0.05 ,0.12 ))#line:364
        O0OO0000O000000OO .mouse_keyUp ('right')#line:365
    def middleClick (OOO000OO00O0OO00O ):#line:368
        OOO000OO00O0OO00O .mouse_keyDown ('middle')#line:369
        time .sleep (random .uniform (0.05 ,0.12 ))#line:370
        OOO000OO00O0OO00O .mouse_keyUp ('middle')#line:371
    def click (OOOO00OO00O0OO0O0 ,keyname ='left'):#line:374
        if keyname =='left':#line:375
            OOOO00OO00O0OO0O0 .leftClick ()#line:376
        elif keyname =='right':#line:377
            OOOO00OO00O0OO0O0 .rightClick ()#line:378
        elif keyname =='middle':#line:379
            OOOO00OO00O0OO0O0 .middleClick ()#line:380
    def doubleClick (O00O0OO0OOOO00O00 ,keyname ='left'):#line:383
        if keyname =='left':#line:384
            O00O0OO0OOOO00O00 .leftClick ()#line:385
            time .sleep (random .uniform (0.05 ,0.12 ))#line:386
            O00O0OO0OOOO00O00 .leftClick ()#line:387
        elif keyname =='right':#line:388
            O00O0OO0OOOO00O00 .rightClick ()#line:389
            time .sleep (random .uniform (0.05 ,0.12 ))#line:390
            O00O0OO0OOOO00O00 .rightClick ()#line:391
        elif keyname =='middle':#line:392
            O00O0OO0OOOO00O00 .middleClick ()#line:393
            time .sleep (random .uniform (0.05 ,0.12 ))#line:394
            O00O0OO0OOOO00O00 .middleClick ()#line:395
    def tripleClick (OOO00OO0OOO00O000 ,keyname ='left'):#line:398
        if keyname =='left':#line:399
            OOO00OO0OOO00O000 .leftClick ()#line:400
            time .sleep (random .uniform (0.05 ,0.12 ))#line:401
            OOO00OO0OOO00O000 .leftClick ()#line:402
            time .sleep (random .uniform (0.05 ,0.12 ))#line:403
            OOO00OO0OOO00O000 .leftClick ()#line:404
        elif keyname =='right':#line:405
            OOO00OO0OOO00O000 .rightClick ()#line:406
            time .sleep (random .uniform (0.05 ,0.12 ))#line:407
            OOO00OO0OOO00O000 .rightClick ()#line:408
            time .sleep (random .uniform (0.05 ,0.12 ))#line:409
            OOO00OO0OOO00O000 .rightClick ()#line:410
        elif keyname =='middle':#line:411
            OOO00OO0OOO00O000 .middleClick ()#line:412
            time .sleep (random .uniform (0.05 ,0.12 ))#line:413
            OOO00OO0OOO00O000 .middleClick ()#line:414
            time .sleep (random .uniform (0.05 ,0.12 ))#line:415
            OOO00OO0OOO00O000 .middleClick ()#line:416
    def scroll (OOO000OO000000O0O ,OOOO0O0000O00OOOO ):#line:421
        try :#line:422
            OOOO0O0000O00OOOO =int (OOOO0O0000O00OOOO )#line:423
            if OOOO0O0000O00OOOO >30 or OOOO0O0000O00OOOO <-30 :#line:425
                print ('输入的滚轮的跨度过大')#line:426
                return #line:427
            OOO000OO000000O0O .__O00OO0OO0O0O0000O =OOO000OO000000O0O .__OOOO0000OOO00000O (''.join (OOO000OO000000O0O .__OO00OO00OOOO0OOO0 ))#line:430
            if OOOO0O0000O00OOOO <0 :#line:432
                OOO00O000000OO0OO ='01'#line:434
                OOOOO0O00O0000O00 =OOO000OO000000O0O .__OO0O00000000OO000 (OOO000OO000000O0O .__OO00OO0O000OOO00O +OOO000OO000000O0O .__O00OO0OO0O0O0000O +['00','00']+[OOO00O000000OO0OO ])#line:436
            else :#line:437
                OOO00O000000OO0OO ='FF'#line:439
                OOOOO0O00O0000O00 =OOO000OO000000O0O .__OO0O00000000OO000 (OOO000OO000000O0O .__OO00OO0O000OOO00O +OOO000OO000000O0O .__O00OO0OO0O0O0000O +['00','00']+[OOO00O000000OO0OO ])#line:441
            OOO000OO000000O0O .__O000OO0O0000OO000 =''.join (OOO000OO000000O0O .__OO00OO0O000OOO00O )#line:452
            OOO000OO000000O0O .__O00OO00000O0OOOOO =OOO000OO000000O0O .__O00OO0OO0O0O0000O [0 ]#line:453
            OOO0O0O0O00O0O0OO =0 #line:456
            for O0OOO0000O0O00OO0 in range (abs (OOOO0O0000O00OOOO )):#line:457
                OOO0O00O00OO00OOO =OOO000OO000000O0O .__O000OO0O0000OO000 +OOO000OO000000O0O .__O00OO00000O0OOOOO +'0000'+OOO00O000000OO0OO +OOOOO0O00O0000O00 #line:459
                OOO000OO000000O0O .__O0OO0OOOO0OOO000O (OOO0O00O00OO00OOO )#line:461
                OOO0O0O0O00O0O0OO =OOO0O0O0O00O0O0OO +1 #line:462
                if OOO0O0O0O00O0O0OO <7 :#line:463
                    time .sleep (random .uniform (0.02 ,0.06 ))#line:464
                else :#line:465
                    time .sleep (random .uniform (0.11 ,0.29 ))#line:466
                    OOO0O0O0O00O0O0OO =0 #line:467
        except Exception as OOOO000OO00O00000 :#line:470
            print ("发送滚轮命令异常,请检测串口连接或者参数")#line:471
    def move_to (OOO000000O0OOO0O0 ,OO0OO000O00OOOOOO ,OO0O000OOOO0O00OO ,O000OOOO0OOOO0O00 ,O0O0000O0OO0O000O ):#line:474
        try :#line:475
            OOO0OO00OO00OO000 =hex ((int (OO0OO000O00OOOOOO )*4096 )//int (O000OOOO0OOOO0O00 ))[2 :]#line:476
            O0000O0O0O0OO00O0 =hex ((int (OO0O000OOOO0O00OO )*4096 )//int (O0O0000O0OO0O000O ))[2 :]#line:477
            if len (OOO0OO00OO00OO000 )==3 :#line:479
                O00O0OOOO0OO0OO0O =[OOO0OO00OO00OO000 [-2 :],'0'+OOO0OO00OO00OO000 [0 :1 ]]#line:480
            elif len (OOO0OO00OO00OO000 )==4 :#line:481
                O00O0OOOO0OO0OO0O =[OOO0OO00OO00OO000 [-2 :],OOO0OO00OO00OO000 [-4 :-2 ]]#line:482
            elif len (OOO0OO00OO00OO000 )==2 :#line:483
                O00O0OOOO0OO0OO0O =[OOO0OO00OO00OO000 [-2 :],'00']#line:484
            else :#line:485
                print ('坐标错误!')#line:486
                return #line:487
            if len (O0000O0O0O0OO00O0 )==3 :#line:489
                O0O00OOOO000O000O =[O0000O0O0O0OO00O0 [-2 :],'0'+O0000O0O0O0OO00O0 [0 :1 ]]#line:490
            elif len (O0000O0O0O0OO00O0 )==4 :#line:491
                O0O00OOOO000O000O =[O0000O0O0O0OO00O0 [-2 :],O0000O0O0O0OO00O0 [-4 :-2 ]]#line:492
            elif len (O0000O0O0O0OO00O0 )==2 :#line:493
                O0O00OOOO000O000O =[O0000O0O0O0OO00O0 [-2 :],'00']#line:494
            else :#line:495
                print ('坐标错误!')#line:496
                return #line:497
            OOO000000O0OOO0O0 .__O00OO0OO0O0O0000O =OOO000000O0OOO0O0 .__OOOO0000OOO00000O (''.join (OOO000000O0OOO0O0 .__OO00OO00OOOO0OOO0 ))#line:500
            O0O00OOO00OOO0OOO =OOO000000O0OOO0O0 .__OO0O00000000OO000 (OOO000000O0OOO0O0 .__OO00OOO0OO0O0O00O +OOO000000O0OOO0O0 .__O00OO0OO0O0O0000O +O00O0OOOO0OO0OO0O +O0O00OOOO000O000O )#line:503
            OOO000000O0OOO0O0 .__OOOOOOO0O000OO0OO =''.join (OOO000000O0OOO0O0 .__OO00OOO0OO0O0O00O )#line:506
            OOO000000O0OOO0O0 .__O00OO00000O0OOOOO =OOO000000O0OOO0O0 .__O00OO0OO0O0O0000O [0 ]#line:507
            O000O0OOO0000OO0O =''.join (O00O0OOOO0OO0OO0O +O0O00OOOO000O000O )#line:508
            OOO00OOO0OOO0O0O0 =OOO000000O0OOO0O0 .__OOOOOOO0O000OO0OO +OOO000000O0OOO0O0 .__O00OO00000O0OOOOO +O000O0OOO0000OO0O +'00'+O0O00OOO00OOO0OOO #line:509
            OOO000000O0OOO0O0 .__O0OO0OOOO0OOO000O (OOO00OOO0OOO0O0O0 )#line:512
        except Exception as O00OO000O00OOO000 :#line:514
            print ('输入分辨率或者坐标错误!')#line:515
        pass #line:517
    def move (OO0000O00O00O000O ,O0OOOOO000O0000OO ,OOOO0O00000OO00OO ):#line:520
        def OOOOOO00000OOOO0O (O0O0OO00OOOO00OO0 ,OOO0OO0OO00OOOO0O ):#line:522
            OO0O0O0000OOO00OO =len (OOO0OO0OO00OOOO0O )-1 #line:523
            O0000O00OOOOO00O0 =np .zeros_like (OOO0OO0OO00OOOO0O [0 ],dtype =float )#line:524
            for OOO000OO0O0O00OO0 ,OO000OO0O0O0000O0 in enumerate (OOO0OO0OO00OOOO0O ):#line:525
                O0000O00OOOOO00O0 +=(np .math .comb (OO0O0O0000OOO00OO ,OOO000OO0O0O00OO0 )*((1 -O0O0OO00OOOO00OO0 )**(OO0O0O0000OOO00OO -OOO000OO0O0O00OO0 ))*(O0O0OO00OOOO00OO0 **OOO000OO0O0O00OO0 )*OO000OO0O0O0000O0 )#line:531
            return O0000O00OOOOO00O0 #line:532
        try :#line:534
            O0OOOOO000O0000OO =int (O0OOOOO000O0000OO )#line:535
            OOOO0O00000OO00OO =int (OOOO0O00000OO00OO )#line:536
            if abs (O0OOOOO000O0000OO )>abs (OOOO0O00000OO00OO ):#line:538
                O00OO00OOO0OOO0OO =abs (O0OOOOO000O0000OO )#line:539
            else :#line:540
                O00OO00OOO0OOO0OO =abs (OOOO0O00000OO00OO )#line:541
            O0OO00OOOOO000O00 =np .array ([0 ,0 ],dtype =float )#line:545
            O000O0O0OOO00O0OO =np .array ([O0OOOOO000O0000OO ,OOOO0O00000OO00OO ],dtype =float )#line:546
            if O0OOOOO000O0000OO ==0 :#line:549
                O000OOO00OO0OOOO0 =random .uniform (-50 ,50 )#line:550
                OO00OOOOO00OO0OO0 =random .uniform (-50 ,50 )#line:551
            else :#line:552
                O000OOO00OO0OOOO0 =random .uniform (O0OOOOO000O0000OO //100 ,O0OOOOO000O0000OO //2 )#line:553
                OO00OOOOO00OO0OO0 =random .uniform (O0OOOOO000O0000OO //100 ,O0OOOOO000O0000OO //2 )#line:554
            if OOOO0O00000OO00OO ==0 :#line:556
                O0000OO0O0O0OOOO0 =random .uniform (-50 ,50 )#line:557
                O0OOOO0O00OOOOO00 =random .uniform (-50 ,50 )#line:558
            else :#line:559
                O0000OO0O0O0OOOO0 =random .uniform (OOOO0O00000OO00OO //100 ,OOOO0O00000OO00OO //2 )#line:560
                O0OOOO0O00OOOOO00 =random .uniform (OOOO0O00000OO00OO //100 ,OOOO0O00000OO00OO //2 )#line:561
            O00OO000OOO0O0OO0 =np .array ([O000OOO00OO0OOOO0 ,O0000OO0O0O0OOOO0 ],dtype =float )#line:563
            OOO0O0O00O00OOOO0 =np .array ([OO00OOOOO00OO0OO0 ,O0OOOO0O00OOOOO00 ],dtype =float )#line:564
            OO0OOOO00OO00OO00 =O00OO00OOO0OOO0OO //8 +random .randint (5 ,10 )#line:567
            OO0O00OOOO00OO000 =np .linspace (0 ,1 ,OO0OOOO00OO00OO00 )#line:568
            O0OOOO00O00OO0000 =[]#line:569
            for OOOOOO000O000O00O in OO0O00OOOO00OO000 :#line:570
                OOO0O0OOO0OOOO0O0 =OOOOOO00000OOOO0O (OOOOOO000O000O00O ,[O0OO00OOOOO000O00 ,O00OO000OOO0O0OO0 ,OOO0O0O00O00OOOO0 ,O000O0O0OOO00O0OO ])#line:571
                O0OOOO00O00OO0000 .append (OOO0O0OOO0OOOO0O0 )#line:572
            O0OOOO00O00OO0000 =np .array (O0OOOO00O00OO0000 ,dtype =int )#line:575
            OO00OO0OO0OOO0O0O =[OO00000O00O00OOO0 [0 ]for OO00000O00O00OOO0 in O0OOOO00O00OO0000 ]#line:578
            OOO0O0OO0O000OO00 =[O0OO00OOO0O0000O0 [1 ]for O0OO00OOO0O0000O0 in O0OOOO00O00OO0000 ]#line:579
            OOO00000OO000OO0O =0 #line:584
            O0OO0O0OOOOO0O0OO =0 #line:585
            for O000O0OOOO000O0OO in range (OO0OOOO00OO00OO00 ):#line:587
                if OO00OO0OO0OOO0O0O [O000O0OOOO000O0OO ]-OOO00000OO000OO0O <0 :#line:593
                    O0OOO0O0OO00OO00O =hex (OO00OO0OO0OOO0O0O [O000O0OOOO000O0OO ]-OOO00000OO000OO0O &0xFF )[2 :].upper ()#line:594
                else :#line:595
                    O0OOO0O0OO00OO00O =hex (OO00OO0OO0OOO0O0O [O000O0OOOO000O0OO ]-OOO00000OO000OO0O )[2 :].zfill (2 ).upper ()#line:596
                if OOO0O0OO0O000OO00 [O000O0OOOO000O0OO ]-O0OO0O0OOOOO0O0OO <0 :#line:598
                    OOO0O0O000O000O00 =hex (OOO0O0OO0O000OO00 [O000O0OOOO000O0OO ]-O0OO0O0OOOOO0O0OO &0xFF )[2 :].upper ()#line:599
                else :#line:600
                    OOO0O0O000O000O00 =hex (OOO0O0OO0O000OO00 [O000O0OOOO000O0OO ]-O0OO0O0OOOOO0O0OO )[2 :].zfill (2 ).upper ()#line:601
                OO0000O00O00O000O .__O00OO0OO0O0O0000O =OO0000O00O00O000O .__OOOO0000OOO00000O (''.join (OO0000O00O00O000O .__OO00OO00OOOO0OOO0 ))#line:606
                OO0000O00O00OO00O =OO0000O00O00O000O .__OO0O00000000OO000 (OO0000O00O00O000O .__OO00OO0O000OOO00O +OO0000O00O00O000O .__O00OO0OO0O0O0000O +[O0OOO0O0OO00OO00O ,OOO0O0O000O000O00 ])#line:609
                OO0000O00O00O000O .__O000OO0O0000OO000 =''.join (OO0000O00O00O000O .__OO00OO0O000OOO00O )#line:612
                OO0000O00O00O000O .__O00OO00000O0OOOOO =OO0000O00O00O000O .__O00OO0OO0O0O0000O [0 ]#line:613
                O00O000O00O0O00OO =''.join ([O0OOO0O0OO00OO00O ,OOO0O0O000O000O00 ])#line:614
                O000OO00000OO000O =OO0000O00O00O000O .__O000OO0O0000OO000 +OO0000O00O00O000O .__O00OO00000O0OOOOO +O00O000O00O0O00OO +'00'+OO0000O00O00OO00O #line:615
                OO0000O00O00O000O .__O0OO0OOOO0OOO000O (O000OO00000OO000O )#line:618
                OOO00000OO000OO0O =OO00OO0OO0OOO0O0O [O000O0OOOO000O0OO ]#line:620
                O0OO0O0OOOOO0O0OO =OOO0O0OO0O000OO00 [O000O0OOOO000O0OO ]#line:621
        except Exception as O000O0OOOOO0O00OO :#line:623
            print ('输入分辨率或者坐标错误!',O000O0OOOOO0O00OO )#line:624

    def fuwei(self):
        self.reset()

    def anxia(self,keyname):
        self.keyDown(keyname)

    def tanqi(self,keyname):
        self.keyUp(keyname)

    def anyixia(self,keyname):
        self.press(keyname)


kk = CH9329('COM4')
#kk = ''


#kk = CH9329('电脑的com口')
#将上面代码取消注释,并填写正确的COM口(例如 COM1 ), 实例化对象
      

# #下面是测试代码
# time.sleep(2)
# #按键测试
# # 键盘单击(小写)
# kk.press('a')
# #键盘单击(大写)
# kk.keyDown('shift')
# kk.press('a')
# kk.keyUp('shift')
# kk.press('A')

#键盘符号输入
# kk.press('#')

#组合输入(粘贴)
# kk.keyDown('ctrl')
# kk.press('c')
# kk.keyUp('ctrl')
# kk.press('right')
# kk.keyDown('ctrl')
# kk.press('v')
# kk.keyUp('ctrl')

#任务管理器
# keyDown('ctrl')
# keyDown('alt')
# press('del')
# keyUp('ctrl')
# keyUp('alt')


#连续字符输入
# kk.input_keys('Hello, World')

#键盘重置
# kk.keyDown('a')
# time.sleep(3)
# kk.reset('key')


#鼠标单击,
# kk.click('left')
# kk.click('right')
# kk.click('middle')

#鼠标双击
# kk.doubleClick()

#鼠标左键按下+拖动
# kk.mouse_keyDown('left')
# kk.move(300,0)
# kk.mouse_keyUp('left')

#鼠标滚轮
# kk.scroll(20)

#鼠标闪现
# kk.move_to(878,712,1920,1080)

#拖动窗口到指定位置
# kk.move_to(71,47,1920,1080)
# kk.mouse_keyDown()
# kk.move_to(423,53,1920,1080)
# kk.mouse_keyUp()

#鼠标相对移动
# kk.move(400,0)

#每次移动随机曲线
# mouse_keyDown('left')
# for i in range(5):
#     kk.move(400,300)
#     time.sleep(1)
#     kk.move(-400,-300)
#     time.sleep(1)
# mouse_keyUp('left')

#拖动窗口移动 300,200
# mouse_keyDown()
# move(300,200)
# mouse_keyUp()