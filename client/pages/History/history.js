Page({
  data: {
    value: '',
    //表格
    listData: [
      { "code": "01", "text": "text1", "type": "type1" },
      { "code": "02", "text": "text2", "type": "type2" },
      { "code": "03", "text": "text3", "type": "type3" },
      { "code": "04", "text": "text4", "type": "type4" },
      { "code": "05", "text": "text5", "type": "type5" },
      { "code": "06", "text": "text6", "type": "type6" },
      { "code": "07", "text": "text7", "type": "type7" }
    ]
    
  },
  //搜索框函数组
  onChange(e) {
    console.log('onChange', e)
    this.setData({
      value: e.detail.value,
    })
  },
  onFocus(e) {
    console.log('onFocus', e)
  },
  onBlur(e) {
    console.log('onBlur', e)
  },
  onConfirm(e) {
    console.log('onConfirm', e)
  },
  onClear(e) {
    console.log('onClear', e)
    this.setData({
      value: '',
    })
  },
  onCancel(e) {
    console.log('onCancel', e)
  },
})
