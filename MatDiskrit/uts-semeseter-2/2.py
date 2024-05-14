# A
# Pernyataan A aku suka piknik atau baca buku
P = True  # aku suka Piknik
Q = False  # aku baca buku
statement_a = P or Q
print("aku suka Piknik atau baca buku:", statement_a)
# Pernyataan ekivalen dengan hukum De Morgan: aku tidak suka Piknik dan tidak baca buku
equivalent_statement_a = not P and not Q
print("Pernyataan ekivalen (hukum De Morgan):", equivalent_statement_a)
print('\n')
# B
# Pernyataan B Dosen Teknik Informatika terdiri dari perempuan atau laki-laki
P = True  # Seorang Dosen Teknik Informatika adalah perempuan
Q = True  # Seorang Dosen Teknik Informatika adalah laki-laki
statement_b = P or Q
print("Dosen Teknik Informatika terdiri dari perempuan atau laki-laki:", statement_b)
# Pernyataan ekivalen dengan hukum De Morgan: Seorang Dosen Teknik Informatika 
# bukanlah perempuan dan bukan laki-laki
equivalent_statement_b = not P and not Q
print("Pernyataan ekivalen (hukum De Morgan):", equivalent_statement_b)
