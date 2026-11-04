<?php
/* Telefon ve uygulama (PWA) içinde güvenilir indirme:
   Sayfada hazırlanan PDF / Word / Excel dosyası buraya gönderilir, sunucu aynı dosyayı
   "indir" başlığıyla geri verir; böylece tarayıcının kendi indirme yöneticisi devreye girer.
   Dosya sunucuda saklanmaz. Yalnızca erdalkarahan.com sayfalarından gelen istek kabul edilir. */
header('X-Content-Type-Options: nosniff');
header('Cache-Control: no-store');
if ($_SERVER['REQUEST_METHOD'] !== 'POST') { http_response_code(405); exit('POST gerekli'); }

$src = '';
if (!empty($_SERVER['HTTP_ORIGIN'])) { $src = $_SERVER['HTTP_ORIGIN']; }
elseif (!empty($_SERVER['HTTP_REFERER'])) { $src = $_SERVER['HTTP_REFERER']; }
$host = parse_url($src, PHP_URL_HOST);
if (!$host || !preg_match('/(^|\.)erdalkarahan\.com$/i', $host)) { http_response_code(403); exit('İzin yok'); }

$types = [
  'pdf'  => 'application/pdf',
  'docx' => 'application/vnd.openxmlformats-officedocument.wordprocessingml.document',
  'xlsx' => 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet',
  'doc'  => 'application/msword',
  'xls'  => 'application/vnd.ms-excel',
];
$name = isset($_POST['n']) ? (string) $_POST['n'] : '';
$name = preg_replace('/[^a-z0-9._-]+/i', '-', $name);
$ext = strtolower(pathinfo($name, PATHINFO_EXTENSION));
if (!isset($types[$ext]) || strlen($name) > 120) { http_response_code(400); exit('Geçersiz dosya'); }

$data = isset($_POST['d']) ? base64_decode((string) $_POST['d'], true) : false;
if ($data === false || $data === '' || strlen($data) > 15 * 1024 * 1024) { http_response_code(400); exit('Geçersiz içerik'); }
$sig = substr($data, 0, 4);
$okSig = ($ext === 'pdf' && $sig === '%PDF') || (($ext === 'docx' || $ext === 'xlsx') && $sig === "PK\x03\x04") || $ext === 'doc' || $ext === 'xls';
if (!$okSig) { http_response_code(400); exit('Geçersiz içerik'); }

header('Content-Type: ' . $types[$ext]);
header('Content-Disposition: attachment; filename="' . $name . '"');
header('Content-Length: ' . strlen($data));
echo $data;
