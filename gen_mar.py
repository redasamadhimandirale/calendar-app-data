import json
import os

data = {
  "1": { "tithi": "फाल्गुन शु. १३", "events": ["प्रदोष"], "flags": {"isPradosh": True} },
  "2": { "tithi": "फाल्गुन शु. १४", "events": ["होळी", "हुताशनी पौर्णिमा", "पौर्णिमा प्रारंभ सायं. ५.५५"], "flags": {} },
  "3": { "tithi": "फाल्गुन पौर्णिमा", "events": ["धुलिवंदन", "चैतन्य जयंती", "करिदिन", "जागतिक वन्यजीव दिन", "खग्रास चंद्रग्रहण", "पौर्णिमा समाप्ती सायं. ५.०७"], "flags": {"isPurnima": True} },
  "4": { "tithi": "फाल्गुन कृ. १", "events": ["वसंतोत्सव प्रारंभ", "ग्रहण करिदिन", "राष्ट्रीय सुरक्षा दिन"], "flags": {} },
  "5": { "tithi": "फाल्गुन कृ. २", "events": ["संत तुकाराम बीज, देहू"], "flags": {} },
  "6": { "tithi": "फाल्गुन कृ. ३", "events": ["संकष्ट चतुर्थी", "चंद्रोदय ९.१६", "छत्रपती शिवाजी महाराज जयंती (तिथीप्रमाणे)"], "flags": {"isChaturthi": True} },
  "7": { "tithi": "फाल्गुन कृ. ४", "events": [], "flags": {} },
  "8": { "tithi": "फाल्गुन कृ. ५", "events": ["कानिफनाथ यात्रा, मढी", "जागतिक महिला दिन", "रंगपंचमी"], "flags": {} },
  "9": { "tithi": "फाल्गुन कृ. ६", "events": ["श्री एकनाथ षष्ठी", "पैठण यात्रा"], "flags": {} },
  "10": { "tithi": "फाल्गुन कृ. ७", "events": ["ज्ञानज्योती सावित्रीबाई फुले स्मृतिदिन"], "flags": {} },
  "11": { "tithi": "फाल्गुन कृ. ८", "events": ["कालाष्टमी", "शहादते हजरत अली", "छत्रपती संभाजीराजे बलिदान दिन"], "flags": {} },
  "12": { "tithi": "फाल्गुन कृ. ९", "events": ["यशवंतराव चव्हाण जयंती", "मामा महाराज देशपांडे पुण्यतिथी"], "flags": {} },
  "13": { "tithi": "फाल्गुन कृ. १०", "events": ["पारशी आबान मासारंभ"], "flags": {} },
  "14": { "tithi": "फाल्गुन कृ. १०", "events": [], "flags": {} },
  "15": { "tithi": "फाल्गुन कृ. ११", "events": ["पापमोचनी एकादशी", "जागतिक ग्राहक दिन", "सकाळचे अन्नदाते : कै.निवृत्ती डुकरे व कै. आनंदा डुकरे स्मर. सुरेश डुकरे, दत्तात्रय डुकरे", "सायं. अन्नदाते : समस्त ग्रामस्थ साकोरी व मंगरुळ झाप"], "flags": {"isEkadashi": True} },
  "16": { "tithi": "फाल्गुन कृ. १२", "events": ["सोमप्रदोष", "वार्षिक अन्नदाते : समस्त ग्रामस्थ साकोरी व मंगरुळ झाप"], "flags": {"isPradosh": True} },
  "17": { "tithi": "फाल्गुन कृ. १३", "events": ["शिवरात्री", "मधुकृष्ण त्रयोदशी"], "flags": {"isShivratri": True} },
  "18": { "tithi": "फाल्गुन कृ. १४", "events": ["दर्श अमावास्या", "शहाजीराजे भोसले जयंती (तारखेप्रमाणे)", "अमावास्या प्रारंभ सकाळी ८.२५"], "flags": {} },
  "19": { "tithi": "फाल्गुन अमावास्या/चैत्र शु. १", "events": ["गुढीपाडवा", "श्री शालिवाहन शके १९४८ प्रारंभ", "अमावास्या समाप्ती सकाळी ६.५३"], "flags": {"isAmavasya": True} },
  "20": { "tithi": "चैत्र शु. २", "events": ["चंद्रदर्शन", "श्री अक्कलकोट स्वामी महाराज प्रकट दिन"], "flags": {} },
  "21": { "tithi": "चैत्र शु. ३", "events": ["मत्स्य जयंती", "रमजान ईद", "जागतिक वनीकरण दिन"], "flags": {} },
  "22": { "tithi": "चैत्र शु. ४", "events": ["विनायक चतुर्थी", "जागतिक जल दिन"], "flags": {"isChaturthi": True} },
  "23": { "tithi": "चैत्र शु. ५", "events": ["श्री पंचमी", "श्री लक्ष्मी पंचमी", "जागतिक हवामान दिन", "क्रांतिवीर भगतसिंग, राजगुरु, सुखदेव शहीद दिन"], "flags": {} },
  "24": { "tithi": "चैत्र शु. ६", "events": ["जागतिक क्षयरोग दिन"], "flags": {} },
  "25": { "tithi": "चैत्र शु. ७", "events": ["एकवीरादेवी पालखी लोणावळा"], "flags": {} },
  "26": { "tithi": "चैत्र शु. ८", "events": ["श्री रामदासस्वामी जयंती", "गजानन महाराज उत्सव, शेगांव", "श्रीराम नवमी", "ग्रामदैवत अंबिकामाता यात्रा आळे,संतवाडी,कोळवाडी", "अखंड हरिनाम सप्ताह प्रारंभ कोळवाडी व पिंपळमळा"], "flags": {} },
  "27": { "tithi": "चैत्र शु. ९", "events": ["श्री स्वामीनारायण जयंती", "जागतिक रंगभूमी दिन", "ग्रामदैवत अंबिकामाता यात्रा", "कुस्ती आखाडा"], "flags": {} },
  "28": { "tithi": "चैत्र शु. १०", "events": ["साईबाबा उत्सव समाप्ती, शिर्डी"], "flags": {} },
  "29": { "tithi": "चैत्र शु. ११", "events": ["कामदा एकादशी", "चैत्री यात्रा, पंढरपूर", "सकाळचे अन्नदाते : अशोक खंडू भुजबळ (सर)", "सायं. अन्नदाते : समस्त ग्रामस्थ आळे व वडगाव आनंद कुंभार समाज"], "flags": {"isEkadashi": True} },
  "30": { "tithi": "चैत्र शु. १२", "events": ["सोमप्रदोष", "वार्षिक अन्नदाते : समस्त ग्रामस्थ आळे व वडगाव आनंद कुंभार समाज"], "flags": {"isPradosh": True} },
  "31": { "tithi": "चैत्र शु. १३", "events": ["दमनक चतुर्दशी", "श्री महावीर जयंती"], "flags": {} }
}

for day_key, day_data in data.items():
    flags = day_data.get('flags', {})
    events = day_data.get('events', [])
    notif_events = []
    
    if flags.get('isPradosh'):
        pradosh_event = next((e for e in events if "प्रदोष" in e), "प्रदोष")
        notif_events.append(pradosh_event)
        
    if flags.get('isPurnima'):
        purnima_event = next((e for e in events if "पौर्णिमा" in e), "पौर्णिमा")
        notif_events.append(purnima_event)
        
    if flags.get('isAmavasya'):
        amavasya_event = next((e for e in events if "अमावास्या" in e and "प्रारंभ" not in e and "समाप्ती" not in e), "अमावास्या")
        notif_events.append(amavasya_event)
        
    if flags.get('isChaturthi'):
        chaturthi_event = next((e for e in events if "चतुर्थी" in e), "चतुर्थी")
        notif_events.append(chaturthi_event)
            
    if flags.get('isEkadashi'):
        ekadashi_event = next((e for e in events if "एकादशी" in e), "एकादशी")
        notif_events.append(ekadashi_event)
        
    if flags.get('isShivratri'):
        notif_events.append("शिवरात्री")
        
    # Also add major yatras/jayantis (filtering out Annadate)
    for event in events:
        if any(k in event for k in ["जयंती", "दिन", "प्रारंभ", "समाप्ती", "यात्रा", "महाशिवरात्री", "सप्तमी", "अष्टमी", "नवमी", "ईद", "गुढीपाडवा", "होळी", "धुलिवंदन"]):
            if "अन्नदाते" not in event and "मुक्काम" not in event and "सप्ताह" not in event and "कीर्तन" not in event and "श्राद्ध" not in event:
                if event not in notif_events:
                    notif_events.append(event)
                    
    if notif_events:
        day_data['notification_events'] = list(dict.fromkeys(notif_events))

out_path = '/Users/suhas/WORK/Vedamit/DnyaneshwarMaharajRedaSamadhiMandir/CalenderApp/MobileApp2/calendar-app-data/2026/Mar/month_details.json'
with open(out_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
