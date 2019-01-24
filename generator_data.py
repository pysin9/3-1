from dbModel import *

name = ["Lickers","Brotherbird Milk & Croissants","Aqua S"," C Plus","A Summer in Paris","Tarte by Cheryl Koh","D9 Cakery","FATCAT Ice Cream Bar","Caffe Fernet","House of MU",
        " Brewerkz Restaurant & Microbrewery","Ramen Keisuke Tonkotsu King"," Ramen Keisuke Tori King","4Fingers Crispy Chicken","Nong Khai Beer House","IPPUDO - Mandarin Gallery","Komala Vilas Restaurant","Al-Azhar Eating Restaurant","Salmon Samurai","Kinki Restaurant & Bar",
"Chicken Up","Lucha Loco","Kim Dae Mun Korean Food","Jai Thai","Nakhon Kitchen","Bei-ing Wanton Mee","Prawnaholic","Jin Ji Teochew Braised Duck","Burgernomics","Yaowarat Thai Kway Chap",
"Hao Lai Ke","Oinkers & Buns","Yokozuna Stall","House of Happiness","Boon’s Noodles","Haru","Two Hana","Two Men Bagel House 2.0","Grids and Circles","Columbus Coffee Co.",
"Clan Cafe","Seven and Ate","Earlybird","Five Oars Coffee Roasters","Bearded Bella","Loving Hut","Komala Vilas Restaurant","Zi Zai Vegetarian(Yishun)","nomVnom","GreenDot",
"Annalakshmi","Kailash Parbat","Hwa Jin Vegetarian Family Restaurant"," Pepper Jade Thai Vegetarian Cuisine","Gokul Vegetarian Restaurant","Spize","Selera Rasa Nasi Lemak","Singapore Zam Zam Restaurant","Halia Restaurant","Hajah Maimunah Restaurant",
"Projcet Acai, Holland Village","Loving Hut","Shinkansen","Afterglow by Anglow","Kilo at Pact","VeganBurg","HICJUICE","Real Food ","GAEST","The Lawn",
"Beng Hiang Restaurant","Bee Heong Palace Restaurant","Beng Thin Hoon Kee Restaurant"," Quan Xin Yuan Restaurant","Spring Court (Yong Chun Yuan) Restaurant","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
    ]

picture = ["https://lh5.googleusercontent.com/p/AF1QipMvBwU-Q-_Muj-Z5mEXbuOIY907FfX8bmtYBP0h=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipODWZFx0zzfZkQPqPSwlmlRkvkL4ZxCDC8zJ6rO=w408-h544-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipNsGQwGXK2HjRg9MpGPuUP6bPwN_vWpakUaytVp=w408-h544-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOCRiN2TCaujggI1nX7IZrIkPbl8dm__AjflTLY=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipN5pTz0c8-8s3o48HxO_fJQEQTLiwR4i8Z8cPDq=w408-h544-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipO2hjihB0WDih5FMNzTqOHnS66EXnUjTPCwMn-f=w408-h306-k-no",
           "https://lh3.googleusercontent.com/proxy/3axcPBn-FL-aqAxR_z8uGSWGe6pKD0Tp-BCwqR3nJv6FpnCbGTqdXoxlLg4_QsqTMXJb4tFG1vDhuxKqMnhcEA3jkDZkZ_AbdgJGGxSV1JFhANiVEc5oz2hYBXa7GPQKFRybxz2YiMDGLSWHFJ2tNC0fQy0CRvs=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMBW8dM6fDXut6cj3hpE05O1rKCV-l9Xg-6yJ-W=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipP3I2w5_ERZjtAKvKk1kABi4Sq6qEZuV9vaQeUv=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNFXBToIYaBH8tH41sMQy8WsiZXT81RvbK_oq7P=w408-h306-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipNrXRtHHu3-nqXY55tUnTT_S_awsySnCo8WtFk9=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipM93Gjm5Bs104QJsRv8_KE-ZlOO5_AN7UIxWk-w=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOA6FezECWZEWWnXBxm20M3_Um-2dkoQ_rpvCON=w408-h270-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPeqg96l8H8b_vdIDcZIH3e05TwQraLRmxgI77U=w408-h725-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPHoSP4w4ufNVdMbr2-w1H0Qi8SLsXtkre67U9M=w408-h271-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMoISQ4jrO3uE1Ib0giwyEVGHkRXNtw3fuVO00j=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMb8hyX3fEVssnwSTuo9gSMWwD1qoX5-xEIThZi=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipP5y1jtcIdFj1R2X4snzVHR1PMtcPauyDNJRx9q=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMJ0mf4snt49oOu7fC7bUhLkWLOI4yZvL7EbrLk=w408-h544-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNk7wlGRGoOHHNlOV7gwxbvzc11GaaQ-PbH8RIs=w408-h306-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipMEYY5_Kc6-LLyhrLImIJAX3uemMzuDv0A8Ge5I=w408-h271-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNVhYZlM8_QYX0YILAfNZZOy11jmPbDoHGZNqDT=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOPWnnvSOpPHq9F5C-2iViDJkRSBDWxs6CLQQbS=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMOBDqvVtUs-xMZLIoqcUugOvyd1JT-Xz7jxkLC=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPeVP-ozujbMF6C_KjVtWpS7t1o1NX6PSmcSaNj=w408-h544-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPHsg5fhKtmOvQoRZp2mgsfn5F2MFNhJyzhPMan=w408-h408-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPE3L6fvzXrDwuChYGyPPij2U-PsDg9xdUcMWSi=w408-h408-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOMK5O36fxZHev_xUC-7wTzFcPzODtVLQ7fNvmE=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMbHspKh8d7Ysa_LLjRnnbIM3FBOXbnJ2IyyTjn=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPucbkUDHioec2Gu125KI8jvK70Pw7OD9eB23EQ=w408-h306-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipNFRiXIEZRR7aeVsCRjWOuH_G5OileAihZaeLPI=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipP_4t8Yr3ob71A7qYL1he8aTz7z_Hkz34IXelf8=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMpYiUYc7hMkDSaoJ8jDPlpG2ptryB9U2swbzs-=w408-h368-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNBcxFFUCY6ELp8WjUOwo0a3LHtCjZKQprf4l5h=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNO-PevCy1PKGWad8UQ0jDp5Wa0H_ZK7w57wU0e=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOQJFxkTYFNJwKcJ-AOcI2r-nvY-4snH3rQoYZC=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipP4HH2eCRJFqcIhMt7IM_foQ3Kjy1p-xrJgHi4x=w408-h544-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOI4kZpXmU1ioBAThxBU0ZBnEfTB4MkhujXVTTv=w408-h229-k-no",
           "https://www.google.com/maps/place/Grids+%26+Circles/@1.2835445,103.8459553,3a,75y,90t/data=!3m8!1e2!3m6!1sAF1QipMRc2Aa-ygCOTp83yGsEXXwQTYmES79NxEzGmt0!2e10!3e12!6shttps:%2F%2Flh5.googleusercontent.com%2Fp%2FAF1QipMRc2Aa-ygCOTp83yGsEXXwQTYmES79NxEzGmt0%3Dw203-h152-k-no!7i4032!8i3024!4m5!3m4!1s0x31da194830928aeb:0xc461df9f6136fa95!8m2!3d1.2835445!4d103.8459553#",
           "https://lh5.googleusercontent.com/p/AF1QipMzvQYY4F8MQoIVr4pygDLgnRumZejutGoj9oSP=w408-h306-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipNsSI_QhNHkcwZ6MfMpM6AV66yzPcMwsSsBQFb2=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMc7pmY5qjfQZU1yF1SpXNMy3n2qoRjqTI90BEo=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipM34BMBuJc-UqF4LAaFeK16sux5iEH1IF25HQBH=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOBs-IwkmiA8bjG5Y4836Dx7CAqIwNU6EzFQGg=w408-h257-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOZswoNgAQPzJq98NP6y88Z1uvmH5uJ21KOLOae=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipM9UtZsSQwnRD8DEMssWmMnYcWwoWxh-sitv-dZ=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMb8hyX3fEVssnwSTuo9gSMWwD1qoX5-xEIThZi=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipO2BAll7-af59V33OC4LrrnEJme0d528ZZ6kWmf=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNVe4oT6gqrJs2iYP2ju3N3H_0-UTsAsHXGkrNi=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipO1C1Zyubv0mU7DaM4wXms305uDWl1ToTJHF8P7=w408-h300-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipMvoa-Dj9T3OlLJxJo_wVlsgr9dekC00lEFoBrA=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOp4oql3490_rsWJdkVAh9ne-XiPyruAhNl-jIe=w408-h200-k-no-pi-0-ya126.15473-ro-0-fo100",
           "https://lh5.googleusercontent.com/p/AF1QipOnERlEq0vD6DkTaFvD060qh2HSuK4hVi0f0v0Z=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNwhuCG-4hTm-Pug_OsrVezQxo_uVD6FBi2echq=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNN06t0FGx7CMTf8p7cohHn1NK365F3cDWtie2f=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipONiv4bQRAVMLWLUQOfqx1eZKXZiinq9EsIXsfm=w408-h264-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMmf5eCKyj83SbkWH7_SMjKOq2sheEKpYHGbFsP=w408-h244-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNYdWnmdo52JETesMY1sHDyJZgiKkdLnlgly_3d=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMLJ7Uj9anP9RyycPXjxj9ryzPnySDyRn6MvmYF=w408-h316-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPPpqDqWYZzmYGeFDEDb9YvbWT-6MTZoGU21Blk=w408-h229-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipNtYsxu6IhH9CRrRaJbO1J5MaUmKlo0Gu1kGBP2=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipM9UtZsSQwnRD8DEMssWmMnYcWwoWxh-sitv-dZ=w408-h272-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNxToLF7drB-uV2t25fLxV42N_H5Fjw3-OJJMpA=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipPRKh6uzeYO9bqNgnbuXuVSL9OAqTHelsL2piC0=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNErxGD-j1eHBn_LioWQFwrX3vl6Hv94o5QkYLh=w408-h220-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipN0lPdV6wF-4V0hcsLOydvZs4EQZ9R92n35Zqpg=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipMhcWClWBnOzW94MO1fjt_svkgzewXk6Doo-mMq=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOHoJucXZ3po4UZFuFsS93vbTP1_uJbPYTS_0WF=w408-h306-k-no",
           "https://lh3.googleusercontent.com/proxy/YWebdbFPRoeHG4w_ByPrc_SSPRbTw_i7FoMwbrT8ywyZ0YvhQMe2hJaM81rQC1LzjokyODeZr1okI8hjdGd_vCU9wU9KRW-4gRJ8gY0_f4ZpUgiaeRSIwmCqIvxf3Bef7rpO2MMM4B_dLDG_jvMkdFy9BhaZyRk=w408-h305-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipNFcFctqyxgVChtlB6o8QZ2In858rN3rOCPpQ9Q=w408-h306-k-no",
            "https://lh5.googleusercontent.com/p/AF1QipP6flUl8zw8NGGyKlKQJFfu3h3q7pptHTnxK4Rq=w408-h271-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipO_-NXqN9tmlc3Alu8AX3k2CGsDScmVLEL0sxIy=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOI8HHJstUsryF2bZXynNDyqilg4NYWWRnC0LZ9=w408-h229-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipP6kwTyXSxxrSKnRXySdlzuAIaactWuo_QtNezX=w408-h306-k-no",
           "https://lh5.googleusercontent.com/p/AF1QipOGWwfCNdKvPqC09tH_4lduLBkX6tvxlP3Cjwc=w408-h306-k-no",
           "","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
            "","","","","","","","","","",
           ]

color = [ "#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59","#fc8d59",
"#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#de2d26",
"#de2d26","#de2d26","#de2d26","#de2d26","#de2d26","#A0522D","#A0522D","#A0522D","#A0522D","#A0522D",
"#A0522D","#A0522D","#A0522D","#A0522D","#A0522D","#E4D03B","#E4D03B","#E4D03B","#E4D03B","#E4D03B",
"#E4D03B","#E4D03B","#E4D03B","#E4D03B","#E4D03B","#377eb8","#377eb8","#377eb8","#377eb8","#377eb8",
"#377eb8","#377eb8","#377eb8","#377eb8","#377eb8","#000000","#000000","#000000","#000000","#000000",
"#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a","#4daf4a",
"#984ea3","#984ea3","#984ea3","#984ea3","#984ea3","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
   ]

longitude = [ "103.8843973","103.8609518","103.8300997","103.8502038","103.819862","103.8292059","103.829335","103.928434","103.8516478","103.8188168",
"103.825078","103.825078","103.8413928","103.8217352","103.8631039","103.8368073","103.8490366","103.9517828","103.8433107","103.851259",
"103.835938","103.8405395","103.8402216","103.8336555","103.8573473","103.9015433","103.9493567","103.8410025","103.9493366","103.8840357",
"103.9279161","103.8443955","103.8515885","103.946526","103.8615516","103.8403082","103.9413478","103.8409243","103.8459553","103.8331812",
"103.8381863","103.8585324","103.8560007","103.8418214","103.8406549","103.8990962","103.8490366","103.8186145","103.8500369","103.8500369",
"103.8352553","103.8529521","103.7490222","103.8486151","103.8502851","103.7784503","103.8120792","103.8562698","103.8127923","103.7458216",
"103.7926024","103.8990962","103.8494971","103.8395119","103.8381399","103.9032825","103.8441913","103.8368403","103.8450926","103.79018",
"103.7380412","103.8269578","103.8469862","103.8560215","103.8423406","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
   ]

latitude = [ "1.352906","1.3118102","1.3033599","1.3177517","1.2650312","1.3065541","1.3058257","1.3284617","1.2828581","1.2828579",
"1.286956","1.2869556","1.274556","1.3005412","1.3028085","1.3019764","1.3071201","1.3520833","1.2787619","1.282568",
"1.2825679","1.278802","1.3004315","1.3004315","1.3581103","1.304875","1.3734568","1.2825943","1.3734203","1.3613732",
"1.3260529","1.279482","1.3402269","1.331614","1.3031133","1.3085134","1.3522959","1.320691","1.2835445","1.3527963",
"1.279295","1.3106718","1.302876","1.2791177","1.277528","1.3111451","1.3071201","1.3759865","1.3125818","1.3125817",
"1.2791177","1.3088181","1.361389","1.3004116","1.3035254","1.346402","1.324144","1.3022337","1.311345","1.3113684",
"1.3103487","1.3111451","1.2828779","1.2801279","1.3004991","1.3209476","1.282349","1.2994795","1.2795028","1.3045496",
"1.3339432","1.3715312","1.285069","1.3096564","1.2843513","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
   ]

location = [ "Blk #01-1446, 124 Hougang Avenue 1, Block 124","114 Lavender Street, #01-05, CT Hub 2","437 Orchard Rd, #B1-01","217 Rangoon Rd","1 Harbourfront Walk, #01-13 VivoCity","1 Scotts Rd #02-12 Shaw Centre","581 Orchard Rd","Bedok North Ave 2, #01-25 Block 416","70 Collyer Quay, #01-05 Customs House","11 Mohamed Sultan Rd",
"30 Merchant Rd, #01-05/06 Riverside Point","1 Tras Link","#03, 100 Tras St, 15 100 AM","277 Orchard Rd, #01-04/05 Orchard Gateway","1 Beach Rd","333A Orchard Rd #04-02 to 04","76-78 Serangoon Rd","Tampines Street 21, #01-1105 Block 201D","100 Tras Street, #01-11","70 Collyer Quay, #02-02 Customs House",
"#01, 48 Tg Pagar Rd, 01","15 Duxton Hill","100 Orchard Rd, #01-03D Concorde Shopping Mall","27 Purvis St, #01-01 An Chuan Building","212 Hougang Street 21, #01-341","50 E Coast Rd","110 Pasir Ris Central, #02-12","335 Smith St, #02-156","110 Pasir Ris Central, #02-03","945 Upper Serangoon Rd",
"204 Bedok North Street 1, #01-393","02-106 7 Maxwell Street (Amoy Street Food Centre","211 Lor 8 Toa Payoh, #01-01","294 Bedok Rd","505 Beach Rd, #01-86","100 Guillemard Rd, #01-06","Century Square, #01-21, 2 Tampines Central 5","103 Irrawaddy Rd, #01-04 Royal Square","200 South Bridge Rd","220 Upper Thomson Rd Thomson Garden Estate",
"31 Bukit Pasoh Rd","78 Horne Rd","17 Jln Pinang","39 Tg Pagar Rd","8 Craig Rd","229 Joo Chiat Rd, #01-01","76-78 Serangoon Rd","236 Yishun Ring Rd","6 Eu Tong Sen Street, #03-105/106/107","60 Paya Lebar Rd, #02-15",
"#01, 20 Havelock Rd, 04 Central Square","93 Syed Alwi Rd","359 Bukit Batok Street 31, #01-393","91 Bencoolen St, 18-19/20 Sunshine Plaza","19 Upper Dickson Rd","131 Rifle Range Rd, #03-04","","697-699 North Bridge Rd","1 Cluny Road, Ginger Garden Singapore Botanic Garden","11 Jln Pisang8",
"27 Lor Liput, Holland Village","229 Joo Chiat Rd, #01-01","10 Collyer Quay B1-08 Ocean Financial Centre","24 Keong Saik Rd","181 Orchard Rd","44 Jln Eunos","31 Club St, #01-01","181 Orchard Road, #02-16 to 19 Orchard Central","21 McCallum St","31 Biopolis Way #01-07 Nanos",
"135 Jurong Gateway Rd, #02-337","4 jalan leban, Sembawang hills Estate","#05-02 OCBC Centre, 65 Chulia St","252 Jln Besar","52-56 Upper Cross St","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
]

category = [ ]

postal_code = [ "Singapore 530124","Singapore 338729","Singapore 238878","Singapore 218457","Singapore 098585","Singapore, 228208","Singapore 238883","Singapore 460416","Singapore 049323","Singapore 239010",
"Singapore 058282","Singapore 078867","Singapore 079027","Singapore 238858","Singapore 189673","Singapore 238897","Singapore 217981","Singapore 524201","Singapore 079027","Singapore 049323",
"Singapore 088469","Singapore 089598","Singapore 238840","Singapore 188604","Singapore 530212","Singapore 428769","","Singapore 050335","","Singapore 534711",
"Singapore 460204","Singapore 069111","Singapore 310211","Singapore 469450","Singapore 199583","Singapore 399718","Singapore 529509","Singapore 329566","Singapore 058749","Singapore 574352",
"Singapore 089845","Singapore 209078","Singapore 199149","Singapore 088462","Singapore 089668","Singapore 427489","Singapore 217981","Singapore 760236","Singapore 059817","Singapore 409051",
"Singapore 059765","Singapore 207669","Singapore 650359","Singapore 189652","Singapore 207478","Singapore 588406","8RF7+MP Singapore","Singapore 198675","Singapore 259569","Singapore 19907",
"Singapore 277738","Singapore 427489","Singapore 049315","Singapore 089131","Singapore 238896","Singapore 419502","Singapore 069468","Singapore 238896","Singapore 069047","Singapore 138669",
"Singapore 600135","Singapore 577548","Singapore 049513","Singapore 208925","Singapore 058348","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",
"","","","","","","","","","",]

if __name__ == '__main__':
    print('Start Generator Data......')
    for colors in color:
        if colors == "#de2d26":
            index_category = "Spicy"
            category.append(index_category)
        elif colors == "#000000":
            index_category = "Halal"
            category.append(index_category)
        elif colors == "#377eb8":
            index_category = " Vegertarian"
            category.append(index_category)
        elif colors == "#4daf4a":
            index_category = "Healthy"
            category.append(index_category)
        elif colors == "#984ea3":
            index_category = "Elder friendly"
            category.append(index_category)
        elif colors == "#fc8d59":
            index_category = " Desert"
            category.append(index_category)
        elif colors == "#A0522D":
            index_category = "Hawker"
            category.append(index_category)
        elif colors == "#E4D03B":
            index_category = "Cafes"
            category.append(index_category)
        else:
            index_category = None
            category.append(index_category)
    for index in range(len(name and picture and color and longitude and latitude and location and category and postal_code)):
        index_name = name[index]
        index_picture = picture[index]
        index_color = color[index]
        index_longtitude = longitude[index]
        index_latitude = latitude[index]
        index_location = location[index]
        index_category = category[index]
        index_postal_code = postal_code[index]
        insert_data = MapPlace(
            Name=index_name ,
            Picture=index_picture,
            Color=index_color,
            Longitude=index_longtitude,
            Latitude=index_latitude,
            Location=index_location,
            Category=index_category,
            Postal_Code=index_postal_code
        )
        db.session.add(insert_data)
    db.session.commit()
    print('Generator Data Done')
