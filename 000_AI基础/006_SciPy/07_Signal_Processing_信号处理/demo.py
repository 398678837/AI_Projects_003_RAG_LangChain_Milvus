#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
SciPy信号处理
展示SciPy的信号处理功能
"""

import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

# 1. 信号生成
print("=== 信号生成 ===")

# 生成时间序列
t = np.linspace(0, 1, 1000)

# 生成正弦信号
freq1 = 5  # 5 Hz
freq2 = 20  # 20 Hz
signal1 = np.sin(2 * np.pi * freq1 * t)
signal2 = np.sin(2 * np.pi * freq2 * t)

# 组合信号
combined_signal = signal1 + 0.5 * signal2

# 添加噪声
noise = np.random.normal(0, 0.2, size=len(t))
noisy_signal = combined_signal + noise

# 绘制信号
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, signal1)
plt.title('5 Hz 正弦信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 2)
plt.plot(t, signal2)
plt.title('20 Hz 正弦信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 3)
plt.plot(t, combined_signal)
plt.title('组合信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 4)
plt.plot(t, noisy_signal)
plt.title('带噪声的信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.tight_layout()
plt.savefig('signal_generation.png')
print("信号生成图已保存为 signal_generation.png")

# 2. 滤波
print("\n=== 滤波 ===")

# 设计低通滤波器
fs = 1000  # 采样频率
cutoff = 10  # 截止频率
order = 4  # 滤波器阶数

# 设计巴特沃斯滤波器
b, a = signal.butter(order, cutoff, btype='low', fs=fs)

# 应用滤波器
filtered_signal = signal.filtfilt(b, a, noisy_signal)

# 绘制滤波结果
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='带噪声的信号')
plt.plot(t, filtered_signal, 'r-', label='滤波后的信号')
plt.plot(t, combined_signal, 'g--', label='原始组合信号')
plt.title('低通滤波示例')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')
plt.legend()
plt.grid(True)
plt.savefig('filtering.png')
print("滤波结果图已保存为 filtering.png")

# 3. 频谱分析
print("\n=== 频谱分析 ===")

# 计算FFT
from scipy.fft import fft, fftfreq

# 原始信号的FFT
yf = fft(noisy_signal)
xf = fftfreq(len(t), 1/fs)

# 滤波后信号的FFT
yf_filtered = fft(filtered_signal)

# 绘制频谱
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(xf[:len(xf)//2], np.abs(yf)[:len(yf)//2])
plt.title('原始信号的频谱')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')

plt.subplot(2, 1, 2)
plt.plot(xf[:len(xf)//2], np.abs(yf_filtered)[:len(yf_filtered)//2])
plt.title('滤波后信号的频谱')
plt.xlabel('频率 (Hz)')
plt.ylabel('幅度')

plt.tight_layout()
plt.savefig('spectrum_analysis.png')
print("频谱分析图已保存为 spectrum_analysis.png")

# 4. 信号检测
print("\n=== 信号检测 ===")

# 生成含有脉冲的信号
pulse_signal = np.zeros_like(t)
pulse_signal[200:250] = 1  # 在200-250样本处添加脉冲

# 检测脉冲
peaks, _ = signal.find_peaks(pulse_signal, height=0.5)

# 绘制脉冲检测结果
plt.figure(figsize=(10, 6))
plt.plot(t, pulse_signal)
plt.plot(t[peaks], pulse_signal[peaks], 'ro', label='检测到的脉冲')
plt.title('脉冲检测示例')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')
plt.legend()
plt.grid(True)
plt.savefig('pulse_detection.png')
print("脉冲检测图已保存为 pulse_detection.png")

# 5. 相关分析
print("\n=== 相关分析 ===")

# 生成参考信号
reference = np.sin(2 * np.pi * freq1 * t)

# 计算互相关
correlation = signal.correlate(noisy_signal, reference, mode='same')

# 绘制相关结果
plt.figure(figsize=(10, 6))
plt.plot(t, correlation)
plt.title('互相关分析')
plt.xlabel('时间 (s)')
plt.ylabel('相关系数')
plt.grid(True)
plt.savefig('correlation_analysis.png')
print("相关分析图已保存为 correlation_analysis.png")

# 6. 信号变换
print("\n=== 信号变换 ===")

# 小波变换
import pywt

# 执行小波变换
coeffs = pywt.wavedec(noisy_signal, 'db4', level=3)

# 重构信号
reconstructed_signal = pywt.waverec(coeffs, 'db4')

# 绘制小波变换结果
plt.figure(figsize=(10, 6))
plt.plot(t, noisy_signal, label='原始信号')
plt.plot(t, reconstructed_signal[:len(t)], 'r-', label='重构信号')
plt.title('小波变换示例')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')
plt.legend()
plt.grid(True)
plt.savefig('wavelet_transform.png')
print("小波变换图已保存为 wavelet_transform.png")

# 7. 系统识别
print("\n=== 系统识别 ===")

# 生成输入信号
input_signal = np.random.randn(len(t))

# 定义系统（低通滤波器）
b_sys, a_sys = signal.butter(2, 0.1)

# 生成输出信号
output_signal = signal.lfilter(b_sys, a_sys, input_signal)

# 估计系统频率响应
freq, resp = signal.freqz(b_sys, a_sys)

# 绘制系统频率响应
plt.figure(figsize=(10, 6))
plt.plot(freq / np.pi, 20 * np.log10(np.abs(resp)))
plt.title('系统频率响应')
plt.xlabel('归一化频率')
plt.ylabel('幅度 (dB)')
plt.grid(True)
plt.savefig('system_identification.png')
print("系统识别图已保存为 system_identification.png")

# 8. 窗函数
print("\n=== 窗函数 ===")

# 生成不同的窗函数
window_hanning = np.hanning(len(t))
window_hamming = np.hamming(len(t))
window_blackman = np.blackman(len(t))

# 应用窗函数
windowed_signal = noisy_signal * window_hanning

# 绘制窗函数
plt.figure(figsize=(10, 6))
plt.subplot(2, 1, 1)
plt.plot(t, window_hanning, label='汉宁窗')
plt.plot(t, window_hamming, label='汉明窗')
plt.plot(t, window_blackman, label='布莱克曼窗')
plt.title('窗函数')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')
plt.legend()

plt.subplot(2, 1, 2)
plt.plot(t, noisy_signal, label='原始信号')
plt.plot(t, windowed_signal, 'r-', label='加窗信号')
plt.title('窗函数应用')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')
plt.legend()

plt.tight_layout()
plt.savefig('window_functions.png')
print("窗函数图已保存为 window_functions.png")

# 9. 调制解调
print("\n=== 调制解调 ===")

# 生成调制信号
carrier_freq = 100  # 载波频率
modulated_signal = np.sin(2 * np.pi * carrier_freq * t) * np.sin(2 * np.pi * freq1 * t)

# 解调
demodulated_signal = modulated_signal * np.sin(2 * np.pi * carrier_freq * t)

# 低通滤波解调信号
b_demod, a_demod = signal.butter(2, 15, fs=fs)
demodulated_filtered = signal.filtfilt(b_demod, a_demod, demodulated_signal)

# 绘制调制解调结果
plt.figure(figsize=(12, 8))

plt.subplot(4, 1, 1)
plt.plot(t, np.sin(2 * np.pi * freq1 * t))
plt.title('原始信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 2)
plt.plot(t, np.sin(2 * np.pi * carrier_freq * t))
plt.title('载波信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 3)
plt.plot(t, modulated_signal)
plt.title('调制信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.subplot(4, 1, 4)
plt.plot(t, demodulated_filtered)
plt.title('解调信号')
plt.xlabel('时间 (s)')
plt.ylabel('幅度')

plt.tight_layout()
plt.savefig('modulation_demodulation.png')
print("调制解调图已保存为 modulation_demodulation.png")

print("\nSciPy信号处理示例完成！")
