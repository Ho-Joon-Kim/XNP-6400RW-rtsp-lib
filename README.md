라이브러리라고 하기에는 뭣하지만 xnp 시리즈 카메라의 rtsp 라우트가 메뉴얼에 쓰여있지 않아 만들어놓는 아카이브......

rtsp://id:pw@ip:554/profile2/media.smp

```shell
pip install ffmpeg-python
```

``` python
from src/index import xnp_rtsp

test = xnp_rtsp()

#location is optional
test.init("rtsp://id:pw@ip:554/profile2/media.smp", "/location")
test.takeImage()
```