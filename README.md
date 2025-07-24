# 天气助手 (Weather Agent)

## 功能描述

这是一个简单的天气查询工具，提供以下功能：
1. 查询指定城市的天气信息（模拟数据）
2. 根据降雨概率给出是否带伞的建议

## 使用方法

1. 确保已安装 Python 3.x
2. 运行脚本：
   ```bash
   python weather_agent.py
   ```
3. 默认查询深圳的天气，如需修改城市，请编辑 `weather_agent.py` 文件中的 `city` 变量

## 输出示例

```
今天Shenzhen的降雨概率为90%，建议带伞。
```

## 依赖项

- Python 3.x
- 标准库：`json`, `os`

## 注意事项

- 当前使用模拟天气数据，如需接入真实API，请修改 `get_weather` 函数
- 代码兼容 Windows/Linux/macOS 系统