from telethon import TelegramClient, events

# ✅ بيانات تسجيل الدخول إلى تيليجرام
api_id = 26037708  # استبدله بـ API ID الخاص بك
api_hash = '769da9951dfadb6113f3afbf33209d4d'  # استبدله بـ API HASH الخاص بك

# ✅ إنشاء الجلسة
client = TelegramClient('multi_group_bot', api_id, api_hash)

# ✅ معرف المسؤول الذي سيصله إشعار عند تشغيل أو إيقاف البوت
admin_user_id = 6747574207  

# ✅ المجموعات المصدر والهدف
source_groups = [-4658871439, -1002035975495]  # مجموعات المصدر
target_groups = [-1002479735760, -1002479735760]  # مجموعات الهدف

async def send_admin_notification(message):
    """إرسال إشعار للمسؤول عند تشغيل أو إيقاف البوت"""
    try:
        await client.send_message(admin_user_id, message)
    except Exception as e:
        print(f"❌ خطأ في إرسال الإشعار: {e}")

@client.on(events.NewMessage(chats=source_groups))  
async def forward_message(event):
    """تحويل الرسائل بين المجموعات"""
    for target in target_groups:
        try:
            if event.message.text:  # إذا كانت الرسالة نصية
                await client.send_message(target, event.message.text)
            elif event.message.media:  # إذا كانت تحتوي على وسائط
                await client.send_file(target, event.message.media)
            print(f"✅ تم تحويل الرسالة من {event.chat_id} إلى {target}")
        except Exception as e:
            print(f"❌ فشل تحويل الرسالة إلى {target}: {e}")

async def main():
    """تشغيل البوت"""
    print("🚀 البوت يعمل الآن وينتظر الرسائل...")
    await send_admin_notification("🚀 البوت بدأ العمل بنجاح!")
    await client.run_until_disconnected()

try:
    with client:
        client.loop.run_until_complete(main())
except KeyboardInterrupt:
    print("⛔ تم إيقاف البوت يدويًا.")
    client.loop.run_until_complete(send_admin_notification("⛔ البوت تم إيقافه يدويًا!"))
except Exception as e:
    print(f"❌ خطأ غير متوقع: {e}")
    client.loop.run_until_complete(send_admin_notification(f"❌ البوت توقف بسبب خطأ: {e}"))
