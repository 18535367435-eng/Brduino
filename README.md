## 项目简介

本项目提供 Brduino (原BCIduino) 脑电放大器的驱动部署、设备连接及基于 Processing 的实时脑电数据可视化解决方案，适用于脑电信号采集与实时分析场景。

## 环境准备

### 硬件要求

-   电脑（Windows 系统）
-   Brduino (原BCIduino) 脑电放大器
-   蓝牙适配器（电脑内置或外置）

### 软件资源

-   Processing 3.5.3 安装包及补丁
-   Brduino (原BCIduino) 放大器资料压缩包（含 OpenBCI Hub 驱动、GUI 可视化程序）
-   配套 libraries 压缩包（Processing 依赖库）

## Processing 安装与配置

### 1. 安装 Processing 主程序

1.  解压 Processing 安装包，进入路径：`D:\新建文件夹\processing3.5.3安装包补丁包\processing-3.5.3`；
2.  找到并运行  `processing.exe`（文件大小 613KB），按照指引完成安装；
3.  启动 Processing 程序后**立即关闭**，系统会自动在 C 盘文档文件夹下生成  `processing`  文件夹，该文件夹内包含  `libraries`  子文件夹。

### 2. 配置依赖库

1.  进入系统文档目录：`C:\文档\Processing\`，找到自动生成的  `libraries`  文件夹；
2.  解压网盘下载的  `libraries.zip`  压缩包（文件大小 34,765KB）；
3.  将解压后的**所有文件夹**原封不动复制到  `C:\文档\Processing\libraries`  中，完成依赖库配置。

## BCIduino 放大器资料部署

1.  解压  `Brduino (原BCIduino) 放大器资料.zip`  到常用目录（示例路径：`D:\新建文件夹\BCIduino资料\openbci`）；
2.  解压后目录包含 3 个核心文件夹，功能如下：
    -   `1`：存储 OpenBCI Hub 驱动程序（作为放大器驱动使用）；
    -   `OpenBCI GUI`：存储 Processing 可视化源码文件；
    -   `pylsl-master1`：存储 LSL 数据传输协议依赖库。

## 设备连接流程

### 1. 蓝牙配对

1.  打开电脑蓝牙设置（路径：系统设置 > 蓝牙和其他设备）；
2.  开启 Brduino (原BCIduino) 放大器，设备会以  `Brduino (X03)`  或  `BUAAWYZ`  为名出现在蓝牙设备列表中；
3.  点击设备名称进行配对，**无需输入密码**，等待配对成功即可。

### 2. 查找 COM 端口

1.  配对成功后，进入「蓝牙设置 > 更多蓝牙选项 > 硬件 > COM 端口」；
2.  记录 Brduino (原BCIduino) 对应的**传出端口**（示例：`COM4`，名称显示为  `BCIduino-0003'RFCOM'`），传入端口（如  `COM3`）无需关注，仅需使用传出端口进行后续连接。

## 实时脑电可视化操作

### 1. 启动放大器驱动

1.  进入路径：`D:\新建文件夹\BCIduino资料\openbci\1\OpenBCIHub`；
2.  找到并双击  `OpenBCIHub.exe`（文件大小 978KB），启动驱动程序（无需安装，运行后在后台驻留）；
    -   注意：同目录下的  `ffmpeg.dll`、`libEGL.dll`、`msvcp140.dll`  等为驱动依赖文件，请勿删除或移动。

### 2. 打开可视化程序

1.  进入路径：`D:\新建文件夹\BCIduino资料\openbci\OpenBCI GUI`；
2.  找到  `OpenBCI_GUI.pde`  文件（文件大小 57KB），双击该文件会自动用 Processing 打开；
    -   注意：该目录包含 57 个相关源码文件（如  `Interactivity.pde`、`InterfaceSerial.pde`  等），请勿修改文件名或路径。

### 3. 配置并启动数据采集

1.  在 Processing 中打开  `OpenBCI_GUI.pde`  后，点击顶部菜单栏「运行」按钮（或按快捷键 Ctrl+R）；
2.  在弹出的 GUI 控制面板中配置参数：
    -   **DATA SOURCE**：选择  `LIVE (from Cyton)`；
    -   **TRANSFER PROTOCOL**：选择  `Serial (from Dongle)`；
    -   **SERIAL/COM PORT**：选择前文记录的 COM 端口（示例：`COM4`）；
    -   其他参数默认：8 通道（8 CHANNELS）、500Hz 采样率（500Hz）、不写入 SD 卡；
3.  点击  `START SYSTEM`  开始采集，面板会实时显示脑电信号波形、FFT 频谱及加速度数据（X/Y/Z 轴）；
4.  采集数据会自动保存至  `SavedData`  目录，文件名格式为  `OpenBCI-RAW-YYYY-MM-DD_HH-MM-SS.txt`。

## 常见问题

1.  **Processing 无法打开 OpenBCI_GUI.pde？**
    
    -   检查 Processing 版本是否为 3.5.3（需匹配源码兼容性）；
    -   确认  `libraries`  依赖库已正确复制到  `C:\文档\Processing\libraries`  目录。
2.  **蓝牙配对成功但找不到 COM 端口？**
    
    -   重新启动 Brduino (原BCIduino) 放大器和电脑蓝牙；
    -   检查放大器是否处于正常工作状态（确保电源充足）。
3.  **GUI 显示无数据输入？**
    
    -   确认  `OpenBCIHub.exe`  已启动（驱动未运行会导致设备无法通信）；
    -   检查 COM 端口选择是否正确（必须选择传出端口）；
    -   重启 Processing 并重新点击「运行」按钮。
4.  **波形显示异常（如帧率过低）？**
    
    -   降低采样率（如从 1000Hz 调整为 500Hz）；
    -   关闭电脑中其他占用系统资源的程序，保证运行性能。

## 版本信息

-   Processing 版本：3.5.3
-   Brduino (原BCIduino) 放大器驱动版本：OpenBCIHub 2018-11-06
-   最后更新日期：2023-05-05

## 注意事项

1.  所有文件路径可自定义，但需保证文件结构完整（尤其是依赖库和驱动文件）；
2.  驱动程序  `OpenBCIHub.exe`  必须在启动 GUI 前运行，否则无法建立设备通信；
3.  数据采集过程中，请勿关闭 Processing 或驱动程序，避免采集中断；
4.  采集数据默认保存为 TXT 格式，可后续导入 MATLAB、Python 等工具进行离线分析。


> Written with [StackEdit](https://stackedit.io/).
