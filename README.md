#SeleKopi (Aplikasi Sortasi Kopi)

Indonesia dikenal sebagai negara agraris, yang mana mayoritas penduduknya memiliki mata pencarian pada sektor pertanian. Salah satu hasil pertanian terbanyak di Indonesia yaitu kopi. Kopi merupakan salah satu komoditi perkebunan tradisional yang mempunyai peran penting dalam perekonomian Indonesia dan kopi merupakan salah satu komoditas ekspor yang cukup besar di indonesia. Jumlah ekspor kopi indonesia pertahun mencapai 350 ton per tahun (Asosiasi Ekspor Kopi Indonesia, 2016). Tingginya angka eskpor kopi tersebut tentunya harus disertai dengan peningkatan kualitas kopi untuk memperkuat daya saing kopi indonesia di mata dunia. 
Tidak hanya sebagai negara pengekspor kopi, kopi juga menjadi salah satu jenis minuman yang banyak diminati oleh masyarakat Indonesia. Kebutuhan kopi di Indonesia tahun 2016 yaitu 400.000.000 Kg dengan komsumsi kopi pert kapita 1.54 Kg/Kapita/tahun. Rata-rata peningkatan konsumsi kopi dalam negeri dari tahun 2010 hingga 2016 yaitu 35.000.000 Kg dan kebutuhan kopi dalam negeri mengalami  peningkatan yang signifikan pada tahun 2015 ke 2016 naik sebesar 50.000.000 Kg (Asosiasi Ekspor Kopi Indonesia , 2016). Namun terdapat permasalahan yang masih terjadi sampai saat ini yaitu, walaupun Indonesia dikenal sebagai negara tropis dengan menghasilkan kualitas kopi yang baik, hal ini tidak dapat dimanafaat oleh petani Indonesia sebaik mungkin. Didalam perkebunan rakyat, kualitas kopi yang dihasilkan yang sebagian besar bermutu rendah disebabkan masalah proses produksi kopi yang seringkali melakukan panen sebelum masak atau dikenal dengan istilah petik hijau, yang seharusnya biji kopi dipetik setelah biji berwarna merah. 
Salah satu faktor yang terpenting dalam peningkatan kualitas kopi adalah dalam pemilihan biji kopi mana yang sudah matang optimal, belum matang atau malahan sudah busuk pada masa pasca panen. Hal ini sangat disayangkan karena pemilihan dan seleksi buah akan sangat mempengaruhi cita rasa dari kopi tersebut.
Di kalangan petani dan koperasi kopi yang tersebar di seluruh indonesia hal ini masih belum di begitu diperhatikan. Selain karena harga antara hijau,merah dan hitam sama, karena keterbatasan teknologi penyeleksian, sehingga kualitas kopi yang dihasilkan rendah. Rendahnya kualitas tersebut juga menjadi pemicu rendahnya perolehan petani karena biji kopi yang berasal dari petani hanya mendapatkan setengah harga dari kopi yang berkualitas baik. Untuk ekspornyapun masalah yang dihadapi Indonesia bukan hanya kebijakan perdagangan, tetapi juga mutu. Kalaupun mereka melakukan penyeleksian pun menggunakan mata telanjang dengan perkiraan dan ingatan saja yang tentunya terbatas. Sifat manusia yang kecenderungan subyektif dan memiliki penilaian berbeda-beda juga salah satu masalah dalam prosesnya. Dari permasalahan tersebut, teknologi merupakan suatu hal yang tidak dapat dipisahkan dalam kegiatan sehari-hari. Teknologi dapat memudahkan berbagai aktivitas kita, oleh sebab itu diperlukan teknologi yang dapat membantu petani kopi untuk menciptakan kopi yang berkualitas. Oleh sebab itu, dibutuhkan suatu teknologi yang dapat membantu penyeleksian kopi dengan cara yang efektif dan efisien.

##Android
Konsep dari aplikasi Androidnya adalah untuk mengambil foto dari kopi. Setelah itu foto tersebut dikirim ke server melalui POST request.
        
        https://github.com/pamungkaski/lavie-selekopi-android
##Back-End 
Back-end dari SeleKopi adalah sebuah Django server dengan Image Prosseing menggunakan library OpenCV 3. foto dari kopi yang dikirim ke server nantinya akan di proses menggunakan color tracing. Setelah itu image diubah ke Base64 kemudian dikirim kembali ke client lewat JSON

##KonVeyor
Kedepanya SeleKopi akan diimplementasikan ke sebuah Alat Konveyor yang dapat digunakan oleh koperasi koperasi petani untuk mempercepat sortasi.

##Demo
    1. Clone Back-End
    2. Hidupin server(gunakan host yang bisa di akses dari hp)
    3. Clone Android 
    4. Di bagian main activity bagi onCreate retrofit URL nya di ganti URL host
    4. Jalanin app nya
    
###Big Thanks To Adrian Rosebrock for his awesome blog www.pyimagesearch.com