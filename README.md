#SeleKopi (Aplikasi Sortasi Kopi)

Efisiensi Sortasi Kopi dinegara Surga Kopi.

##Latarbelakang
Rendahnya kesadaran akan pentingnya sortasi kopi untuk meningkatkan kualitas kopi.

##Android
Konsep dari aplikasi Androidnya adalah untuk mengambil foto dari kopi. Setelah itu foto tersebut dikirim ke server melalui POST request.
        
        https://github.com/pamungkaski/lavie-selekopi-android
##Back-End 
Back-end dari SeleKopi adalah sebuah Django server dengan Image Prosseing menggunakan library OpenCV 3. foto dari kopi yang dikirim ke server nantinya akan di proses menggunakan color tracing. Setelah itu image diubah ke Base64 kemudian dikirim kembali ke client lewat JSON

##KonVeyor
Kedepanya SeleKopi akan diimplementasikan ke sebuah Alat Konveyor yang dapat digunakan oleh koperasi koperasi petani untuk mempercepat sortasi.

[![IMAGE ALT TEXT HERE](https://www.youtube.com/watch?v=72VDbO8vKdU/0.jpg)](https://www.youtube.com/watch?v=72VDbO8vKdU)

##Demo
    1. Clone Back-End
    2. Hidupin server(gunakan host yang bisa di akses dari hp)
    3. Clone Android 
    4. Di bagian main activity bagi onCreate retrofit URL nya di ganti URL host
    4. Jalanin app nya
    
###Big Thanks To Adrian Rosebrock for his awesome blog www.pyimagesearch.com