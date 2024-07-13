
# Port Scanner
================

## Tanım
Port Scanner, hedef ana bilgisayar üzerinde açık portları tarayan ve bu portlarda çalışan hizmetler hakkında bilgi sağlayan bir Python programıdır. Birden fazla bağlantı noktasını aynı anda taramak için çoklu iş parçacığı kullanır, bu da onu daha hızlı ve daha verimli hale getirir.

## Özellikler
### Tarama
* Hedef ana bilgisayar üzerinde portları tarar
* Bannerlar, protokoller ve sürümler dahil olmak üzere açık portlarda çalışan hizmetler hakkında bilgi sağlar
### Verim
* Aynı anda birden fazla port taramak için çoklu iş parçacığı kullanır
### Özelleştirme
* Bir dizi bağlantı noktasının taranmasını destekler
### Raporlama
* Taramayı tamamlamak için geçen sürenin bir özetini sağlar

## Kullanım
### Programı Çalıştırma
1. Terminalinizde `python port_scanner.py` komutunu çalıştırarak programı çalıştırın.
### Giriş
2. İstendiğinde taranacak hedef ana bilgisayarun url adresini veya IP adresini girin.
3. İstendiğinde taranacak başlangıç ​​ve bitiş port numaralarını girin.
### Çıktı
Program, açık portları ve bu portlarda çalışan hizmetlerle ilgili bilgiler de dahil olmak üzere tarama sonuçlarını görüntüler.

## Örnek Çıktı
Taranacak ana bilgisayarı girin: example.com Ana bilgisayarda tarama başlatılıyor: 192.0.2.1

Port 22 açık Banner: SSH-2.0-OpenSSH_7.2p2 Ubuntu 4ubuntu2.10 Protokol: SSH Sürümü: OpenSSH_7.2p2 Ubuntu 4ubuntu2.10

Port 80 açık Banner: Apache/2.4.7 (Ubuntu) Protokol: HTTP Sürümü: Apache/2.4.7 (Ubuntu)

Port 443 açık Banner: Apache/2.4.7 (Ubuntu) Protokol: HTTPS Sürümü: Apache/2.4.7 (Ubuntu)

Harcanan süre: 2,53 saniye


## Gereksinimler
### Python
* Python 3.x
### Modüller
* 'soket' modülü

## Yazar
[Burhan]

## Sürüm
1.0
