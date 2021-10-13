import EnergiBeregning as calc

tek_07_kontorbygg_True = calc.EnergiBeregning(
    areal_oppv=15000,
    norm_varmekap=65.00,
    kuldebro_normalisert=0.06,
    temp_settpunkt_oppvarming=21.00,
    temp_settpunkt_oppvarming_natt=19.00,
    areal_tak=2500.00,
    areal_vegg_oest=900.00,
    areal_vegg_vest=900.00,
    areal_vegg_soer=900.00,
    areal_vegg_nord=900.00,
    areal_gulv_mot_det_fri=0.00,
    areal_vindu_oest=745.00,
    areal_vindu_vest=745.00,
    areal_vindu_soer=745.00,
    areal_vindu_nord=745.00,
    areal_vindu_tak=0.00,
    areal_dor=20.00,
    U_tak=0.18,
    U_vegg_oest=0.22,
    U_vegg_vest=0.22,
    U_vegg_soer=0.22,
    U_vegg_nord=0.22,
    U_gulv_mot_det_fri=0.18,
    U_dor=1.60,
    U_vindu_oest=1.60,
    U_vindu_vest=1.60,
    U_vindu_soer=1.60,
    U_vindu_nord=1.60,
    U_vindu_tak=1.60,
    varmetapsfaktor_uoppv=0.95,
    areal_mot_uoppvarmet=0.00,
    U_mot_uoppvarmet_sone=0.18,
    areal_gulv_kjeller=2500.00,
    faseforskjell_utetemp_varmetap=1,
    aarsmiddeltemp_inne=21.00,
    omkrets_gulv=200.00,
    U_gulvkonstruksjon=0.15,
    U_kjellerveggskonstruksjon=0.18,
    tykkelse_grunnmur=0.30,
    oppfyllingshoyde_kjellervegg=0.01,
    varmekonduktivitet_kantisol=0.30,
    kantisol_tykkelse=0.20,
    kantisol_horisontal_dybde=0.20,
    kantisol_vertikal_bredde=0.20,
    dybde_periodisk_nedtrengning=3.20,
    varmekonduktivitet_grunn=2.00,
    tempvirkningsgrad_varmegjenvinner=0.70,
    luftmengde_spesifikk_i_driftstid=10.00,
    luftmengde_spesifikk_utenfor_driftstid=3.00,
    terrengskjermingskoeff_e=0.07,
    terrengskjermingskoeff_f=15.00,
    lekkasjetall=1.50,
    etasjehoyde_innvendig=2.80,
    luftmengde_spesifikk_tilluft=10.00,
    luftmengde_spesifikk_avtrekksluft=10.00,
    vifteeffekt_spesifikk_i_driftstid=2.00,
    vifteeffekt_spesifikk_utenfor_driftstid=1.00,
    frostsikringstemperatur=-10.00,
    solskjermingsfaktor_horisont_oest=0.9,
    solskjermingsfaktor_horisont_vest=0.9,
    solskjermingsfaktor_horisont_soer=0.9,
    solskjermingsfaktor_horisont_nord=0.9,
    solskjermingsfaktor_horisont_tak=0.9,
    solskjermingsfaktor_overheng_oest=0.9,
    solskjermingsfaktor_overheng_vest=0.9,
    solskjermingsfaktor_overheng_soer=0.9,
    solskjermingsfaktor_overheng_nord=0.9,
    solskjermingsfaktor_overheng_tak=0.9,
    solskjermingsfaktor_finner_oest=0.9,
    solskjermingsfaktor_finner_vest=0.9,
    solskjermingsfaktor_finner_soer=0.9,
    solskjermingsfaktor_finner_nord=0.9,
    solskjermingsfaktor_finner_tak=0.9,
    arealfraksjon_karm_oest=0.1,
    arealfraksjon_karm_vest=0.1,
    arealfraksjon_karm_soer=0.1,
    arealfraksjon_karm_nord=0.1,
    arealfraksjon_karm_tak=0.1,
    sol_tidsvariabel_soer_jan=0.04,
    sol_tidsvariabel_soer_feb=0.11,
    sol_tidsvariabel_soer_mars=0.17,
    sol_tidsvariabel_soer_april=0.24,
    sol_tidsvariabel_soer_mai=0.27,
    sol_tidsvariabel_soer_juni=0.30,
    sol_tidsvariabel_soer_juli=0.28,
    sol_tidsvariabel_soer_aug=0.26,
    sol_tidsvariabel_soer_sept=0.19,
    sol_tidsvariabel_soer_okt=0.11,
    sol_tidsvariabel_soer_nov=0.08,
    sol_tidsvariabel_soer_des=0.05,
    sol_tidsvariabel_ost_vest_jan=0.01,
    sol_tidsvariabel_ost_vest_feb=0.04,
    sol_tidsvariabel_ost_vest_mars=0.08,
    sol_tidsvariabel_ost_vest_april=0.19,
    sol_tidsvariabel_ost_vest_mai=0.22,
    sol_tidsvariabel_ost_vest_juni=0.32,
    sol_tidsvariabel_ost_vest_juli=0.29,
    sol_tidsvariabel_ost_vest_aug=0.18,
    sol_tidsvariabel_ost_vest_sept=0.10,
    sol_tidsvariabel_ost_vest_okt=0.06,
    sol_tidsvariabel_ost_vest_nov=0.03,
    sol_tidsvariabel_ost_vest_des=0.01,
    sol_tidsvariabel_nord_jan=0.00,
    sol_tidsvariabel_nord_feb=0.00,
    sol_tidsvariabel_nord_mars=0.01,
    sol_tidsvariabel_nord_april=0.05,
    sol_tidsvariabel_nord_mai=0.11,
    sol_tidsvariabel_nord_juni=0.22,
    sol_tidsvariabel_nord_juli=0.16,
    sol_tidsvariabel_nord_aug=0.04,
    sol_tidsvariabel_nord_sept=0.01,
    sol_tidsvariabel_nord_okt=0.00,
    sol_tidsvariabel_nord_nov=0.00,
    sol_tidsvariabel_nord_des=0.00,
    solfaktor_vindu_oest=0.51,
    solfaktor_vindu_vest=0.51,
    solfaktor_vindu_soer=0.51,
    solfaktor_vindu_nord=0.51,
    solfaktor_vindu_tak=0.51,
    solfaktor_total_glass_skjerming_oest=0.25,
    solfaktor_total_glass_skjerming_vest=0.25,
    solfaktor_total_glass_skjerming_soer=0.20,
    solfaktor_total_glass_skjerming_nord=0.27,
    solfaktor_total_glass_skjerming_tak=0.20,
    varmetilskudd_lys_jan=8.00,
    varmetilskudd_lys_feb=8.00,
    varmetilskudd_lys_mar=8.00,
    varmetilskudd_lys_apr=8.00,
    varmetilskudd_lys_mai=8.00,
    varmetilskudd_lys_jun=8.00,
    varmetilskudd_lys_jul=8.00,
    varmetilskudd_lys_aug=8.00,
    varmetilskudd_lys_sep=8.00,
    varmetilskudd_lys_okt=8.00,
    varmetilskudd_lys_nov=8.00,
    varmetilskudd_lys_des=8.00,
    varmetilskudd_utstyr_jan=11.00,
    varmetilskudd_utstyr_feb=11.00,
    varmetilskudd_utstyr_mar=11.00,
    varmetilskudd_utstyr_apr=11.00,
    varmetilskudd_utstyr_mai=11.00,
    varmetilskudd_utstyr_jun=11.00,
    varmetilskudd_utstyr_jul=11.00,
    varmetilskudd_utstyr_aug=11.00,
    varmetilskudd_utstyr_sep=11.00,
    varmetilskudd_utstyr_okt=11.00,
    varmetilskudd_utstyr_nov=11.00,
    varmetilskudd_utstyr_des=11.00,
    varmetilskudd_person_jan=4.00,
    varmetilskudd_person_feb=4.00,
    varmetilskudd_person_mar=4.00,
    varmetilskudd_person_apr=4.00,
    varmetilskudd_person_mai=4.00,
    varmetilskudd_person_jun=4.00,
    varmetilskudd_person_jul=4.00,
    varmetilskudd_person_aug=4.00,
    varmetilskudd_person_sep=4.00,
    varmetilskudd_person_okt=4.00,
    varmetilskudd_person_nov=4.00,
    varmetilskudd_person_des=4.00,
    energibehov_tappevann=5.00,
    energibehov_belysning=25.00,
    energibehov_utstyr=34.00,
    areal_avkjoelt_andel=1.00,
    temp_settpunkt_kjoeling=22.00,
    pumpeeffekt_spesifikk_oppv=0.50,
    tid_drift_pumpe_oppv=4000,
    temp_differanse_veskekrets_oppvarming=20.00,
    pumpeeffekt_spesifikk_kjoling=0.6,
    tid_drift_pumpe_kjoling=2890,
    temp_differanse_veskekrets_kjoling=4.00,
    el_solcelle_andel_el_spesifikt_forbruk=0,
    el_er_andel_energi_oppv_ventilasjon=0.4,
    el_hp_andel_energi_oppv_ventilasjon=0,
    el_Tsol_andel_energi_oppv_ventilasjon=0,
    el_er_andel_energi_tappevann_varme=0.2,
    el_hp_andel_energi_tappevann_varme=0,
    el_Tsol_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_solcelle=100,
    systemvirkningsgrad_elektrisk_oppv_ventilasjon=0.98,
    systemvirkningsgrad_elektrisk_tappevann_varme=0.98,
    systemvirkningsgrad_varmepumpeanlegg_oppv_ventilasjon=2.26,
    systemvirkningsgrad_varmepumpeanlegg_tappevann_varme=2.26,
    systemvirkningsgrad_solfanger_termisk_oppv_ventilasjon=8.12,
    systemvirkningsgrad_solfanger_termisk_tappevann_varme=8.12,
    effektfaktor_kjoeleanlegg=2.4,
    olje_andel_energi_oppv_ventilasjon=0.3,
    olje_andel_energi_tappevann_varme=0.5,
    systemvirkningsgrad_olje_oppv_ventilasjon=0.77,
    systemvirkningsgrad_olje_tappevann_varme=0.77,
    gass_andel_energi_oppv_ventilasjon=0.1,
    gass_andel_energi_tappevann_varme=0.1,
    systemvirkningsgrad_gass_oppv_ventilasjon=0.81,
    systemvirkningsgrad_gass_tappevann_varme=0.81,
    fjernvarme_andel_energi_oppv_ventilasjon=0.2,
    fjernvarme_andel_energi_tappevann_varme=0.2,
    systemvirkningsgrad_fjernvarme_oppv_ventilasjon=0.88,
    systemvirkningsgrad_fjernvarme_tappevann=0.88,
    bio_andel_energi_oppv_ventilasjon=0,
    bio_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_bio_oppv_ventilasjon=0.73,
    systemvirkningsgrad_bio_tappevann=0.73,
    annet_andel_energi_oppv_ventilasjon=0,
    annet_andel_energi_tappevann_varme=0,
    systemvirkningsgrad_annet_oppv_ventilasjon=0.5,
    systemvirkningsgrad_annet_tappevann=0.5,
    CO2_faktor_el=0.357,
    CO2_faktor_olje=0.273,
    CO2_faktor_gass=0.202,
    CO2_faktor_fjernvarme=0.176,
    CO2_faktor_bio=0.025,
    CO2_faktor_annet=0,
    Primaerenergi_faktor_el=1.5,
    Primaerenergi_faktor_olje=1.35,
    Primaerenergi_faktor_gass=1.36,
    Primaerenergi_faktor_fjernvarme=1.25,
    Primaerenergi_faktor_bio=1.05,
    Primaerenergi_faktor_annet=1,
    Energipris_el=0.8,
    Energipris_olje=0.9,
    Energipris_gass=0.75,
    Energipris_fjernvarme=0.55,
    Energipris_bio=0.35,
    Energipris_annet=0.9,
    Energipol_vektingsfaktor_el=1.2,
    Energipol_vektingsfaktor_olje=1.5,
    Energipol_vektingsfaktor_gass=1.3,
    Energipol_vektingsfaktor_fjernvarme=1.05,
    Energipol_vektingsfaktor_bio=0.8,
    Energipol_vektingsfaktor_annet=0.9,
    tid_drift_oppv_belysn_utstyr_jan=372,
    tid_drift_oppv_belysn_utstyr_feb=336,
    tid_drift_oppv_belysn_utstyr_mar=372,
    tid_drift_oppv_belysn_utstyr_apr=360,
    tid_drift_oppv_belysn_utstyr_mai=372,
    tid_drift_oppv_belysn_utstyr_jun=360,
    tid_drift_oppv_belysn_utstyr_jul=372,
    tid_drift_oppv_belysn_utstyr_aug=372,
    tid_drift_oppv_belysn_utstyr_sep=360,
    tid_drift_oppv_belysn_utstyr_okt=372,
    tid_drift_oppv_belysn_utstyr_nov=360,
    tid_drift_oppv_belysn_utstyr_des=372,
    tid_drift_vent_jan=372,
    tid_drift_vent_feb=336,
    tid_drift_vent_mar=372,
    tid_drift_vent_apr=360,
    tid_drift_vent_mai=372,
    tid_drift_vent_jun=360,
    tid_drift_vent_jul=372,
    tid_drift_vent_aug=372,
    tid_drift_vent_sep=360,
    tid_drift_vent_okt=372,
    tid_drift_vent_nov=360,
    tid_drift_vent_des=372,
    tid_drift_person_jan=372,
    tid_drift_person_feb=336,
    tid_drift_person_mar=372,
    tid_drift_person_apr=360,
    tid_drift_person_mai=372,
    tid_drift_person_jun=360,
    tid_drift_person_jul=372,
    tid_drift_person_aug=372,
    tid_drift_person_sep=360,
    tid_drift_person_okt=372,
    tid_drift_person_nov=360,
    tid_drift_person_des=372,
    utetemp_jan=-3.7,
    utetemp_feb=-4.8,
    utetemp_mar=-0.5,
    utetemp_apr=4.8,
    utetemp_mai=11.7,
    utetemp_jun=16.5,
    utetemp_jul=17.5,
    utetemp_aug=16.9,
    utetemp_sep=11.5,
    utetemp_okt=6.4,
    utetemp_nov=0.5,
    utetemp_des=-2.5,
    aarsmiddeltemp_ute=7.50,
    straalingsfluks_soer_jan=28.00,
    straalingsfluks_soer_feb=61.00,
    straalingsfluks_soer_mars=106.00,
    straalingsfluks_soer_april=135.00,
    straalingsfluks_soer_mai=134.00,
    straalingsfluks_soer_juni=150.00,
    straalingsfluks_soer_juli=140.00,
    straalingsfluks_soer_aug=142.00,
    straalingsfluks_soer_sept=113.00,
    straalingsfluks_soer_okt=70.00,
    straalingsfluks_soer_nov=44.00,
    straalingsfluks_soer_des=28.00,
    straalingsfluks_ostvest_jan=11.00,
    straalingsfluks_ostvest_feb=32.00,
    straalingsfluks_ostvest_mars=55.00,
    straalingsfluks_ostvest_april=112.00,
    straalingsfluks_ostvest_mai=124.00,
    straalingsfluks_ostvest_juni=166.00,
    straalingsfluks_ostvest_juli=142.00,
    straalingsfluks_ostvest_aug=109.00,
    straalingsfluks_ostvest_sept=66.00,
    straalingsfluks_ostvest_okt=37.00,
    straalingsfluks_ostvest_nov=18.00,
    straalingsfluks_ostvest_des=9.00,
    straalingsfluks_nord_jan=6.00,
    straalingsfluks_nord_feb=17.00,
    straalingsfluks_nord_mars=25.00,
    straalingsfluks_nord_april=50.00,
    straalingsfluks_nord_mai=75.00,
    straalingsfluks_nord_juni=98.00,
    straalingsfluks_nord_juli=83.00,
    straalingsfluks_nord_aug=54.00,
    straalingsfluks_nord_sept=36.00,
    straalingsfluks_nord_okt=16.00,
    straalingsfluks_nord_nov=7.00,
    straalingsfluks_nord_des=3.00,
    straalingsfluks_tak_jan=13.00,
    straalingsfluks_tak_feb=43.00,
    straalingsfluks_tak_mars=90.00,
    straalingsfluks_tak_april=153.00,
    straalingsfluks_tak_mai=198.00,
    straalingsfluks_tak_juni=249.00,
    straalingsfluks_tak_juli=219.00,
    straalingsfluks_tak_aug=175.00,
    straalingsfluks_tak_sept=107.00,
    straalingsfluks_tak_okt=45.00,
    straalingsfluks_tak_nov=19.00,
    straalingsfluks_tak_des=8.00,
    temp_avtrekk=22.0,
    varmekapasitet_luft=0.33,
    temp_amplitudevar=11.2,
    tid_jan=0.744,
    tid_feb=0.672,
    tid_mar=0.744,
    tid_apr=0.72,
    tid_mai=0.744,
    tid_jun=0.72,
    tid_jul=0.744,
    tid_aug=0.744,
    tid_sep=0.72,
    tid_okt=0.744,
    tid_nov=0.72,
    tid_des=0.744,
    varmekapasitet_vann=4180,
    densitet_vann=988,
    varmekapasitet_kuldebaerer=4210,

    densitet_kuldebaerer=999.8,
    BygningskategoriErForretningsbygg=True,
)

tek_07_kontorbygg_True_expected_output = calc.Output(
    Romoppvarming=805611,
    Ventilasjonsvarme=0,
    Varmtvann=75000,
    Vifter=419750,
    Belysning=375000,
    Pumper=11619,
    Teknisk_utstyr=510000,
    Kjoeling=798836,
    Totalt_netto_energibehov=2995815,
    Elektrisitet=1993344,
    Olje=362576,
    Gass=108717,
    Fjernvarme=200139,
    Biobrensel=0,
    Annen_energivare=0,
    Totalt_levert_energi=2664776,
    Primaerenergi=3877522,
    CO2_utslipp=867792,
    Energi_kostnader=2112607,
    Energi_politisk=3287354 ,
)

