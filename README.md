# OP - Windows 自动化插件

[[GitHub]](https://github.com/WallBreaker2/op)

### 使用 `build.py` 构建项目

#### 准备事项
- **没有安装CMake**
    1. 以**管理员身份**打开 PowerShell。  
    2. 执行：

    ```powershell
    winget install Kitware.CMake --source winget
    ```
    3. 安装完成后关闭 PowerShell，重新打开一个新的 PowerShell 窗口，执行：

    ```powershell
    cmake --version
    ```


默认配置：

- **构建类型**: `Release`
- **生成器**: `vs2022`（Visual Studio 2022）
- **架构**: `x64`

#### 参数说明

- **`-t, --type`**: 构建类型  
  可选：`Debug` / `Release`（默认）/ `RelWithDebInfo`

- **`--vcpkg-root`**: 指定已经存在的 `vcpkg` 根目录。


#### vcpkg 使用说明

python路径是你本地安装的路径

- **已安装 vcpkg 的情况**

  在命令行使用 `--vcpkg-root` 传入路径，例如：

  ```powershell
  python build.py --vcpkg-root "C:\vcpkg" --python64-root "C:\Users\Gavin\AppData\Local\Programs\Python\Python311"
  ```

- **未安装 vcpkg 的情况**

  如果你本机没有装 vcpkg，可以直接在项目根目录运行：

  ```powershell
  python build.py --python64-root "C:\Users\Gavin\AppData\Local\Programs\Python\Python311"
  ```

### SWIG说明

#### 下载 SWIG
- 下载地址：https://sourceforge.net/projects/swig/files/swigwin/
- 选择最新版下载解压后你会得到类似 `D:\swigwin-4.4.1\swig.exe` 的可执行文件

#### 生成命令

swig -python -c++ -outdir ..\cases easyop.i
