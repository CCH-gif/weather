import json
import os
from typing import Dict, Any

def get_weather(city: str) -> str:
    """
    获取指定城市的天气信息
    :param city: 城市名称
    :return: JSON格式的天气信息
    """
    # 模拟天气数据
    weather_data = {
        "beijing": {
            "location": "Beijing",
            "temperature": {"current": 32, "low": 26, "high": 35},
            "rain_probability": 10,
            "humidity": 40
        },
        "shenzhen": {
            "location": "Shenzhen",
            "temperature": {"current": 28, "low": 24, "high": 31},
            "rain_probability": 90,
            "humidity": 85
        }
    }

    city_key = city.lower()
    if city_key in weather_data:
        return json.dumps(weather_data[city_key], ensure_ascii=False)
    return json.dumps({"error": "Weather Unavailable"}, ensure_ascii=False)

def decide_umbrella(weather_info: str) -> str:
    """
    根据天气信息决定是否需要带伞
    :param weather_info: JSON格式的天气信息
    :return: 建议字符串
    """
    try:
        weather: Dict[str, Any] = json.loads(weather_info)
        if "error" in weather:
            return "无法获取天气信息，请稍后再试。"
        
        rain_prob = weather["rain_probability"]
        location = weather["location"]
        
        if rain_prob > 50:
            return f"今天{location}的降雨概率为{rain_prob}%，建议带伞。"
        else:
            return f"今天{location}的降雨概率为{rain_prob}%，可以不带伞。"
    except json.JSONDecodeError:
        return "天气信息格式错误"

if __name__ == "__main__":
    # 测试示例
    city = "shenzhen"
    weather_info = get_weather(city)
    advice = decide_umbrella(weather_info)
    print(advice)