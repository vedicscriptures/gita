---
description: GET All Chapters details of Shreemad Bhagavad Gita
---

# GET /chapters

{% api-method method="get" host="https://bhagavadgitaapi.in" path="/chapters" %}
{% api-method-summary %}
/chapters
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to get all Chapters details of Shreemad Bhagavad Gita.  
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-headers %}
{% api-method-parameter name="x-api-key" type="string" required=false %}
Authentication token to track down who is emptying our stocks.
{% endapi-method-parameter %}
{% endapi-method-headers %}

{% api-method-query-parameters %}
{% api-method-parameter type="string" name="api\_key" %}
Alternate way to send Authentication token
{% endapi-method-parameter %}
{% endapi-method-query-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
successfully retrieved.
{% endapi-method-response-example-description %}

```
[
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
  },
  {"chapter 2": "chapter 17"},
  {
    "chapter_number": 18,
    "verses_count": 78,
    "name": "मोक्षसंन्यासयोग",
    "translation": "Moksha Sanyaas Yoga",
    "transliteration": "Mokṣha Sanyās Yog",
    "meaning": {
      "en": "Yoga through the Perfection of Renunciation and Surrender",
      "hi": "उपसंहार-संन्यास की सिद्धि"
    },
    "summary": {
      "en": "The eighteenth chapter of the Bhagavad Gita is Moksha Sanyas Yoga. Arjuna requests the Lord to explain the difference between the two types of renunciations - sanyaas(renunciation of actions) and tyaag(renunciation of desires). Krishna explains that a sanyaasi is one who abandons family and society in order to practise spiritual discipline whereas a tyaagi is one who performs their duties without attachment to the rewards of their actions and dedicating them to the God. Krishna recommends the second kind of renunciation - tyaag. Krishna then gives a detailed analysis of the effects of the three modes of material nature. He declares that the highest path of spirituality is pure, unconditional loving service unto the Supreme Divine Personality, Krishna. If we always remember Him, keep chanting His name and dedicate all our actions unto Him, take refuge in Him and make Him our Supreme goal, then by His grace, we will surely overcome all obstacles and difficulties and be freed from this cycle of birth and death.",
      "hi": "भगवद गीता का अठारहवा अध्याय मोक्षसन्यासयोग है। अर्जुन कृष्ण से अनुरोध करते हैं कि वे संन्यास और त्याग के बीच अंतर को समझाने की कृपा करें। कृष्ण बताते हैं कि एक संन्यासी वह है जो आध्यात्मिक अनुशासन का अभ्यास करने के लिए परिवार और समाज को त्याग देता है जबकि एक त्यागी वह है जो अपने कर्मों के फलों कि चिंता करे बिना भगवन को समर्पित करके कर्म करता रहता है। कृष्ण बताते हैं कि त्याग संन्यास से श्रेष्ठ है। फिर कृष्णा भौतिक संसार के तीन प्रकार के गुणों का विस्तारपूर्वक वर्णन करते हैं। कृष्णा घोषणा करते हैं कि परमात्मा की शुद्ध एवं सत्य भक्ति ही आध्यात्मिकता का उच्चतम मार्ग है। अगर हम हर क्षण उनका स्मरण करते रहें, उनका नाम जपते रहें, अपना सर्वस्व उनको समर्पित कर दें, उन्हें ही अपना सर्वोच्च लक्ष्य बना लें तो उनकी कृपा से हम निश्चित रूप से सभी बाधाओं और कठिनाइओं को दूर कर पाएंगे और इस जन्म और मृत्यु के चक्र से मुक्त हो पाएंगे।"
    }
  }
]
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Could not find a matching this query.
{% endapi-method-response-example-description %}

```
{ error: 'Internal Server Error'}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



