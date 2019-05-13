import pymysql
import requests
from bs4 import BeautifulSoup
from mongodb import common
from bson.objectid import ObjectId
baseUrl  = "https://movie.douban.com/top250?start=%d&filter="

def get_movies():
    lists = []  # 存储此页面的电影数据
    for var in range(0,10):
        start = var*25
        url = baseUrl % start   # 拼接爬取链接
        html = requests.get(url)    # requests请求页面内容，由于豆瓣没有限制爬取，所以不用设置伪请求头
        soup = BeautifulSoup(html.content, "html.parser")   # BeautifulSoup解析页面内容
        items = soup.find("ol", "grid_view").find_all("li") # 获取所有的电影内容
        for i in items:
            movie = {}      # 临时存取电影的数据
            movie["rank"] = i.find("em").text   # 电影排行榜
            movie["link"] = i.find("div","pic").find("a").get("href")   # 电影详情页链接
            movie["img_url"]=i.find("div", "pic").find("a").find('img').get("src").split("poster/public/")[1]
            movie["poster"] = i.find("div","pic").find("a").find('img').get("src")  # 电影海报地址
            movie["name"] = i.find("span", "title").text    # 电影名字
            movie["score"] = i.find("span", "rating_num").text  # 电影评分
            a=float(i.find("span", "rating_num").text) / 2.0555
            movie["importance"] =float('%.1f'%a) # 电影评分
            movie["Year"] = (i.find("div", "bd").find("p").text).split("\xa0/\xa0")[0].split("\n                            ")[2] # 年份
            movie["Type"] = (i.find("div", "bd").find("p").text).split("\xa0/\xa0")[2].split(" ")[0]  # 类型
            movie["Countries"] = (i.find("div", "bd").find("p").text).split("\xa0/\xa0")[1]   # 主演
            movie["Director"] = (i.find("div","bd").find("p").text).split("\xa0")[0].split("导演: ") [1]  # 导演
            movie["quote"] = i.find("span", "inq").text if(i.find("span", "inq")) else "" # 某些电影没有点评，没有就设为空
            movie["star"]=True
            lists.append(movie) # 保存到返回数组中
    return lists
# 下载图片
def donwload_poster_url(url):
    res = requests.get(url)
    file_name = str.split(url,'/')[-1]
    file_path = r'C:\Users\hewencheng\Desktop\新建文件夹/' + file_name
    print('download img file_path = ',file_path)
    with open(file_path,'wb') as f:
        f.write(res.content)

def mongo_insert(movie_list):
    coll_name = 'movie_table'
    mongodata=common.conn_mongo(coll_name)
    for val in movie_list:
        mongodata.insert(val)
    print("End")


if __name__ == '__main__':
    movie_list=get_movies()
    mongo_insert(movie_list)
