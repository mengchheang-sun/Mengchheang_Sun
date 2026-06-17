from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import os
import fitz  # PyMuPDF
from PIL import Image, ImageSequence
from docx2pdf import convert as docx2pdf_convert
from telegram.ext import MessageHandler, filters

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder, CommandHandler, MessageHandler,
    ContextTypes, ConversationHandler, CallbackQueryHandler, filters
)

# Replace with your bot token
BOT_TOKEN = "8540584952:AAEO5SoA_zoVdzYhzAs5jCY49auOfSQi76o"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "សួរស្តី! 👋\nសួមស្វាគមន៍ មកកាន់ក្រុមព័ត៌មានទូទៅ ដោយចុចតាមតំណភ្ជាប់តាមនេះ 👉https://t.me/+HTQz34LXv21lYTM1.\nសូមចុចត្រង់នេះសម្រាប់ជួយលោកអ្នកត្រូវការជំនួយបន្ថែមទៀត👉 /help ."
    )

import os
from datetime import datetime

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes


async def contacts_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
លោក/លោកស្រីអាចរកព័ត៌មានទាក់ទងនិងគ្រូបន្ទុកថ្នាក់បានដូចខាងក្រោមនេះ!

សម្រាប់តេឡេក្រាម Telegram: @MENGCHHEANG_SUN

សម្រាប់លេខទំនាក់ទំនង Tel: 071-628-5771, 089-556-321

សូមអរគុណ! | Thanks!
        """
    )

async def leaveform_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        """
សូមលោកគ្រូ/អ្នកគ្រូចុចលីងខាងក្រោមរួចបំពេញតាមសំណួរខាងក្នុង!

ទម្រង់សុំច្បាប់ : https://forms.gle/RRXrPoFfz4UrM3ueA

លីងសម្រាប់ចូលទៅទាញយកឯកសារក្នុង (google drive) : https://drive.google.com/drive/folders/1S0hz8Ond3-FGd95W5AoioL9A4QQ7L-UG

សូមអរគុណ! | Thanks!
        """
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "/start - Start the bot\n"
        "/aboutschool - អំពីសាលាយើង\n"
        "/contact - លេខទូរស័ព្ទគ្រូបន្ទុកថ្នាក់"
    )

async def សូមស្វាគមន៍(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"ជម្រាបសួរ និងសូមស្វាគមន៍ លោក/លោកស្រី {user}! 😊")

    # 2 rows, landscape buttons
    keyboard = [
        [
            InlineKeyboardButton("Facebook", url="https://web.facebook.com/profile.php?id=100091418500015"),
            InlineKeyboardButton("Telegram", url="https://t.me/+HTQz34LXv21lYTM1")
        ],
        [
            InlineKeyboardButton("ថ្នាលកម្មវិធី PLP", url="https://plp.moeys.gov.kh/"),
            InlineKeyboardButton("Group", url="https://www.messenger.com/t/24801870859452034/"),
            InlineKeyboardButton("ទីតាំងសាលា", url="https://maps.app.goo.gl/HDKPmV5xUes8uZts9")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # image path
    file_path = r"D:\Testing Telegram bot\logo\Logo.jpg"

    print("Checking path:", file_path)
    print("Exists:", os.path.exists(file_path))

    if os.path.exists(file_path):
        with open(file_path, "rb") as photo:
            await update.message.reply_photo(photo, caption="សាលាបឋមសិក្សា តាំងរលាង", reply_markup=reply_markup)
    elif os.path.exists("Logo.jpg"):
        with open("Logo.jpg", "rb") as photo:
            await update.message.reply_photo(photo, caption="សាលាបឋមសិក្សា តាំងរលាង", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Logo image not found in both locations.")

async def plp_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user.first_name
    await update.message.reply_text(f"ជម្រាបសួរ និងសូមស្វាគមន៍ លោក/លោកស្រី {user}! 😊")

    # 2 rows, landscape buttons
    keyboard = [
        [
            InlineKeyboardButton("ថ្នាលកម្មវិធី PLP", url="https://plp.moeys.gov.kh/"),
            InlineKeyboardButton("ថ្នាលតេស្តនិងប្រឡង", url="https://exam.plpmoeys.com/auth/login")
        ],
        [
            InlineKeyboardButton("ស្តង់ដាសាលាបឋមសិក្សាគំរូ", url="https://plp-mss.moeys.gov.kh/login"),
            InlineKeyboardButton("វីដេអូរៀនបន្ថែម", url="https://plp-files.moeys.gov.kh/video")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # image path
    file_path = r"D:\PythonProject\logo\PLP.png"

    print("Checking path:", file_path)
    print("Exists:", os.path.exists(file_path))

    if os.path.exists(file_path):
        with open(file_path, "rb") as photo:
            await update.message.reply_photo(photo, caption="ថ្នាលបឋម (PLP)", reply_markup=reply_markup)
    elif os.path.exists("Logo.jpg"):
        with open("Logo.jpg", "rb") as photo:
            await update.message.reply_photo(photo, caption="ថ្នាលបឋម (PLP)", reply_markup=reply_markup)
    else:
        await update.message.reply_text("Logo image not found in both locations.")

async def converter_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📄 សូមលោកអ្នកផ្ញើមកជាឯកសារ (PDF, DOCX, or image) ខាងយើងនិងផ្ញើត្រឡប់ទៅវិញជារូបភាព (JPG).")

async def handle_document(update: Update, context: ContextTypes.DEFAULT_TYPE):
    file = await update.message.document.get_file()
    filename = update.message.document.file_name
    file_ext = os.path.splitext(filename)[1].lower()
    file_path = f"input{file_ext}"
    await file.download_to_drive(file_path)

    async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE):
        photo = update.message.photo[-1]  # highest resolution
        file = await photo.get_file()

        input_path = "photo_input.jpg"
        output_path = "converted.jpg"

        await file.download_to_drive(input_path)

        img = Image.open(input_path).convert("RGB")
        img.save(output_path, "JPEG", quality=85)

        with open(output_path, "rb") as out:
            await update.message.reply_photo(out, caption="Converted to JPG")

        os.remove(input_path)
        os.remove(output_path)

    try:
        # 1️⃣ DOCX → PDF → JPG
        if file_ext == ".docx":
            pdf_file = "temp.pdf"
            docx2pdf_convert(file_path, pdf_file)
            pdf = fitz.open(pdf_file)
            for i in range(len(pdf)):
                page = pdf.load_page(i)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_path = f"page_{i+1}.jpg"
                pix.save(img_path)
                with open(img_path, "rb") as out_img:
                    await update.message.reply_photo(photo=out_img, caption=f"Page {i+1}")
                os.remove(img_path)
            pdf.close()
            os.remove(pdf_file)

        # 2️⃣ PDF → JPG
        elif file_ext == ".pdf":
            pdf = fitz.open(file_path)
            for i in range(len(pdf)):
                page = pdf.load_page(i)
                pix = page.get_pixmap(matrix=fitz.Matrix(2, 2))
                img_path = f"page_{i+1}.jpg"
                pix.save(img_path)
                with open(img_path, "rb") as out_img:
                    await update.message.reply_photo(photo=out_img, caption=f"Page {i+1}")
                os.remove(img_path)
            pdf.close()

        # 3️⃣ Images → JPG
        elif file_ext in [".png", ".jpg", ".jpeg", ".bmp", ".tiff", ".tif", ".webp"]:
            img = Image.open(file_path)
            for i, frame in enumerate(ImageSequence.Iterator(img)):
                frame = frame.convert("RGB")
                img_path = f"converted_{i+1}.jpg"
                frame.save(img_path, "JPEG", optimize=True, quality=60)
                caption = f"Page {i+1}" if file_ext in [".tif", ".tiff"] else "Converted to JPG"
                try:
                    await update.message.reply_photo(photo=open(img_path, "rb"), caption=caption)
                except:
                    await update.message.reply_document(document=open(img_path, "rb"), caption=caption)
                os.remove(img_path)

        else:
            await update.message.reply_text("❌ Unsupported file type.")

    except Exception as e:
        await update.message.reply_text(f"⚠️ Conversion failed: {e}")

    finally:
        if os.path.exists(file_path):
            os.remove(file_path)



def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("leaveform", leaveform_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("aboutschool", សូមស្វាគមន៍))
    app.add_handler(CommandHandler("contacts", contacts_command))
    app.add_handler(CommandHandler("converter", converter_command))
    app.add_handler(CommandHandler("plp", plp_command))



    # ✅ Correct order
    app.add_handler(MessageHandler(filters.Document.ALL, handle_document))


    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
