# 05_Static_Generation_静态生成

## 学习目标
- 理解Next.js的静态生成机制
- 掌握getStaticProps和getStaticPaths的使用
- 熟悉静态生成的重新验证功能
- 学会处理动态路由的静态生成

## 知识点总结
1. **基本静态生成**：使用getStaticProps获取数据并生成静态页面
2. **重新验证**：使用revalidate参数实现增量静态再生
3. **动态路由的静态生成**：使用getStaticPaths生成动态路由的静态路径
4. **嵌套动态路由**：处理多层动态路由的静态生成
5. **fallback选项**：控制未生成路径的处理方式

## 参考资料
- [Next.js 静态生成文档](https://nextjs.org/docs/pages/building-your-application/rendering/static-generation)
- [Next.js 增量静态再生文档](https://nextjs.org/docs/pages/building-your-application/data-fetching/incremental-static-regeneration)
