# Pic2Gif

## 功能

将指定文件夹下的多张图片（JPG或PNG格式）按照文件名顺序合并为一张指定时间间隔的GIF图片。

## 使用的第三方库

> imageio

## 使用方法

安装[imageio](http://imageio.github.io/)库，具体方法请自行搜索。

``` bash
python main.py [-i image] [-f jpg] [-o out] [-d 0.5]
```

## 参数

- `-i`或`--input`: 图片目录路径。可以为相对路径（如`image`），也可以为绝对路径（如`/Users/ntflc/image`）。默认值为"image"。
- `-f`或`--format`: 图片格式。可以为"jpg"或"png"，但只能指定一种格式。一旦确定了格式，图片目录下其他格式的文件将被忽略、默认值为"jpg"。
- `-o`或`--output`: 输出GIF图片文件名。仅为文件名，不包括后缀名。默认值为"out"。
- `-d`或`--duration`: 两张图片之间的时间间隔。必须为数字，可以为小数。默认值为"0.5"。

## 其他

由于Python自带排序函数sorted()对文件名进行排序时是按照ASCII码顺序的，即对于`1.jpg`、`2.jpg`、`10.jpg`，会排序为`1.jpg`、`10.jpg`、`2.jpg`。为了解决这个问题，这里采用StackOverflow上[这个问题](http://stackoverflow.com/questions/12093940/reading-files-in-a-particular-order-in-python)下[Martijn Pieters](http://stackoverflow.com/users/100297/martijn-pieters)回答的方法：

``` python
def numerical_sort(value):
    numbers = re.compile(r"(\d+)")
    parts = numbers.split(value)
    parts[1::2] = map(int, parts[1::2])
    return parts

file_names = sorted((fn for fn in os.listdir(image_path) if fn.endswith(image_format)), key=numerical_sort)
```
