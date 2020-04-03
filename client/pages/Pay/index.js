import { $wuxNotification } from '../../dist/index'
Component({
  data: {
    args: {
      fee: 1,             // 支付金额，单位为分
      paymentArgs: 'A', // 将传递到功能页函数的自定义参数
      currencyType: 'USD' // 货币符号，页面显示货币简写 US$ 
    }
  },
  methods: {
    // 支付成功的回调接口
    paymentSuccess: function (e) {
      console.log(e);
      e.detail.extraData.timeStamp // 用 extraData 传递数据，详见下面功能页函数代码
    },
    // 支付失败的回调接口
    paymentFailed: function (e) {
      console.log(e);
    },
    //通知栏
    showNotification() {
      this.closeNotification = $wuxNotification().show({
        image: '/image/icon-mine.png',
        title: "客服兼作者",
        text: '嘤嘤嘤，微信官方开通这个太麻烦了，暂时不支持！！可以走支付宝，我们人工登记!!!!记得备注信息哦亲，买不了吃亏买不了上当',
        duration: 5000,
        onClick(data) {
          console.log(data)
        },
        onClose(data) {
          console.log(data)
        },
      })
    }
  }
})