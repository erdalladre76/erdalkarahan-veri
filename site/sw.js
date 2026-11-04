/* SMMM Erdal Karahan - çevrimdışı çalışma için hizmet çalışanı */
var CACHE = 'ek-v5';
var CORE = ['./', './index.html', './manifest.webmanifest', './oranlar.json', './app-icons/icon-192.png', './app-icons/icon-512.png', './app-icons/favicon.svg', './img/buro-640.webp', './img/buro-640.jpg', './img/ismmmo.png'];
self.addEventListener('install', function (e) {
  e.waitUntil(caches.open(CACHE).then(function (c) { return c.addAll(CORE); }).then(function () { return self.skipWaiting(); }));
});
self.addEventListener('activate', function (e) {
  e.waitUntil(caches.keys().then(function (keys) {
    return Promise.all(keys.filter(function (k) { return k !== CACHE; }).map(function (k) { return caches.delete(k); }));
  }).then(function () { return self.clients.claim(); }));
});
self.addEventListener('fetch', function (e) {
  var req = e.request, url = new URL(req.url);
  if (req.method !== 'GET' || url.origin !== location.origin) return; /* kurlar, haberler, yazı tipleri: ağdan */
  if (url.pathname.endsWith('oranlar.json') || req.mode === 'navigate') {
    /* önce ağ, olmazsa önbellek: güncel oranlar ve sayfa */
    e.respondWith(fetch(req).then(function (r) { var c = r.clone(); caches.open(CACHE).then(function (ca) { ca.put(req, c); }); return r; })
      .catch(function () { return caches.match(req).then(function (m) { return m || caches.match('./index.html'); }); }));
    return;
  }
  e.respondWith(caches.match(req).then(function (m) {
    return m || fetch(req).then(function (r) { var c = r.clone(); caches.open(CACHE).then(function (ca) { ca.put(req, c); }); return r; });
  }));
});
