import os
import pandas as pd
import re
from groq import Groq

# Set API key (biasanya disimpan sebagai environment variable)
api_key = os.environ.get("GROQ_API_KEY")

# Buat instance client Groq
client = Groq(api_key=api_key)

# Fungsi untuk membaca dan memparse file soal.txt
def read_transactions(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    
    transactions = []
    for line in lines[1:]:
        match = re.match(r'(\d+) Januari, (.+)', line.strip())
        if match:
            day = match.group(1)
            transaction = match.group(2)
            transactions.append((int(day), transaction))
    
    return transactions

# Fungsi untuk mengirim data transaksi ke Groq dan mendapatkan hasil
def get_financial_reports(transactions):
    transaction_texts = [f"{day} Januari: {transaction}" for day, transaction in transactions]
    prompt = "Berikut adalah data transaksi:\n" + "\n".join(transaction_texts) + "\n\nBuatlah jurnal umum, buku besar, dan neraca saldo dari data di atas."
    
    print("Prompt yang dikirim ke Groq:")
    print(prompt)
    
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
        model="llama3-8b-8192",
    )

    result = chat_completion.choices[0].message.content
    print("Hasil dari Groq:")
    print(result)
    
    return result

# Fungsi untuk memparse hasil dari Groq menjadi DataFrame
def parse_groq_result(groq_result):
    sections = groq_result.split("\n\n")
    journal = []
    ledger = {}
    trial_balance = []

    for section in sections:
        lines = section.split("\n")
        if "Jurnal Umum" in lines[0]:
            for line in lines[1:]:
                if line.strip():
                    parts = line.split(", ")
                    journal.append(parts)
        elif "Buku Besar" in lines[0]:
            if " - " in lines[0]:
                account = lines[0].split(" - ")[1]
                ledger_entries = []
                for line in lines[1:]:
                    if line.strip():
                        parts = line.split(", ")
                        ledger_entries.append(parts)
                ledger[account] = ledger_entries
        elif "Neraca Saldo" in lines[0]:
            for line in lines[1:]:
                if line.strip():
                    parts = line.split(", ")
                    trial_balance.append(parts)
    
    journal_df = pd.DataFrame(journal, columns=["Tanggal", "Debit", "Kredit", "Jumlah"])
    ledger_dfs = {account: pd.DataFrame(entries, columns=["Tipe", "Tanggal", "Jumlah", "Saldo"]) for account, entries in ledger.items()}
    trial_balance_df = pd.DataFrame(trial_balance, columns=["Akun", "Debit", "Kredit", "Saldo"])
    
    return journal_df, ledger_dfs, trial_balance_df

# Fungsi untuk menyimpan data ke dalam file teks
def save_to_text(journal, ledger, trial_balance, file_path):
    with open(file_path, 'w') as file:
        file.write("Jurnal Umum\n")
        journal_text = journal.to_string(index=False)
        file.write(journal_text + "\n\n")

        for account, entries in ledger.items():
            file.write(f"Buku Besar - {account}\n")
            ledger_text = entries.to_string(index=False)
            file.write(ledger_text + "\n\n")
        
        file.write("Neraca Saldo\n")
        trial_balance_text = trial_balance.to_string(index=False)
        file.write(trial_balance_text + "\n")

# Main program
if __name__ == "__main__":
    transactions = read_transactions('soal.txt')
    groq_result = get_financial_reports(transactions)
    journal_df, ledger_dfs, trial_balance_df = parse_groq_result(groq_result)
    save_to_text(journal_df, ledger_dfs, trial_balance_df, 'output_pembukuan.txt')

