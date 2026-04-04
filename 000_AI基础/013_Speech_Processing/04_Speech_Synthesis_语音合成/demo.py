#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音合成
展示语音合成的基本方法
"""

import pyttsx3
import os

# 1. 基础语音合成
print("=== 基础语音合成 ===")

try:
    # 初始化语音引擎
    engine = pyttsx3.init()
    print("语音引擎初始化成功")
    
    # 获取可用的语音
    voices = engine.getProperty('voices')
    print("\n可用的语音:")
    for i, voice in enumerate(voices):
        print(f"{i+1}. {voice.name} ({voice.id})")
    
    # 设置语音
    engine.setProperty('voice', voices[0].id)  # 使用第一个语音
    
    # 设置语速
    rate = engine.getProperty('rate')
    print(f"\n当前语速: {rate}")
    engine.setProperty('rate', 150)  # 设置语速为150
    
    # 设置音量
    volume = engine.getProperty('volume')
    print(f"当前音量: {volume}")
    engine.setProperty('volume', 1.0)  # 设置音量为最大
    
    # 合成并播放语音
    text = "你好，这是一个语音合成示例。"
    print(f"\n合成文本: {text}")
    engine.say(text)
    engine.runAndWait()
    
    # 保存语音到文件
    engine.save_to_file(text, "synthesized_speech.wav")
    engine.runAndWait()
    print("语音已保存为 synthesized_speech.wav")
    
    # 测试不同语音
    if len(voices) > 1:
        print("\n使用不同语音合成:")
        for i, voice in enumerate(voices[:2]):  # 测试前两个语音
            engine.setProperty('voice', voice.id)
            engine.say(f"这是使用{voice.name}语音合成的示例。")
            engine.runAndWait()
            
except Exception as e:
    print(f"语音合成失败: {e}")
    print("使用模拟数据进行演示")

# 2. 多语言语音合成
print("\n=== 多语言语音合成 ===")

try:
    if 'engine' in locals():
        # 测试不同语言的合成
        texts = [
            ("zh-CN", "你好，欢迎使用语音合成。"),
            ("en-US", "Hello, welcome to speech synthesis."),
            ("ja-JP", "こんにちは、音声合成へようこそ。"),
            ("ko-KR", "안녕하세요, 음성 합성에 오신 것을 환영합니다.")
        ]
        
        print("多语言语音合成测试:")
        for lang, text in texts:
            print(f"\n{lang}: {text}")
            # 注意：需要安装对应语言的语音包
            try:
                engine.say(text)
                engine.runAndWait()
            except Exception as e:
                print(f"合成失败: {e}")

except Exception as e:
    print(f"多语言合成测试失败: {e}")

# 3. 语音合成的应用
print("\n=== 语音合成的应用 ===")

print("语音合成在以下领域有广泛应用:")
print("1. 有声读物: 将文本转换为语音，方便阅读")
print("2. 导航系统: 提供语音导航指令")
print("3. 智能助手: 如Siri、Alexa等的语音回应")
print("4. 无障碍服务: 为视障人士提供文本转语音服务")
print("5. 教育应用: 语言学习、朗读练习等")
print("6. 电话客服: 自动语音响应系统")
print("7. 游戏和动画: 角色语音生成")
print("8. 多语言翻译: 实时翻译并合成语音")

# 4. 语音合成的技术方法
print("\n=== 语音合成的技术方法 ===")

print("语音合成的主要技术方法:")
print("1. 拼接合成: 拼接预先录制的语音片段")
print("2. 参数合成: 使用语音参数模型生成语音")
print("3. 统计参数合成: 基于统计模型的合成方法")
print("4. 深度学习合成: 使用神经网络生成语音")
print("5. 端到端合成: 直接从文本生成语音的端到端模型")

# 5. 语音合成的评估指标
print("\n=== 语音合成的评估指标 ===")

print("语音合成系统的主要评估指标:")
print("1. 自然度: 合成语音的自然程度")
print("2. 清晰度: 合成语音的清晰可懂程度")
print("3. 表现力: 合成语音的表现力和情感")
print("4. 语速和节奏: 合成语音的语速和节奏是否自然")
print("5. 发音准确性: 合成语音的发音是否准确")
print("6. 实时性: 合成语音的生成速度")

# 6. 语音合成的挑战
print("\n=== 语音合成的挑战 ===")

print("语音合成面临的主要挑战:")
print("1. 自然度: 合成语音往往听起来机械、不自然")
print("2. 情感表达: 难以表达恰当的情感和语调")
print("3. 个性化: 生成具有个人特色的语音")
print("4. 多语言支持: 支持多种语言和方言")
print("5. 实时性: 实时生成高质量语音")
print("6. 资源消耗: 高质量合成需要大量计算资源")

# 7. 语音合成的未来发展
print("\n=== 语音合成的未来发展 ===")

print("语音合成技术的未来发展趋势:")
print("1. 超自然语音: 生成更加自然、流畅的语音")
print("2. 个性化语音: 根据用户需求定制语音风格")
print("3. 多模态合成: 结合视觉等其他模态信息")
print("4. 低资源语言: 为资源较少的语言提供合成支持")
print("5. 边缘设备部署: 在边缘设备上实现高质量合成")
print("6. 情感化合成: 生成具有丰富情感的语音")
print("7. 实时对话: 实现低延迟的实时语音合成")

# 8. 语音合成的最佳实践
print("\n=== 语音合成的最佳实践 ===")

print("使用语音合成的最佳实践:")
print("1. 文本预处理: 对输入文本进行适当的预处理")
print("2. 语音选择: 根据应用场景选择合适的语音")
print("3. 参数调整: 根据需要调整语速、音量等参数")
print("4. 情感匹配: 使合成语音的情感与内容匹配")
print("5. 上下文考虑: 考虑上下文信息，使合成更加自然")
print("6. 用户反馈: 收集用户反馈，不断改进合成效果")
print("7. 多语言支持: 根据目标用户选择合适的语言")

# 9. 其他语音合成库
print("\n=== 其他语音合成库 ===")

print("除了pyttsx3外，还有以下语音合成库:")
print("1. gTTS (Google Text-to-Speech): 使用Google的TTS服务")
print("2. Microsoft Azure Text-to-Speech: 微软的语音合成服务")
print("3. Amazon Polly: 亚马逊的语音合成服务")
print("4. Mozilla TTS:  Mozilla的开源语音合成系统")
print("5. ESPnet-TTS: 基于深度学习的语音合成系统")
print("6. WaveNet: Google的深度学习语音合成模型")
print("7. Tacotron: 端到端的语音合成模型")

print("\n语音合成示例完成！")
