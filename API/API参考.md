# API参考

var schemas = {
  home: 'snssdk1128://feed?refer=web&gd_label={{gd_label}}',
  // 首页feed
  detail: 'snssdk1128://aweme/detail/{{id}}?refer=web&gd_label={{gd_label}}&appParam={{appParam}}&needlaunchlog=1',
  // 作品详情页
  user: 'snssdk1128://user/profile/{{uid}}?refer=web&gd_label={{gd_label}}&type={{type}}&needlaunchlog=1',
  // 用户主页
  challenge: 'snssdk1128://challenge/detail/{{id}}?refer=web&is_commerce=0',
  // 挑战详情
  music: 'snssdk1128://music/detail/{{id}}?refer=web',
  // 音乐详情
  live: 'snssdk1128://live?room_id={{room_id}}&user_id={{user_id}}&u_code={{u_code}}&from=webview&refer=web',
  // 直播间
  webview: 'snssdk1128://webview?url={{url}}&from=webview&refer=web',
  // webview
  webview_fullscreen: 'snssdk1128://webview?url={{url}}&from=webview&hide_nav_bar=1&refer=web',
  // webview 沉浸式
  poidetail: 'snssdk1128://poi/detail?id={{id}}&from=webview&refer=web',
  // poi详情页
  forward: 'snssdk1128://forward/detail/{{id}}',
  // 转发详情页
  billboard_word: 'snssdk1128://search/trending',
  // 热搜词榜
  billboard_video: 'snssdk1128://search/trending?type=1',
  // 热搜视频榜
  billboard_music: 'snssdk1128://search/trending?type=2',
  // 热搜音乐榜
  billboard_positive: 'snssdk1128://search/trending?type=3',
  // 正能量榜
  billboard_star: 'snssdk1128://search/trending?type=4' // 明星榜

}; // universal link url