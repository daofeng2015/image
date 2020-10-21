from bilibiliuploader.bilibiliuploader import BilibiliUploader
from bilibiliuploader.core import VideoPart

if __name__ == '__main__':
    uploader = BilibiliUploader()
    
    # 登录
    uploader.login_by_access_token("14243d1782808c04bd17be51f21e17a1")

    # 处理视频文件
    parts = []
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-000.mp4",
        title="p1",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-001.mp4",
        title="p2",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-002.mp4",
        title="p3",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-003.mp4",
        title="p4",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-004.mp4",
        title="p5",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-005.mp4",
        title="p6",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-006.mp4",
        title="p7",
        desc=""
    ))
    parts.append(VideoPart(
        path="/home/df2020/st/download/夏小芫/2020-10-20/夏小芫-2020-10-20-part-007.mp4",
        title="p8",
        desc=""
    ))

    # 上传
    avid, bvid = uploader.upload(
        parts=parts,
        copyright=2,
        title='夏小芫-2020-10-20',
        tid=17,
        tag=",".join(["单机游戏"]),
        desc="斗鱼录像",
        source='douyu.com',
        thread_pool_workers=5,
    )
    
