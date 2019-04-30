//express_demo.js 文件
var express = require('express');
var cors = require('cors')
var app = express();

var corsOptions = {
    origin: 'http://10.0.75.1:8082', //只有百度可以访问
    optionsSuccessStatus: 200 
  }
 
app.get('/', function (req, res) {
   res.send('Hello World');
})

app.get('/person', cors(corsOptions), function (req, res, next) {
    res.json({msg: '只有http://10.0.75.1:8082可以访问'})
  })
  
//   app.listen(80, function () {
//     console.log('CORS-enabled web server listening on port 80')
//   })
 
var server = app.listen(8081, function () {
 
  var host = server.address().address
  var port = server.address().port
 
  console.log("应用实例，访问地址为 http://%s:%s", host, port)
 
})