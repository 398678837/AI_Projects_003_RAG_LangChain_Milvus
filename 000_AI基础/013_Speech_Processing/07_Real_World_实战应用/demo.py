#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音处理实战应用
展示语音处理在实际应用中的使用
"""

import numpy as np
import scipy.io.wavfile as wav
import speech_recognition as sr
import pyttsx3
import os

# 1. 语音助手
print("=== 语音助手 ===")

try:
    # 初始化语音识别器和语音合成引擎
    recognizer = sr.Recognizer()
    engine = pyttsx3.init()
    
    def voice_assistant():
        """简单的语音助手"""
        print("语音助手已启动，说'你好'开始对话，说'退出'结束对话")
        
        while True:
            try:
                # 录制音频
                with sr.Microphone() as source:
                    print("\n请说话...")
                    recognizer.adjust_for_ambient_noise(source, duration=1)
                    audio = recognizer.listen(source, timeout=5)
                
                # 识别语音
                text = recognizer.recognize_google(audio, language="zh-CN")
                print(f"你说: {text}")
                
                # 处理命令
                if "你好" in text:
                    response = "你好！我是你的语音助手，有什么可以帮助你的吗？"
                elif "退出" in text:
                    response = "再见！"
                    engine.say(response)
                    engine.runAndWait()
                    break
                elif "时间" in text:
                    import datetime
                    now = datetime.datetime.now()
                    response = f"现在是 {now.hour} 点 {now.minute} 分"
                elif "天气" in text:
                    response = "今天天气晴朗，温度适宜"
                elif "你是谁" in text:
                    response = "我是一个基于Python的语音助手"
                else:
                    response = f"我听到你说: {text}"
                
                # 合成并播放回应
                print(f"助手: {response}")
                engine.say(response)
                engine.runAndWait()
                
            except sr.UnknownValueError:
                print("抱歉，我没有听懂，请再说一遍")
                engine.say("抱歉，我没有听懂，请再说一遍")
                engine.runAndWait()
            except sr.RequestError as e:
                print(f"语音识别服务出错: {e}")
                break
            except Exception as e:
                print(f"出错: {e}")
                break
    
    # 运行语音助手
    # voice_assistant()  # 注释掉以避免在非交互环境中运行
    print("语音助手示例已准备就绪")
    
except Exception as e:
    print(f"语音助手初始化失败: {e}")
    print("使用模拟数据进行演示")

# 2. 语音转文字
print("\n=== 语音转文字 ===")

def speech_to_text(audio_file):
    """将语音转换为文本"""
    try:
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        
        text = recognizer.recognize_google(audio, language="zh-CN")
        print(f"识别结果: {text}")
        return text
    except Exception as e:
        print(f"语音转文字失败: {e}")
        return None

# 生成示例音频
def generate_sample_audio():
    """生成示例音频"""
    sample_rate = 16000
    duration = 2
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    audio = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 880 * t)
    audio = np.int16(audio * 32767)
    wav.write("sample_audio.wav", sample_rate, audio)
    print("生成示例音频: sample_audio.wav")
    return "sample_audio.wav"

# 测试语音转文字
sample_audio = generate_sample_audio()
# speech_to_text(sample_audio)  # 注释掉以避免在非交互环境中运行
print("语音转文字示例已准备就绪")

# 3. 文本转语音
print("\n=== 文本转语音 ===")

def text_to_speech(text, output_file="output_speech.wav"):
    """将文本转换为语音"""
    try:
        engine = pyttsx3.init()
        engine.save_to_file(text, output_file)
        engine.runAndWait()
        print(f"文本转语音成功，已保存为 {output_file}")
        return output_file
    except Exception as e:
        print(f"文本转语音失败: {e}")
        return None

# 测试文本转语音
test_text = "这是一个文本转语音的示例，用于展示语音处理在实际应用中的使用。"
# text_to_speech(test_text)  # 注释掉以避免在非交互环境中运行
print("文本转语音示例已准备就绪")

# 4. 语音命令控制系统
print("\n=== 语音命令控制系统 ===")

class VoiceControlSystem:
    """简单的语音命令控制系统"""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.commands = {
            "打开": self.open_app,
            "关闭": self.close_app,
            "播放": self.play_music,
            "停止": self.stop_music,
            "音量": self.adjust_volume
        }
    
    def open_app(self, app_name):
        """打开应用"""
        response = f"正在打开{app_name}"
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()
    
    def close_app(self, app_name):
        """关闭应用"""
        response = f"正在关闭{app_name}"
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()
    
    def play_music(self, song_name):
        """播放音乐"""
        response = f"正在播放{song_name}"
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()
    
    def stop_music(self):
        """停止音乐"""
        response = "正在停止音乐"
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()
    
    def adjust_volume(self, level):
        """调整音量"""
        response = f"正在将音量调整到{level}"
        print(response)
        self.engine.say(response)
        self.engine.runAndWait()
    
    def listen_and_execute(self):
        """监听并执行命令"""
        print("语音命令控制系统已启动，请说出命令")
        
        try:
            with sr.Microphone() as source:
                print("\n请说话...")
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                audio = self.recognizer.listen(source, timeout=5)
            
            text = self.recognizer.recognize_google(audio, language="zh-CN")
            print(f"你说: {text}")
            
            # 解析命令
            for command, func in self.commands.items():
                if command in text:
                    # 提取参数
                    parts = text.split(command)
                    if len(parts) > 1:
                        param = parts[1].strip()
                        func(param)
                    else:
                        func()
                    break
            else:
                response = "抱歉，我不理解这个命令"
                print(response)
                self.engine.say(response)
                self.engine.runAndWait()
                
        except Exception as e:
            print(f"出错: {e}")

# 初始化语音命令控制系统
# voice_control = VoiceControlSystem()
# voice_control.listen_and_execute()  # 注释掉以避免在非交互环境中运行
print("语音命令控制系统示例已准备就绪")

# 5. 语音情感分析
print("\n=== 语音情感分析 ===")

def analyze_emotion(audio_file):
    """简单的语音情感分析"""
    try:
        # 读取音频文件
        sample_rate, data = wav.read(audio_file)
        
        # 提取特征
        audio_float = data.astype(np.float32) / 32768.0
        
        # 计算能量
        energy = np.mean(audio_float ** 2)
        
        # 计算零交叉率
        zero_crossings = np.sum(np.abs(np.diff(np.sign(audio_float)))) / (2 * len(audio_float))
        
        # 计算语速（简单模拟）
        speech_rate = zero_crossings * sample_rate
        
        # 简单的情感分类
        if energy > 0.1 and speech_rate > 100:
            emotion = "愤怒"
        elif energy < 0.05 and speech_rate < 80:
            emotion = "悲伤"
        elif energy > 0.08 and speech_rate > 90:
            emotion = "快乐"
        else:
            emotion = "中性"
        
        print(f"音频情感分析结果: {emotion}")
        print(f"能量: {energy:.4f}, 零交叉率: {zero_crossings:.4f}, 语速: {speech_rate:.2f}")
        
        return emotion
    except Exception as e:
        print(f"情感分析失败: {e}")
        return None

# 测试语音情感分析
analyze_emotion(sample_audio)

# 6. 语音识别与翻译
print("\n=== 语音识别与翻译 ===")

def speech_to_translation(audio_file, target_language="en"):
    """语音识别与翻译"""
    try:
        # 语音识别
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file) as source:
            audio = recognizer.record(source)
        
        # 识别中文
        text = recognizer.recognize_google(audio, language="zh-CN")
        print(f"识别结果: {text}")
        
        # 翻译（模拟）
        translations = {
            "你好": "Hello",
            "谢谢": "Thank you",
            "再见": "Goodbye",
            "我爱你": "I love you"
        }
        
        if text in translations:
            translation = translations[text]
        else:
            translation = f"[翻译] {text}"
        
        print(f"翻译结果: {translation}")
        
        # 合成翻译后的语音
        engine = pyttsx3.init()
        engine.say(translation)
        engine.runAndWait()
        
        return translation
    except Exception as e:
        print(f"语音识别与翻译失败: {e}")
        return None

# 测试语音识别与翻译
# speech_to_translation(sample_audio)  # 注释掉以避免在非交互环境中运行
print("语音识别与翻译示例已准备就绪")

# 7. 语音会议记录
print("\n=== 语音会议记录 ===")

def meeting_recording():
    """会议记录"""
    try:
        recognizer = sr.Recognizer()
        print("会议记录已开始，按Ctrl+C结束")
        
        # 录制音频
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration=1)
            print("请开始说话...")
            audio = recognizer.listen(source)
        
        # 保存录音
        with open("meeting_recording.wav", "wb") as f:
            f.write(audio.get_wav_data())
        print("会议录音已保存为 meeting_recording.wav")
        
        # 识别语音
        text = recognizer.recognize_google(audio, language="zh-CN")
        print("会议记录:")
        print(text)
        
        # 保存为文本文件
        with open("meeting_notes.txt", "w", encoding="utf-8") as f:
            f.write(text)
        print("会议记录已保存为 meeting_notes.txt")
        
        return text
    except Exception as e:
        print(f"会议记录失败: {e}")
        return None

# 测试会议记录
# meeting_recording()  # 注释掉以避免在非交互环境中运行
print("语音会议记录示例已准备就绪")

# 8. 语音处理的实际应用总结
print("\n=== 语音处理的实际应用总结 ===")

print("语音处理在以下领域有广泛应用:")
print("1. 智能助手: 如Siri、Alexa、小度等")
print("2. 语音识别: 语音转文字，如会议记录、字幕生成等")
print("3. 语音合成: 文本转语音，如有声读物、导航系统等")
print("4. 语音命令控制: 语音控制设备和应用")
print("5. 语音情感分析: 分析说话人的情感状态")
print("6. 语音翻译: 实时语音翻译")
print("7. 会议记录: 自动记录会议内容")
print("8. 语音增强: 提高语音质量")
print("9. 说话人识别: 身份验证、说话人分离等")
print("10. 语音压缩: 语音数据压缩")

print("\n语音处理实战应用示例完成！")
