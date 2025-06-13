const https = require('https');
const http = require('http');
const fs = require('fs');
const httpProxy = require('./http-proxy/lib/http-proxy');
const WebSocket = require('ws');  // ✅ Only declare this once

const proxy = httpProxy.createProxyServer({});

const options = {
  key: fs.readFileSync('./certs/privkey.pem'),
  cert: fs.readFileSync('./certs/fullchain.pem')
};

// ✅ Create ONE shared HTTPS server for both HTTP and WebSocket
const server = https.createServer(options, (req, res) => {
  if (req.url.startsWith("/v1/")) {
    proxy.web(req, res, { target: 'http://127.0.0.1:8080' });
  } else {
    res.writeHead(404);
    res.end("Not found");
  }
});

server.listen(8443, '0.0.0.0', () => {
  console.log('✅ HTTPS proxy + signaling running on all interfaces at https://<your-ip>:8443');
});

// ✅ WebSocket signaling on same server (port 8443)
const wss = new WebSocket.Server({ server });

let sender = null;
let receiver = null;

wss.on('connection', (ws) => {
  ws.on('message', (msg) => {
    const data = JSON.parse(msg);

    if (data.role === 'sender') sender = ws;
    if (data.role === 'receiver') receiver = ws;

    const target = ws === sender ? receiver : sender;
    if (target && target.readyState === WebSocket.OPEN) {
      target.send(JSON.stringify(data));
    }
  });

  ws.on('close', () => {
    if (ws === sender) sender = null;
    if (ws === receiver) receiver = null;
  });
});

