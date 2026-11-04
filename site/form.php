<?php
/* Üyelik ve iletişim formu alıcısı.
   - Gelen kaydı form-veri/uyeler.csv veya form-veri/mesajlar.csv dosyasına ekler (klasör dışarıya kapalı).
   - info@erdalkarahan.com adresine bildirim e-postası gönderir.
   Kayıtları görmek için: Plesk > Dosyalar > httpdocs > form-veri klasöründeki .csv dosyalarını indirin (Excel ile açılır). */
date_default_timezone_set('Europe/Istanbul');
header('Content-Type: application/json; charset=utf-8');
header('Cache-Control: no-store');
$TO = 'info@erdalkarahan.com';
$FROM = 'web@erdalkarahan.com';

function out($ok, $msg = '') { echo json_encode(['ok' => $ok, 'msg' => $msg], JSON_UNESCAPED_UNICODE); exit; }
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); out(false, 'POST gerekli'); }

$raw = file_get_contents('php://input');
$d = json_decode($raw, true);
if (!is_array($d)) { $d = $_POST; }
function v($d, $k, $max = 200) { $s = isset($d[$k]) ? trim((string) $d[$k]) : ''; $s = str_replace(["\r", "\0"], '', $s); return mb_substr($s, 0, $max, 'UTF-8'); }

// bot tuzağı: gizli alan doluysa sessizce kabul et, kaydetme
if (v($d, 'web') !== '') { out(true); }

$tip = v($d, 'tip', 10) === 'iletisim' ? 'iletisim' : 'uye';
$ad = v($d, 'ad', 120);
$mail = v($d, 'mail', 160);
$tel = v($d, 'tel', 40);
if ($ad === '' || !filter_var($mail, FILTER_VALIDATE_EMAIL)) { http_response_code(422); out(false, 'Ad soyad ve geçerli e-posta gerekli'); }

$dir = __DIR__ . '/form-veri';
if (!is_dir($dir)) { @mkdir($dir, 0755, true); }
if (!file_exists($dir . '/.htaccess')) { @file_put_contents($dir . '/.htaccess', "Require all denied\nDeny from all\n"); }

// basit hız sınırı: aynı IP'den 1 dakikada en fazla 5 gönderim
$ip = isset($_SERVER['REMOTE_ADDR']) ? $_SERVER['REMOTE_ADDR'] : '';
$rl = $dir . '/.rl-' . md5($ip . date('YmdHi'));
$cnt = (int) @file_get_contents($rl);
if ($cnt >= 5) { http_response_code(429); out(false, 'Çok fazla deneme, biraz sonra tekrar deneyin'); }
@file_put_contents($rl, (string) ($cnt + 1));
foreach (glob($dir . '/.rl-*') ?: [] as $g) { if (filemtime($g) < time() - 600) { @unlink($g); } }

$now = date('d.m.Y H:i');
if ($tip === 'uye') {
    $tur = v($d, 'tur', 60);
    $ilgi = v($d, 'ilgi', 200);
    $row = [$now, $ad, $mail, $tel, $tur, $ilgi];
    $head = ['Tarih', 'Ad soyad', 'E-posta', 'Telefon', 'İşletme türü', 'İlgi alanları'];
    $file = $dir . '/uyeler.csv';
    $subject = 'Yeni üye: ' . $ad;
    $body = "Siteden yeni üyelik başvurusu\n\nAd soyad: $ad\nE-posta: $mail\nTelefon: $tel\nİşletme türü: $tur\nİlgi alanları: $ilgi\nTarih: $now\n";
} else {
    $konu = v($d, 'konu', 120);
    $mesaj = v($d, 'mesaj', 5000);
    if ($mesaj === '') { http_response_code(422); out(false, 'Mesaj boş olamaz'); }
    $row = [$now, $ad, $mail, $tel, $konu, $mesaj];
    $head = ['Tarih', 'Ad soyad', 'E-posta', 'Telefon', 'Konu', 'Mesaj'];
    $file = $dir . '/mesajlar.csv';
    $subject = 'Web sitesi: ' . ($konu !== '' ? $konu : 'mesaj') . ' - ' . $ad;
    $body = "Siteden yeni mesaj\n\nAd soyad: $ad\nE-posta: $mail\nTelefon: $tel\nKonu: $konu\nTarih: $now\n\n$mesaj\n";
}

$new = !file_exists($file);
$fp = @fopen($file, 'a');
if (!$fp) { http_response_code(500); out(false, 'Kayıt yapılamadı'); }
flock($fp, LOCK_EX);
if ($new) { fwrite($fp, "\xEF\xBB\xBF"); fputcsv($fp, $head, ';'); }
fputcsv($fp, array_map(function ($x) { return preg_match('/^[=+\-@]/', $x) ? "'" . $x : $x; }, $row), ';');
flock($fp, LOCK_UN);
fclose($fp);

$hdr = "From: =?UTF-8?B?" . base64_encode('erdalkarahan.com') . "?= <$FROM>\r\n"
     . "Reply-To: $mail\r\nMIME-Version: 1.0\r\nContent-Type: text/plain; charset=UTF-8\r\nContent-Transfer-Encoding: 8bit\r\n";
@mail($TO, '=?UTF-8?B?' . base64_encode($subject) . '?=', $body, $hdr, '-f' . $FROM);

out(true);
