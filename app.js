var express = require('express');
var app = express();
var path = require('path');
var public = path.join(__dirname, 'public');

// viewed at http://localhost:8080
app.get('/assets', function(req, res) {
    res.sendFile(path.join(public, 'index.html'));
});

app.get('/', function(req, res) {
    res.send("Welcome to image assets serivce");
});

app.use('/assets', express.static(public));

app.listen(1000);
console.log(`Example app listening on port 1000!`)