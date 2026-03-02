from google import genai

# 配置客户端
client = genai.Client(api_key="AIzaSyChPAh1WIx9zLWRFXdnwdwtjvlJeSlaTo8")

# 指定模型名称
response = client.models.generate_content(
    model="gemini-3-pro-preview",
    contents="你好，请列出三个Google Gemini模型的优点",
)
print(response.text)