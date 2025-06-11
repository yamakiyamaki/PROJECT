const https = require('https');
const http = require('http');
const fs = require('fs');
const httpProxy = require('./http-proxy/lib/http-proxy');

const proxy = httpProxy.createProxyServer({});

const options = {
  key: fs.readFileSync('./certs/privkey.pem'),
  cert: fs.readFileSync('./certs/fullchain.pem')
};

https.createServer(options, (req, res) => {
  if (req.url.startsWith("/v1/")) {
    proxy.web(req, res, { target: 'http://127.0.0.1:8080' });
  } else {
    res.writeHead(404);
    res.end("Not found");
  }
}).listen(8443, () => {
  console.log('✅ HTTPS proxy running at https://localhost:8443');
});
