
from pyrogram import Client, filters
from pyrogram.types import Message

@Client.on_message(filters.private & filters.command("help"))
async def help_command(client, message: Message):
    help_text = (
        "👋 **বট ব্যবহারের নিয়ম:**

"
        "1️⃣ আপনার ফাইলটি বটে পাঠান।
"
        "2️⃣ বট আপনাকে জিজ্ঞেস করবে – রিনেম করতে চান কিনা।
"
        "3️⃣ ✅ হ্যাঁ চাপলে নতুন নাম দিন (এক্সটেনশন সহ)।
"
        "4️⃣ বট ফাইল রিনেম করে দিয়ে দেবে!

"
        "📌 **কমান্ড:**
"
        "`/start` - বট চালু করুন
"
        "`/help` - সাহায্য মেনু
"
        "`/about` - বট সম্পর্কে তথ্য"
    )
    await message.reply_text(help_text)

@Client.on_message(filters.private & filters.command("about"))
async def about_command(client, message: Message):
    about_text = (
        "ℹ️ **বট সম্পর্কিত তথ্য:**

"
        "🔹 নাম: ফাইল রিনেমার বট
"
        "🔹 কাজ: টেলিগ্রামে ফাইল রিনেম করা
"
        "🔹 ডেভেলপার: @yourusername
"
        "🔹 আপডেট চ্যানেল: @yourchannel

"
        "❤️ ধন্যবাদ বট ব্যবহার করার জন্য!"
    )
    await message.reply_text(about_text)
