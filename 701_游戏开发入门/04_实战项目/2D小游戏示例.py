#!/usr/bin/env python3
"""
2D小游戏示例 - 简单的贪吃蛇游戏
使用Pygame库实现
"""

import pygame
import random
import sys

# 初始化Pygame
pygame.init()

# 游戏配置
WIDTH, HEIGHT = 800, 600
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# 颜色定义
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# 方向定义
UP = (0, -1)
DOWN = (0, 1)
LEFT = (-1, 0)
RIGHT = (1, 0)

class SnakeGame:
    def __init__(self):
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("贪吃蛇游戏")
        self.clock = pygame.time.Clock()
        self.reset()
    
    def reset(self):
        """重置游戏状态"""
        self.snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
        self.direction = RIGHT
        self.food = self.generate_food()
        self.score = 0
        self.game_over = False
    
    def generate_food(self):
        """生成食物位置"""
        while True:
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            if food not in self.snake:
                return food
    
    def handle_events(self):
        """处理用户输入"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if self.game_over:
                    if event.key == pygame.K_r:
                        self.reset()
                    elif event.key == pygame.K_q:
                        pygame.quit()
                        sys.exit()
                else:
                    if event.key == pygame.K_UP and self.direction != DOWN:
                        self.direction = UP
                    elif event.key == pygame.K_DOWN and self.direction != UP:
                        self.direction = DOWN
                    elif event.key == pygame.K_LEFT and self.direction != RIGHT:
                        self.direction = LEFT
                    elif event.key == pygame.K_RIGHT and self.direction != LEFT:
                        self.direction = RIGHT
    
    def update(self):
        """更新游戏状态"""
        if not self.game_over:
            # 移动蛇头
            head_x, head_y = self.snake[0]
            dir_x, dir_y = self.direction
            new_head = ((head_x + dir_x) % GRID_WIDTH, (head_y + dir_y) % GRID_HEIGHT)
            
            # 检查碰撞
            if new_head in self.snake:
                self.game_over = True
            else:
                self.snake.insert(0, new_head)
                
                # 检查是否吃到食物
                if new_head == self.food:
                    self.score += 10
                    self.food = self.generate_food()
                else:
                    self.snake.pop()
    
    def draw(self):
        """绘制游戏画面"""
        self.screen.fill(BLACK)
        
        # 绘制蛇
        for segment in self.snake:
            x, y = segment
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
            pygame.draw.rect(self.screen, GREEN, rect)
        
        # 绘制食物
        food_x, food_y = self.food
        food_rect = pygame.Rect(food_x * GRID_SIZE, food_y * GRID_SIZE, GRID_SIZE - 1, GRID_SIZE - 1)
        pygame.draw.rect(self.screen, RED, food_rect)
        
        # 绘制分数
        font = pygame.font.Font(None, 36)
        score_text = font.render(f"分数: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))
        
        # 游戏结束界面
        if self.game_over:
            game_over_font = pygame.font.Font(None, 72)
            game_over_text = game_over_font.render("游戏结束", True, RED)
            self.screen.blit(game_over_text, (WIDTH // 2 - 150, HEIGHT // 2 - 50))
            
            restart_text = font.render("按 R 重新开始，Q 退出", True, WHITE)
            self.screen.blit(restart_text, (WIDTH // 2 - 150, HEIGHT // 2 + 50))
        
        pygame.display.flip()
    
    def run(self):
        """游戏主循环"""
        while True:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10)  # 控制游戏帧率

if __name__ == "__main__":
    game = SnakeGame()
    game.run()