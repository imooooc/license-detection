Component({
  data: {
    selected: 0,
    color: "#7A7E83",
    selectedColor: "#3cc51f",
    list: [{
      pagePath: "/pages/analysis/index",
      iconPath: "/image/flask-outline.png",
      selectedIconPath: "/image/flask-sharp.png",
      text: "Analysis"
    }, {
      pagePath: "/pages/datechart/index",
      iconPath: "/image/pulse-outline.png",
      selectedIconPath: "/image/pulse-sharp.png",
      text: "DateChart"
      },{
      pagePath: "/pages/home/index",
      iconPath: "/image/person-outline.png",
      selectedIconPath: "/image/person-sharp.png",
      text: "Home"
      }]
  },
  attached() {
  },
  methods: {
    switchTab(e) {
      const data = e.currentTarget.dataset
      const url = data.path
      wx.switchTab({url})
      this.setData({
        selected: data.index
      })
    }
  }
})