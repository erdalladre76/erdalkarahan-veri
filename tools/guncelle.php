<?php
/* Otomatik güncelleme: GitHub'daki erdalladre76/erdalkarahan-veri deposunun site/ klasörünü
   bu klasöre (httpdocs) kopyalar. Yalnızca değişen dosyalar indirilir; hiçbir dosya silinmez.
   Dışarıdan veri almaz, sadece kendi deposunu okur; bu yüzden kim çağırırsa çağırsın zararsızdır.
   Kötüye kullanıma karşı 20 saniyede bir çalışır. */
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
@set_time_limit(120);
$REPO = 'erdalladre76/erdalkarahan-veri';
$BR = 'main';
$ROOT = __DIR__;
$SKIP = ['guncelle.php'];                 // kendini asla üzerine yazmaz
$ALLOW = '/^(?:[a-z0-9._-]+|app-icons\/[a-z0-9._-]+|img\/[a-z0-9._-]+)$/i';
$EXT = '/\.(html|php|js|json|webmanifest|xml|txt|ico|png|jpg|jpeg|webp|svg|css)$/i';

function out($a) { echo json_encode($a, JSON_UNESCAPED_UNICODE | JSON_UNESCAPED_SLASHES); exit; }
function get($url) {
    $h = ["User-Agent: erdalkarahan-guncelle", "Accept: application/vnd.github+json"];
    if (function_exists('curl_init')) {
        $c = curl_init($url);
        curl_setopt_array($c, [CURLOPT_RETURNTRANSFER => true, CURLOPT_TIMEOUT => 40, CURLOPT_HTTPHEADER => $h, CURLOPT_FOLLOWLOCATION => true]);
        $r = curl_exec($c); $code = curl_getinfo($c, CURLINFO_HTTP_CODE); curl_close($c);
        return $code === 200 ? $r : false;
    }
    $ctx = stream_context_create(['http' => ['header' => implode("\r\n", $h), 'timeout' => 40]]);
    return @file_get_contents($url, false, $ctx);
}

$lock = $ROOT . '/form-veri/.guncelle';
if (!is_dir($ROOT . '/form-veri')) { @mkdir($ROOT . '/form-veri', 0755, true); }
if (file_exists($lock) && time() - filemtime($lock) < 20) { out(['ok' => false, 'msg' => 'Az önce çalıştı, biraz bekleyin']); }
@touch($lock);

$ref = get("https://api.github.com/repos/$REPO/commits/$BR");
$sha = $ref ? (json_decode($ref, true)['sha'] ?? '') : '';
if (!preg_match('/^[0-9a-f]{40}$/', $sha)) { out(['ok' => false, 'msg' => 'GitHub okunamadı']); }
$tree = get("https://api.github.com/repos/$REPO/git/trees/$sha?recursive=1");
$t = $tree ? json_decode($tree, true) : null;
if (!$t || empty($t['tree'])) { out(['ok' => false, 'msg' => 'Dosya listesi alınamadı']); }

$changed = []; $same = 0; $err = [];
foreach ($t['tree'] as $n) {
    if (($n['type'] ?? '') !== 'blob' || strpos($n['path'], 'site/') !== 0) { continue; }
    $rel = substr($n['path'], 5);
    if (in_array($rel, $SKIP, true) || !preg_match($ALLOW, $rel) || !preg_match($EXT, $rel) || strpos($rel, '..') !== false) { continue; }
    $dst = $ROOT . '/' . $rel;
    if (is_file($dst)) {
        $cur = file_get_contents($dst);
        if (sha1('blob ' . strlen($cur) . "\0" . $cur) === $n['sha']) { $same++; continue; }
    }
    $data = get("https://raw.githubusercontent.com/$REPO/$sha/" . str_replace('%2F', '/', rawurlencode($n['path'])));
    if ($data === false || sha1('blob ' . strlen($data) . "\0" . $data) !== $n['sha']) { $err[] = $rel; continue; }
    $dir = dirname($dst);
    if (!is_dir($dir)) { @mkdir($dir, 0755, true); }
    $tmp = $dst . '.yeni';
    if (@file_put_contents($tmp, $data) === false || !@rename($tmp, $dst)) { @unlink($tmp); $err[] = $rel; continue; }
    $changed[] = $rel;
}
@file_put_contents($ROOT . '/form-veri/guncelle.log', date('c') . ' ' . substr($sha, 0, 7) . ' degisen:' . implode(',', $changed) . ($err ? ' HATA:' . implode(',', $err) : '') . "\n", FILE_APPEND);
out(['ok' => !$err, 'surum' => substr($sha, 0, 7), 'degisen' => $changed, 'ayni' => $same, 'hata' => $err]);
