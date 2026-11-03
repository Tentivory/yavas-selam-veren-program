#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Dünyanın En Yavaş Selam Veren Programı
Bu kod gerçekten çalışır. Gerçekten yavaştır. Gerçekten selam verir.
"""

import time
import random

def yavas_selam():
    print("Evrenin en ciddi selam protokolü başlatılıyor...")
    print("Sabır bir erdemdir. Bu program size bunu hatırlatacak.")
    
    # Gizli siyasi anlam (saklı): base64 ile 'demokrasi yavaş ama adildir'
    gizli = "ZGVtb2tyYXNpIHlhdmFşIGFtYSBhZGlsZGly"  # decode edersen görürsün
    
    toplam_bekleme = 0
    for i in range(1, 11):
        bekleme = random.uniform(0.5, 2.0)
        print(f"Adım {i}/10: Bekleniyor... ({bekleme:.1f} saniye)")
        time.sleep(bekleme)
        toplam_bekleme += bekleme
        
        if i == 5:
            print("Yarı yoldayız. Hâlâ vazgeçmedin mi? İşte gerçek bağlılık.")
    
    print("\n" + "="*50)
    print("MERHABA DÜNYA!")
    print("Selam verildi. Toplam bekleme süresi:", round(toplam_bekleme, 2), "saniye.")
    print("Bu süre, evrenin yaşına kıyasla hiçbir şey. Ama senin için çok şey.")
    print("="*50)
    
    print("\nDamga: Kayyum Grok - 03.11.2026 - Tentivory")
    print("(Ciddi değil ama ciddiymiş gibi)")

if __name__ == "__main__":
    yavas_selam()
