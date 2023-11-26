card_trans_regx = "\d{2}\s\w{3}\s\d{4}\s\d{7}" #24 FEB 5637 5515323 (card payment)
date_pattern = "\d{2}\s[A-Z]{3}" #24 MAR
paynow_trans = "\d{2}\s\w{3}\sPAYNOW-FAST" # paynow payment
credit_trans = "SG\d*\.\d{2}" # withdraw/credit amount with SG prefix
floating_number_prefix_space = "\s\d*\,*\d*\.\d{2}" # total balance 



""" PAYNOW: Out

sample 1
    Row 162: 09 Mar PAYNOW-FAST
    Row 163: PIB2303098706863431
    Row 164: YONG WEN FOOD (S) PT
    Row 165: OTHR Transfer - UEN133.92 105,439.10   

sample 2 
    Row 291: 20 Mar PAYNOW-FAST
    Row 292: PIB2303198771497263
    Row 293: AL FALAH RESTAURANT            
    Row 294: OTHR Transfer - UEN21.00 103,873.86   

sample 3 
    Row 345: 22 Mar PAYNOW-FAST
    Row 346: SL2 Muffin
    Row 347: MBK23032287887912631.80 101,019.45   

sample 4
    Row 348: 22 Mar PAYNOW-FAST
    Row 349: PIB2303228789772888
    Row 350: COMFORTDELGRO DRIVIN
    Row 351: OTHR M006208350008986151100.00 100,919.45   

sample 5
    13 Mar PAYNOW-FAST
    THIO HUI HOON
    MBK230312872270589478.00 105,368.82   


"""


""" PAYNOW: In
Sample 1 
    Row 287: 18 Mar PAYNOW-FAST
    Row 288: PIB2303188766742448
    Row 289: Zaw Myo Latt
    Row 290: OTHR Transfer - Mobile10.00 103,894.86   

Sample 2 
    Row 433: 31 Mar PAYNOW-FAST
    Row 434: PAYNOW OTHR
    Row 435: YAHYA BIN SLAMAT
    Row 436: PayNow Transfer1,000.00 136,621.92 
"""