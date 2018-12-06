#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "errrolyan"
# Date: 18-10-16
# Describe = "乐谱xml文件转化未为拼音”

import os,re,sys
import os.path
import xml.etree.ElementTree as ET
import pinyin
from collections import Counter

def coverFiles(sourceDir,  targetDir):
    for file in os.listdir(sourceDir):
        sourceFile = os.path.join(sourceDir,  file)
        targetFile = os.path.join(targetDir,  file)
        if os.path.isfile(sourceFile):
            open(targetFile, "wb").write(open(sourceFile, "rb").read())


def fileread(filepath):
    pathDir = os.listdir(filepath)
    for s in pathDir:
        newDir = os.path.join(filepath, s)
        if os.path.isfile(newDir):
            if os.path.splitext(newDir)[1] == ".xml":
                print(newDir)
                name1 = newDir[13:39]
                tree = ET.parse(newDir)
                root = tree.getroot()
                for text in root.iter('text'):
                    text.text = re.sub(u"[\s.。？?！!;；\/_：,%^*(\"“”《》$\，']|[cdeov123456789al、~@#￥%……&*（））]", '', text.text)
                    new_pinyin = pinyin.get(text.text, format="numerical", delimiter=" ") #  format="strip"  "numerical"
                    print(new_pinyin)
                    text.text = str(new_pinyin)
                    text.set('updated', 'yes')
        print("第" + newDir + "首歌完成！！！")
        tree.write(newDir)

def xml_to_pinyin(xml_in_dir, xml_out_dir):
    coverFiles(xml_in_dir, xml_out_dir)
    fileread(xml_out_dir)

if __name__=="__main__":

    usage = 'Usage: xml_to_Pinyin.py  xml_in_dir  xml_out_dir'
    if len(sys.argv) != 3:
        print(usage)
        exit()
    xmlInPath = sys.argv[1]
    xmlOutPath = sys.argv[2]

    xml_to_pinyin(xmlInPath,xmlOutPath)
    print("完成转换拼音")
