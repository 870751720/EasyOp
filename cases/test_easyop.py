import os
import sys


def _ensure_paths() -> str:
    """
    确保当前目录可直接导入 easyop，并让 DLL/扩展模块从同目录解析依赖。

    约定：所有依赖（easyop.py、_easyop.pyd 及其 DLL）都在本文件同目录下，
    不额外添加任何其它搜索路径。
    """
    base_dir = os.path.dirname(os.path.abspath(__file__))

    # 让 `from easyop import ...` 优先命中当前目录下的 easyop.py
    if base_dir not in sys.path:
        sys.path.insert(0, base_dir)

    # 让相对路径与“同目录 DLL”行为更稳定（不引入其它目录）
    try:
        os.chdir(base_dir)
    except OSError:
        pass

    return base_dir




def main():
    base_dir = _ensure_paths()
    # 延迟导入，避免路径未就绪
    from easyop import libop

    op = libop()

    print("=== 基础功能测试开始 ===")

    # 1. 版本号
    try:
        ver = op.Ver()
        print("Ver():", ver)
    except Exception as e:
        print("调用 Ver() 出错：", e)

    # 2. 路径相关
    try:
        ret = op.SetPath(base_dir)
        print("SetPath(base_dir) 返回值:", ret)
        print("GetPath():", op.GetPath())
        print("GetBasePath():", op.GetBasePath())
    except Exception as e:
        print("路径相关接口出错：", e)

    # 3. 当前前台窗口信息
    try:
        hwnd = op.GetForegroundWindow()
        print("GetForegroundWindow():", hwnd)
        if hwnd:
            print("GetWindowTitle(hwnd):", op.GetWindowTitle(hwnd))
            print("GetWindowRect(hwnd):", op.GetWindowRect(hwnd))
    except Exception as e:
        print("窗口相关接口出错：", e)

    # 4. 鼠标位置和取色（不依赖绑定窗口，最容易测试）
    try:
        pos = op.GetCursorPos()
        # SWIG 包装的 GetCursorPos 通常会返回 3 个值（例如 x, y, ret/状态）
        if isinstance(pos, (tuple, list)):
            if len(pos) < 2:
                raise ValueError(f"GetCursorPos() 返回值长度异常: {pos!r}")
            x, y = int(pos[0]), int(pos[1])
        else:
            raise TypeError(f"GetCursorPos() 返回类型异常: {type(pos)!r}, 值: {pos!r}")
        print("GetCursorPos():", pos)
        color = op.GetColor(x, y)
        print(f"GetColor({x}, {y}):", color)
    except Exception as e:
        print("鼠标/取色相关接口出错：", e)

    print("=== 基础功能测试结束 ===")


if __name__ == "__main__":
    main()

