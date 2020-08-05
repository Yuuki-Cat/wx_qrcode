# -*- coding: utf-8 -*-
# author Yuuki-Cat
import requests as req
from PIL import Image
from io import BytesIO


str1 =			'''
		$WxxC"0x ($
              cxxxx    #   xu
            Yxxxxxx  n Iz  mxx$
           xxxxxc( }   h$kI   ($
         $xxxxW  -#"    kkk -
         xxxxW           C  #n---
         xxxL               I    p
        $xxx   kkkk#%a&p-      p
        $xxx   kkkkkkkkkkkkkkkk C
        $xxx   &kkkkkkkkkkkkkk  $
         xxx    ffffffmkkkkkk  -
         dxx8    fffffffkkka
          uxx-    nffffffkI   $
           xxx       hmo
            $xWakkoW"    b1\C$
             a$xxxxx     Iw\bp
             $xxxxxxd   hnun
              xxxxW# f       p #  n
              xxxxx          h     "
              xxxxxf p       I
           kkk#xxxxx    nO- f      C
           $k$cxxxxxxW    pxx
              xxxxxxxxxxxxxcd(
            $ xxxxxxxxx$
              nxxxxL
                >p$
            n
             $    $'''
print str1
print 'by xiaohui'
print '\n'
name = raw_input(unicode('请输入你要生成二维码公众号的微信号:','utf-8').encode('gbk'))
img_src = 'http://open.weixin.qq.com/qr/code?username='+name

response = req.get(img_src)
image = Image.open(BytesIO(response.content))
image.show()

