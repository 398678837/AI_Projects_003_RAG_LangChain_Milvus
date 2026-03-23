#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
语音增强
展示语音增强的基本方法
"""

import numpy as np
import matplotlib.pyplot as plt
import scipy.io.wavfile as wav
import scipy.signal as signal
import os

# 1. 基础语音增强
print("=== 基础语音增强 ===")

# 生成带噪声的音频
def generate_noisy_audio():
    """生成带噪声的音频"""
    sample_rate = 16000
    duration = 3
    t = np.linspace(0, duration, int(sample_rate * duration), endpoint=False)
    
    # 生成原始语音信号（正弦波模拟）
    speech = 0.5 * np.sin(2 * np.pi * 440 * t) + 0.3 * np.sin(2 * np.pi * 880 * t)
    
    # 生成噪声信号
    noise = 0.2 * np.random.randn(len(t))
    
    # 混合语音和噪声
    noisy_speech = speech + noise
    
    # 归一化
    noisy_speech = noisy_speech / np.max(np.abs(noisy_speech))
    
    # 转换为16位整数
    speech_int = np.int16(speech * 32767)
    noisy_speech_int = np.int16(noisy_speech * 32767)
    
    # 保存文件
    wav.write("clean_speech.wav", sample_rate, speech_int)
    wav.write("noisy_speech.wav", sample_rate, noisy_speech_int)
    
    print("生成带噪声的音频文件:")
    print("- clean_speech.wav: 干净的语音")
    print("- noisy_speech.wav: 带噪声的语音")
    
    return sample_rate, speech, noisy_speech

# 读取音频文件
def read_audio(file_path):
    """读取音频文件"""
    try:
        sample_rate, data = wav.read(file_path)
        # 转换为浮点数
        data = data.astype(np.float32) / 32768.0
        return sample_rate, data
    except Exception as e:
        print(f"读取音频文件失败: {e}")
        return None, None

# 生成或读取音频
sample_rate, clean_speech, noisy_speech = generate_noisy_audio()

# 2. 噪声 reduction
print("\n=== 噪声 reduction ===")

def spectral_subtraction(noisy_speech, sample_rate, frame_size=0.02, hop_size=0.01, alpha=0.9, beta=2):
    """频谱减法降噪"""
    frame_length = int(frame_size * sample_rate)
    hop_length = int(hop_size * sample_rate)
    
    # 分帧
    frames = []
    for i in range(0, len(noisy_speech) - frame_length, hop_length):
        frame = noisy_speech[i:i+frame_length]
        frames.append(frame)
    
    # 应用汉明窗
    window = np.hamming(frame_length)
    windowed_frames = [frame * window for frame in frames]
    
    # 计算噪声功率谱（假设前几帧为纯噪声）
    noise_frames = windowed_frames[:5]
    noise_fft = [np.fft.fft(frame) for frame in noise_frames]
    noise_power = np.mean([np.abs(fft) ** 2 for fft in noise_fft], axis=0)
    
    # 对每一帧应用频谱减法
    enhanced_frames = []
    for frame in windowed_frames:
        # 计算FFT
        fft_result = np.fft.fft(frame)
        power_spec = np.abs(fft_result) ** 2
        
        # 频谱减法
        enhanced_power = np.maximum(power_spec - alpha * noise_power, beta * noise_power)
        
        # 保持相位不变
        enhanced_fft = np.sqrt(enhanced_power) * np.exp(1j * np.angle(fft_result))
        
        # 逆FFT
        enhanced_frame = np.real(np.fft.ifft(enhanced_fft))
        enhanced_frames.append(enhanced_frame)
    
    # 重叠相加
    enhanced_speech = np.zeros(len(noisy_speech))
    for i, frame in enumerate(enhanced_frames):
        start = i * hop_length
        end = start + frame_length
        enhanced_speech[start:end] += frame
    
    # 归一化
    enhanced_speech = enhanced_speech / np.max(np.abs(enhanced_speech))
    
    print("频谱减法降噪完成")
    return enhanced_speech

# 应用频谱减法降噪
enhanced_speech = spectral_subtraction(noisy_speech, sample_rate)

# 保存增强后的音频
enhanced_speech_int = np.int16(enhanced_speech * 32767)
wav.write("enhanced_speech.wav", sample_rate, enhanced_speech_int)
print("增强后的音频已保存为 enhanced_speech.wav")

# 3. 滤波增强
print("\n=== 滤波增强 ===")

def apply_bandpass_filter(audio, sample_rate, lowcut=300, highcut=3400):
    """应用带通滤波器"""
    nyquist = 0.5 * sample_rate
    low = lowcut / nyquist
    high = highcut / nyquist
    
    # 设计带通滤波器
    b, a = signal.butter(4, [low, high], btype='band')
    
    # 应用滤波器
    filtered_audio = signal.lfilter(b, a, audio)
    
    # 归一化
    filtered_audio = filtered_audio / np.max(np.abs(filtered_audio))
    
    print(f"应用带通滤波器，频率范围: {lowcut}-{highcut} Hz")
    return filtered_audio

# 应用带通滤波器
filtered_speech = apply_bandpass_filter(noisy_speech, sample_rate)

# 保存滤波后的音频
filtered_speech_int = np.int16(filtered_speech * 32767)
wav.write("filtered_speech.wav", sample_rate, filtered_speech_int)
print("滤波后的音频已保存为 filtered_speech.wav")

# 4. 维纳滤波
print("\n=== 维纳滤波 ===")

def wiener_filter(noisy_speech, sample_rate, frame_size=0.02, hop_size=0.01):
    """维纳滤波降噪"""
    frame_length = int(frame_size * sample_rate)
    hop_length = int(hop_size * sample_rate)
    
    # 分帧
    frames = []
    for i in range(0, len(noisy_speech) - frame_length, hop_length):
        frame = noisy_speech[i:i+frame_length]
        frames.append(frame)
    
    # 应用汉明窗
    window = np.hamming(frame_length)
    windowed_frames = [frame * window for frame in frames]
    
    # 计算噪声功率谱（假设前几帧为纯噪声）
    noise_frames = windowed_frames[:5]
    noise_fft = [np.fft.fft(frame) for frame in noise_frames]
    noise_power = np.mean([np.abs(fft) ** 2 for fft in noise_fft], axis=0)
    
    # 对每一帧应用维纳滤波
    enhanced_frames = []
    for frame in windowed_frames:
        # 计算FFT
        fft_result = np.fft.fft(frame)
        power_spec = np.abs(fft_result) ** 2
        
        # 维纳滤波
        snr = power_spec / (noise_power + 1e-10)
        wiener_gain = snr / (snr + 1)
        enhanced_fft = wiener_gain * fft_result
        
        # 逆FFT
        enhanced_frame = np.real(np.fft.ifft(enhanced_fft))
        enhanced_frames.append(enhanced_frame)
    
    # 重叠相加
    enhanced_speech = np.zeros(len(noisy_speech))
    for i, frame in enumerate(enhanced_frames):
        start = i * hop_length
        end = start + frame_length
        enhanced_speech[start:end] += frame
    
    # 归一化
    enhanced_speech = enhanced_speech / np.max(np.abs(enhanced_speech))
    
    print("维纳滤波降噪完成")
    return enhanced_speech

# 应用维纳滤波
wiener_enhanced = wiener_filter(noisy_speech, sample_rate)

# 保存维纳滤波后的音频
wiener_enhanced_int = np.int16(wiener_enhanced * 32767)
wav.write("wiener_enhanced.wav", sample_rate, wiener_enhanced_int)
print("维纳滤波后的音频已保存为 wiener_enhanced.wav")

# 5. 语音增强效果评估
print("\n=== 语音增强效果评估 ===")

def calculate_snr(clean, noisy):
    """计算信噪比"""
    signal_power = np.mean(clean ** 2)
    noise_power = np.mean((clean - noisy) ** 2)
    snr = 10 * np.log10(signal_power / noise_power)
    return snr

# 计算各方法的SNR
clean_noisy_snr = calculate_snr(clean_speech, noisy_speech)
spectral_snr = calculate_snr(clean_speech, enhanced_speech)
filtered_snr = calculate_snr(clean_speech, filtered_speech)
wiener_snr = calculate_snr(clean_speech, wiener_enhanced)

print(f"原始带噪声语音 SNR: {clean_noisy_snr:.2f} dB")
print(f"频谱减法增强后 SNR: {spectral_snr:.2f} dB")
print(f"带通滤波增强后 SNR: {filtered_snr:.2f} dB")
print(f"维纳滤波增强后 SNR: {wiener_snr:.2f} dB")

# 6. 语音波形对比
print("\n=== 语音波形对比 ===")

def plot_waveforms(clean, noisy, enhanced, sample_rate, title):
    """绘制原始、带噪声和增强后的波形"""
    plt.figure(figsize=(12, 8))
    time = np.linspace(0, len(clean) / sample_rate, len(clean))
    
    plt.subplot(3, 1, 1)
    plt.plot(time, clean)
    plt.title("干净的语音")
    plt.xlabel("时间 (秒)")
    plt.ylabel("振幅")
    plt.grid(True)
    
    plt.subplot(3, 1, 2)
    plt.plot(time, noisy)
    plt.title("带噪声的语音")
    plt.xlabel("时间 (秒)")
    plt.ylabel("振幅")
    plt.grid(True)
    
    plt.subplot(3, 1, 3)
    plt.plot(time, enhanced)
    plt.title("增强后的语音")
    plt.xlabel("时间 (秒)")
    plt.ylabel("振幅")
    plt.grid(True)
    
    plt.tight_layout()
    plt.savefig(f"{title.replace(' ', '_').lower()}.png")
    print(f"{title}对比图已保存为 {title.replace(' ', '_').lower()}.png")

# 绘制频谱减法增强对比
plot_waveforms(clean_speech, noisy_speech, enhanced_speech, sample_rate, "频谱减法增强对比")

# 绘制维纳滤波增强对比
plot_waveforms(clean_speech, noisy_speech, wiener_enhanced, sample_rate, "维纳滤波增强对比")

# 7. 语音增强的应用
print("\n=== 语音增强的应用 ===")

print("语音增强在以下领域有广泛应用:")
print("1. 语音识别: 提高语音识别系统的准确率")
print("2. 电话通信: 提高通话质量")
print("3. 会议记录: 提高会议记录的清晰度")
print("4. 助听器: 帮助听力障碍人士")
print("5. 视频会议: 提高视频会议的音频质量")
print("6. 安防监控: 提高监控音频的清晰度")
print("7. 语音存储: 提高存储语音的质量")
print("8. 多媒体处理: 提高多媒体内容的音频质量")

# 8. 语音增强的挑战
print("\n=== 语音增强的挑战 ===")

print("语音增强面临的主要挑战:")
print("1. 噪声类型多样: 不同类型的噪声需要不同的处理方法")
print("2. 噪声水平变化: 噪声水平随时间变化")
print("3. 语音失真: 增强过程可能导致语音失真")
print("4. 实时性要求: 许多应用需要实时处理")
print("5. 计算资源限制: 资源受限设备上的处理")
print("6. 多说话人场景: 多人同时说话的处理")
print("7. 混响环境: 混响环境下的处理")

# 9. 语音增强的未来发展
print("\n=== 语音增强的未来发展 ===")

print("语音增强技术的未来发展趋势:")
print("1. 深度学习方法: 使用深度学习模型进行语音增强")
print("2. 端到端模型: 直接从带噪声语音到干净语音的端到端模型")
print("3. 多麦克风阵列: 使用多麦克风阵列进行噪声抑制")
print("4. 自适应方法: 自适应处理不同的噪声环境")
print("5. 多模态融合: 结合视觉等其他模态信息")
print("6. 实时处理: 低延迟的实时语音增强")
print("7. 边缘设备部署: 在边缘设备上实现高质量增强")

print("\n语音增强示例完成！")
