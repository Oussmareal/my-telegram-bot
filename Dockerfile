# استخدم Python 3.9
FROM python:3.9

# تحديد مجلد العمل داخل الحاوية
WORKDIR /app

# نسخ الملفات إلى الحاوية
COPY . .

# تثبيت المتطلبات وتحديث pip
RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

# تعيين المتغيرات البيئية
ENV API_ID=26037708
ENV API_HASH="769da9951dfadb6113f3afbf33209d4d"
ENV ADMIN_USER_ID=6747574207
ENV SOURCE_GROUPS="-4658871439,-1002035975495"
ENV TARGET_GROUPS="-1002479735760,-1002479735760"

# تشغيل البوت
CMD ["python", "bot.py"]
