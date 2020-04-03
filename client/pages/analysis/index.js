var app=getApp();
var StepNum=app.globalData.StepNum;
Component({
  data: {
    current:StepNum,
    visible2: false,//helpflag
    chooesVideo:'',  //上传视频地址
    urls:" "
  },
  methods: {
    /**
      * 生命周期函数--监听页面加载
      */
    onLoad: function (options) {
      
      console.log(options.status)
    },
    /**
       * 生命周期函数--监听页面初次渲染完成
       */
    onReady: function (res) {
      this.videoContext = wx.createVideoContext('prew_video');
    },
    //分析功能 ————跳转到结果页面
    analysis:function(){
      //跳转结果页
      wx.navigateTo({
        url: '/pages/Result/index'
      })
      //步骤条
      const current = 2
      this.setData({
        current,
      })
    },
    //本地图片上传
    PhotoUpload:function(){ 
      //步骤条
      const current = 1
      this.setData({
        current,
      })
      //本地图片上传
      let that = this
      wx.chooseImage({
        count: 1, // 默认9
        sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
        sourceType: ['album', 'camera'], // 可以指定来源是相册还是相机，默认二者都有
        success: function (res) {
          console.log(res)
          var tempFilePaths = res.tempFilePaths
          that.data.images = tempFilePaths
          // 单图片
          that.data.urls = tempFilePaths[0]
          that.setData({
            images: tempFilePaths[0],
            urls: that.data.urls
          })
        }
      })
      },
    //本地视频上传
    VideoUpload: function () {
      //步骤条
      const current = 1
      this.setData({
        current,
      })
      //本地视频上传
      let that = this
      wx.chooseVideo({
        sourceType: ['album', 'camera'],
        maxDuration: 60,
        camera: 'back',
        success: function (res) {
          that.setData({
            chooesVideo: res.tempFilePath
          })
        }
      })
    },
    //视频全屏播放
    bindVideoScreenChange: function (e) {
      var status = e.detail.fullScreen;
      var play = {
        playVideo: false
      }
      if (status) {
        play.playVideo = true;
      } else {
        this.videoContext.pause();
      }
      this.setData(play);
    },

    //摄像头调用
    CreamStartUpload: function () {
      //步骤条
      const current = 1
      this.setData({
        current,
      })
      //摄像头调用
      wx.navigateTo({
        url: '../Camera/Camera'
      })
    },
    //在线素材
    IntetnetUpload: function () {
      //步骤条
      const current = 1
      this.setData({
        current,
      })
      //在线素材上传
      console.log("eee")
    },
    //步骤栏触发变化
    onClick() {
      const current = 1
      this.setData({
        current,
      })
    },
    //Help me
    HelpOpen:function() {
      this.setData({
        visible2: true,
      })
    },
    HelpClose:function() {
      this.setData({
        visible2: false,
      })
    },
  },
  pageLifetimes: {
    show() {
      if (typeof this.getTabBar === 'function' &&
        this.getTabBar()) {
        this.getTabBar().setData({
          selected: 0
        })
      }
    }
  }
})

