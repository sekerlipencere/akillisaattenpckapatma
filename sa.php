<?php
$dosyaAdi = "metin.txt"; // Metni saklayacağınız dosyanın adı

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $yeni_metin = $_POST["yeni_metin"];
    file_put_contents($dosyaAdi, $yeni_metin); // Yeni metni dosyaya yaz
}

$saklanan_metin = file_get_contents($dosyaAdi); // Dosyadan saklanan metni oku
?>

<!DOCTYPE html>
<html>
<head>
    <title>Metin Değiştirme</title>
</head>
<body>
    <h1>Metin Değiştirme</h1>
    <p>Şu anki metin: <?php echo $saklanan_metin; ?></p>
    <form method="post" action="<?php echo $_SERVER["PHP_SELF"]; ?>">
        Yeni Metin: <input type="text" name="yeni_metin">
        <input type="submit" value="Metni Değiştir">
    </form>
</body>
</html>
