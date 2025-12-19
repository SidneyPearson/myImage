import urllib.request
import os

# 图片下载函数
def download_image(url, save_path):
    try:
        print(f"正在下载: {url}")
        urllib.request.urlretrieve(url, save_path)
        print(f"下载成功: {save_path}")
        return True
    except Exception as e:
        print(f"下载失败: {e}")
        return False

# 图片URL列表
images = [
    {
        "name": "LeBron James",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/25/LeBron_James_%2831944784377%29.jpg/800px-LeBron_James_%2831944784377%29.jpg",
        "save_path": "/Users/chentao/Documents/my_project/image_preview/images/test_image_1.jpg"
    },
    {
        "name": "Kevin Durant",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/30/Kevin_Durant_%2832874759254%29.jpg/800px-Kevin_Durant_%2832874759254%29.jpg",
        "save_path": "/Users/chentao/Documents/my_project/image_preview/images/test_image_2.jpg"
    },
    {
        "name": "Stephen Curry",
        "url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Stephen_Curry_%2839849115094%29.jpg/800px-Stephen_Curry_%2839849115094%29.jpg",
        "save_path": "/Users/chentao/Documents/my_project/image_preview/images/test_image_3.jpg"
    }
]

# 创建images目录（如果不存在）
os.makedirs(os.path.dirname(images[0]["save_path"]), exist_ok=True)

# 下载所有图片
for image in images:
    download_image(image["url"], image["save_path"])

print("所有图片下载完成！")
