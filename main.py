import requests  

urls = [  
    "http://example.com/file1.jpg",  
    "http://example.com/file2.pdf",  
]  

def download_file(url):  
    try:  
        response = requests.get(url)  
        response.raise_for_status() 
        file_name = url.split("/")[-1]  

        with open(file_name, 'wb') as file:  
            file.write(response.content)  
        print(f"فایل {file_name} با موفقیت دانلود شد.")  
    except requests.exceptions.RequestException as e:  
        print(f"خطا در دانلود {url}: {e}")  

for url in urls:  
    download_file(url)
