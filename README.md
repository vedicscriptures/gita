---
description: A public service Bhagavad Gita API is A lightweight Rest API
---

# Bhagavad Gita Api

![Bhagavad Gita API](https://repository-images.githubusercontent.com/314205765/0bb18d80-2b22-11eb-8f6f-ccf20c0c2679)

 [![Devloper](https://img.shields.io/badge/Devloper-Pt.%20Prashant%20Tripathi-Success.svg?style=flat-square)](https://github.com/PtPrashantTripathi) [![License](https://img.shields.io/github/license/vedicscriptures/bhagavad-gita-api.svg?style=flat-square)](https://github.com/vedicscriptures/bhagavad-gita-api/LICENSE) [![Website Status](https://img.shields.io/website/http/ptprashanttripathi.github.io.svg?down_message=Down&up_message=Online&style=flat-square)](https://vedicscriptures.github.io) [![stars-shield](https://img.shields.io/github/stars/vedicscriptures/bhagavad-gita-api.svg?style=flat-square)](https://github.com/vedicscriptures/bhagavad-gita-api/stargazers) [![forks-shield](https://img.shields.io/github/forks/vedicscriptures/bhagavad-gita-api.svg?style=flat-square)](https://github.com/vedicscriptures/bhagavad-gita-api/network/members) [![Total-Downlode](https://img.shields.io/github/downloads/vedicscriptures/bhagavad-gita-api/total.svg?style=flat-square)](https://github.com/vedicscriptures/bhagavad-gita-api/graphs/traffic)

 [View Demo](https://vedicscriptures.github.io) · [Report Bug](https://github.com/vedicscriptures/bhagavad-gita-api/issues/new/choose) · [Request Feature](https://github.com/vedicscriptures/bhagavad-gita-api/issues/new/choose)

 Loved the tool? Please consider [donating](https://paypal.me/ptprashanttripathi/100) 💸 to help it improve!  
  
 [![Donate](https://img.shields.io/badge/support-PayPal-blue?logo=PayPal&style=flat-square&label=Donate)](https://paypal.me/PtPrashantTripathi) [![Buy Coffee for ptprashanttripathi](https://cdn.ko-fi.com/cdn/kofi3.png?v=2)](https://ko-fi.com/ptprashanttripathi) [![Buy Me A Coffee](https://cdn.buymeacoffee.com/buttons/default-orange.png)](https://www.buymeacoffee.com/ptprashanttripathi) [![Support Via UPI](https://raw.githubusercontent.com/PtPrashantTripathi/linkpe/main/img/linkpebadge.svg)](https://ptprashanttripathi.github.io/linkpe?pa=pt1998@ybl&pn=Pt.+Prashant+Tripathi)

### About

> Bhagavad-Gita-API is A lightweight Node.js based Bhagavad Gita API server

### 🚀 How to use

#### 4. GET \[/:ch\]

> GET Particular Chapters details of Shreemad Bhagavad Gita

* **`URL`** [`https://bhagavadgitaapi.in{/:ch}`](https://bhagavadgitaapi.in/1)
* **`Method`** : **`GET`**
* **`Attributes`** :
  * **`:ch`** : `[interger]` specfic chapter number from any of 18 chapters 
* **`Response 200`**  :  **`(application/json)`**  

```perl
{
  "chapter_number": 1,
  "verses_count": 47,
  "name": "अर्जुनविषादयोग",
  "translation": "Arjuna Visada Yoga",
  "transliteration": "Arjun Viṣhād Yog",
  "meaning": {
    "en": "Arjuna's Dilemma",
    "hi": "अर्जुन विषाद योग"
  },
  "summary": {
    "en": "The first chapter of the Bhagavad Gita - Arjuna Vishada Yoga introduces the setup, the setting, the characters and the circumstances that led to the epic battle of Mahabharata, fought between the Pandavas and the Kauravas. It outlines the reasons that led to the revelation of the of Bhagavad Gita.\nAs both armies stand ready for the battle, the mighty warrior Arjuna, on observing the warriors on both sides becomes increasingly sad and depressed due to the fear of losing his relatives and friends and the consequent sins attributed to killing his own relatives. So, he surrenders to Lord Krishna, seeking a solution. Thus, follows the wisdom of the Bhagavad Gita.",
    "hi": "भगवद गीता का पहला अध्याय अर्जुन विशाद योग उन पात्रों और परिस्थितियों का परिचय कराता है जिनके कारण पांडवों और कौरवों के बीच महाभारत का महासंग्राम हुआ। यह अध्याय उन कारणों का वर्णन करता है जिनके कारण भगवद गीता का ईश्वरावेश हुआ। जब महाबली योद्धा अर्जुन दोनों पक्षों पर युद्ध के लिए तैयार खड़े योद्धाओं को देखते हैं तो वह अपने ही रिश्तेदारों एवं मित्रों को खोने के डर तथा फलस्वरूप पापों के कारण दुखी और उदास हो जाते हैं। इसलिए वह श्री कृष्ण को पूरी तरह से आत्मसमर्पण करते हैं। इस प्रकार, भगवद गीता के ज्ञान का प्रकाश होता है।"
  }
}
```

#### 5. GET \[/:ch/:sl\]

> GET JSON of Slok from Particuler slok & chapter of Shreemad Bhagavad Gita

* **`URL`** : [`https://bhagavadgitaapi.in{/:ch/:sl}`](https://bhagavadgitaapi.in/1/1)
* **`Method`** : **`GET`**
* **`Attributes`** :
  * **`:ch`** : `[interger]` specfic Adhyay\(chapter\) number from any of 18 chapters 
  * **`:sl`** : `[interger]` specfic Slok\(verse\) number avilable in taht particuler `chapter` 
* **`Response 200`**  :  **`(application/json)`**  

```perl
{
  "_id": "BG1.1",
  "chapter": 1,
  "verse": 1,
  "slok": "धृतराष्ट्र उवाच |\nधर्मक्षेत्रे कुरुक्षेत्रे समवेता युयुत्सवः |\nमामकाः पाण्डवाश्चैव किमकुर्वत सञ्जय ||१-१||",
  "transliteration": "dhṛtarāṣṭra uvāca .\ndharmakṣetre kurukṣetre samavetā yuyutsavaḥ .\nmāmakāḥ pāṇḍavāścaiva kimakurvata sañjaya ||1-1||",
  "tej": {
    "author": "Swami Tejomayananda",
    "ht": "।।1.1।।धृतराष्ट्र ने कहा -- हे संजय ! धर्मभूमि कुरुक्षेत्र में एकत्र हुए युद्ध के इच्छुक (युयुत्सव:) मेरे और पाण्डु के पुत्रों ने क्या किया?"
  },
  "siva": {
    "author": "Swami Sivananda",
    "et": "1.1 Dhritarashtra said  What did my people and the sons of Pandu do when they had assembled\ntogether eager for battle on the holy plain of Kurukshetra, O Sanjaya.",
    "ec": "1.1 धर्मक्षेत्रे on the holy plain? कुरुक्षेत्रे in Kurukshetra? समवेताः assembled together? युयुत्सवः desirous to fight? मामकाः my people? पाण्डवाः the sons of Pandu? च and? एव also? किम् what? अकुर्वत did do? सञ्जय O Sanjaya.Commentary Dharmakshetra -- that place which protects Dharma is Dharmakshetra. Because it was in the land of the Kurus? it was called Kurukshetra.Sanjaya is one who has conered likes and dislikes and who is impartial."
  },
  "purohit": {
    "author": "Shri Purohit Swami",
    "et": "1.1 The King Dhritarashtra asked: \"O Sanjaya! What happened on the sacred battlefield of Kurukshetra, when my people gathered against the Pandavas?\""
  },
  "chinmay": {
    "author": "Swami Chinmayananda",
    "hc": "।।1.1।। सम्पूर्ण गीता में यही एक मात्र श्लोक अन्ध वृद्ध राजा धृतराष्ट्र ने कहा है। शेष सभी श्लोक संजय के कहे हुए हैं जो धृतराष्ट्र को युद्ध के पूर्व की घटनाओं का वृत्तान्त सुना रहा था।\nनिश्चय ही अन्ध वृद्ध राजा धृतराष्ट्र को अपने भतीजे पाण्डवों के साथ किये गये घोर अन्याय का पूर्ण भान था। वह दोनों सेनाओं की तुलनात्मक शक्तियों से परिचित था। उसे अपने पुत्र की विशाल सेना की सार्मथ्य पर पूर्ण विश्वास था। यह सब कुछ होते हुये भी मन ही मन उसे अपने दुष्कर्मों के अपराध बोध से हृदय पर भार अनुभव हो रहा था और युद्ध के अन्तिम परिणाम के सम्बन्ध में भी उसे संदेह था। कुरुक्षेत्र में क्या हुआ इसके विषय में वह संजय से प्रश्न पूछता है। महर्षि वेदव्यास जी ने संजय को ऐसी दिव्य दृष्टि प्रदान की थी जिसके द्वारा वह सम्पूर्ण युद्धभूमि में हो रही घटनाओं को देख और सुन सकता था।"
  },
  "san": {
    "author": "Dr.S.Sankaranarayan",
    "et": "1.1. Dhrtarastra said  O Sanjaya ! What did my men and the sons of Pandu do in the Kuruksetra, the field of  righteousness, where the entire warring class has assembled ?\nor\nO Sanjaya !  What did the selfish intentions and the intentions born of wisdom do in the human body which is the field-of-duties,  the repository of the senseorgans and in which all the murderous ones (passions and asceticism etc.) are confronting [each other]."
  },
  "adi": {
    "author": "Swami Adidevananda",
    "et": "1.1 Dhrtarastra said  On the holy field of Kuruksetra, gathered together eager for battle, what did my people and the Pandavas do, O Sanjaya?"
  },
  "gambir": {
    "author": "Swami Gambirananda",
    "et": "1.1. Dhrtarastra said  O Sanjaya, what did my sons (and others) and Pandu's sons (and others) actually do when, eager for battle, they assembled on the sacred field, the Kuruksetra (Field of the Kurus)?"
  },
  "madhav": {
    "author": "Sri Madhavacharya",
    "sc": "।।1.1।।Sri Madhvacharya  did not comment on this sloka. The commentary starts from 2.11."
  },
  "anand": {
    "author": "Sri Anandgiri",
    "sc": "।।1.1।।एवं गीताशास्त्रस्य साध्यसाधनभूतनिष्ठाद्वयविषयस्य परापराभिधेयप्रयोजनवतो व्याख्येयत्वं प्रतिपाद्य व्याख्यातुकामः शास्त्रं तदेकदेशस्य प्रथमाध्यायस्य द्वितीयाध्यायैकदेशसहितस्य तात्पर्यमाह   अत्र चेति। गीताशास्त्रे प्रथमाध्याये प्रथमश्लोके कथासंबन्धप्रदर्शनपरे स्थिते सतीति यावत्। तत्रैवमक्षरयोजना   धृतराष्ट्र उवाचेति। धृतराष्ट्रो हि प्रज्ञाचक्षुर्बाह्यचक्षुरभावाद्बाह्यमर्थं प्रत्यक्षयितुमनीशः सन्नभ्याशवर्तिनं संजयमात्मनो हितोपदेष्टारं पृच्छति   धर्मक्षेत्र इति। धर्मस्य तद्वृद्धेश्च क्षेत्रमभिवृद्धिकारणं यदुच्यते कुरुक्षेत्रमिति तत्र समवेताः संगता युयुत्सवो योद्धुकामास्ते च केचिन्मदीया दुर्योधनप्रभृतयः पाण्डवाश्चापरे युधिष्ठिरादयस्ते च सर्वे युद्धभूमौ संगता भूत्वा किमकुर्वत कृतवन्तः।"
  },
  "rams": {
    "author": "Swami Ramsukhdas",
    "ht": "।।1.1।। धृतराष्ट्र बोले (टिप्पणी प0 1.2) - हे संजय! (टिप्पणी प0 1.3) धर्मभूमि कुरुक्षेत्र में युद्ध की इच्छा से इकट्ठे हुए मेरेे और पाण्डु के पुत्रों ने भी क्या किया?",
    "hc": "1।।व्याख्या--'धर्मक्षेत्रे' 'कुरुक्षेत्रे' --कुरुक्षेत्रमें देवताओंने यज्ञ किया था। राजा कुरुने भी यहाँ तपस्या की थी। यज्ञादि धर्ममय कार्य होनेसे तथा राजा कुरुकी तपस्याभूमि होनेसे इसको धर्मभूमि कुरुक्षेत्र कहा गया है।\n\nयहाँ ॓'धर्मक्षेत्रे' और 'कुरुक्षेत्रे' पदोंमें 'क्षेत्र' शब्द देनेमें धृतराष्ट्रका अभिप्राय है कि यह अपनी कुरुवंशियोंकी भूमि है। यह केवल लड़ाईकी भूमि ही नहीं है, प्रत्युत तीर्थभूमि भी है, जिसमें प्राणी जीते-जी पवित्र कर्म करके अपना कल्याण कर सकते हैं। इस तरह लौकिक और पारलौकिक सब तरहका लाभ हो जाय--ऐसा विचार करके एवं श्रेष्ठ पुरुषोंकी सम्मति लेकर ही युद्धके लिये यह भूमि चुनी गयी है।\n\nसंसारमें प्रायः तीन बातोंको लेकर लड़ाई होती है-- भूमि, धन और स्त्री। इस तीनोंमें भी राजाओंका आपसमें लड़ना मुख्यतः जमीनको लेकर होता है। यहाँ 'कुरुक्षेत्रे' पद देनेका तात्पर्य भी जमीनको लेकर ल़ड़नेमें है। कुरुवंशमें धृतराष्ट्र और पाण्डुके पुत्र सब एक हो जाते हैं। कुरुवंशी होनेसे दोनोंका कुरुक्षेत्रमें अर्थात् राजा कुरुकी जमीनपर समान हक लगता है। इसलिये (कौरवों द्वारा पाण्डवोंको उनकी जमीन न देनेके कारण) दोनों जमीनके लिये लड़ाई करने आये हुए हैं।\n\nयद्यपि अपनी भूमि होनेके कारण दोनोंके लिये 'कुरुक्षेत्रे' पद देना युक्तिसंगत, न्यायसंगत है, तथापि हमारी सनातन वैदिक संस्कृति ऐसी विलक्षण है कि कोई भी कार्य करना होता है, तो वह धर्मको सामने रखकर ही होता है। युद्ध-जैसा कार्य भी धर्मभूमि--तीर्थभूमिमें ही करते हैं, जिससे युद्धमें मरनेवालोंका उद्धार हो जाय, कल्याण हो जाय। अतः यहाँ कुरुक्षेत्रके साथ 'धर्मक्षेत्रे' पद आया है।\n\nयहाँ आरम्भ में 'धर्म' पदसे एक और बात भी मालूम होती है। अगर आरम्भके 'धर्म' पदमेंसे 'धर्' लिया जाय और अठारहवें अध्यायके अन्तिम श्लोकके 'मम' पदोंसे 'म' लिया जाय, तो 'धर्म' शब्द बन जाता है। अतः सम्पूर्ण गीता धर्मके अन्तर्गत है अर्थात् धर्मका पालन करनेसे गीताके सिद्धान्तोंका पालन हो जाता है और गीताके सिद्धान्तोंके अनुसार कर्तव्यकर्म करनेसे धर्मका अनुष्ठान हो जाता है।\n\nइन 'धर्मक्षेत्रे कुरुक्षेत्रे' पदोंसे सभी मनुष्योंको यह शिक्षा लेनी चाहिये कि कोई भी काम करना हो तो वह धर्मको सामने रखकर ही करना चाहिये। प्रत्येक कार्य सबके हितकी दृष्टिसे ही करना चाहिये, केवल अपने सुख-आराम-की दृष्टिसे नहीं; और कर्तव्य-अकर्तव्यके विषयमें शास्त्रको सामने रखना चाहिये (गीता 16। 24)।\n\n'समवेता युयुत्सवः' --राजाओंके द्वारा बारबार सन्धिका प्रस्ताव रखनेपर भी दुर्योधनने सन्धि करना स्वीकार नहीं किया। इतना ही नहीं, भगवान् श्रीकृष्णके कहनेपर भी मेरे पुत्र दुर्योधनने स्पष्ट कह दिया कि बिना युद्धके मैं तीखी सूईकी नोक-जितनी जमीन भी पाण्डवोंको नहीं दूँगा। (टिप्पणी प0 2.1) तब मजबूर होकर पाण्डवोंने भी युद्ध करना स्वीकार किया है। इस प्रकार मेरे पुत्र और पाण्डुपुत्र--दोनों ही सेनाओंके सहित युद्धकी इच्छासे इकट्ठे हुए हैं।\n\nदोनों सेनाओंमें युद्धकी इच्छा रहनेपर भी दुर्योधनमें युद्धकी इच्छा विशेषरूपसे थी। उसका मुख्य उद्देश्य राज्य-प्राप्तिका ही था। वह राज्य-प्राप्ति धर्मसे हो चाहे अधर्मसे, न्यायसे हो चाहे अन्यायसे, विहित रीतिसे हो चाहे निषिद्ध रीतिसे, किसी भी तरहसे हमें राज्य मिलना चाहिये--ऐसा उसका भाव था। इसलिये विशेषरूपसे दुर्योधनका पक्ष ही युयुत्सु अर्थात् युद्धकी इच्छावाला था।\n\nपाण्डवोंमें धर्मकी मुख्यता थी। उनका ऐसा भाव था कि हम चाहे जैसा जीवन-निर्वाह कर लेंगे, पर अपने धर्ममें बाधा नहीं आने देंगे, धर्मके विरुद्ध नहीं चलेंगे। इस बातको लेकर महाराज युधिष्ठिर युद्ध नहीं करना चाहते थे। परन्तु जिस माँकी आज्ञासे युधिष्ठिरने चारों भाइयोंसहित द्रौपदीसे विवाह किया था, उस माँकी आज्ञा होनेके कारण ही महाराज युधिष्ठिरकी युद्धमें प्रवृत्ति हुई थी (टिप्पणी प0 2.2) अर्थात् केवल माँके आज्ञा-पालनरूप धर्मसे ही युधिष्ठिर युद्धकी इच्छावाले हुये हैं। तात्पर्य है कि दुर्योधन आदि तो राज्यको लेकर ही युयुत्सु थे, पर पाण्डव धर्मको लेकर ही युयुत्सु बने थे।\n\n'मामकाः पाण्डवाश्चैव'-- पाण्डव धृतराष्ट्रको (अपने पिताके बड़े भाई होनेसे) पिताके समान समझते थे और उनकी आज्ञाका पालन करते थे। धृतराष्ट्रके द्वारा अनुचित आज्ञा देनेपर भी पाण्डव उचित-अनुचितका विचार न करके उनकी आज्ञाका पालन करते थे। अतः यहाँ 'मामकाः' पदके अन्तर्गत कौरव (टिप्पणी प0 3.1) और पाण्डव दोनों आ जाते हैं। फिर भी 'पाण्डवाः' पद अलग देनेका तात्पर्य है कि धृतराष्ट्रका अपने पुत्रोंमें तथा पाण्डुपुत्रोंमें समान भाव नहीं था। उनमें पक्षपात था ,अपने पुत्रोंके प्रति मोह था। वे दुर्योधन आदिको तो अपना मानते थे, पर पाण्डवोंको अपना नहीं मानते थे। (टिप्पणी प0 3.2) इस कारण उन्होंने अपने पुत्रोंके लिये 'मामकाः' और पाण्डुपुत्रोंके लिये 'पाण्डवा' पदका प्रयोग किया है; क्योंकि जो भाव भीतर होते हैं, वे ही प्रायः वाणीसे बाहर निकलते हैं। इस द्वैधीभावके कारण ही धृतराष्ट्रको अपने कुलके संहारका दुःख भोगना पड़ा। इससे मनुष्यमात्रको यह शिक्षा लेनी चाहिये कि वह अपने घरोंमें, मुहल्लोंमें, गाँवोंमें, प्रान्तोंमें, देशोंमें, सम्प्रदायोंमें द्वैधीभाव अर्थात् ये अपने हैं, ये दूसरे हैं--ऐसा भाव न रखे। कारण कि द्वैधीभावसे आपसमें प्रेम, स्नेह नहीं होता, प्रत्युत कलह होती है।\n\nयहाँ 'पाण्डवाः' पदके साथ 'एव' पद देनेका तात्पर्य है कि पाण्डव तो बड़े धर्मात्मा हैं; अतः उन्हें युद्ध नहीं करना चाहिये था। परन्तु वे भी युद्धके लिये रणभूमिमें आ गये तो वहाँ आकर उन्होंने क्या किया?\n\n'मामकाः' और 'पाण्डवाः' (टिप्पणी प0 3.3) इनमेंसे पहले 'मामकाः' पदका उत्तर सञ्जय आगेके (दूसरे) श्लोकसे तेरहवें श्लोकतक देंगे कि आपके पुत्र दुर्योधनने पाण्डवोंकी सेना को देखकर द्रोणाचार्यके मनमें पाण्डवोंके प्रति द्वेष पैदा करनेके लिये उनके पास जाकर पाण्डवोंके मुख्य-मुख्य सेनापतियोंके नाम लिये। उसके बाद दुर्योधनने अपनी सेनाके मुख्य-मुख्य योद्धाओंके नाम लेकर उनके रण-कौशल आदिकी प्रशंसा की। दुर्योधनको प्रसन्न करनेके लिये भीष्मजीने जोरसे शंख बजाया। उसको सुनकर कौरव-सेनामें शंख आदि बाजे बज उठे। फिर चौदहवें श्लोकसे उन्नीसवें श्लोकतक 'पाण्डवाः' पदका उत्तर देंगे कि रथमें बैठे हुए पाण्डवपक्षीय श्रीकृष्णने शंख बजाया। उसके बाद अर्जुन, भीम, युधिष्ठिर, नकुल, सहदेव आदिने अपने-अपने शंख बजाये, जिससे दुर्योधनकी सेनाका हृदय दहल गया। उसके बाद भी सञ्जय पाण्डवोंकी बात कहते-कहते बीसवें श्लोकसे श्रीकृष्ण और अर्जुनके संवादका प्रसङ्ग आरम्भ कर देंगे।\n\n'किमकुर्वत'--'किम्' शब्दके तीन अर्थ होते हैं--विकल्प, निन्दा (आक्षेप) और प्रश्न।\n\nयुद्ध हुआ कि नहीं? इस तरहका विकल्प तो यहाँ लिया नहीं जा सकता; क्योंकि दस दिनतक युद्ध हो चुका है और भीष्मजीको रथसे गिरा देनेके बाद सञ्जय हस्तिनापुर आकर धृतराष्ट्रको वहाँकी घटना सुना रहे हैं।\n\n'मेरे और पाण्डुके पुत्रोंने यह क्या किया, जो कि युद्ध कर बैठे! उनको युद्ध नहीं करना चाहिये था'--ऐसी निन्दा या आक्षेप भी यहाँ नहीं लिया जा सकता; क्योंकि युद्ध तो चल ही रहा था और धृतराष्ट्रके भीतर भी आक्षेपपूर्वक पूछनेका भाव नहीं था।यहाँ 'किम्' शब्दका अर्थ प्रश्न लेना ही ठीक बैठता है। धृतराष्ट्र सञ्जयसे भिन्न-भिन्न प्रकारकी छोटी-बड़ी सबघटनाओंको अनुक्रमसे विस्तारपूर्वक ठीक-ठीक जाननेके लिये ही प्रश्न कर रहे हैं।सम्बन्ध-- धृतराष्ट्रके प्रश्नका उत्तर सञ्जय आगेके श्लोकसे देना आरम्भ करते हैं।"
  },
  "raman": {
    "author": "Sri Ramanuja",
    "sc": "।।1.1।।धृतराष्ट्र उवाच  सञ्जय उवाच  दुर्योधनः स्वयमेव भीमाभिरक्षितं पाण्डवानां बलम् आत्मीयं च भीष्माभिरक्षितं बलम् अवलोक्य आत्मविजये तस्य बलस्य पर्याप्तताम् आत्मीयस्य बलस्य तद्विजये चापर्याप्तताम् आचार्याय निवेद्य अन्तरे विषण्णः अभवत्। तस्य विषादम् आलोक्य भीष्मः तस्य हर्षं जनयितुं सिंहनादं शङ्खाध्मानं च कृत्वा शङ्खभेरीनिनादैः च विजयाभिशंसिनं घोषं च अकारयत्। ततः तं घोषम् आकर्ण्य सर्वेश्वरेश्वरः पार्थसारथी रथी च पाण्डुतनयः त्रैलोक्यविजयोपकरणभूते महति स्यन्दने स्थितौ त्रैलोक्यं कम्पयन्तौ श्रीमत्पाञ्चजन्यदेवदत्तौ दिव्यौ शङ्खौ प्रदध्मतुः। ततो युधिष्ठिरवृकोदरादयः च स्वकीयान् शङ्खान् पृथक् पृथक् प्रदध्मुः। स घोषो दुर्योधनप्रमुखानां सर्वेषाम् एव भवत्पुत्राणां हृदयानि बिभेद। अद्य एव नष्टं कुरूणां बलम् इति धार्त्तराष्ट्रा मेनिरे। एवं तद्विजयाभिकाङ्क्षिणे धृतराष्ट्राय संजयः अकथयत्।अथ युयुत्सून् अवस्थितान् धार्तराष्ट्रान् भीष्मद्रोणप्रमुखान् दृष्ट्वा लङ्कादहनवानरध्वजः पाण्डुतनयो ज्ञानशक्तिबलैश्वर्यवीर्यतेजसां निधिं स्वसंकल्पकृतजगदुदयविभवलयलीलं हृषीकेशं परावरनिखिलजनान्तर्बाह्यसर्वकरणानां सर्वप्रकारकनियमने अवस्थितं समाश्रितवात्सल्यविवशतया स्वसारथ्ये अवस्थितं युयुत्सून् यथावत् अवेक्षितुं तदीक्षणक्षमे स्थाने रथं स्थापय इति अचोदयत्।",
    "et": "1.1 - 1.19 Dhrtarastra said - Sanjaya said  Duryodhana, after viewing the forces of Pandavas protected by Bhima, and his own forces protected by Bhisma conveyed his views thus to Drona, his teacher, about the adeacy of Bhima's forces for conering the Kaurava forces and the inadeacy of his own forces for victory against the Pandava forces. He was grief-stricken within.\n\nObserving his (Duryodhana's) despondecny, Bhisma, in order to cheer him, roared like a lion, and then blowing his conch, made his side sound their conchs and kettle-drums, which made an uproar as a sign of victory. Then, having heard that great tumult, Arjuna and Sri Krsna the Lord of all lords, who was acting as the charioteer of Arjuna, sitting in their great chariot which was powerful enough to coner the three worlds; blew their divine conchs Srimad Pancajanya and Devadatta. Then, both Yudhisthira and Bhima blew their respective conchs separately. That tumult rent asunder the hearts of your sons, led by Duryodhana. The sons of Dhrtarastra then thought, 'Our cause is almost lost now itself.' So said Sanjaya to Dhrtarastra who was longing for their victory.\n\nSanjaya said to Dhrtarastra:  Then, seeing the Kauravas, who were ready for battle, Arjuna, who had Hanuman, noted for his exploit of burning Lanka, as the emblem on his flag on his chariot, directed his charioteer Sri Krsna, the Supreme Lord-who is overcome by parental love for those who take shelter in Him who is the treasure-house of knowledge, power, lordship, energy, potency and splendour, whose sportive delight brings about the origin, sustentation and dissolution of the entire cosmos at His will, who is the Lord of the senses, who controls in all ways the senses inner and outer of all, superior and inferior - by saying, 'Station my chariot in an appropriate place in order that I may see exactly my enemies who are eager for battle.'"
  },
  "abhinav": {
    "author": "Sri Abhinav Gupta",
    "sc": "।।1.1।।धर्मक्षेत्र इति।  अत्र केचित् व्याख्याविकल्पमाहुः  कुरूणां करणानां यत् क्षेत्रमनुग्राहकं अतएव सांसारिकधर्माणां (S सांसारिकत्वधर्माणां) सर्वेषां क्षेत्रम् उत्पत्तिनिमित्तत्वात्। अयं स परमो धर्मो यद्योगेनात्मदर्शनम् (या. स्मृ. I 8) इत्यस्य च धर्मस्य क्षेत्रम् समस्तधर्माणां क्षयात् अपवर्गप्राप्त्या त्राणभूतं तदधिकारिशरीरम्।  सर्वक्षत्राणां क्षदेः हिंसार्थत्वात् परस्परं वध्यघातकभावेन (S परस्परवध्य  ) वर्तमानानां रागवैराग्यक्रोधक्षमाप्रभृतीनां समागमो यत्र तस्मिन् स्थिता ये मामका अविद्यापुरुषोचिता अविद्यामयाः संकल्पाः पाण्डवाः शुद्धविद्यापुरुषोचिता विद्यात्मानः ते किमकुर्वत कैः खलु के जिताः  इति।  मामकः अविद्यापुरुषः पाण्डुः शुद्धः।",
    "et": "1.1  Dharmaksetre etc. Here some [authors] offer a different explanation as1 :-Kuruksetra : the man's body is the ksetra i.e., the facilitator, of the kurus, i.e., the sense-organs. 2 The same is the field of all wordly duties, since it is the cuse of their birth; which is also the field of the righteous act that has been described as :\n\n'This is the highest righteous act viz., to realise the Self by means of the Yogas';\n\n\nand which is the protector4 [of the embodied Self] by achieving emancipation [by means of this], through the destruction of all duties. It is the location where there is the confrontation among all ksatras, the murderous ones-because the root ksad means 'to kill' - viz, passion and asceticism, wrath and forbearance, and others that stand in the mutual relationship of the slayer and the slain. Those that exist in it are the mamakas,-i.e., the intentions that are worthy of man of ignorance and are the products of ignorance-and those that are born of Pandu: i.e., the intentions, of which the soul is the very knowledge itself5 and which are worthy of persons of pure knowledge. What did they do? In other words, which were vanished by what? Mamaka : a man of ignorance as he utters [always] 'mine'6. Pandu : the pure one.7"
  },
  "sankar": {
    "author": "Sri Shankaracharya",
    "ht": "।।1.1।।Sri Sankaracharya did not comment on this sloka.",
    "sc": "1.1 Sri Sankaracharya did not comment on this sloka. The commentary starts from 2.10.",
    "et": "1.1 Sri Sankaracharya did not comment on this sloka. The commentary starts from 2.10."
  },
  "jaya": {
    "author": "Sri Jayatritha",
    "sc": "।।1.1।।Sri Jayatirtha did not comment on this sloka. The commentary starts from 2.11."
  },
  "vallabh": {
    "author": "Sri Vallabhacharya",
    "sc": "।।1.1।।धर्मक्षेत्रे इत्यारभ्यस घोषो धार्तराष्ट्राणां 1।19 इत्यन्तं सम्बन्धः। अत्रैतदध्यायव्याख्या श्रीविठ्ठलेशप्रभुकृता बोध्या।"
  },
  "ms": {
    "author": "Sri Madhusudan Saraswati",
    "sc": "।।1.1।।तत्रअशोच्यान्वशोचस्त्वम् इत्यादिना शोकमोहादिसर्वासुरपाप्मनिवृत्त्युपायोपदेशेन स्वधर्मानुष्ठानात्पुरुषार्थः प्राप्यतामिति भगवदुपदेशः सर्वसाधारणः। भगवदर्जुनसंवादरूपा चाख्यायिका विद्यास्तुत्यर्थाजनकयाज्ञवल्क्यसंवादादिवदुपनिषत्सु। कथं प्रसिद्धमहानुभावोऽप्यर्जुनो राज्यगुरुपुत्रमित्रादिष्वहमेषां ममैत इत्येवंप्रत्ययनिमित्तस्नेहनिमित्ताभ्यां शोकमोहाभ्यामभिभूतविवेकविज्ञानः स्वतएव क्षत्रधर्मे युद्धे प्रवृत्तोऽपि तस्माद्युद्धादुपरराम। परधर्मं च भिक्षाजीवनादि क्षत्रियंप्रति प्रतिषिद्धं कर्तुं प्रववृते। तथाच महत्यनर्थे मग्नोऽभूत् भगवदुपदेशाच्चेमां विद्यां लब्धवा शोकमोहावपनीय पुनः स्वधर्मे प्रवृत्तः कृतकृत्यो बभूवेति प्रशस्ततरेयं महाप्रयोजना विद्येति स्तूयते। अर्जुनापदेशेन चोपदेशाधिकारी दर्शितः। तथाच व्याख्यास्यते। स्वधर्मप्रवृत्तौ जातायामपि तत्प्रच्युतिहेतुभूतौ शोकमोहौकथं भीष्ममहं संख्ये इत्यादिनार्जुनेन दर्शितौ। अर्जुनस्य युद्धाख्ये स्वधर्में विनापि विवेकं किंनिमित्ता प्रवृत्तिरितिदृष्ट्वा तु पाण्डवानीकम् इत्यादिना परसैन्यचेष्टितं तन्निमित्तमुक्तम्। तदुपोद्धातत्वेन धृतराष्ट्रप्रश्नः संजयं प्रति धर्मक्षेत्रे इत्यादिना श्लोकेन। तत्र धृतराष्ट्र उवाचेति वैशम्पायनवाक्यं जनमेजयं प्रति। पाण्डवानां जयकारणं बहुविधं पूर्वमाकर्ण्य स्वपुत्रराज्यभ्रंशाद्भीतो धृतराष्ट्रः पप्रच्छ स्वपुत्रजयकारणमाशंसन्। पूर्वं युयुत्सवो योद्धुमिच्छवोऽपि सन्तः कुरुक्षेत्रे समवेताः संगताः मामका मदीया दुर्योधनादयः पाण्डवाश्च युधिष्ठिरादयः किमकुर्वत किं कृतवन्तः। किं पुर्वोद्भूतयुयुत्सानुसारेण युद्धमेव कृतवन्त उत केनचिन्निमित्तेन युयुत्सानिवृत्त्यान्यदेव किंचित्कृतवन्तः भीष्मार्जुनादिवीरपुरुषनिमित्तं दृष्टभयं युयुत्सानिवृत्तिकारणं प्रसिद्धमेव अदृष्टभयमपि दर्शयितुमाह  धर्मक्षेत्र इति। धर्मस्य पूर्वमविद्यमानस्योत्पत्तेर्विद्यमानस्य च वृद्धेर्निमित्तं सस्यस्येव क्षेत्रं यत्कुरुक्षेत्रं सर्वश्रुतिस्मृतिप्रसिद्धम्।बृहस्पतिरुवाच याज्ञवल्क्यं यदनु कुरुक्षेत्रं देवानां देवयजनं सर्वेषां भूतानां ब्रह्मसदनम् इति जाबालश्रुतेःकुरुक्षेत्रं वै देवयजनम् इति शतपथश्रुतेश्च। तस्मिन् गताः पाण्डवाः पूर्वमेव धार्मिकाः यदि पक्षद्वयहिंसानिमित्तादधर्माद्गीता निवर्तेरंस्ततः प्राप्तराज्या एव मत्पुत्राः अथवा धर्मक्षेत्रमाहात्म्येन पापानामपि मत्पुत्राणां कदाचिच्चित्तप्रसादः स्यात्तदा च तेऽनुतप्ताः प्राक्कपटोपात्तं राज्यं पाण्डवेभ्यो यदि दद्युस्तर्हि विनापि युद्धं हता एवेति स्वपुत्रराज्यलाभे पाण्डवराज्यलाभे च दृढतरमुपायमपश्यतो महानुद्वेग एव प्रश्नबीजम्। संजयेति च संबोधनं रागद्वेषादिदोषान्सम्यग्जितवानसीति कृत्वा निर्व्याजमेव  कथनीयं त्वयेति सूचनार्थम्। मामकाः किमकुर्वतेत्येतावतैव प्रश्ननिर्वाहे पाण्डवाश्चेति पृथङ्निर्दिशन्पाण्डवेषु ममकाराभावप्रदर्शनेन तद्द्रोहमभिव्यनक्ति।"
  },
  "srid": {
    "author": "Sri Sridhara Swami",
    "sc": "।।1.1।। इह खलु सकललोकहितावतारः सकलवन्दितचरणः परमकारुणिको भगवान् देवकीनन्दनस्तत्त्वाज्ञानविजृम्भितशोकमोहविभ्रंशितविवेकतया निजधर्मत्यागपरधर्माभिसंधिपरमर्जुनं धर्मज्ञानरहस्योपदेशप्लवेन तस्माच्छोकमोहसागरादुद्दधार। तमेव भगवदुपदिष्टमर्थं कृष्णद्वैपायनः सप्तभिः श्लोकशतैरुपनिबबन्ध। तत्र च प्रायशः श्रीकृष्णमुखनिःसृतानेव श्लोकानलिखत् कांश्चित्तत्संगतये स्वयं व्यरचयत्। यथोक्तं गीतामाहात्म्ये  गीता सुगीता कर्तव्या किमन्यैः शास्त्रविस्तरैः। या स्वयं पद्मनाभस्य मुखपद्माद्विनिःसृता।। इति। तत्र तावद्धर्मक्षेत्र इत्यादिना विषीदन्निदमब्रवीदित्यन्तेन ग्रन्थेन श्रीकृष्णार्जुनसंवादप्रस्तावाय कथा निरूप्यते   धर्मक्षेत्र इति। भो संजय धर्मभूमौ कुरुक्षेत्रे मत्पुत्राः पाण्डुपुत्राश्च युयुत्सवो योद्धुमिच्छन्तः समवेता मिलिताः सन्तः किं कृतवन्तः।"
  },
  "dhan": {
    "author": "Sri Dhanpati",
    "sc": "।।1.1।।  इह खलु परमकारुणिकः परिपूर्णानन्दस्वभावः सकलैश्वर्यसंपन्नस्त्रिगुणात्मिकया स्ववशीकृतया निजमाययोपात्तकायो भगवान् वासुदेवः शोकमोहाभिभूतं जीवनिकायमुद्दिधीर्षुर्यद्गीताशास्त्रं सर्ववेदसारभूतं काण्डत्रयात्मकं तत्त्वम्पदाखण्डार्थप्रतिपादकं निजविग्रहायार्जुनाय ग्राहयामास। तदेव क्रमप्राप्तं दयानिधिर्वेदव्यासो महाभारते निबध्नाति   धृतराष्ट्र उवाचेत्यादि। तत्र धृतराष्ट्र उवाच  केषां प्रहृष्टास्तत्राग्रे योधा युध्यन्ति संजय। उदग्रमनसः केऽत्र के वा दीना विचेतसः।।के पूर्वं प्राहरंस्तत्र युद्धे हृदयकम्पिनि। मामकाः पाण्डवानां वा तन्ममाचक्ष्व संजय।। इत्यादिना कृतं प्रश्नं वैशंपायनो जनमेजयंप्रति संक्षिप्योपोद्धातायानुवदति   धृतराष्ट्र उवाचेति। मामकाः मदीयाः दुर्योधनादयः पाण्डवाः पाण्डुपुत्राः युधिष्ठिरादयः युयुत्सवः योद्धुमिच्छवः। धर्मस्योपचयस्थानत्वात् धर्मक्षेत्रे कुरुक्षेत्रे श्रुतिस्मृतिलोकप्रसिद्धे समवेता मिलिताः सन्तः किमकुर्वत किं कृतवन्तः। स्वधर्मभूतं धर्मयुद्धं कृतवन्त उताधर्मयुद्धमिति धर्मक्षेत्रपदेन बोधितम्। युयुत्सया समवेता इति मया विस्तरेण श्रुतं तदनन्तरं यथा यत्कृतवन्तः तथा तद्विस्तरेण वदेत्याशयः। भीष्मपतनेन कलहस्यानर्थबोधकानां भवदादिवाक्यानां सम्यग्जयो जात इति ध्वनयन्संबोधयति   संजयेति। रागद्वेषादिदोषान्सभ्यग्जितवानसीति कृत्वा निर्व्याजेन त्वया कथनीयमिति सूचनार्थं संजयेति संबोधनमिति केचित्। किमा आक्षेपोऽपि ध्वनितः। अयोग्यं कृतवन्त इत्यर्थः। धर्मक्षेत्रे हिंसाप्रधानस्य युद्धस्यानुचितत्वात्। मामकानामधार्मिकत्वेन तत्संभवेऽपि परमधार्मिकत्वेन प्रसिद्धाः पाण्डवाः युधिष्ठिरादयो भीष्मादिपातनं किं कृतवन्त इति द्योतयन्नाह   पाण्डवाश्चेति। पाण्डवेषु ममकाराभावप्रदर्शनेन तेषु द्रोहमभिव्यनक्तीति केचित्। यत्तु पाण्डवानां जयकारणं बहुविधं पूर्वमाकर्ण्य स्वपुत्रराज्यभ्रंशाद्भीतो धृतराष्ट्रः पप्रच्छ स्वपुत्रजयकारणमाशंसन् धृतराष्ट्र इत्यादिना। किं कृतवन्तः किं पूर्वोक्तयुयुत्सानुसारेण युद्धमेव कृतवन्तः उत केनचिन्निमित्तेन युयुत्सानिवृत्त्याऽन्यदेव किंचित्कृतवन्तः। भीमार्जुनादिवीरपुरुषनिमित्तं दृष्टभयं युयुत्सानिवृत्तिकारणं प्रसिद्धमेव। अदृष्टभयमपि दर्शयितुमाह धर्मक्षेत्र इति। तस्मिन् गताः पाण्डवाः पूर्वमेव धार्मिकाः। यदि पक्षद्वयहिंसानिमित्तादधर्माद्भीता निवर्तेन् ततः प्राप्तराज्या एव मत्पुत्राः। अथवा धर्मक्षेत्रमाहात्म्येन पापिनामपि मत्पुत्राणां कदाचिच्चित्तप्रसादाः स्यात्तदा च तेऽनुतप्ताः कपटोपात्तं राज्यं पाण्डवेभ्यो यदि दद्युः तर्हि विनापि युद्धं हता एवेति स्वपुत्रराज्यलाभे पाण्डवराज्यालाभे च दृढतरमुपायमपश्यतो महानुद्वेग एव प्रश्नबीजमिति केचिद्वर्णयन्ति तदुपेक्ष्यम्।अथ गावल्गणिर्धीमान्समरादेत्य संजयः। प्रत्यक्षदर्शी सर्वस्य भूतभव्यभविष्यतः।।ध्यायतो धृतराष्ट्रस्य सहसोपेत्य दुःखितः। आचष्ट निहतं भीष्म भारतानां पितामहम्। संजयोऽहं महाराज नमस्ते भरतर्षभ।।हतो भीष्मः शान्तनवो भारतानां पितामहः। यो ररक्ष समेतानां दशरात्रमनीकहा।।जगामास्तमिवादित्यः कृत्वा कर्म सुदुष्करम्। यः स शक्र इवाक्षोभ्यो वर्षन्बाणन्सहस्त्रशः।।जघान युधि योधानामर्बुदं दशभिर्दिनैः। स शेते निहतो भूमौ वातरुग्ण इव द्रुमः।। इत्यादिसंक्षेपोक्तिपरपूर्वग्रन्थविरोधात्। ननु संक्षेपेण श्रुतमपि मोहाद्विस्मृत्य धृतराष्ट्रेण प्रश्नः कृत इतिचेन्न। प्रश्नस्य पूर्वग्रन्थानुरोधेनास्मदीयोक्तरीत्या सभ्यगुपपत्तेः। पूर्वोक्तविरुद्धप्रश्नव्याख्यानकर्तृ़णामेव मोहादिति दिक्। यत्त्वन्ये  धर्मक्षेत्रपदं कुरुक्षेत्रपदादविमुक्तक्षेत्रप्रतिपत्तिर्माभूदित्येतदर्थमिति। तन्न। कुरुक्षेत्रादागतं संजयं किमविमुक्तक्षेत्रे समवेता इति संशयरहितंप्रति विशेषणानर्थक्यात्। अन्येषामपि लोकप्रसिद्य्धा पूर्वग्रन्थेन च निर्णयस्य सत्त्वात्।"
  },
  "venkat": {
    "author": "Vedantadeshikacharya Venkatanatha",
    "sc": "।।1.1।।धर्मक्षेत्रे  धर्मस्य स्थानभूते समराध्वरसमुचिते इति भावः।कुरुक्षेत्रे पाण्डवधार्तराष्ट्राणां स्वकूटस्थनामोपलक्षितत्वेन बहुमानविषय इति भावः।युयुत्सवः समवेताः मिथः प्रत्यनीकरूपेण व्यूढा इत्यर्थः।च एव इत्यव्ययद्व्यमनतिरिक्तार्थम् यद्वा समस्तभूमण्डलवर्तिनां राज्ञां तत्र समाहारेऽपि तादर्थ्याद्वर्गद्वयमेव तथाऽभूदित्येवकाराभिप्रायः।अकुर्वत इत्यात्मनेपदेन कर्त्रभिप्रायक्रियाफलविषयेण स्वार्थतोक्ता।"
  },
  "puru": {
    "author": "Sri Purushottamji",
    "sc": "।।1.1।।वैशम्पायनस्तु जनमेजयाय कथासङ्गतिं वक्तुं प्रथमतो धृतराष्ट्रसंवादमाह। तत्र धृतराष्ट्रो बहुधा पाण्डवान् धर्मपरानेवावगत्य बन्धलक्षणमधर्मं कथं कृतवन्त इत्यभिप्रेत्य पृच्छति। अत्र ह्येवं कथाप्रकारः सञ्जय आगत्य पूर्वं सेनापतिमरणं वक्ति ततो धृतराष्ट्रेण तत्परिदेवने कृते पश्चात्तन्निवृत्तौ सर्वा कथां विस्तारेण वदतीति। तत्र पाण्डवानां स्वल्पं सैन्यं स्वस्य तु महत् स्वस्य शूराश्च भूयांसः तेषां सर्वेषामेव पश्यतां तैरुपेक्षितो भीष्मो रणे पतितः उत पाण्डवैः प्रसह्य मारितः पाण्डवाश्च तादृशे क्षेत्रे पितामहावज्ञालक्षणमधर्मं कथं कृतवन्तः इति ज्ञातुं हे सञ्जय धर्मक्षेत्रे धर्मोत्पत्तिभूमौ कुरुक्षेत्रे मामकाः मत्पुत्राः पाण्डवाः पाण्डुपुत्राश्च युयुत्सवो योद्धुकामाः समवेताः मिलिताः किमकुर्वत किं कृतवन्तः।\n\nस्वपुत्राणामधर्मपरायणत्वाद्धर्मक्षेत्रेऽप्यधर्ममेव कृतवन्तः किंवा धर्ममिति स्वीयानां प्रश्नः पाण्डवाश्च धर्मपरायणास्तत्र धर्मक्षेत्रे द्रोणादीन् गुरून् कथं मारितवन्तः इति तेषां प्रश्नः। इदमेव चकारेण द्योतितम्यत्तेषां धर्मपरायणत्वम्। तथा चैकमरणेनैवान्यस्य राज्यप्राप्तिरिति निश्चित्यापि किं कृतवन्त इत्यर्थः। सञ्जयस्य वरप्राप्तसर्वज्ञत्वमालक्ष्य सम्बोधनम्।"
  },
  "neel": {
    "author": "Sri Neelkanth",
    "sc": "।।1.1।।तत्र युद्धोद्यमं श्रुत्वौत्सुक्यादग्रिमं वृत्तान्तं बुभुत्सुर्धृतराष्ट्र उवाच   धर्मक्षेत्र इति। तत्र वेदेतेषां कुरुक्षेत्रं देवयजनमास इति कर्मकाण्डप्रसिद्धं कुरुक्षेत्रमन्यत्अविमुक्तं वै कुरुक्षेत्रं देवानां देवयजनं सर्वेषां भूतानां ब्रह्मसदनम् इत्यविमुक्ताख्यं ब्रह्मप्राप्तिस्थानभूतं कुरुक्षेत्रमन्यत्। ब्रह्मसदनत्वं चास्य  अत्र हि जन्तोः प्राणेषूत्क्रममाणेषु रुद्रस्तारकं ब्रह्म व्याचष्टे येनासावमृतीभूत्वा मोक्षी भवतीति वाक्यशेषेण व्युत्पादितम्। एतद्व्यावृत्त्यर्थं धर्मक्षेत्रे इति विशेषणम्। कुरुदेशान्तर्गतं हि कुरुक्षेत्रं धर्मक्षेत्रमेव नतु तद्ब्रह्मसदनम्। प्रवर्ग्यकाण्डे तस्य धर्मक्षेत्रत्वमात्रश्रवणात्। तत्र समवेता मिलिताः युयुत्सवो योद्धुमिच्छवः। पाण्डवानां पृथग्ग्रहणं तेषु ममत्वाभावसूचनार्थम्।"
  }
}
```

#### 6. GET \[/gita.svg\]

> GET SVG of Random Slok of Shreemad Bhagavad Gita

* **`URL`**  : [`https://bhagavadgitaapi.in/gita.svg`](https://bhagavadgitaapi.in/gita.svg)
* **`Method`** : **`GET`**
* **`Response 200`**  :  **`(image/svg+xml)`**

#### 7. GET \[/gita.svg?ch={chapter\_num}\]

> GET SVG of Randome Slok from Particuler chapter of Shreemad Bhagavad Gita

* **`URL`** : [`https://bhagavadgitaapi.in/gita.svg?ch={chapter_num}`](https://bhagavadgitaapi.in/gita.svg?ch=1)
* **`Method`** : **`GET`**
* **`Attributes`** :
  * **`{chapter_num}`** : `[interger]` specfic chapter number from any of 18 chapters 
* **`Response 200`**  :  **`(image/svg+xml)`**

#### 8. GET \[.svg?ch={chapter\_num}&sl={slok\_num}\]

> GET SVG of Slok from Particuler slok & chapter of Shreemad Bhagavad Gita

* **`URL`** : [`https://bhagavadgitaapi.in/gita.svg?ch={chapter_num}&sl={slok_num}`](https://bhagavadgitaapi.in/gita.svg?ch=1&sl=1)
* **`Method`** : **`GET`**
* **`Attributes`** :
  * **`{chapter_num}`** : `[interger]` specfic chapter number from any of 18 chapters 
  * **`{slok_num}`** : `[interger]` specfic slok number avilable in taht particuler `chapter` 
* **`Response 200`**  :  **`(image/svg+xml)`**

### 📚 Source Book

|  [**Swami Tejomayananda** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07QB1YNWG&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Shrimad-Bhagavad-Gita-Audio-Discourses/dp/B07QB1YNWG/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=vedicscriptur-21&linkId=7a8fbbb4713a9cc1949e4ed30a2e1678) |  [**Swami Sivananda** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8170520002&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Swami-Sivananda/dp/8170520002/ref=as_li_ss_il?crid=3FE20X9W8N3U0&dchild=1&keywords=swami+sivananda+books&qid=1607076078&sprefix=Swami+Sivananda+,popular,614&sr=8-7&linkCode=li2&tag=vedicscriptur-21&linkId=b2ff2a12ee00604c1b020453d18f5fd6) |  [**Shri Purohit Swami** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B08CG7F9F8&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Philosophy-life/dp/B08CG7F9F8/ref=as_li_ss_il?dchild=1&keywords=Shri+Purohit+Swami+book&qid=1607076143&sr=8-1&linkCode=li2&tag=vedicscriptur-21&linkId=2bc6d056223d04817a074d6ccb444a53) |  [**Swami Chinmayananda** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07P9JQJ1Q&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shrimad-Bhagavad-Gita-Swami-Chinmayananda/dp/B07P9JQJ1Q/ref=as_li_ss_il?crid=YV9WCXZRPI38&dchild=1&keywords=swami+chinmayananda+bhagavad+gita&qid=1607076179&sprefix=Swami+Chinmayananda,aps,644&sr=8-4&linkCode=li2&tag=vedicscriptur-21&linkId=ef8d52f4c1fb01404f7532ffc7caf5b6) |  [**Dr.S.Sankaranarayan** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8185141142&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shri-Sankara-Dr-S-Sankaranarayanan/dp/8185141142/ref=as_li_ss_il?dchild=1&qid=1607076492&refinements=p_27:Dr.+S.Sankaranarayanan&s=books&sr=1-2&linkCode=li2&tag=vedicscriptur-21&linkId=c4346687887547ee0f540fbdabe783f0) |
| :--- | :--- | :--- | :--- | :--- |
|  [**Swami Adidevananda** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8178235188&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shri-Ramanuja-Gita-Bhasya-English/dp/8178235188/ref=as_li_ss_il?dchild=1&keywords=Swami+Adidevananda&qid=1607076583&s=books&sr=1-4&linkCode=li2&tag=vedicscriptur-21&linkId=25fbd382c61b77b39b947c30a75f3a76) |  [**Swami Gambirananda** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07QMVG2NR&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Shankaracharya-Gambhirananda-Swami-ebook/dp/B07QMVG2NR/ref=as_li_ss_il?dchild=1&keywords=Swami+Gambirananda&qid=1607076775&s=digital-text&sr=1-1-spell&linkCode=li2&tag=vedicscriptur-21&linkId=fc8d7b3cdebb18073090685b0e19bddb) |  [**Shri Madhavacharya** ![](https://images-na.ssl-images-amazon.com/images/I/51shx3o7mUL._SX428_BO1,204,203,200_.jpg)](https://www.amazon.com-Tatparya-Nirnaya-Anandatirtha-Volumes/dp/B00T9X23JA?) |  [**Shri Anandgiri** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8170847133&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shriMADBHAGAVADGITA-Translation-SANKARABHASYA-ANANDGIRI-VYAKHYA/dp/8170847133/ref=as_li_ss_il?dchild=1&keywords=shri+Anandgiri&qid=1607077935&sr=8-2-fkmr0&linkCode=li2&tag=vedicscriptur-21&linkId=45ad6e84fd919fe30da6ee46efe0916f) |  [**Swami Ramsukhdas** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07SQQGV7M&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.inpress-Shrimad-Bhagwatgeeta-Sanjivni-Translation/dp/B07SQQGV7M/ref=as_li_ss_il?crid=1NI6FMT26UILQ&dchild=1&keywords=swami+ramsukhdas+gita+hindi&qid=1607077996&sprefix=Swami+Ramsukhdas,aps,429&sr=8-2&linkCode=li2&tag=vedicscriptur-21&linkId=7208b48e307c51ed8f3501a7dfad3f46) |
|  [**Shri Ramanuja** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=1499696914&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Based-Ramanujas-Gitabhashyam/dp/1499696914/ref=as_li_ss_il?dchild=1&keywords=shri+Ramanuja's+Gitabhashyam&qid=1607078174&sr=8-1&linkCode=li2&tag=vedicscriptur-21&linkId=fe84187cb9ca2e15e226e9c533757ec4) |  [**Shri Abhinav Gupta** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8186569448&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Abhinavaguptas-Commentary-Bhagavad-Gita-Gitartha-Samgraha/dp/8186569448/ref=as_li_ss_il?dchild=1&keywords=shri+abhinavgupta+gita&qid=1607078269&sr=8-2&linkCode=li2&tag=vedicscriptur-21&linkId=722405c6c94d6e2e00c09531d49ff627) |  [**Shri Shankaracharya** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8185208085&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Commentary-shri-Sankaracharya/dp/8185208085/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=vedicscriptur-21&linkId=67d6e12a556466297498fa4f344336aa) |  [**Shri Jayatritha** ![](https://images-na.ssl-images-amazon.com/images/I/41qWJc3IxiL._SX368_BO1,204,203,200_.jpg)](https://www.amazon.com-Bhashyam-Commentary-Jayatirtha-Raghavendratirtha/dp/9381275408) |  [**Shri Vallabhacharya** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8170308607&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Subodhini-Commentry-Mahaprabhu-Vallabhacharya-Translation/dp/8170308607/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=vedicscriptur-21&linkId=be20615f65dca1914be6ed7f4424ef51) |
|  [**Shri M. Saraswati** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8175051949&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Annotation-Gudhartha-Dipika/dp/8175051949/ref=as_li_ss_il?dchild=1&qid=1607079583&refinements=p_27:Madhusudana+Saraswati&s=books&sr=1-1&linkCode=li2&tag=vedicscriptur-21&linkId=c72ec55fccfe3d5182a30a06b18b8de9) |  [**Shri shridhara Swami** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8178234920&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shrimad-Bhagavad-Gita-shridhara-Swami/dp/8178234920/ref=as_li_ss_il?dchild=1&keywords=shri+shridhara+Swami&qid=1607079632&s=books&sr=1-1&linkCode=li2&tag=vedicscriptur-21&linkId=025a7ddde09dfe6f0c2cc95d7b670aca) |  [**Shri Dhanpati** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07QR2D2X4&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/shrimad-Bhagavad-Gita-Swarupananda-Swam…tag=vedicscriptur-21&linkId=adf8f369848073dee2f2c305b3d2bfec) |  [**Vedantadeshika** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=8175053321&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Bhagavad-Gita-Viewed-Swami-Vivekananda/dp/8175053321/ref=as_li_ss_il?dchild=1&keywords=Vedanta+gita&qid=1607080279&s=books&sr=1-2&linkCode=li2&tag=vedicscriptur-21&linkId=e9ff0620537ab376d45bb6440820592f) |  [**Shri Purushottamji** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B00FHU52LA&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Hima-Communications-Purushothama-Yoga-Bhagavad/dp/B00FHU52LA/ref=as_li_ss_il?ie=UTF8&linkCode=li2&tag=vedicscriptur-21&linkId=8ed142cc3911078375cbdd3fdc9a0611) |
|  [**Shri Neelkanth** ![](https://ws-in.amazon-adsystem.com/widgets/q?_encoding=UTF8&ASIN=B07JD7Q9MB&Format=_SL160_&ID=AsinImage&MarketPlace=IN&ServiceVersion=20070822&WS=1&tag=vedicscriptur-21)](https://www.amazon.in/Shri-Krushnayan-Gopal-Neelkanth-Dandekar/dp/B07JD7Q9MB/ref=as_li_ss_il?dchild=1&keywords=shri+neelkanth&qid=1607083622&s=books&sr=1-4&linkCode=li2&tag=vedicscriptur-21&linkId=6e0a0e1ae62aac762405a6dd2635813d) |  |  |  |  |

### 💻 Built with

![Node.js](https://img.shields.io/badge/node.js%20-%2343853D.svg?&style=for-the-badge&logo=node.js&logoColor=white) ![express](https://img.shields.io/badge/express.js%20-%23404d59.svg?&style=for-the-badge) ![MongoDB](https://img.shields.io/badge/MongoDB-%234ea94b.svg?&style=for-the-badge&logo=mongodb&logoColor=white) ![Heroko](https://img.shields.io/badge/heroku%20-%23430098.svg?&style=for-the-badge&logo=heroku&logoColor=white)

### 🙏 Support ✨

|  [**Pt. Prashant Tripathi**](https://github.com/ptprashanttripathi) |
| :--- |
|  [![](https://avatars2.githubusercontent.com/u/26687933?s=200&v=4)](https://github.com/ptprashanttripathi) |

### Questions and Feedback

**Please contact me using one of the following:**

[![](https://img.shields.io/badge/twitter-%231DA1F2.svg?&style=for-the-badge&logo=twitter&logoColor=white)](https://twitter.com/ptprashant09) [![](https://img.shields.io/badge/linkedin-%230077B5.svg?&style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/ptprashanttripathi/) [![](https://img.shields.io/badge/instagram-%23E4405F.svg?&style=for-the-badge&logo=instagram&logoColor=white)](https://www.instagram.com/ptprashanttripathi/) [![](https://img.shields.io/badge/telegram-%233498DB.svg?&style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/ptprashanttripathi/) [![](https://img.shields.io/badge/facebook-%231877F2.svg?&style=for-the-badge&logo=facebook&logoColor=white)](https://www.facebook.com/ptprashanttripathi) [![](https://img.shields.io/badge/DEV.TO-%230A0A0A.svg?&style=for-the-badge&logo=dev-dot-to&logoColor=white)](https://dev.to/ptprashanttripathi)

Developed with ❤️ in India 🇮🇳

