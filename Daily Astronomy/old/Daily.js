
/*const request = require('request');

request('https://apod.nasa.gov/apod/', { json: true }, (err, res, body) => {
    if (err) { return console.log(err); }
    console.log(body.url);
    console.log(body.explanation);
  });*/
var selem
function doit(textMessage) {
    selem = document.getElementById("s");
    selem.innerText = textMessage;
}
fetch("https://www.sciencealert.com/", {//"https://feeds.feedburner.com/sciencealert-latestnews", {
  mode: 'cors',
  method: 'get',
  headers: {'Origin':  "http://feedproxy.google.com/~r/sciencealert-latestnews/~3/"}//"https://www.sciencealert.com/"}
})
//  .then(doit())
  .then(function(Request) {
  Request.text().then(function(text) {
    console.log(text);
    doit(text);
  })
})
  .catch(function(error) {
    doit(error);
  });