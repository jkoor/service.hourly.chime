# Hourly Chime

> Chimes on the hour or half hour when you watching videos.

This addon for `KODI` is designed to solve the problem of watching videos with too much attention and forgetting the time.

The addon will send out a notification to remind the video watching progress at each full and half hour.

## Customize notification title and text

Default notification title: `22:15`

Default notification text: `Watch process: 40%`

U can change it by using `f-string`:

Available variables: 

`total_time`: video total time (s)

`watched_time`: video watched time (s)

`watched_percent`: video watched process (%)

`nowtime`: current system time

Some examples:

`Current Time {nowtime}`  : `Current Time 22:15`

`Watched: {int(watched_time / 60)} min` : `Watched: 6 min`

`Left: {int((total_time - watched_time) / 60 )} min` : `Left: 6 min`



## 中文

> 在每个时间段的整点和半点会发出通知报时，因为常常观看视频过于投入，废寝忘食，导致了这个插件的产生。想法来源自 CCTV 的整点报时功能。

可以通过使用 `f-string` 自定义通知内容: 

可用变量：

`total_time`: 视频总时长 (s)

`watched_time`: 视频观看时长 (s)

`watched_percent`: 观看进度百分比 (%)

`nowtime`: 当前系统时间

举个例子：

`当前时间 {nowtime}`  : `当前时间 22:15`

`已观看: {int(watched_time / 60)} min` : `已观看: 6 min`

`剩余时间: {int((total_time - watched_time) / 60 )} min` : `剩余时间: 6 min`
