#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音处理基础概念与环境
展示语音处理的基础概念和环境设置
"""

import numpy as np
import matplotlib.pyplot as plt
import sounddevice as sd
import scipy.io.wavfile as wav
import os

# 1. 基础概念介绍
print("=== 语音处理基础概念 ===")
print("语音处理是一门研究如何处理和分析语音信号的学科，包含以下核心概念：")
print("- 语音信号：声波的数字化表示")
print("- 采样率：每秒采样的次数，常见的有8kHz、16kHz、44.1kHz等")
print("- 量化精度：每个采样点的位数，常见的有8位、16位、24位等")
print("- 声道数：单声道、立体声等")
print("- 频谱：语音信号的频率成分分布")
print("- 特征提取：从语音信号中提取有意义的特征")
print("- 语音识别：将语音转换为文本")
print("- 语音合成：将文本转换为语音")
print("- 说话人识别：识别说话人的身份")
print("- 语音增强：提高语音信号的质量")

# 2. 环境检查
print("\n=== 环境检查 ===")
try:
    import sounddevice
    print(f"SoundDevice版本: {sounddevice.__version__}")
except ImportError:
    print("SoundDevice未安装")

try:
    import scipy
    print(f"SciPy版本: {scipy.__version__}")
except ImportError:
    print("SciPy未安装")

try:
    import numpy
    print(f"NumPy版本: {numpy.__version__}")
except ImportError:
    print("NumPy未安装")

try:
    import matplotlib
    print(f"Matplotlib版本: {matplotlib.__version__}")
except ImportError:
    print("Matplotlib未安装")

try:
    import librosa
    print(f"Librosa版本: {librosa.__version__}")
except ImportError:
    print("Librosa未安装")

try:
    import speech_recognition
    print(f"SpeechRecognition版本: {speech_recognition.__version__}")
except ImportError:
    print("SpeechRecognition未安装")

# 3. 生成并播放简单的声音
print("\n=== 生成并播放简单的声音 ===")

# 生成正弦波
def generate_sine_wave(frequency, duration, sample_rate=44100):
    """生成正弦波"""
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    wave = 0.5 * np.sin(2 * np.pi * frequency * t)
    return wave

# 生成不同频率的正弦波
frequencies = [440, 880, 1320, 1760]  # A4, A5, E6, A6
for freq in frequencies:
    print(f"生成 {freq} Hz 的正弦波")
    wave = generate_sine_wave(freq, 1)  # 1秒
    
    # 播放声音
    try:
        sd.play(wave, 44100)
        sd.wait()
    except Exception as e:
        print(f"播放失败: {e}")

# 4. 录制声音
print("\n=== 录制声音 ===")

def record_audio(duration=5, sample_rate=44100):
    """录制音频"""
    print(f"开始录制 {duration} 秒...")
    audio = sd.rec(int(duration * sample_rate), samplerate=sample_rate, channels=1, dtype=np.int16)
    sd.wait()
    print("录制完成")
    return audio

# 录制音频
try:
    recorded_audio = record_audio(3)  # 录制3秒
    # 保存为WAV文件
    wav.write("recorded_audio.wav", 44100, recorded_audio)
    print("录音已保存为 recorded_audio.wav")
except Exception as e:
    print(f"录制失败: {e}")

# 5. 读取和显示音频文件
print("\n=== 读取和显示音频文件 ===")

def plot_audio(audio_file):
    """读取并显示音频文件"""
    try:
        sample_rate, data = wav.read(audio_file)
        print(f"采样率: {sample_rate} Hz")
        print(f"音频长度: {len(data) / sample_rate:.2f} 秒")
        print(f"数据类型: {data.dtype}")
        
        # 绘制波形图
        plt.figure(figsize=(12, 6))
        time = np.linspace(0, len(data) / sample_rate, len(data))
        plt.plot(time, data)
        plt.title("音频波形图")
        plt.xlabel("时间 (秒)")
        plt.ylabel("振幅")
        plt.grid(True)
        plt.tight_layout()
        plt.savefig("audio_waveform.png")
        print("音频波形图已保存为 audio_waveform.png")
        
        return sample_rate, data
    except Exception as e:
        print(f"读取音频文件失败: {e}")
        return None, None

# 读取录制的音频文件
if os.path.exists("recorded_audio.wav"):
    sample_rate, data = plot_audio("recorded_audio.wav")
else:
    print("录制的音频文件不存在，使用示例数据")
    # 生成示例数据
    sample_rate = 44100
    duration = 2
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    data = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4 440Hz
    data = np.int16(data * 32767)
    wav.write("example_audio.wav", sample_rate, data)
    sample_rate, data = plot_audio("example_audio.wav")

# 6. 音频特征提取
print("\n=== 音频特征提取 ===")

def extract_features(audio_data, sample_rate):
    """提取音频特征"""
    # 转换为浮点数
    audio_float = audio_data.astype(np.float32) / 32768.0
    
    # 计算能量
    energy = np.sum(audio_float ** 2)
    print(f"能量: {energy:.4f}")
    
    # 计算零交叉率
    zero_crossings = np.sum(np.abs(np.diff(np.sign(audio_float)))) / 2
    print(f"零交叉率: {zero_crossings:.2f}")
    
    # 计算短时能量
    frame_size = int(sample_rate * 0.02)  # 20ms帧
    hop_size = int(sample_rate * 0.01)  # 10ms步长
    frames = []
    for i in range(0, len(audio_float) - frame_size, hop_size):
        frame = audio_float[i:i+frame_size]
        frame_energy = np.sum(frame ** 2)
        frames.append(frame_energy)
    
    # 绘制短时能量
    plt.figure(figsize=(12, 4))
    time = np.linspace(0, len(audio_data) / sample_rate, len(frames))
    plt.plot(time, frames)
    plt.title("短时能量")
    plt.xlabel("时间 (秒)")
    plt.ylabel("能量")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("short_time_energy.png")
    print("短时能量图已保存为 short_time_energy.png")

if data is not None:
    extract_features(data, sample_rate)

# 7. 音频频谱分析
print("\n=== 音频频谱分析 ===")

def plot_spectrum(audio_data, sample_rate):
    """绘制音频频谱"""
    # 转换为浮点数
    audio_float = audio_data.astype(np.float32) / 32768.0
    
    # 计算FFT
    n_fft = 1024
    freq = np.fft.fftfreq(n_fft, 1/sample_rate)
    fft_result = np.fft.fft(audio_float[:n_fft])
    magnitude = np.abs(fft_result)
    
    # 只取正频率部分
    positive_freq = freq[:n_fft//2]
    positive_magnitude = magnitude[:n_fft//2]
    
    # 绘制频谱
    plt.figure(figsize=(12, 6))
    plt.plot(positive_freq, positive_magnitude)
    plt.title("音频频谱")
    plt.xlabel("频率 (Hz)")
    plt.ylabel("幅度")
    plt.grid(True)
    plt.tight_layout()
    plt.savefig("audio_spectrum.png")
    print("音频频谱图已保存为 audio_spectrum.png")

if data is not None:
    plot_spectrum(data, sample_rate)

# 8. 语音处理的应用场景
print("\n=== 语音处理的应用场景 ===")
print("语音处理在以下领域有广泛应用:")
print("1. 语音识别: 将语音转换为文本，如智能助手、语音输入等")
print("2. 语音合成: 将文本转换为语音，如有声读物、导航系统等")
print("3. 说话人识别: 识别说话人的身份，如语音解锁、安全验证等")
print("4. 语音增强: 提高语音信号的质量，如降噪、回声消除等")
print("5. 情感识别: 识别说话人的情感状态")
print("6. 语音分割: 将连续语音分割为不同的说话人或语音段")
print("7. 语音编码: 压缩语音数据，如电话、语音消息等")
print("8. 音乐信息检索: 基于音频特征检索音乐")

print("\n语音处理基础概念与环境设置示例完成！")
