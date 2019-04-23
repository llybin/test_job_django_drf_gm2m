Test job
-

Django, DRF, celery, generic many-to-many, docker, docker-compose

See test.pdf

[Variant non-generic](https://github.com/llybin/test_job_django_drf_m2m)

File fixtures
-

cp -r base/fixtures/media/* media

Web
-

docker-compose up runserver celery

Admin access: root:root

http://0.0.0.0:8000/admin/
http://0.0.0.0:8000/api/v1/

GET http://0.0.0.0:8000/api/v1/pages/ 200

```
{
    "count": 3,
    "next": "http://127.0.0.1:8000/api/v1/pages/?limit=2&offset=2",
    "previous": null,
    "results": [
        {
            "id": 3,
            "url": "http://127.0.0.1:8000/api/v1/pages/3/",
            "title": "The third page",
            "created_at": "2019-02-25T21:44:54.414000Z",
            "modified_at": "2019-02-25T21:44:54.414000Z"
        },
        {
            "id": 2,
            "url": "http://127.0.0.1:8000/api/v1/pages/2/",
            "title": "The second empty page",
            "created_at": "2019-02-25T21:44:38.644000Z",
            "modified_at": "2019-02-25T21:44:38.644000Z"
        }
    ]
}
```

GET http://127.0.0.1:8000/api/v1/pages/3/ 200

```
{
    "id": 3,
    "url": "http://0.0.0.0:8000/api/v1/pages/3/",
    "title": "The third page",
    "created_at": "2019-04-22T21:44:54.414000Z",
    "modified_at": "2019-04-22T21:44:54.414000Z",
    "content": [
        {
            "id": 2,
            "counter": 0,
            "title": "The second text",
            "text": "blabla text for second",
            "created_at": "2019-04-22T21:43:13.455000Z",
            "modified_at": "2019-04-22T21:43:13.455000Z",
            "type": "text"
        },
        {
            "id": 2,
            "counter": 0,
            "title": "The second video without sub",
            "video": "/media/video/SampleVideo_360x240_1mb_PE9n3eM.mp4",
            "subtitles": null,
            "created_at": "2019-04-22T21:43:59.994000Z",
            "modified_at": "2019-04-22T21:43:59.994000Z",
            "type": "video"
        }
    ]
}
```


Tests
-

docker-compose up autotests
