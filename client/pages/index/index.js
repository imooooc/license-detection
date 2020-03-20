//index.js
//获取应用实例
const app = getApp()

Page({
    chooseImage: function (e) {
        wx.chooseImage({
            count: 2, // 默认9
            sizeType: ['original', 'compressed'], // 可以指定是原图还是压缩图，默认二者都有
            sourceType: ['camera'], // 可以指定来源是相册还是相机，默认二者都有
            success: function (res) {
                // 返回选定照片的本地文件路径列表，tempFilePath可以作为img标签的src属性显示图片
                var tempFilePaths = res.tempFilePaths
                wx.showModal({
                  title: '路径',
                  content: tempFilePaths[0],
                })
            }
        })
    }

})
