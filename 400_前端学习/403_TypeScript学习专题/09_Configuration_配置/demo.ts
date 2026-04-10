// TypeScript 配置示例

// 1. tsconfig.json 基本配置
/*
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "esModuleInterop": true,
    "forceConsistentCasingInFileNames": true,
    "strict": true,
    "skipLibCheck": true
  }
}
*/

// 2. tsconfig.json 完整配置
/*
{
  "compilerOptions": {
    // 基本配置
    "target": "es2016",
    "module": "commonjs",
    "lib": ["es2016", "dom"],
    "allowJs": true,
    "checkJs": true,
    "jsx": "react-jsx",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "composite": true,
    "incremental": true,
    "tsBuildInfoFile": "./dist/.tsbuildinfo",
    
    // 严格模式
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true,
    
    // 额外检查
    "noUnusedLocals": true,
    "noUnusedParameters": true,
    "noImplicitReturns": true,
    "noFallthroughCasesInSwitch": true,
    "noUncheckedIndexedAccess": true,
    "noImplicitOverride": true,
    "noPropertyAccessFromIndexSignature": true,
    
    // 模块解析
    "moduleResolution": "node",
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"]
    },
    "rootDirs": ["src", "tests"],
    "typeRoots": ["node_modules/@types", "src/types"],
    "types": ["node", "jest"],
    
    // 其他选项
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "forceConsistentCasingInFileNames": true,
    "skipLibCheck": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist", "tests"],
  "references": [{ "path": "./tsconfig.node.json" }]
}
*/

// 3. tsconfig.node.json 配置
/*
{
  "compilerOptions": {
    "composite": true,
    "skipLibCheck": true,
    "module": "ESNext",
    "moduleResolution": "bundler",
    "allowSyntheticDefaultImports": true
  },
  "include": ["vite.config.ts"]
}
*/

// 4. tsconfig.json 用于 React 项目
/*
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "esModuleInterop": true,
    "allowSyntheticDefaultImports": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noFallthroughCasesInSwitch": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "noEmit": true,
    "jsx": "react-jsx"
  },
  "include": ["src"]
}
*/

// 5. tsconfig.json 用于 Next.js 项目
/*
{
  "compilerOptions": {
    "target": "es5",
    "lib": ["dom", "dom.iterable", "esnext"],
    "allowJs": true,
    "skipLibCheck": true,
    "strict": true,
    "forceConsistentCasingInFileNames": true,
    "noEmit": true,
    "esModuleInterop": true,
    "module": "esnext",
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "isolatedModules": true,
    "jsx": "preserve",
    "incremental": true
  },
  "include": ["next-env.d.ts", "**/*.ts", "**/*.tsx"],
  "exclude": ["node_modules"]
}
*/

// 6. tsconfig.json 用于 Node.js 项目
/*
{
  "compilerOptions": {
    "target": "es2016",
    "module": "commonjs",
    "lib": ["es2016"],
    "allowJs": true,
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
*/

// 7. tslint.json 配置
/*
{
  "defaultSeverity": "error",
  "extends": ["tslint:recommended"],
  "jsRules": {},
  "rules": {
    "no-console": false,
    "object-literal-sort-keys": false,
    "member-ordering": false
  },
  "rulesDirectory": []
}
*/

// 8. eslintrc.json 配置
/*
{
  "env": {
    "browser": true,
    "es2021": true,
    "node": true
  },
  "extends": [
    "eslint:recommended",
    "plugin:@typescript-eslint/recommended",
    "plugin:react/recommended"
  ],
  "parser": "@typescript-eslint/parser",
  "parserOptions": {
    "ecmaFeatures": {
      "jsx": true
    },
    "ecmaVersion": 12,
    "sourceType": "module"
  },
  "plugins": [
    "@typescript-eslint",
    "react"
  ],
  "rules": {
    "no-console": "warn",
    "@typescript-eslint/no-explicit-any": "off"
  }
}
*/

// 9. .prettierrc 配置
/*
{
  "semi": true,
  "trailingComma": "all",
  "singleQuote": true,
  "printWidth": 80,
  "tabWidth": 2
}
*/

// 10. package.json 中的脚本
/*
{
  "scripts": {
    "build": "tsc",
    "dev": "ts-node src/index.ts",
    "test": "jest",
    "lint": "eslint src --ext .ts,.tsx",
    "format": "prettier --write src/**/*.ts src/**/*.tsx"
  }
}
*/

// 11. ts-node 配置
// tsconfig.json
/*
{
  "ts-node": {
    "compilerOptions": {
      "module": "commonjs"
    }
  }
}
*/

// 12. 环境变量配置
// .env
/*
NODE_ENV=development
API_URL=http://localhost:3000/api
*/

// 13. 类型声明文件配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "typeRoots": ["node_modules/@types", "src/types"],
    "types": ["node", "jest"]
  }
}
*/

// 14. 路径别名配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "baseUrl": ".",
    "paths": {
      "@/*": ["src/*"],
      "@/components/*": ["src/components/*"],
      "@/utils/*": ["src/utils/*"]
    }
  }
}
*/

// 15. 增量编译配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "incremental": true,
    "tsBuildInfoFile": "./dist/.tsbuildinfo"
  }
}
*/

// 16. 复合项目配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "composite": true
  },
  "references": [
    { "path": "./packages/package1" },
    { "path": "./packages/package2" }
  ]
}
*/

// 17. 模块解析配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "moduleResolution": "node",
    "resolveJsonModule": true,
    "allowSyntheticDefaultImports": true,
    "esModuleInterop": true
  }
}
*/

// 18. 严格模式配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "strict": true,
    "noImplicitAny": true,
    "strictNullChecks": true,
    "strictFunctionTypes": true,
    "strictBindCallApply": true,
    "strictPropertyInitialization": true,
    "noImplicitThis": true,
    "alwaysStrict": true
  }
}
*/

// 19. 输出配置
// tsconfig.json
/*
{
  "compilerOptions": {
    "outDir": "./dist",
    "rootDir": "./src",
    "declaration": true,
    "declarationMap": true,
    "sourceMap": true
  }
}
*/

// 20. 包含和排除配置
// tsconfig.json
/*
{
  "include": ["src/**/*", "tests/**/*"],
  "exclude": ["node_modules", "dist", "build"]
}
*/
