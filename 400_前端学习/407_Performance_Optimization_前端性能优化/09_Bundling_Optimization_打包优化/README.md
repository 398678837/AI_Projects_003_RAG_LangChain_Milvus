# 打包优化

## 什么是打包优化？

打包优化是指通过各种技术和策略，减少打包后文件的大小，提高打包速度，优化代码结构的过程。打包优化是前端性能优化的重要组成部分，直接影响应用的加载速度和用户体验。

## 打包优化的重要性

1. **文件大小**：优化的打包可以减少文件大小，提高加载速度。
2. **加载速度**：更小的文件大小意味着更快的加载速度。
3. **构建速度**：优化的打包配置可以提高构建速度，提升开发效率。
4. **代码质量**：打包优化过程中可以进行代码检查和优化，提高代码质量。

## 打包优化的技术和策略

### 1. 代码分割

- **路由级别分割**：根据路由分割代码，实现按需加载。
- **组件级别分割**：根据组件分割代码，实现按需加载。
- **第三方库分割**：将第三方库单独打包，利用浏览器缓存。

### 2. Tree Shaking

- **ES模块导入**：使用ES模块导入，便于Tree Shaking。
- **副作用标记**：使用`/*#__PURE__*/`标记纯函数，避免被误删。
- **配置优化**：配置打包工具，确保Tree Shaking生效。

### 3. 代码压缩

- **JavaScript压缩**：使用Terser等工具压缩JavaScript代码。
- **CSS压缩**：使用cssnano等工具压缩CSS代码。
- **HTML压缩**：使用html-minifier等工具压缩HTML代码。

### 4. 图片优化

- **图片压缩**：使用imagemin等工具压缩图片。
- **图片格式转换**：将图片转换为WebP等现代格式。
- **图片懒加载**：实现图片懒加载，减少初始加载时间。

### 5. 字体优化

- **字体子集**：只包含使用的字符，减少字体文件大小。
- **字体格式**：使用WOFF2等现代字体格式。
- **字体加载**：使用font-display属性优化字体加载。

### 6. 构建优化

- **缓存配置**：配置构建缓存，提高构建速度。
- **并行构建**：使用多线程并行构建，提高构建速度。
- **增量构建**：只构建修改的文件，提高构建速度。

### 7. 输出优化

- **文件名哈希**：使用内容哈希命名文件，利用浏览器缓存。
- **输出目录结构**：优化输出目录结构，便于管理。
- **资源路径**：配置正确的资源路径，确保资源加载正常。

## 打包优化的最佳实践

### 1. Webpack优化

- **配置SplitChunks**：优化代码分割，减少重复代码。
- **使用ModuleFederation**：实现微前端，共享模块。
- **配置缓存**：使用持久化缓存，提高构建速度。
- **使用SpeedMeasurePlugin**：分析构建速度，找出瓶颈。

### 2. Vite优化

- **使用ES模块**：利用浏览器原生ES模块，提高开发速度。
- **配置缓存**：使用文件系统缓存，提高构建速度。
- **使用插件**：使用官方插件和社区插件，扩展功能。

### 3. Rollup优化

- **配置Tree Shaking**：确保Tree Shaking生效，减少代码体积。
- **使用插件**：使用官方插件和社区插件，扩展功能。
- **输出格式**：根据目标环境选择合适的输出格式。

## 示例配置

### 1. Webpack配置示例

```javascript
// webpack.config.js
const path = require('path');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const MiniCssExtractPlugin = require('mini-css-extract-plugin');
const TerserWebpackPlugin = require('terser-webpack-plugin');
const CssMinimizerPlugin = require('css-minimizer-webpack-plugin');
const { CleanWebpackPlugin } = require('clean-webpack-plugin');

module.exports = {
  mode: 'production',
  entry: {
    main: './src/index.js',
    vendor: ['react', 'react-dom']
  },
  output: {
    path: path.resolve(__dirname, 'dist'),
    filename: '[name].[contenthash].js',
    chunkFilename: '[name].[contenthash].chunk.js'
  },
  optimization: {
    splitChunks: {
      chunks: 'all',
      cacheGroups: {
        vendor: {
          name: 'vendor',
          test: /[\\/]node_modules[\\/]/,
          chunks: 'all'
        }
      }
    },
    minimize: true,
    minimizer: [
      new TerserWebpackPlugin({
        terserOptions: {
          compress: {
            drop_console: true
          }
        }
      }),
      new CssMinimizerPlugin()
    ]
  },
  module: {
    rules: [
      {
        test: /\\.jsx?$/,
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-react'],
            plugins: ['@babel/plugin-transform-runtime']
          }
        }
      },
      {
        test: /\\.css$/,
        use: [MiniCssExtractPlugin.loader, 'css-loader']
      },
      {
        test: /\\.(png|jpg|jpeg|gif|webp)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[contenthash].[ext]',
              outputPath: 'images'
            }
          },
          {
            loader: 'image-webpack-loader',
            options: {
              mozjpeg: {
                quality: 75
              },
              pngquant: {
                quality: [0.65, 0.90]
              }
            }
          }
        ]
      },
      {
        test: /\\.(woff|woff2|eot|ttf|otf)$/,
        use: [
          {
            loader: 'file-loader',
            options: {
              name: '[name].[contenthash].[ext]',
              outputPath: 'fonts'
            }
          }
        ]
      }
    ]
  },
  plugins: [
    new CleanWebpackPlugin(),
    new HtmlWebpackPlugin({
      template: './public/index.html',
      minify: {
        removeComments: true,
        collapseWhitespace: true
      }
    }),
    new MiniCssExtractPlugin({
      filename: '[name].[contenthash].css',
      chunkFilename: '[name].[contenthash].chunk.css'
    })
  ]
};
```

### 2. Vite配置示例

```javascript
// vite.config.js
import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  build: {
    outDir: 'dist',
    assetsDir: 'assets',
    minify: 'terser',
    terserOptions: {
      compress: {
        drop_console: true
      }
    },
    rollupOptions: {
      output: {
        manualChunks: {
          vendor: ['react', 'react-dom'],
          router: ['react-router-dom'],
          ui: ['antd']
        }
      }
    },
    cssCodeSplit: true,
    sourcemap: false
  },
  resolve: {
    alias: {
      '@': resolve(__dirname, 'src')
    }
  }
});
```

### 3. Rollup配置示例

```javascript
// rollup.config.js
import resolve from '@rollup/plugin-node-resolve';
import commonjs from '@rollup/plugin-commonjs';
import babel from '@rollup/plugin-babel';
import terser from '@rollup/plugin-terser';
import css from 'rollup-plugin-css-only';

export default {
  input: 'src/index.js',
  output: [
    {
      file: 'dist/bundle.js',
      format: 'esm',
      sourcemap: false
    },
    {
      file: 'dist/bundle.min.js',
      format: 'esm',
      plugins: [terser()]
    }
  ],
  plugins: [
    resolve(),
    commonjs(),
    babel({
      babelHelpers: 'runtime',
      exclude: 'node_modules/**'
    }),
    css({
      output: 'bundle.css'
    })
  ],
  external: ['react', 'react-dom']
};
```

## 打包优化工具

### 1. 构建工具

- **Webpack**：功能强大的打包工具，支持代码分割、Tree Shaking等。
- **Vite**：基于ES模块的构建工具，开发速度快。
- **Rollup**：专注于库的打包，Tree Shaking效果好。
- **Parcel**：零配置打包工具，简单易用。

### 2. 压缩工具

- **Terser**：JavaScript压缩工具，支持ES6+。
- **cssnano**：CSS压缩工具。
- **html-minifier**：HTML压缩工具。
- **imagemin**：图片压缩工具。

### 3. 分析工具

- **Webpack Bundle Analyzer**：分析Webpack打包结果。
- **Rollup Plugin Visualizer**：分析Rollup打包结果。
- **SpeedMeasurePlugin**：分析Webpack构建速度。
- **Lighthouse**：分析页面性能，包括打包优化建议。

### 4. 其他工具

- **Babel**：JavaScript编译器，支持新特性。
- **PostCSS**：CSS处理工具，支持现代CSS特性。
- **ESLint**：代码检查工具，提高代码质量。
- **Prettier**：代码格式化工具，保持代码风格一致。

## 学习资源

- [Webpack Documentation](https://webpack.js.org/)
- [Vite Documentation](https://vitejs.dev/)
- [Rollup Documentation](https://rollupjs.org/)
- [Tree Shaking](https://webpack.js.org/guides/tree-shaking/)
- [Code Splitting](https://webpack.js.org/guides/code-splitting/)
- [Bundle Optimization](https://web.dev/optimize-your-bundle/)