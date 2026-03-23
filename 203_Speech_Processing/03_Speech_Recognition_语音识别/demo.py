#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音识别
展示语音识别的基本方法
"""

import speech_recognition as sr
import numpy as np
import scipy.io.wavfile as wav
import os

# 1. 基础语音识别
print("=== 基础语音识别 ===")

# 初始化语音识别器
r = sr.Recognizer()

# 录制音频
def record_audio(duration=5, filename="recorded_audio.wav"):
    """录制音频"""
    with sr.Microphone() as source:
        print(f"请说话，开始录制 {duration} 秒...")
        # 调整环境噪声
        r.adjust_for_ambient_noise(source, duration=1)
        # 录制音频
        audio = r.listen(source, timeout=duration)
        print("录制完成")
        
        # 保存音频
        with open(filename, "wb") as f:
            f.write(audio.get_wav_data())
        print(f"录音已保存为 {filename}")
        return audio

# 从文件加载音频
def load_audio_from_file(filename):
    """从文件加载音频"""
    try:
        with sr.AudioFile(filename) as source:
            audio = r.record(source)
        print(f"从文件加载音频: {filename}")
        return audio
    except Exception as e:
        print(f"加载音频文件失败: {e}")
        return None

# 执行语音识别
def recognize_speech(audio, language="zh-CN"):
    """执行语音识别"""
    try:
        print(f"使用Google Speech Recognition进行识别...")
        text = r.recognize_google(audio, language=language)
        print(f"识别结果: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition无法理解音频")
        return None
    except sr.RequestError as e:
        print(f"Google Speech Recognition请求失败: {e}")
        return None

# 测试语音识别
print("\n测试1: 从麦克风录制并识别")
try:
    recorded_audio = record_audio(3)
    recognize_speech(recorded_audio)
except Exception as e:
    print(f"录制失败: {e}")
    print("使用示例音频文件进行测试")

# 测试2: 从文件识别
print("\n测试2: 从文件识别")
# 检查是否存在示例音频文件
if not os.path.exists("example_audio.wav"):
    # 生成示例音频
    sample_rate = 16000
    duration = 2
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4 440Hz
    audio = np.int16(audio * 32767)
    wav.write("example_audio.wav", sample_rate, audio)
    print("生成示例音频文件: example_audio.wav")

# 加载并识别
if os.path.exists("example_audio.wav"):
    audio_from_file = load_audio_from_file("example_audio.wav")
    if audio_from_file:
        recognize_speech(audio_from_file)

# 2. 多语言语音识别
print("\n=== 多语言语音识别 ===")

languages = [
    ("zh-CN", "中文"),
    ("en-US", "英语"),
    ("ja-JP", "日语"),
    ("ko-KR", "韩语")
]

print("支持的语言:")
for lang_code, lang_name in languages:
    print(f"- {lang_name} ({lang_code})")

# 3. 语音识别的应用
print("\n=== 语音识别的应用 ===")

print("语音识别在以下领域有广泛应用:")
print("1. 智能助手: 如Siri、Alexa、小度等")
print("2. 语音输入: 语音转文字，提高输入效率")
print("3. 电话客服: 自动语音识别和处理")
print("4. 会议记录: 自动记录会议内容")
print("5. 字幕生成: 为视频自动生成字幕")
print("6. 无障碍服务: 为视障人士提供帮助")
print("7. 语音搜索: 通过语音进行搜索")
print("8. 智能家居: 语音控制智能家居设备")

# 4. 语音识别的挑战
print("\n=== 语音识别的挑战 ===")

print("语音识别面临的主要挑战:")
print("1. 环境噪声: 背景噪声会影响识别准确率")
print("2. 口音差异: 不同地区的口音会影响识别")
print("3. 语速变化: 语速过快或过慢会影响识别")
print("4. 词汇量: 专业词汇或生僻词汇识别困难")
print("5. 多人对话: 多人同时说话时识别困难")
print("6. 实时性: 实时识别的延迟问题")
print("7. 资源消耗: 高质量识别需要大量计算资源")

# 5. 本地语音识别选项
print("\n=== 本地语音识别选项 ===")

print("除了在线API外，还有以下本地语音识别选项:")
print("1. CMU Sphinx: 开源的语音识别引擎")
print("2. VOSK: 开源的语音识别工具包")
print("3. Whisper: OpenAI开源的语音识别模型")
print("4. Wav2Vec2: Facebook AI的语音识别模型")
print("5. DeepSpeech: Mozilla开源的语音识别引擎")

# 6. 语音识别的未来发展
print("\n=== 语音识别的未来发展 ===")

print("语音识别技术的未来发展趋势:")
print("1. 端到端模型: 直接从语音到文本的端到端模型")
print("2. 多语言支持: 支持更多语言和方言")
print("3. 低资源语言: 为资源较少的语言提供识别支持")
print("4. 个性化识别: 适应特定说话人的语音特征")
print("5. 多模态融合: 结合视觉等其他模态信息")
print("6. 实时低延迟: 实现更低延迟的实时识别")
print("7. 边缘设备部署: 在边缘设备上实现高质量识别")

# 7. 语音识别的评估指标
print("\n=== 语音识别的评估指标 ===")

print("语音识别系统的主要评估指标:")
print("1. 词错率 (WER): 识别错误的词数占总词数的比例")
print("2. 句错率 (SER): 识别错误的句子数占总句子数的比例")
print("3. 准确率 (Accuracy): 正确识别的词数占总词数的比例")
print("4. 召回率 (Recall): 正确识别的词数占实际词数的比例")
print("5. F1分数: 准确率和召回率的调和平均值")
print("6. 实时因子 (RTF): 识别时间与音频长度的比值")

# 8. 语音识别的最佳实践
print("\n=== 语音识别的最佳实践 ===")

print("提高语音识别准确率的最佳实践:")
print("1. 减少背景噪声: 在安静的环境中使用")
print("2. 清晰发音: 说话清晰，语速适中")
print("3. 适应口音: 使用适合自己口音的语言模型")
print("4. 上下文信息: 提供相关的上下文信息")
print("5. 后处理: 对识别结果进行后处理和修正")
print("6. 模型选择: 根据应用场景选择合适的模型")
print("7. 持续学习: 利用用户反馈不断改进模型")

print("\n语音识别示例完成！")
