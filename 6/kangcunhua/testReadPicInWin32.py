#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Kang.Cunhua
# @Date:   2015-11-19 13:26:32
# @Last Modified by:   Kang.Cunhua
# @Last Modified time: 2015-11-19 14:59:19
read_data = """GET /2012.jpg HTTP/1.1
Host: 127.0.0.1:9000
Connection: keep-alive
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.93 Safari/537.36
Accept-Encoding: gzip, deflate, sdch
Accept-Language: zh-CN,zh;q=0.8"""
pic_name = read_data.split(" ")[1][1:]
print pic_name
print "Win32环境下，打开文件必须指定'rb'参数，才能读取图片的全部数据"
with file(pic_name, 'rb') as f:
    pic_content = f.read()
    print f
    print ' pic_content:', pic_content.encode('hex')
    length = len(pic_content)

    print length

print 'win32:', "环境下，不加'rb'参数，只读取图片的头文件部分"
with file(pic_name) as f:
    pic_content = f.read()
    print f
    print ' pic_content:', pic_content.encode('hex')
    length = len(pic_content)

    print length


# 2012.jpg
# [Decode error - output not utf-8]
# [Decode error - output not utf-8]

# <open file '2012.jpg', mode 'rb' at 0x016E3910>
# pic_content: ffd8ffe000104a46494600010101006000600000ffdb00430001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101ffdb00430101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101ffc00011080052008203011100021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a161718191a25262728292a3435363738393a434445464748494a535455565758595a636465666768696a737475
# .....省略...
# b9ce3fb7f5fc7a7f498500140050014005001400500140050014005001400500140050014005007ffd9
# 13939
# win32: 环境下，不加'rb'参数，只读取图片的头文件部分
# <open file '2012.jpg', mode 'r' at 0x016E3968>
#  pic_content: ffd8ffe000104a46494600010101006000600000ffdb00430001010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101ffdb00430101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101010101ffc00011080052008203011100021101031101ffc4001f0000010501010101010100000000000000000102030405060708090a0bffc400b5100002010303020403050504040000017d01020300041105122131410613516107227114328191a1082342b1c11552d1f02433627282090a16171819
# 274
# [Finished in 2.2s]