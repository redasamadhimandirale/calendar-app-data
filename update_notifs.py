import json
import os

def update_month(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    for day_key, day_data in data.items():
        flags = day_data.get('flags', {})
        events = day_data.get('events', [])
        
        # We only add notification_events if there are major flags or specific important events
        if flags or any("महाशिवरात्री" in e for e in events):
            notif_events = []
            
            # Map flags to notification event names based on what's in 'events' or defaults
            if flags.get('isPradosh'):
                notif_events.append("प्रदोष")
                
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
                
            # Mahashivratri is important even without a specific metadata flag in this app (wait, October had isShivratri: true, let's add it if found)
            if any("महाशिवरात्री" in e for e in events):
                notif_events.append("महाशिवरात्री")
                day_data['flags']['isShivratri'] = True
                
            if notif_events:
                # Remove duplicates
                day_data['notification_events'] = list(dict.fromkeys(notif_events))

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

update_month('/Users/suhas/WORK/Vedamit/DnyaneshwarMaharajRedaSamadhiMandir/CalenderApp/MobileApp2/calendar-app-data/2026/Jan/month_details.json')
update_month('/Users/suhas/WORK/Vedamit/DnyaneshwarMaharajRedaSamadhiMandir/CalenderApp/MobileApp2/calendar-app-data/2026/Feb/month_details.json')
