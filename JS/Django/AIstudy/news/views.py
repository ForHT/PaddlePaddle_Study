from django.shortcuts import render
import json
from django.http import HttpResponse, JsonResponse

def index(request):
    return render(request, 'news/index.html')


import qianfan

def ask(request):
    question = request.GET.get('question', '')
    model = request.GET.get('model', 'ERNIE-Bot-4')  # 百度模型名示例
    
    # 初始化千幡客户端（需先在百度云控制台获取API Key和Secret Key）
    chat_comp = qianfan.ChatCompletion(
        ak="7uSYZqKPnztAFaIRdg0YqxPu",  # 替换为实际API Key
        sk="88l5syOhZ3ZijuYKn28tUdVnBBBNuBTh"  # 替换为实际Secret Key
    )

    # 构造prompt（保持原有逻辑）
    prompt = f"""
    我需要你帮助我将知识内容拆分为四个学习模块，请按照以下要求：
    1. 每个模块包含"模块主题"和"本模块内容简介"
    2. 内容简介需控制在30个汉字左右
    3. 使用纯JSON数组格式输出
    参考示例：[{{"模块主题": "基础概念", "本模块内容简介": "学习机器学习的基本定义和核心思想"}}]
    需要拆分的知识点是：{question}
    """

    try:
        resp = chat_comp.do(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.1
        )
        
        # 提取原始响应内容
        raw_answer = resp["body"]["result"]
        print("Raw API Response:", raw_answer)

        # 清洗响应内容（关键步骤）
        cleaned_answer = raw_answer.replace('```json', '').replace('```', '').strip()
        
        # 解析JSON
        try:
            modules = json.loads(cleaned_answer)
            return JsonResponse(modules, safe=False)
        except json.JSONDecodeError as e:
            print(f"JSON解析失败: {str(e)}")
            print(f"清洗后内容: {cleaned_answer}")
            return JsonResponse({"error": "API返回格式异常"}, status=500)

    except Exception as e:
        print("API Error:", str(e))
        return JsonResponse({"error": str(e)}, status=500)