#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
import argparse
import re
import imageio
import logging

# 全局使用UTF-8编码
reload(sys)
sys.setdefaultencoding('utf-8')


def numerical_sort(value):
    numbers = re.compile(r"(\d+)")
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts


def main():
    # 添加参数-i，为图片目录
    # 添加参数-f，为图片格式
    # 添加参数-o，为输出文件名
    # 添加参数-d，为两张图片之间的时间间隔
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", help="path of images, such as 'image' or '/home/user/image', "
                                              "default: 'image'", default="image")
    parser.add_argument("-f", "--format", help="format of images, such as 'jpg', default: 'jpg'", default="jpg")
    parser.add_argument("-o", "--output", help="output gif file name, such as 'out', default: 'out'", default="out")
    parser.add_argument("-d", "--duration", help="duration, such as '0.5', default: '0.5'", default="0.5")
    args = parser.parse_args()
    image_path = args.input
    image_format = "." + args.format
    output_name = args.output + ".gif"
    try:
        duration = float(args.duration)
    except Exception as e:
        print "Error: duration must be a number"
        logging.error(e)
        sys.exit(1)
    # 判断图片目录是否存在
    if not os.path.exists(image_path):
        print "Error: cannot open %s" % image_path
        sys.exit(2)
    # 判断图片目录是否为文件夹
    if not os.path.isdir(image_path):
        print "Error: %s is not a directory" % image_path
        sys.exit(3)
    # 从图片目录读取指定格式图片，并按照文件名排序
    file_names = sorted((fn for fn in os.listdir(image_path) if fn.endswith(image_format)), key=numerical_sort)
    file_names = [image_path+"/"+fn for fn in file_names]
    # 读取图片，并写入gif文件
    images = []
    for fn in file_names:
        images.append(imageio.imread(fn))
    imageio.mimwrite(output_name, images, duration=duration)


if __name__ == "__main__":
    main()
