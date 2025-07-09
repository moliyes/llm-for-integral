import os
from wolframclient.evaluation import WolframLanguageSession
from wolframclient.language import wl, wlexpr
os.environ["MATHEMATICA_HOME"] = r"D:\Program Files\Wolfram Research\Wolfram\14.2"
KERNEL_PATH = r"D:\Program Files\Wolfram Research\Wolfram\14.2\WolframKernel.exe"
session = WolframLanguageSession(KERNEL_PATH)


def test():
    try:
        session.evaluate(wlexpr("1+1"))
        print("Started Successfully")
    except Exception as e:
        print("BOOMED!")
        print(e)
        exit(0)
test()

def latex_to_mathematica(latex_str):
    """将 LaTeX 转换为 Mathematica 表达式"""
    try:
        # 直接指定内核路径
        kernel_path = r"D:\Program Files\Wolfram Research\Wolfram\14.2\WolframKernel.exe"
        
        with WolframLanguageSession(kernel=kernel_path) as session:
            # 构建转换表达式
            expr = f'ToExpression["{latex_str}", TeXForm]'
            result = session.evaluate(expr)
            return result
    except Exception as e:
        print(f"转换失败: {e}")
        return None

# 测试转换
latex_expr = r"\\frac{\\sin (x)+\\cos (x)}{\\sqrt[3]{\\sin (x)-\\cos (x)}}"
result = latex_to_mathematica(latex_expr)
print("转换结果:", result)
