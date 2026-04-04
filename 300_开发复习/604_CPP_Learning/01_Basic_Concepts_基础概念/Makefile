# Makefile for C++ projects

# 使用Homebrew安装的g++编译器
CXX = /opt/homebrew/bin/g++-15
CXXFLAGS = -std=c++17 -Wall -Wextra -pedantic

# 目标文件
TARGET = main

# 源文件
SRCS = main.cpp

# 默认目标
all: $(TARGET)

# 编译目标
$(TARGET): $(SRCS)
	$(CXX) $(CXXFLAGS) -o $(TARGET) $(SRCS)

# 运行程序
run: $(TARGET)
	./$(TARGET)

# 清理生成的文件
clean:
	rm -f $(TARGET)

# 伪目标
.PHONY: all run clean