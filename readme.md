# Deskripsi
Proyek ini adalah sebuah aplikasi yang menggunakan API Groq dan Gemini untuk menghasilkan laporan keuangan berdasarkan data transaksi yang diberikan. Aplikasi ini memanfaatkan teknologi AI untuk memproses data transaksi dan menghasilkan jurnal umum, buku besar, dan neraca saldo.

# Kegunaan
Aplikasi ini berguna untuk:
- Mengotomatisasi pembuatan laporan keuangan.
- Mengurangi kesalahan manusia dalam proses pembukuan.
- Mempercepat proses analisis data keuangan.

# Fungsi
Aplikasi ini memiliki beberapa fungsi utama:
1. **Membaca dan Memparse Data Transaksi**: Membaca data transaksi dari file teks dan memparse-nya menjadi format yang dapat diproses.
2. **Mengirim Data ke API Groq**: Mengirim data transaksi ke API Groq untuk mendapatkan laporan keuangan.
3. **Memparse Hasil dari API Groq**: Memparse hasil laporan keuangan dari API Groq menjadi DataFrame.
4. **Menyimpan Data ke File**: Menyimpan hasil laporan keuangan ke dalam file teks atau Excel.

# Bagaimana Menjalankan
1. **Persiapan Lingkungan**:
   - Pastikan Anda memiliki Python dan pip terinstal di sistem Anda.
   - Instal dependensi yang diperlukan dengan menjalankan perintah berikut:
     ```bash
     pip install -r requirements.txt
     ```

2. **Menjalankan Aplikasi**:
   - Setel variabel lingkungan untuk API key Groq:
     ```bash
     export GROQ_API_KEY="gsk_yIQm2F"
     ```
   - Jalankan aplikasi dengan perintah berikut:
     ```bash
     python main.py
     ```

3. **Menjalankan Aplikasi React**:
   - Pindah ke direktori `tampilan/chat-app`:
     ```bash
     cd /github/AI-Financial-Analysis/tampilan/chat-app
     ```
   - Instal dependensi Node.js:
     ```bash
     npm install
     ```
   - Jalankan aplikasi React:
     ```bash
     npm start
     ```

# Kesimpulan
Aplikasi ini memberikan solusi yang efisien dan akurat untuk pembuatan laporan keuangan dengan memanfaatkan teknologi AI. Dengan menggunakan aplikasi ini, proses pembukuan menjadi lebih cepat dan minim kesalahan, sehingga memungkinkan pengguna untuk fokus pada analisis data keuangan yang lebih mendalam.

Referensi kode:

```1:5:conection/main.py
import os
import pandas as pd
import re
from groq import Groq

```

```136:139:conection/main.py
    transactions = read_transactions('soal.txt')
    groq_result = get_financial_reports(transactions)
    journal_df, ledger_dfs, trial_balance_df = parse_groq_result(groq_result)
    save_to_excel(journal_df, ledger_dfs, trial_balance_df, 'output_pembukuan.xlsx')
```

```5:9:tampilan/readme.md
cd /github/AI-Financial-Analysis/tampilan
python app.py

cd /github/AI-Financial-Analysis/tampilan/chat-app
npm start
```

cara menjalankan nya
export GROQ_API_KEY="gsk_yIQm2F"

pip install -r requirements.txt

python main.py