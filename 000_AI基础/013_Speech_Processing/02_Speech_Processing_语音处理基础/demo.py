#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音处理基础
展示语音处理的基础操作
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal
import os

# 1. 音频预处理
print("=== 音频预处理 ===")

# 生成示例音频
def generate_example_audio():
    """生成示例音频"""
    sample_rate = 16000
    duration = 2
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # 生成混合信号：440Hz正弦波 + 880Hz正弦波 + 噪声
    signal1 = 0.5 * np.sin(2 * np.pi * 440 * t)  # A4
    signal2 = 0.3 * np.sin(2 * np.pi * 880 * t)  # A5
    noise = 0.1 * np.random.randn(len(t))  # 噪声
    
    audio = signal1 + signal2 + noise
    audio = np.int16(audio * 32767)
    
    wav.write("example_audio.wav", sample_rate, audio)
    print("示例音频已生成: example_audio.wav")
    return sample_rate, audio

# 读取音频文件
def read_audio(file_path):
    """读取音频文件"""
    try:
        sample_rate, data = wav.read(file_path)
        print(f"读取音频文件: {file_path}")
        print(f"采样率: {sample_rate} Hz")
        print(f"音频长度: {len(data) / sample_rate:.2f} 秒")
        print(f"数据类型: {data.dtype}")
        return sample_rate, data
    except Exception as e:
        print(f"读取音频文件失败: {e}")
        return None, None

# 生成或读取音频
sample_rate, audio = read_audio("example_audio.wav")
if sample_rate is None:
    sample_rate, audio = generate_example_audio()

# 2. 音频归一化
print("\n=== 音频归一化 ===")

def normalize_audio(audio):
    """归一化音频"""
    audio_float = audio.astype(np.float32)
    max_amplitude = np.max(np.abs(audio_float))
    if max_amplitude > 0:
        normalized_audio = audio_float / max_amplitude
    else:
        normalized_audio = audio_float
    print(f"音频归一化完成，最大振幅: {max_amplitude}")
    return normalized_audio

normalized_audio = normalize_audio(audio)

# 3. 音频滤波
print("\n=== 音频滤波 ===")

def apply_filter(audio, sample_rate, cutoff_freq, filter_type='lowpass'):
    """应用滤波器"""
    nyquist = 0.5 * sample_rate
    normalized_cutoff = cutoff_freq / nyquist
    
    # 设计滤波器
    b, a = signal.butter(4, normalized_cutoff, btype=filter_type)
    
    # 应用滤波器
    filtered_audio = signal.lfilter(b, a, audio)
    print(f"应用{filter_type}滤波器，截止频率: {cutoff_freq} Hz")
    return filtered_audio

# 应用低通滤波器
lowpass_audio = apply_filter(normalized_audio, sample_rate, 1000, 'lowpass')

# 应用高通滤波器
highpass_audio = apply_filter(normalized_audio, sample_rate, 300, 'highpass')

# 4. 重采样
print("\n=== 重采样 ===")

def resample_audio(audio, original_rate, target_rate):
    """重采样音频"""
    num_samples = int(len(audio) * target_rate / original_rate)
    resampled_audio = signal.resample(audio, num_samples)
    print(f"重采样完成，从 {original_rate} Hz 到 {target_rate} Hz")
    return resampled_audio, target_rate

# 重采样到8kHz
resampled_audio, resampled_rate = resample_audio(normalized_audio, sample_rate, 8000)

# 5. 分帧
print("\n=== 分帧 ===")

def frame_audio(audio, sample_rate, frame_size=0.02, hop_size=0.01):
    """将音频分帧"""
    frame_length = int(frame_size * sample_rate)
    hop_length = int(hop_size * sample_rate)
    
    frames = []
    for i in range(0, len(audio) - frame_length, hop_length):
        frame = audio[i:i+frame_length]
        frames.append(frame)
    
    print(f"分帧完成，帧大小: {frame_size*1000:.0f}ms, 步长: {hop_size*1000:.0f}ms, 总帧数: {len(frames)}")
    return frames, frame_length, hop_length

frames, frame_length, hop_length = frame_audio(normalized_audio, sample_rate)

# 6. 加窗
print("\n=== 加窗 ===")

def apply_window(frames, window_type='hamming'):
    """对帧应用窗函数"""
    if window_type == 'hamming':
        window = np.hamming(len(frames[0]))
    elif window_type == 'hann':
        window = np.hanning(len(frames[0]))
    elif window_type == 'blackman':
        window = np.blackman(len(frames[0]))
    else:
        window = np.ones(len(frames[0]))
    
    windowed_frames = [frame * window for frame in frames]
    print(f"应用{window_type}窗函数")
    return windowed_frames

windowed_frames = apply_window(frames, 'hamming')

# 7. 特征提取
print("\n=== 特征提取 ===")

def extract_mfcc(frames, sample_rate, n_mfcc=13):
    """提取MFCC特征"""
    mfcc_features = []
    frame_length = len(frames[0])
    
    for frame in frames:
        # 计算FFT
        fft_result = np.fft.fft(frame)
        magnitude = np.abs(fft_result)[:frame_length//2]
        
        # 计算梅尔滤波器组
        mel_filters = mel_filter_bank(sample_rate, frame_length, 20)
        
        # 应用梅尔滤波器组
        mel_spectrum = np.dot(mel_filters, magnitude)
        
        # 取对数
        log_mel_spectrum = np.log(mel_spectrum + 1e-10)
        
        # 计算DCT
        mfcc = dct(log_mel_spectrum)[:n_mfcc]
        mfcc_features.append(mfcc)
    
    print(f"MFCC特征提取完成，特征维度: {n_mfcc}")
    return np.array(mfcc_features)

def mel_filter_bank(sample_rate, n_fft, n_filters):
    """创建梅尔滤波器组"""
    low_freq = 0
    high_freq = sample_rate / 2
    
    # 转换到梅尔频率
    low_mel = 2595 * np.log10(1 + low_freq / 700)
    high_mel = 2595 * np.log10(1 + high_freq / 700)
    
    # 生成梅尔频率点
    mel_points = np.linspace(low_mel, high_mel, n_filters + 2)
    
    # 转换回频率
    freq_points = 700 * (10 ** (mel_points / 2595) - 1)
    
    # 计算FFT bin
    bin_points = np.floor((n_fft + 1) * freq_points / sample_rate)
    
    # 创建滤波器组
    filters = np.zeros((n_filters, n_fft // 2))
    for i in range(1, n_filters + 1):
        left = int(bin_points[i-1])
        center = int(bin_points[i])
        right = int(bin_points[i+1])
        
        # 线性上升部分
        for j in range(left, center):
            filters[i-1, j] = (j - left) / (center - left)
        
        # 线性下降部分
        for j in range(center, right):
            filters[i-1, j] = (right - j) / (right - center)
    
    return filters

def dct(signal, n=None):
    """离散余弦变换"""
    if n is None:
        n = len(signal)
    
    result = np.zeros(n)
    for k in range(n):
        sum_val = 0
        for i in range(len(signal)):
            sum_val += signal[i] * np.cos(np.pi * k * (2*i + 1) / (2 * len(signal)))
        result[k] = sum_val
    
    return result

# 提取MFCC特征
try:
    mfcc_features = extract_mfcc(windowed_frames, sample_rate)
    print(f"MFCC特征形状: {mfcc_features.shape}")
except Exception as e:
    print(f"MFCC特征提取失败: {e}")
    print("使用模拟数据进行演示")
    mfcc_features = np.random.rand(len(windowed_frames), 13)

# 8. 特征可视化
print("\n=== 特征可视化 ===")

def plot_features(features, title):
    """可视化特征"""
    plt.figure(figsize=(12, 6))
    plt.imshow(features.T, aspect='auto', origin='lower')
    plt.title(title)
    plt.xlabel("帧")
    plt.ylabel("特征维度")
    plt.colorbar()
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    print(f"{title}可视化已保存为 {title.replace(' ', '_').lower()}.png")

if 'mfcc_features' in locals():
    plot_features(mfcc_features, "MFCC特征")

# 9. 音频波形对比
print("\n=== 音频波形对比 ===")

def plot_waveforms(original, filtered, sample_rate, title):
    """绘制原始和滤波后的波形"""
    plt.figure(figsize=(12, 6))
    time = np.linspace(0, len(original) / sample_rate, len(original))
    
    plt.subplot(2, 1, 1)
    plt.plot(time, original)
    plt.title("原始音频")
    plt.xlabel("时间 (秒)")
    plt.ylabel("振幅")
    plt.grid(True)
    
    plt.subplot(2, 1, 2)
    plt.plot(time, filtered)
    plt.title("滤波后音频")
    plt.xlabel("时间 (秒)")
    plt.ylabel("振幅")
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    print(f"{title}对比图已保存为 {title.replace(' ', '_').lower()}.png")

plot_waveforms(normalized_audio, lowpass_audio, sample_rate, "低通滤波对比")
plot_waveforms(normalized_audio, highpass_audio, sample_rate, "高通滤波对比")

# 10. 语音处理基础技术总结
print("\n=== 语音处理基础技术总结 ===")
print("语音处理的基础技术包括：")
print("1. 音频预处理: 归一化、滤波、重采样等")
print("2. 分帧和加窗: 将连续音频分割为帧并应用窗函数")
print("3. 特征提取: 提取MFCC、梅尔频谱等特征")
print("4. 频谱分析: 分析音频的频率成分")
print("5. 信号处理: 应用各种信号处理技术")

print("\n语音处理基础示例完成！")
