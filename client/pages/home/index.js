const app = getApp();
import { $wuxToast } from '../../dist/index'
Page({
  /**
   * 页面的初始数据
   */
  data: {
    visible2: false,//helpflag
    userInfo: {},
    hasUserInfo: false,
    canIUse: wx.canIUse('button.open-type.getUserInfo')
  },

  /**
   * 生命周期函数--监听页面加载
   */
  onLoad: function (options) {
    var that = this;
    if (app.globalData.userInfo) {
      that.setUserInfo(app.globalData.userInfo);
    } else if (that.data.canIUse) {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        that.setUserInfo(res.userInfo);
      }
    } else {
      // 在没有 open-type=getUserInfo 版本的兼容处理
      wx.getUserInfo({
        success: res => {
          that.setUserInfo(res.userInfo);
        }
      })
    }
  },

  getUserInfo: function (e) {
    this.setUserInfo(e.detail.userInfo);
  },

  setUserInfo: function (userInfo) {
    if (userInfo != null) {
      app.globalData.userInfo = userInfo
      this.setData({
        userInfo: userInfo,
        hasUserInfo: true
      })
    }
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
  },
  //跳转VIP购买页面
  ToVIP:function(){
    wx.navigateTo({
      url: '/pages/Pay/index',
    })
  },
  //跳转History页面
  ToHistory:function(){
    wx.navigateTo({
      url: '/pages/History/history'
    })
  },
  //Help me
  HelpOpen: function () {
    this.setData({
      visible2: true,
    })
  },
  HelpClose: function () {
    this.setData({
      visible2: false,
    })
  },
  //未开发功能
  showToastErr() {
    $wuxToast().show({
      type: 'forbidden',
      duration: 1500,
      color: '#fff',
      text: '功能待开发',
      success: () => console.log('功能待开发')
    })
  },
  //转发功能
  onShareAppMessage:function(res){
    if(res.from=='button'){
      console.log(res.target,res)
    }
    return{
      title:"开启你的车辆探索",
      path:"pages/Verify/index",
      imageUrl:"../../image/title.jpg"
    }
  }
})