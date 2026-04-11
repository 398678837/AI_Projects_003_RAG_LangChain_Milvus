# 06_Dependency_Management_依赖管理

## 学习目标
- 理解依赖的类型和版本
- 掌握依赖冲突的解决
- 学会锁定依赖版本
- 了解依赖的安全管理

## 知识点总结
1. **依赖类型**：
   - dependencies：生产依赖
   - devDependencies：开发依赖
   - peerDependencies：同伴依赖
   - optionalDependencies：可选依赖
2. **版本控制**：
   - 语义化版本
   - 版本范围符：^, ~, *, >, >=, <, <=
   - 精确版本
3. **依赖冲突**：
   - 多版本共存
   - peerDependencies 冲突
   - 解决方案
4. **锁定文件**：
   - package-lock.json
   - yarn.lock
   - pnpm-lock.yaml
5. **安全管理**：
   - npm audit
   - dependabot
   - 安全更新

## 参考资料
- [About semantic versioning](https://docs.npmjs.com/about-semantic-versioning)
- [npm audit](https://docs.npmjs.com/cli/v9/commands/npm-audit)
