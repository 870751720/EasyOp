import os
import sys


def _ensure_paths():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    cases_dir = os.path.join(base_dir, "cases")
    dist_release_dir = os.path.join(base_dir, "dist", "Release")

    if cases_dir not in sys.path:
        sys.path.insert(0, cases_dir)

    # 让 Python 能找到 _easyop.pyd 以及其依赖的 DLL
    if hasattr(os, "add_dll_directory"):
        os.add_dll_directory(dist_release_dir)
    else:
        os.environ["PATH"] = dist_release_dir + os.pathsep + os.environ.get("PATH", "")

    # 同时把 dist/Release 放到 sys.path，方便直接 import easyop
    if dist_release_dir not in sys.path:
        sys.path.insert(0, dist_release_dir)

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
        x, y = op.GetCursorPos()
        print("GetCursorPos():", (x, y))
        color = op.GetColor(x, y)
        print(f"GetColor({x}, {y}):", color)
    except Exception as e:
        print("鼠标/取色相关接口出错：", e)

    print("=== 基础功能测试结束 ===")


if __name__ == "__main__":
    main()

