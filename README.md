# Annhub

Annhub将在线分析工具和分析人员相结合，以应对与日俱增的Android应用安全问题。

## Documentation

##### 安装 yara， yara-python
首先复制文件 `annhub_yara.c` 到 `yara/libyara/modules/`。

修改 `yara/libyara/modules/module_list`，添加 `MODULE(annhub_yara)` 模块：
```text
#ifdef CUCKOO
MODULE(cuckoo)
MODULE(annhub_yara)
#endif
```
修改 `yara/libyara/Makefile.am`，添加 `MODULES += modules/annhub_yara.c`:
```text
if CUCKOO
MODULES += modules/cuckoo.c
MODULES += modules/annhub_yara.c
endif
```
编译安装：
```bash
$ ./modules/tools/yara/configure --enable-cuckoo
$ make
$ sudo make install
$ sudo pip install yara-pythonsssss
```
## Requirements
```text
mysql_connector
```

## LICENSE
```
GPL-3
COPYRIGHT (C) 2017 firmy
```
