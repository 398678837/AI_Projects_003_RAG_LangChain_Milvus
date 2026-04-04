#!/bin/bash

# 检查Homebrew是否安装
if ! command -v brew &> /dev/null; then
    echo "Homebrew未安装，请先安装Homebrew"
    exit 1
fi

# 检查g++-15是否安装
if ! command -v /opt/homebrew/bin/g++-15 &> /dev/null; then
    echo "g++-15未安装，正在安装gcc..."
    brew install gcc
fi

# 编译代码
echo "正在编译代码..."
/opt/homebrew/bin/g++-15 main.cpp -o main -std=c++17 -Wall -Wextra -pedantic

# 检查编译是否成功
if [ $? -eq 0 ]; then
    echo "编译成功"
    echo "运行程序..."
    ./main
else
    echo "编译失败"
    exit 1
fi