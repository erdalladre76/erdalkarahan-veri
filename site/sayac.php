<?php
/* Ziyaretçi sayacı: yeni sitedeki ziyaretleri sayac-veri/sayac.txt dosyasında tutar.
   ?hit=1 ile çağrılırsa 1 artırır, her durumda güncel sayıyı JSON döndürür.
   Eski siteden gelen 125.947 başlangıç sayısı index.html içindeki SITE_STAT.onceki değerindedir. */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
$dir = __DIR__ . '/sayac-veri';
if (!is_dir($dir)) { @mkdir($dir, 0755, true); @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }
$f = $dir . '/sayac.txt';
$hit = isset($_GET['hit']) && $_GET['hit'] === '1';
if ($hit && preg_match('/headless|lighthouse|pingdom|uptime|facebookexternalhit|whatsapp|telegram|discord|skype|linkedin|google|bing|yandex|ahrefs|semrush/', $ua)) { $hit = false; }
$ua = isset($_SERVER['HTTP_USER_AGENT']) ? strtolower($_SERVER['HTTP_USER_AGENT']) : '';
if ($hit && ($ua === '' || preg_match('/bot|crawl|spider|slurp|preview|monitor|curl|wget|python/', $ua))) { $hit = false; }
$ben = isset($_GET['ben']) && $_GET['ben'] === '1';
if ($ben) { $hit = false; }
date_default_timezone_set('Europe/Istanbul');

/* günlük kayıt: tekil ziyaretçi (IP+tarayıcı özetinin karması; IP saklanmaz) ve ziyaret sayısı */
if ($hit) {
    $ip = !empty($_SERVER['HTTP_CF_CONNECTING_IP']) ? $_SERVER['HTTP_CF_CONNECTING_IP'] : (isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '');
    $g = $dir . '/gun-' . date('Y-m-d') . '.txt';
    $h = substr(hash('sha256', date('Y-m-d') . '|' . $ip . '|' . $ua . '|ek-tuz-7'), 0, 16);
    $dev = preg_match('/mobi|android|iphone/', $ua) ? 'm' : 'd';
    @file_put_contents($g, $h . ' ' . $dev . "\n", FILE_APPEND | LOCK_EX);
}

/* rapor: sayac.php?rapor=1 — son 30 gün */
if (isset($_GET['rapor'])) {
    header('Content-Type: text/html; charset=utf-8');
    $rows = ''; $tt = 0; $tu = 0; $all = [];
    for ($i = 0; $i < 30; $i++) {
        $d = date('Y-m-d', strtotime("-$i day")); $g = $dir . '/gun-' . $d . '.txt';
        if (!file_exists($g)) { continue; }
        $L = array_filter(explode("\n", (string) @file_get_contents($g)));
        $u = []; $m = 0;
        foreach ($L as $x) { $p = explode(' ', $x); $u[$p[0]] = isset($p[1]) ? $p[1] : 'd'; $all[$p[0]] = 1; }
        foreach ($u as $v) { if ($v === 'm') { $m++; } }
        $tt += count($L); $tu += count($u);
        $rows .= '<tr><td>' . date('d.m.Y', strtotime($d)) . '</td><td>' . count($u) . '</td><td>' . count($L) . '</td><td>' . $m . ' / ' . (count($u) - $m) . '</td></tr>';
    }
    echo '<!doctype html><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="noindex"><title>Ziyaretçi raporu</title><style>body{font:15px/1.5 system-ui,sans-serif;margin:24px;color:#111;background:#f6f6fb}table{border-collapse:collapse;background:#fff;min-width:320px}td,th{border:1px solid #ddd;padding:8px 12px;text-align:right}th{background:#5B3FA8;color:#fff}td:first-child,th:first-child{text-align:left}</style>';
    echo '<h2>erdalkarahan.com · ziyaretçi raporu</h2><p>Sizin cihazlarınız (#ben ile işaretlenenler) ve arama motoru botları sayılmaz.</p>';
    echo '<table><tr><th>Gün</th><th>Tekil ziyaretçi</th><th>Ziyaret</th><th>Telefon / Bilgisayar</th></tr>' . ($rows ?: '<tr><td colspan="4">Henüz kayıt yok</td></tr>') . '<tr><th>Toplam (30 gün)</th><th>' . $tu . '</th><th>' . $tt . '</th><th></th></tr></table>';
    exit;
}

$fp = @fopen($f, 'c+');
if (!$fp) { echo json_encode(['ziyaret' => null]); exit; }
flock($fp, LOCK_EX);
$n = (int) stream_get_contents($fp);
if ($hit) { $n++; ftruncate($fp, 0); rewind($fp); fwrite($fp, (string) $n); fflush($fp); }
flock($fp, LOCK_UN);
fclose($fp);
echo json_encode(['ziyaret' => $n]);
